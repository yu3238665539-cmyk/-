#!/usr/bin/env bash
# 一键把当前改动提交并推到 GitHub
set -euo pipefail

cd "$(dirname "$0")"

MSG="${1:-Update heritage-hhr on $(date '+%Y-%m-%d %H:%M')}"

git add -A
if git diff --cached --quiet; then
  echo "没有新改动，无需推送。"
  exit 0
fi

git -c user.name='yu3238665539-cmyk' \
    -c user.email='yu3238665539-cmyk@users.noreply.github.com' \
    commit -m "$MSG"

git push origin main
echo "已推送到: https://github.com/yu3238665539-cmyk/-"
