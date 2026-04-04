#!/usr/bin/env bash
# One-time setup after cloning. Configures git hooks and initializes submodules
# and external synced directories.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

echo "==> Pointing git hooks at .githooks/"
git config core.hooksPath .githooks
chmod +x .githooks/*

echo "==> Initializing submodules"
git submodule update --init --recursive

# Source our new helper
source .githooks/sync-subdir.sh

# Sync our external subdirectories
sync_subdir "https://github.com/mattpocock/skills.git" --prefix="tdd" --target="skills/tdd"

echo ""
echo "Setup complete."
echo "  - Git hooks active from .githooks/"
echo "  - External directories synced"
