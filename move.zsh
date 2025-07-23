#!/usr/bin/env zsh
set -eux

# --- 1. create target dirs ----------------------------------------------------
dirs=(agents code product strategy)
for d in $dirs; do
  mkdir -p "$d"
done

# --- 2. define file groups ----------------------------------------------------
typeset -a agents_files=(
  assistant.apr24.yaml
  assistant.yaml
  feai.yaml
  none.yaml
  pyai.yaml
  pycmd.yaml
  zshai.yaml
  zshcmd.yaml
  researcher.yaml
  lexer.yaml
  gold_nuggets/websearch-assistant.yaml
  gold_nuggets/gemini-system-prompt.md
  gold_nuggets/analyze-stock-industry.yaml
)

typeset -a code_files=(
  merge.yaml
  readable.yaml
  simplify.yaml
  refactor.yaml
  gold_nuggets/detect-duplication.yaml
  gold_nuggets/breakdown-feature.md
  gold_nuggets/capture-code-author-intent.md
  gold_nuggets/clear_text_definition.yaml
  gold_nuggets/compress-history-2.md
  gold_nuggets/compress-history.md
  gold_nuggets/humanlike-writing.md
  gold_nuggets/transcribe.yaml
  .compress_base.yaml
)

typeset -a product_files=(
  create-prd.yaml
  gold_nuggets/mvp-definition.yaml
)


# --- 3. move files ------------------------------------------------------------
for fp in $agents_files;   do [[ -e $fp ]] && mv "$fp" agents/;   done
for fp in $code_files;     do [[ -e $fp ]] && mv "$fp" code/;     done
for fp in $product_files;  do [[ -e $fp ]] && mv "$fp" product/;  done

# --- 4. clean up empty directory if nothing left ------------------------------
rmdir -p gold_nuggets 2>/dev/null || true
set +x