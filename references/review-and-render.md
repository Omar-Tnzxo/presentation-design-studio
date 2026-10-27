# Render, look, review, deliver

## Render and look
1. Build the HTML (generator or hand edit), then `scripts/render_pdf.sh deck.html "Out.pdf"`.
2. `swift scripts/pdf_pages.swift Out.pdf pages/` renders every page to JPG.
3. Put two or three slides side by side with `swift scripts/contact_sheet.swift sheet.jpg 560 pages/p3.jpg pages/p4.jpg` and read every changed slide, every round. Look for overlaps, overflow, clipped glows, wrong bidi order, labels running into neighbours, and the layout-logic rules.
4. `python3 -I scripts/deck_audit.py deck.html` lists per slide the words, numbers, Latin words and jargon, plus double names and dashes. Pass extra terms to flag as arguments. Slides marked HEAVY are candidates for a split or the appendix.

## Audience-eye review
When the deck is otherwise finished, or the user asks "will people understand this?", get a read that is not anchored on yours: give a fresh subagent only the page images and a brief like this, adapted to the real audience.

> Read every slide image in order, as two real readers of this deck, separately: [the least prepared reader, e.g. a 55-year-old businessman, not technical, who reads Arabic slowly] and [the most demanding one, e.g. a 28-year-old expert in the field]. Report only what would confuse, overwhelm or lose them, or look unprofessional. A: words they would not understand (exact text, slide number, plain replacement). B: slides where a reader gets lost. C: numbers or claims that are unclear or contradict between slides. D: anything that reduces trust (borrowed material passing as own, inconsistent terms, typos). E: top 10 fixes ranked by impact. Under 900 words.

Verify each finding against the source before reporting it to the user, present the fixes with a recommendation, and apply them after he agrees.

## Deliver
- English, professional file names (for example "Portfolio 2026.pdf" or "<Project> Presentation.pdf") and the same title in the HTML `<title>` so PDF viewers show it. Remove superseded copies you generated.
- Deliver the full PDF and a light copy: `swift scripts/lite_pdf.swift Out.pdf "Out (Light).pdf" 1.25 0.8`.
- Before calling it done: search the source for the em and en dash, re-render, and check the pages that changed.
