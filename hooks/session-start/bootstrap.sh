#!/bin/sh
# Agent Triforce session bootstrap
# POSIX sh — no bash-isms (avoids bash 5.3+ hang bugs)
# Surfaces in-progress work for agent SIGN IN checklists

set -e

PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0
cd "$PROJECT_ROOT"

echo "[triforce-bootstrap] project: $(basename "$PROJECT_ROOT")"

# 1. Active worktrees
WORKTREE_COUNT=$(git worktree list | wc -l | tr -d ' ')
if [ "$WORKTREE_COUNT" -gt 1 ]; then
    git worktree list | tail -n +2 | while IFS= read -r line; do
        echo "[triforce-bootstrap] worktree: $line"
    done
fi

# 2. Uncommitted changes
DIRTY_COUNT=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
if [ "$DIRTY_COUNT" -gt 0 ]; then
    echo "[triforce-bootstrap] dirty: $DIRTY_COUNT uncommitted files"
fi

# 3. Pending specs (specs without corresponding review files)
if [ -d "docs/specs" ]; then
    for spec in docs/specs/*.md; do
        [ -f "$spec" ] || continue
        basename_no_ext=$(basename "$spec" .md)
        # Skip non-feature files
        case "$basename_no_ext" in
            README|backlog|feature-roadmap|future-roadmap|growth-plan|plugin-promotion-plan) continue ;;
        esac
        if [ ! -f "docs/reviews/${basename_no_ext}-review.md" ]; then
            echo "[triforce-bootstrap] pending-spec: $basename_no_ext (no review yet)"
        fi
    done
fi

# 4. Pending review findings (reviews with CHANGES REQUIRED verdict)
if [ -d "docs/reviews" ]; then
    for review in docs/reviews/*-review.md; do
        [ -f "$review" ] || continue
        if grep -q "CHANGES REQUIRED" "$review" 2>/dev/null; then
            echo "[triforce-bootstrap] open-findings: $(basename "$review")"
        fi
    done
fi

# 5. TECH_DEBT.md staleness
if [ -f "TECH_DEBT.md" ]; then
    LAST_MOD=$(stat -f "%m" "TECH_DEBT.md" 2>/dev/null || stat -c "%Y" "TECH_DEBT.md" 2>/dev/null || echo "0")
    NOW=$(date +%s)
    DAYS_OLD=$(( (NOW - LAST_MOD) / 86400 ))
    if [ "$DAYS_OLD" -gt 7 ]; then
        echo "[triforce-bootstrap] tech-debt: last updated $DAYS_OLD days ago"
    fi
fi
