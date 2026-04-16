#!/usr/bin/env bash
# One-time setup after cloning. Configures git hooks and initializes submodules
# and external synced directories.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

echo "==> Pointing git hooks at .githooks/"
git config --local core.hooksPath .githooks
chmod +x .githooks/*

echo "==> Initializing submodules (if any)"
git submodule update --init --recursive || true

echo "==> Executing .githooks/post-merge once"
./.githooks/post-merge

echo ""
echo "Setup complete."
echo "  - Git hooks active from .githooks/"
echo "  - External directories synced"
