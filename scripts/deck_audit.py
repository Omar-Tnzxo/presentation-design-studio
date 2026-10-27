"""Usage: python3 -I deck_audit.py deck.html [extra_term ...]

Per slide: word count, number count, Latin words, and plain-language red flags.
Also reports one thing named two ways and the em or en dash. It points at slides to
look at; it does not judge them.
"""
import html
import re
import sys

# app jargon a non-technical reader stumbles on (Arabic decks); extend per project
JARGON = ["بروفايل", "الشات", "الترويج", "التراجع", "مؤشر القراءة", "البروموكود", "الإحالة",
          "بمكافأة", "الوسائط", "الكود المصدري", "شغّالة", "افتراضيًا", "السيرفر", "OTP", "MVP"]
# pairs that must not both appear: the same thing under two names
PAIRS = [("لوحة التحكم", "لوحة الإدارة"), ("الشات", "المحادثة"), ("بروفايل", "الملف الشخصي")]


def slides(path):
    s = open(path, encoding="utf-8").read()
    for sec in re.findall(r'<section class="slide[^"]*"[^>]*>(.*?)</section>', s, re.S):
        t = re.sub(r"<svg.*?</svg>", " ", sec, flags=re.S)
        t = html.unescape(re.sub(r"<[^>]+>", " ", t))
        yield re.sub(r"\s+", " ", t).strip()


def main():
    terms = JARGON + sys.argv[2:]
    texts = list(slides(sys.argv[1]))
    whole = " ".join(texts)
    for i, t in enumerate(texts, 1):
        words, nums = len(t.split()), len(re.findall(r"\d[\d,.]*", t))
        latin = sorted(set(re.findall(r"[A-Za-z][A-Za-z.]+", t)))
        flags = [w for w in terms if w in t]
        heavy = " HEAVY" if words > 180 or nums > 30 else ""
        print(f"{i:02d} words={words:4d} nums={nums:3d}{heavy} latin={' '.join(latin)} jargon={'، '.join(flags)}")
    for a, b in PAIRS:
        if a in whole and b in whole:
            print(f"!! two names for one thing: {a} ({whole.count(a)}) / {b} ({whole.count(b)})")
    dashes = whole.count("—") + whole.count("–")
    if dashes:
        print(f"!! {dashes} em/en dash characters")


if __name__ == "__main__":
    main()
