#!/usr/bin/env bash
# Syncs canonical source files to the plugin distribution directory.
# Run this after editing any agent, skill, or tool file.
#
# Usage:
#   ./scripts/sync-plugin.sh          # sync all files
#   ./scripts/sync-plugin.sh --check  # check for drift (exit 1 if out of sync)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PLUGIN_DIR="$REPO_ROOT/agent-triforce"

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

# Define all source → plugin mappings
declare -a AGENTS=(
  "prometeo-pm"
  "forja-dev"
  "centinela-qa"
)

declare -a SKILLS=(
  "feature-spec"
  "implement-feature"
  "review-findings"
  "security-audit"
  "code-health"
  "release-check"
  "generate-tests"
  "checklist-health"
  "simulate-failure"
  "traceability"
  "reindex"
)

declare -a TOOLS=(
  "dashboard.py"
  "security-scanner.py"
  "handoff-generator.py"
  "workflow-tracker.py"
  "gate-checker.py"
  "memory-sync.py"
  "traceability.py"
  "session-tracker.py"
  "codebase-indexer.py"
)

check_mode=false
if [[ "${1:-}" == "--check" ]]; then
  check_mode=true
fi

drift_count=0

sync_file() {
  local src="$1"
  local dst="$2"

  if [[ ! -f "$src" ]]; then
    echo -e "${RED}MISSING${NC} $src"
    drift_count=$((drift_count + 1))
    return
  fi

  if [[ ! -f "$dst" ]]; then
    if $check_mode; then
      echo -e "${RED}DRIFT${NC} $dst (missing)"
      drift_count=$((drift_count + 1))
    else
      mkdir -p "$(dirname "$dst")"
      cp "$src" "$dst"
      echo -e "${GREEN}CREATED${NC} $dst"
    fi
    return
  fi

  if ! diff -q "$src" "$dst" > /dev/null 2>&1; then
    if $check_mode; then
      echo -e "${RED}DRIFT${NC} $dst"
      drift_count=$((drift_count + 1))
    else
      cp "$src" "$dst"
      echo -e "${GREEN}SYNCED${NC} $dst"
    fi
  else
    if ! $check_mode; then
      echo "  OK    $dst"
    fi
  fi
}

echo "=== Agent Triforce Plugin Sync ==="
echo ""

echo "Agents:"
for agent in "${AGENTS[@]}"; do
  sync_file "$REPO_ROOT/.claude/agents/$agent.md" "$PLUGIN_DIR/agents/$agent.md"
done

echo ""
echo "Skills:"
for skill in "${SKILLS[@]}"; do
  sync_file "$REPO_ROOT/.claude/skills/$skill/SKILL.md" "$PLUGIN_DIR/skills/$skill/SKILL.md"
done

echo ""
echo "Tools:"
for tool in "${TOOLS[@]}"; do
  sync_file "$REPO_ROOT/tools/$tool" "$PLUGIN_DIR/tools/$tool"
done

echo ""
if $check_mode; then
  if [[ $drift_count -gt 0 ]]; then
    echo -e "${RED}$drift_count file(s) out of sync. Run ./scripts/sync-plugin.sh to fix.${NC}"
    exit 1
  else
    echo -e "${GREEN}All plugin files are in sync.${NC}"
    exit 0
  fi
else
  echo -e "${GREEN}Sync complete.${NC}"
fi
