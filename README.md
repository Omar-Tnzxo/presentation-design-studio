# Presentation Design Studio

An agent skill that designs professional presentations and slide decks as print-ready PDFs, Arabic (RTL) first and usable in any language. It works for any topic: a portfolio, a pitch, a case study, a report, a proposal or a course.

It teaches your coding agent the process a careful designer follows:

- **Study the reference to the pixel.** Measure the reference deck (colours, type scale, components) and write it down before designing.
- **Decide in gates.** Show 3 to 6 style drafts, then a few sample slides, and build the rest only after the owner approves.
- **One visual system.** Edge light, section colours, a type scale with roles and a small set of reused components. A dark tech style is included as a worked example.
- **Physical and logical layout.** Arrows come from above and land on their target, badges crown their card, steps rise in reading direction, and nothing sits on or under anything without a reason.
- **Text anyone can follow.** When the agent writes the copy, it uses plain words, one name per thing and one idea per slide, explains every symbol before using it, and moves detail to an appendix.
- **Review before delivery.** The agent renders every page and looks at it, runs an audit, and asks a fresh agent to read the deck as its least and most prepared readers.

## Install

With the [skills CLI](https://github.com/vercel-labs/skills) (Claude Code, Codex, Cursor, Gemini CLI and other agents):

```bash
npx skills add Omar-Tnzxo/presentation-design-studio
```

Or copy this folder into your agent's skills directory, for example `~/.claude/skills/presentation-design-studio`.

## Use

Ask your agent for a deck, for example: "Make an Arabic presentation of my portfolio in the style of this reference" or "Review this deck: will a non-technical reader understand it?". The skill loads when the request fits.

## What is inside

| Path | Purpose |
|---|---|
| `SKILL.md` | The workflow, gates and rules |
| `references/` | Reference study, visual system, layout logic, text clarity, review and rendering |
| `scripts/render_pdf.sh` | HTML slides to PDF with Brave or Chrome in headless mode |
| `scripts/pdf_pages.swift` | Every PDF page to JPG for visual checks |
| `scripts/contact_sheet.swift` | Slides side by side |
| `scripts/deck_audit.py` | Words, numbers, jargon, double names and dashes per slide |
| `scripts/blur.swift` | Blur personal data in screenshots |
| `scripts/lite_pdf.swift` | A light PDF for messaging apps |
| `assets/example-deck/` | A 9-slide example with every component, plus the measured style study behind it |

## Requirements

- A Chromium-based browser (Brave, Chrome or Chromium) for rendering.
- macOS for the Swift helpers (they use PDFKit, AppKit and Core Image); `deck_audit.py` needs only Python 3.
- Fonts: the example uses Tajawal and Lalezar from Google Fonts, and an installed "Mohawla Typeface" first when available.

## Credits

The example style was measured from a public UI/UX portfolio deck on Behance; the study in `assets/example-deck/STYLE-STUDY.md` names its source.

Created by [Omar-Tnzxo](https://github.com/Omar-Tnzxo). Licensed under Apache-2.0.
