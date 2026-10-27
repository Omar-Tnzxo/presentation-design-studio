# Studying a reference deck to the pixel

The owner judges the deck against the reference he sent. "You did not study the reference enough" came twice before the measured study below was made. A study is measured numbers, not adjectives.

## Get every slide locally
- Behance and similar pages load slides lazily: open the project in the browser, scroll to the end so every image loads, then collect the full-size image URLs from the page (`img` `src`/`srcset`, largest variant) with a script in the page and download them into their own folder.
- Make contact sheets (`scripts/contact_sheet.swift`) of 6 to 8 slides per row to see the rhythm of the whole deck, then open single slides full size for detail.

## Measure, then write it down
Write a `STYLE-STUDY.md` next to the deck before building. `assets/example-deck/STYLE-STUDY.md` is a finished one; match its depth.

1. **Canvas.** Source width, the scale to the 1920 x 1080 canvas, outer margins.
2. **Background and light.** Sample pixels (a tiny Swift or Python script reading pixel values at chosen points) for the base black and every glow colour. Note where the light enters (edges, never a centred blob), how many bands, how wide, and which colour belongs to which section.
3. **Type scale.** Measure cap heights of the hero word, section words, card titles, slide titles, numbers, labels and body text, and convert them to the 1920 canvas. Then map each role to an installed font for the target script (Arabic example: a condensed display face such as "Mohawla Typeface" for hero and section words, "Tajawal" for everything else).
4. **Components.** For each repeated component (section bar, gradient cards, staggered cards, process panel, device mockups, translucent content cards), record shape, radius, gradient stops with colours, what overlaps what, and spacing.
5. **What it means for our deck.** Five to eight short rules, including mirroring for RTL (start edge becomes the right).

## Show drafts before building
- Show 3 to 6 style drafts of the first two slides (cover and contents) as one PDF, different enough to be real choices. The owner picks and comments; only then build more.
- After the pick, build 3 to 4 representative slides (cover, contents, one data or comparison slide, one process slide), get approval, and only then the full deck. Keep the approved slides byte-identical when the rest is generated (for example, keep them in a hand-edited `draft.html` and have the generator copy their `<section>` blocks unchanged).
- When the owner sends a screenshot or names a flaw ("the rings cover the letter", "dark shadow behind the object"), fix that instance and then search the whole deck for the same class of flaw.
