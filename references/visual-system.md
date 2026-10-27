# Visual system

A deck needs one system decided before the slides: canvas, background and light, a small palette with one colour per section, a type scale with roles, a handful of components reused everywhere, and an icon style. Derive it from the reference study; with no reference, offer 3 to 6 directions as style drafts. Keep it consistent: the same component always looks the same, the same colour always means the same thing.

The rest of this file is the system the owner approved in Oct 2026 (a dark tech style from a UI/UX portfolio deck), as a worked example and as the default when he asks for "the same style". Its implementation lives in `assets/example-deck/build_deck.py` (every component with sample content); reuse its CSS and helpers instead of rewriting them.

## Canvas and page
- One `<section class="slide">` per page, 1920 x 1080 px, `@page { size: 1920px 1080px; margin: 0 }`, `print-color-adjust: exact`, `html dir="rtl"`.
- Outer margin about 78 px. Titles start at the start edge (right in RTL).

## Light
- Near-black base per section (#000104 blue, #040100 amber, #000202 teal).
- Silky bands entering from two opposite edges: thick blurred SVG paths (`feGaussianBlur` 90 and about 42) in the section's deep, mid and bright colours. Never a centred blob. A soft ellipse of the mid colour may sit behind a device group as backlight.
- One light colour per section, kept on every slide of that section (the example used blue, amber and teal). Section bar colours: #1d5c95, #b0581d, #2f7f86.

## Type (Arabic example)
- Display words (hero, section bars, card titles): "Mohawla Typeface" (commercial; the example falls back to the free "Lalezar"). It draws the digit 4 wrongly, so write numbers inside it in words, or set the number in the body font.
- Everything else: "Tajawal" 500 to 800. Body at least 26 to 30 px; slide titles 56 to 64 px; big numbers 80 to 120 px.
- Use installed font family names; loading system fonts through file `@font-face` failed in print.

## Components
- **Section bar:** a pill flush to the start edge, top 64 px, height 118 px, gradient from the solid section colour to transparent along its length, condensed text "Section | slide subject".
- **Gradient cards:** radius about 50 px, no borders, lit from the bottom: navy `#010102 > #182433 > #2a3b50 > #24476b`. The recommended item uses the orange version `#4a240c > #763f18 > #c47a45 > #f2883d`.
- **Staircase cards** for anything that grows step by step: levels, plans, stages (see layout-logic.md for the rules).
- **Process panel:** one wide rounded panel (orange top, black middle, navy bottom), peach icon circles (#feefe8 to #ffd7c1) with orange line icons (#e8833d), chevrons pointing in reading direction.
- **Phones:** CSS silver frame (`.phone`, aspect 1080/2310, radius 15% / 7%) with the screenshot inside and its status bar cropped by a negative top margin. Groups of three: the middle one larger and in front, the side ones rotated about 7 degrees and dimmed (`filter: brightness(.8)`).
- **Service chips:** dark translucent pills with a coloured line icon; one colour per service, the same colour everywhere in the deck.
- **Tags:** small pills in the item's line ("+ add-on name"), one colour for all add-on tags.

## Print gotchas (Chromium print to PDF)
- `box-shadow` with blur prints as hard rectangles: use blurred divs or SVG filters instead.
- `perspective` and `rotateY` can print as black boxes: use 2D `rotate` only.
- SVG blur filters need `filterUnits="userSpaceOnUse"` with a big region (for example x=-600 y=-600 width=3120 height=2280) or the glow is clipped to a hard edge.
- Class names are global: a generic class reused on two slides (`.ph` for phases and for photo tiles) silently breaks one of them. Prefix per slide.
- Absolutely positioned children in RTL take their static position from the right: give an explicit `left: 0` before `translateX(-50%)` centring.
- Bidi: keep product names on one line with non-breaking spaces ("Google Play", "App Store"); never put `direction: ltr` on Arabic text; write ranges in words ("من 15 إلى 30 بالمئة") when a percent sign lands on the wrong side.
- A 30-slide deck with many SVG blurs prints at about 45 MB. Also deliver a light copy (`scripts/lite_pdf.swift`, scale 1.25, JPEG 0.8, about 7 MB) for WhatsApp and email.
