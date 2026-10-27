---
name: presentation-design-studio
description: Design and build a professional presentation or slide deck delivered as a print-ready PDF, on any topic (portfolio, pitch, case study, report, proposal, course), Arabic RTL or any language. It covers studying a reference deck to the pixel, style drafts, a coherent visual system, physical and logical layout rules, clear text any reader can follow when Claude writes the copy, an audience-eye review and HTML-to-PDF rendering. Use when the user wants slides or a deck designed, restyled like a reference, or reviewed for design quality, logic or clarity. Not for editable .pptx files. Created by Omar-Tnzxo.
author: Omar-Tnzxo
metadata:
  author: Omar-Tnzxo
  version: "1.1.0"
  created: "2026-10-28"
  updated: "2026-10-28"
---

# Presentation Design Studio

Author: Omar-Tnzxo. Distilled from an Arabic deck built in Oct 2026 on the visual language of a Behance UI/UX portfolio presentation; the owner approved its design after several rounds of corrections, and those corrections are the rules below.

The goal is a deck that looks designed by a professional and that any reader can follow alone: one idea per slide, a clear order, nothing on the page without a reason. Work in gates: study and propose, the user decides, then build. The user decides the style, the wording he cares about and anything that goes to his audience.

## Workflow

1. **Brief.** Topic, audience (who reads it, how technical, which language and register), the reference deck if any, the author or sender name, and whether Claude writes the text or the user supplies it. Ask about facts you do not have; never fill them with guesses.
2. **Reference study.** When there is a reference, measure it before designing and write `STYLE-STUDY.md`: [references/reference-study.md](references/reference-study.md).
3. **Style drafts (gate).** 3 to 6 drafts of the cover and contents as one PDF; the user picks. Then 3 to 4 representative slides; the user approves. Build the rest only after that, keeping approved slides unchanged.
4. **Build.** Visual system and print rules: [references/visual-system.md](references/visual-system.md), with a working implementation in `assets/example-deck/`. Layout must make physical and logical sense: [references/layout-logic.md](references/layout-logic.md).
5. **Text.** When Claude writes or edits the copy, follow [references/content-clarity.md](references/content-clarity.md). When the user supplies the text, keep it and only point out what a reader may not understand.
6. **Look, review, deliver.** Render, look at every changed slide, run the audit, get an audience-eye review before the final delivery, then deliver: [references/review-and-render.md](references/review-and-render.md).

## Rules that came from the owner's corrections

- Study the reference with measurements; "it looks similar" is not a study, and the owner notices.
- Every element must make physical and logical sense: an arrow comes from above and lands on its target, a badge crowns its card, steps and charts rise in reading direction, nothing sits under or over something without a reason, and slide order follows the contents slide.
- Big, confident type and full slides; one dominant element per slide; no empty halves.
- Everything the reader needs is in the main flow in plain words; exhaustive or technical material goes to an appendix.
- Borrowed images (other people's apps, sites or work) are labelled as illustration; personal data in them is blurred.
- When the owner flags one flaw, fix every instance of that class of flaw in the deck.
- Ask before changing anything the owner already approved; apply directly what he explicitly instructs.
- Never write the em dash or en dash anywhere.

## Tools (macOS)

| Script | Use |
|---|---|
| `scripts/render_pdf.sh deck.html out.pdf` | HTML slides to PDF with Brave or Chrome headless |
| `swift scripts/pdf_pages.swift out.pdf dir [scale]` | every page to JPG for looking |
| `swift scripts/contact_sheet.swift sheet.jpg height a.jpg b.jpg ...` | slides or images side by side |
| `python3 -I scripts/deck_audit.py deck.html [term ...]` | words, numbers, Latin words, jargon, double names, dashes per slide |
| `swift scripts/blur.swift in.png out.jpg width x,y,w,h ...` | blur personal data in a screenshot, resize for the deck |
| `swift scripts/lite_pdf.swift in.pdf out.pdf 1.25 0.8` | light PDF for messaging apps |

`assets/example-deck/` is a worked example of the approved style with neutral sample content: `build_deck.py` writes a 9-slide `deck.html` showing every component (edge light, section bars, cover, contents cards, process panel, phone trio with mock screens, staircase with arrows and a crown badge, add-on grid, timeline with payment pins, table with a highlighted column, closing), and `STYLE-STUDY.md` is the measured reference study behind it. Copy it into the new project and replace the content.
