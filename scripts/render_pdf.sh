#!/bin/bash
# Usage: render_pdf.sh deck.html "Out Name.pdf"
# Prints an HTML deck (one <section class="slide"> per 1920x1080 page, @page sized in CSS)
# to PDF with a Chromium browser in headless mode. Brave first, then Chrome, then Chromium.
set -e
HTML="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
OUT="$2"
for B in "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser" \
         "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
         "/Applications/Chromium.app/Contents/MacOS/Chromium" \
         "$(command -v chromium || true)" "$(command -v google-chrome || true)"; do
  [ -n "$B" ] && [ -x "$B" ] && break
done
[ -x "$B" ] || { echo "no Chromium-based browser found"; exit 1; }
# virtual-time-budget gives web fonts and images time to load before printing
"$B" --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=25000 \
  --run-all-compositor-stages-before-draw --print-to-pdf="$OUT" "file://$HTML" 2>&1 | grep -E "bytes written" || true
[ -s "$OUT" ] || { echo "PDF was not written"; exit 1; }
