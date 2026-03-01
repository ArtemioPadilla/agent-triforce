#!/usr/bin/env python3
"""Spec-to-Implementation Traceability Matrix Generator.

Reads a feature spec, extracts acceptance criteria, scans implementation,
test, and review files, and generates a traceability matrix showing coverage.

Usage::

    python3 tools/traceability.py generate <feature-name>
    python3 tools/traceability.py update <feature-name>
    python3 tools/traceability.py list

Zero external dependencies. Python 3.9+.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SPEC_DIR = PROJECT_ROOT / "docs" / "specs"
SRC_DIR = PROJECT_ROOT / "src"
TESTS_DIR = PROJECT_ROOT / "tests"
REVIEW_DIR = PROJECT_ROOT / "docs" / "reviews"
TRACEABILITY_DIR = PROJECT_ROOT / "docs" / "traceability"

# File extensions to scan per language
SOURCE_EXTENSIONS = {
    ".py", ".ts", ".tsx", ".js", ".jsx", ".rs", ".go",
    ".java", ".sol", ".rb", ".swift", ".kt",
}

TEST_EXTENSIONS = SOURCE_EXTENSIONS


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------


@dataclass
class AcceptanceCriterion:
    """A single acceptance criterion extracted from a spec."""

    criterion_id: str
    text: str
    given: str = ""
    when: str = ""
    then: str = ""


@dataclass
class TraceLink:
    """Links a criterion to implementation, tests, and findings."""

    criterion: AcceptanceCriterion
    implementation_files: List[str] = field(default_factory=list)
    test_files: List[str] = field(default_factory=list)
    findings: List[str] = field(default_factory=list)
    status: str = "Missing"  # Covered, Partial, Missing


@dataclass
class TraceabilityMatrix:
    """Complete traceability matrix for a feature."""

    feature_name: str
    spec_file: str
    generated_at: str
    criteria_count: int
    covered_count: int
    partial_count: int
    missing_count: int
    links: List[TraceLink] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------


def _read_file_safe(path: Path) -> str:
    """Read a file, returning empty string on any error."""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ""


def _find_spec_file(feature_name: str) -> Optional[Path]:
    """Find the spec file for a feature name."""
    # Direct match
    direct = SPEC_DIR / f"{feature_name}.md"
    if direct.exists():
        return direct

    # Try with common prefixes/suffixes
    for pattern in [f"*{feature_name}*"]:
        matches = list(SPEC_DIR.glob(pattern))
        if len(matches) == 1:
            return matches[0]

    return None


def _extract_feature_id(feature_name: str) -> str:
    """Derive a feature ID from the feature name for criterion IDs."""
    # Use the feature name as-is, replacing spaces/special chars
    clean = re.sub(r"[^a-zA-Z0-9]+", "-", feature_name).strip("-").lower()
    # Shorten if too long
    if len(clean) > 20:
        clean = clean[:20].rstrip("-")
    return clean


def extract_acceptance_criteria(spec_text: str, feature_id: str) -> List[AcceptanceCriterion]:
    """Extract GIVEN/WHEN/THEN acceptance criteria from a spec.

    Supports two formats:
    1. GIVEN...WHEN...THEN blocks (paragraph style)
    2. Numbered items in an acceptance criteria section
    """
    criteria: List[AcceptanceCriterion] = []

    # Find the Acceptance Criteria section
    ac_section = ""
    ac_match = re.search(
        r"(?:###+\s*Acceptance Criteria|###+\s*ACs?)\s*\n(.*?)(?=\n##|\Z)",
        spec_text,
        re.DOTALL | re.IGNORECASE,
    )
    if ac_match:
        ac_section = ac_match.group(1)
    else:
        # Fallback: search the entire document for GIVEN/WHEN/THEN blocks
        ac_section = spec_text

    # Extract GIVEN/WHEN/THEN blocks
    # Pattern: GIVEN ... WHEN ... THEN ... (may span multiple lines)
    gwt_pattern = re.compile(
        r"GIVEN\s+(.+?)\s*,?\s*\n?\s*WHEN\s+(.+?)\s*,?\s*\n?\s*THEN\s+(.+?)(?=\n\s*(?:GIVEN|$|\n\n))",
        re.DOTALL | re.IGNORECASE,
    )

    for idx, match in enumerate(gwt_pattern.finditer(ac_section), start=1):
        given = _clean_text(match.group(1))
        when = _clean_text(match.group(2))
        then = _clean_text(match.group(3))
        full_text = f"GIVEN {given}, WHEN {when}, THEN {then}"
        criterion_id = f"{feature_id}-AC-{idx:03d}"
        criteria.append(AcceptanceCriterion(
            criterion_id=criterion_id,
            text=full_text,
            given=given,
            when=when,
            then=then,
        ))

    # If no GIVEN/WHEN/THEN found, try numbered items
    if not criteria:
        numbered_pattern = re.compile(r"^\s*(?:\d+[.)]\s*|[-*]\s*)(.*)", re.MULTILINE)
        for idx, match in enumerate(numbered_pattern.finditer(ac_section), start=1):
            text = _clean_text(match.group(1))
            if text and len(text) > 10:  # Skip very short items
                criterion_id = f"{feature_id}-AC-{idx:03d}"
                criteria.append(AcceptanceCriterion(
                    criterion_id=criterion_id,
                    text=text,
                ))

    return criteria


def _clean_text(text: str) -> str:
    """Clean extracted text: collapse whitespace, strip markdown."""
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[`*_]", "", text)
    return text.strip().rstrip(",.")


# ---------------------------------------------------------------------------
# Scanning
# ---------------------------------------------------------------------------


def _scan_directory(directory: Path, extensions: set, feature_name: str) -> List[str]:
    """Scan a directory for files mentioning a feature.

    Uses keyword matching: the feature name, words from it, and common
    derivations.
    """
    if not directory.exists():
        return []

    # Build search terms from feature name
    search_terms = _build_search_terms(feature_name)
    matches: List[str] = []

    for path in _walk_files(directory, extensions):
        content = _read_file_safe(path)
        if not content:
            continue
        content_lower = content.lower()
        for term in search_terms:
            if term in content_lower:
                rel = str(path.relative_to(PROJECT_ROOT))
                if rel not in matches:
                    matches.append(rel)
                break

    return sorted(matches)


def _build_search_terms(feature_name: str) -> List[str]:
    """Build search terms from a feature name.

    For 'auth-login', produces: ['auth-login', 'auth_login', 'authlogin',
    'auth login', 'auth', 'login'].
    """
    name = feature_name.lower()
    terms = [name]

    # Variations
    terms.append(name.replace("-", "_"))
    terms.append(name.replace("-", ""))
    terms.append(name.replace("-", " "))

    # Individual words (only if 3+ chars)
    words = re.split(r"[-_ ]+", name)
    for word in words:
        if len(word) >= 3:
            terms.append(word)

    return list(set(terms))


def _walk_files(directory: Path, extensions: set) -> List[Path]:
    """Walk a directory tree and yield files with matching extensions."""
    files: List[Path] = []
    if not directory.exists():
        return files
    try:
        for item in directory.rglob("*"):
            if item.is_file() and item.suffix in extensions:
                # Skip hidden dirs and common non-source dirs
                parts = item.relative_to(directory).parts
                if any(p.startswith(".") or p in ("node_modules", "__pycache__", "venv", ".venv") for p in parts):
                    continue
                files.append(item)
    except PermissionError:
        pass
    return files


def _scan_reviews(feature_name: str) -> List[str]:
    """Scan review files for findings referencing a feature."""
    if not REVIEW_DIR.exists():
        return []

    search_terms = _build_search_terms(feature_name)
    matches: List[str] = []

    for path in sorted(REVIEW_DIR.glob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        content = _read_file_safe(path)
        content_lower = content.lower()

        # Also match on the review filename itself
        if feature_name in path.stem.lower():
            matches.append(str(path.relative_to(PROJECT_ROOT)))
            continue

        for term in search_terms:
            if term in content_lower:
                matches.append(str(path.relative_to(PROJECT_ROOT)))
                break

    return sorted(set(matches))


# ---------------------------------------------------------------------------
# Matrix generation
# ---------------------------------------------------------------------------


def generate_matrix(feature_name: str) -> Optional[TraceabilityMatrix]:
    """Generate a traceability matrix for a feature.

    Returns None if the spec file is not found.
    """
    spec_file = _find_spec_file(feature_name)
    if spec_file is None:
        return None

    spec_text = _read_file_safe(spec_file)
    if not spec_text:
        return None

    feature_id = _extract_feature_id(feature_name)
    criteria = extract_acceptance_criteria(spec_text, feature_id)

    if not criteria:
        # Still produce a matrix, but with a warning
        pass

    # Scan for implementation, tests, and reviews
    impl_files = _scan_directory(SRC_DIR, SOURCE_EXTENSIONS, feature_name)
    test_files = _scan_directory(TESTS_DIR, TEST_EXTENSIONS, feature_name)
    review_findings = _scan_reviews(feature_name)

    # Build links
    links: List[TraceLink] = []
    covered = 0
    partial = 0
    missing = 0

    for criterion in criteria:
        # Simple heuristic: all impl/test files apply to all criteria
        # More sophisticated matching would parse criterion text against
        # function names, but that exceeds the zero-dependency constraint
        link = TraceLink(
            criterion=criterion,
            implementation_files=impl_files,
            test_files=test_files,
            findings=review_findings,
        )

        # Determine status
        if impl_files and test_files:
            link.status = "Covered"
            covered += 1
        elif impl_files:
            link.status = "Partial"
            partial += 1
        else:
            link.status = "Missing"
            missing += 1

        links.append(link)

    return TraceabilityMatrix(
        feature_name=feature_name,
        spec_file=str(spec_file.relative_to(PROJECT_ROOT)),
        generated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        criteria_count=len(criteria),
        covered_count=covered,
        partial_count=partial,
        missing_count=missing,
        links=links,
    )


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------


def format_matrix_markdown(matrix: TraceabilityMatrix) -> str:
    """Format the traceability matrix as markdown."""
    lines = [
        f"# Traceability Matrix: {matrix.feature_name}",
        "",
        f"**Spec**: `{matrix.spec_file}`",
        f"**Generated**: {matrix.generated_at}",
        f"**Criteria**: {matrix.criteria_count} total | "
        f"{matrix.covered_count} covered | "
        f"{matrix.partial_count} partial | "
        f"{matrix.missing_count} missing",
        "",
    ]

    # Coverage bar
    if matrix.criteria_count > 0:
        pct = (matrix.covered_count / matrix.criteria_count) * 100
        lines.append(f"**Coverage**: {pct:.0f}%")
        lines.append("")

    # Matrix table
    lines.extend([
        "| Criterion ID | Criterion | Implementation | Tests | Findings | Status |",
        "|---|---|---|---|---|---|",
    ])

    for link in matrix.links:
        impl_str = ", ".join(f"`{f}`" for f in link.implementation_files) or "None"
        test_str = ", ".join(f"`{f}`" for f in link.test_files) or "None"
        findings_str = ", ".join(f"`{f}`" for f in link.findings) or "None"

        # Truncate criterion text for table readability
        text = link.criterion.text
        if len(text) > 80:
            text = text[:77] + "..."

        status_marker = {
            "Covered": "Covered",
            "Partial": "**Partial**",
            "Missing": "**MISSING**",
        }.get(link.status, link.status)

        lines.append(
            f"| {link.criterion.criterion_id} | {text} | {impl_str} | {test_str} | {findings_str} | {status_marker} |"
        )

    lines.append("")

    # Detailed criteria (full text)
    if matrix.links:
        lines.extend(["", "## Criteria Details", ""])
        for link in matrix.links:
            c = link.criterion
            lines.append(f"### {c.criterion_id}")
            if c.given:
                lines.extend([
                    f"- **GIVEN**: {c.given}",
                    f"- **WHEN**: {c.when}",
                    f"- **THEN**: {c.then}",
                ])
            else:
                lines.append(f"{c.text}")
            lines.append(f"- **Status**: {link.status}")
            lines.append("")

    # Recommendations
    if matrix.missing_count > 0:
        lines.extend([
            "## Recommendations",
            "",
            f"- {matrix.missing_count} criteria have no implementation. These need development work.",
        ])
    if matrix.partial_count > 0:
        lines.append(
            f"- {matrix.partial_count} criteria have implementation but no tests. "
            "Consider running `/generate-tests` to close the gap."
        )

    lines.append("")
    lines.append(f"---\n*Generated by tools/traceability.py on {matrix.generated_at}*")
    lines.append("")

    return "\n".join(lines)


def save_matrix(matrix: TraceabilityMatrix) -> Path:
    """Save the traceability matrix to docs/traceability/."""
    TRACEABILITY_DIR.mkdir(parents=True, exist_ok=True)
    output_path = TRACEABILITY_DIR / f"{matrix.feature_name}-matrix.md"
    content = format_matrix_markdown(matrix)
    output_path.write_text(content, encoding="utf-8")
    return output_path


# ---------------------------------------------------------------------------
# CLI commands
# ---------------------------------------------------------------------------


def cmd_generate(args: argparse.Namespace) -> int:
    """Generate a traceability matrix for a feature."""
    matrix = generate_matrix(args.feature_name)
    if matrix is None:
        print(
            f"Error: Spec file not found for feature '{args.feature_name}'.\n"
            f"Expected: docs/specs/{args.feature_name}.md",
            file=sys.stderr,
        )
        return 1

    output_path = save_matrix(matrix)
    print(format_matrix_markdown(matrix))
    print(f"\nMatrix saved to {output_path.relative_to(PROJECT_ROOT)}", file=sys.stderr)
    return 0


def cmd_update(args: argparse.Namespace) -> int:
    """Update an existing traceability matrix (alias for generate)."""
    return cmd_generate(args)


def cmd_list(args: argparse.Namespace) -> int:
    """List all available specs that can have traceability matrices."""
    if not SPEC_DIR.exists():
        print("No specs directory found.", file=sys.stderr)
        return 1

    specs = sorted(SPEC_DIR.glob("*.md"))
    if not specs:
        print("No spec files found in docs/specs/.", file=sys.stderr)
        return 1

    print("Available specs for traceability analysis:")
    print()
    for spec in specs:
        if spec.name.lower() == "readme.md":
            continue
        feature_name = spec.stem
        matrix_exists = (TRACEABILITY_DIR / f"{feature_name}-matrix.md").exists()
        marker = "[matrix exists]" if matrix_exists else "[no matrix]"
        print(f"  {feature_name}  {marker}")

    print()
    print("Generate a matrix: python3 tools/traceability.py generate <feature-name>")
    return 0


def main() -> None:
    """Entry point for the traceability CLI."""
    parser = argparse.ArgumentParser(
        description="Spec-to-Implementation Traceability Matrix Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python3 tools/traceability.py generate auth-login\n"
            "  python3 tools/traceability.py update auth-login\n"
            "  python3 tools/traceability.py list\n"
        ),
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # generate
    gen_parser = subparsers.add_parser("generate", help="Generate traceability matrix")
    gen_parser.add_argument("feature_name", help="Feature name (matches docs/specs/<name>.md)")
    gen_parser.set_defaults(func=cmd_generate)

    # update
    upd_parser = subparsers.add_parser("update", help="Update existing traceability matrix")
    upd_parser.add_argument("feature_name", help="Feature name")
    upd_parser.set_defaults(func=cmd_update)

    # list
    list_parser = subparsers.add_parser("list", help="List available specs")
    list_parser.set_defaults(func=cmd_list)

    args = parser.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
