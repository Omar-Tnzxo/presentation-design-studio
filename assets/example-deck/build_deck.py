"""Example deck: every component of the dark tech system with neutral sample content.

Run `python3 -I build_deck.py` to write deck.html next to this file, then print it with
scripts/render_pdf.sh. Replace the sample text and the CSS phone mock screens with real
content (screenshots go in <img> tags inside .scr, see phone()). Fonts: Tajawal and Lalezar
load from Google Fonts; an installed "Mohawla Typeface" is used first for display words.
"""
from pathlib import Path

HERE = Path(__file__).parent

# ---------------------------------------------------------------- light and section bars
PAL = {  # one light colour per section; bar = solid colour of the section bar
    "blue":  {"deep": "#001e57", "mid": "#003a61", "bright": "#006ea0", "accent": "#0084a9", "bar": "29,92,149", "bg": "#000104"},
    "amber": {"deep": "#3c2600", "mid": "#5e3c00", "bright": "#8e5301", "accent": "#8e5301", "bar": "176,88,29", "bg": "#040100"},
    "teal":  {"deep": "#0b3438", "mid": "#15585d", "bright": "#3d898f", "accent": "#2c7a80", "bar": "47,127,134", "bg": "#000202"},
}
_n = [0]


def light(pal, variant="a", glow=None):
    """Silky bands entering from two opposite edges (never a centred blob).
    a: top right + bottom left, b: top left + bottom right. glow=(x, y, rx, ry) backlights a device group."""
    p = PAL[pal]; _n[0] += 1; f = f"f{_n[0]}"
    region = 'filterUnits="userSpaceOnUse" x="-600" y="-600" width="3120" height="2280"'  # or the glow clips
    out = (f'<svg class="light" viewBox="0 0 1920 1080" aria-hidden="true"><defs>'
           f'<filter id="{f}a" {region}><feGaussianBlur stdDeviation="90"/></filter>'
           f'<filter id="{f}b" {region}><feGaussianBlur stdDeviation="42"/></filter></defs>')
    if variant == "a":
        out += (f'<path d="M1500 -150 C 1700 150, 1820 400, 2080 520" stroke="{p["mid"]}" stroke-width="380" fill="none" filter="url(#{f}a)"/>'
                f'<path d="M1600 -120 C 1780 140, 1880 360, 2060 430" stroke="{p["bright"]}" stroke-width="130" fill="none" filter="url(#{f}b)" opacity=".8"/>'
                f'<path d="M-240 560 C 80 700, 160 920, 120 1260" stroke="{p["deep"]}" stroke-width="420" fill="none" filter="url(#{f}a)"/>'
                f'<path d="M-140 760 C 90 840, 170 980, 160 1200" stroke="{p["accent"]}" stroke-width="110" fill="none" filter="url(#{f}b)" opacity=".7"/>')
    else:
        out += (f'<path d="M420 -160 C 220 120, 100 360, -160 480" stroke="{p["mid"]}" stroke-width="380" fill="none" filter="url(#{f}a)"/>'
                f'<path d="M320 -120 C 140 140, 40 340, -140 420" stroke="{p["bright"]}" stroke-width="120" fill="none" filter="url(#{f}b)" opacity=".75"/>'
                f'<path d="M2160 560 C 1840 700, 1760 920, 1800 1260" stroke="{p["deep"]}" stroke-width="420" fill="none" filter="url(#{f}a)"/>'
                f'<path d="M2060 780 C 1830 860, 1760 990, 1770 1200" stroke="{p["accent"]}" stroke-width="100" fill="none" filter="url(#{f}b)" opacity=".6"/>')
    if glow:
        x, y, rx, ry = glow
        out += f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{p["mid"]}" filter="url(#{f}a)" opacity=".9"/>'
    return out + "</svg>"


def bar(pal, text):
    c = PAL[pal]["bar"]
    return (f'<div class="sbar" style="background:linear-gradient(270deg,rgb({c}) 0%,rgba({c},.75) 40%,rgba({c},0) 100%)">'
            f'<span>{text}</span></div>')


def slide(pal, body, cls=""):
    return f'<section class="slide {cls}" style="background:{PAL[pal]["bg"]}">{body}</section>'


# ---------------------------------------------------------------- icons, chips, tags
ICON = {
    "design": '<path d="M12 3a9 9 0 1 0 0 18c1 0 1.6-.8 1.6-1.6 0-.5-.2-.8-.5-1.1-.3-.3-.5-.7-.5-1.1 0-.9.7-1.6 1.6-1.6H16a5 5 0 0 0 5-5C21 6.6 17 3 12 3z"/><circle cx="7.5" cy="11" r="1"/><circle cx="10" cy="7.5" r="1"/><circle cx="14.5" cy="7.5" r="1"/>',
    "app": '<rect x="6" y="2.5" width="12" height="19" rx="3"/><path d="M10.5 18.5h3"/>',
    "db": '<ellipse cx="12" cy="5.5" rx="7.5" ry="2.8"/><path d="M4.5 5.5v13c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8v-13"/><path d="M4.5 12c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8"/>',
    "bell": '<path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20a2 2 0 0 0 4 0"/>',
    "user": '<circle cx="9" cy="8" r="4"/><path d="M2 21c0-3.9 3.1-7 7-7s7 3.1 7 7"/><path d="M19 8v6M16 11h6"/>',
    "list": '<path d="M9 6h11M9 12h11M9 18h11"/><path d="M3 6l1.5 1.5L7 5M3 12l1.5 1.5L7 11M3 18l1.5 1.5L7 17"/>',
    "card": '<rect x="5" y="3" width="14" height="18" rx="3"/><circle cx="12" cy="10" r="3"/><path d="M8 17c.8-1.6 2.3-2.5 4-2.5s3.2.9 4 2.5"/>',
    "heart": '<path d="M12 20s-6.5-3.9-8.3-7.9C2.6 9.4 4.4 6 7.5 6c1.8 0 3 1 4.5 2.6C13.5 7 14.7 6 16.5 6c3.1 0 4.9 3.4 3.8 6.1C18.5 16.1 12 20 12 20z"/>',
    "chat": '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/><path d="M8.5 12h.01M12 12h.01M15.5 12h.01"/>',
    "crown": '<path d="M3 8l4.5 4L12 5l4.5 7L21 8l-2 11H5z"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    "shield": '<path d="M12 2.5l8 3v6c0 5-3.4 8.6-8 10-4.6-1.4-8-5-8-10v-6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
}
SVC = {  # one colour per service, the same everywhere in the deck
    "ux": ("التصميم", "#f2883d", "design"), "app": ("التطبيق", "#54c5f8", "app"),
    "db": ("قاعدة البيانات", "#3ecf8e", "db"), "push": ("الإشعارات", "#ffca28", "bell"),
    "sec": ("الأمان", "#ff8a65", "shield"),
}


def icon(name, color, size=34, sw=1.8):
    return (f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[name]}</svg>')


def chips(keys):
    return ('<div class="svc"><div class="svc-l">الخدمات خلف الشاشة</div><div class="chips">'
            + "".join(f'<span class="chip">{icon(SVC[k][2], SVC[k][1], 26, 2)}{SVC[k][0]}</span>' for k in keys) + "</div></div>")


def tag(name):  # names an optional module; the legend explains (+) once per slide that uses it
    return f'<i class="tg">+ {name}</i>'


# ---------------------------------------------------------------- phones with mock screens
def screen(kind):
    """CSS skeleton of an app screen. Replace with <img src="assets/....jpg"> of a real screenshot."""
    rows = {
        "list": '<div class="sk-h"></div>' + "".join('<div class="sk-row"><i></i><b></b></div>' for _ in range(6)),
        "card": '<div class="sk-h"></div><div class="sk-hero"></div><div class="sk-chips"><i></i><i></i><i></i></div><b class="sk-l"></b><b class="sk-l s"></b>',
        "form": '<div class="sk-h"></div><b class="sk-t"></b>' + "".join('<div class="sk-in"></div>' for _ in range(3)) + '<div class="sk-btn"></div>',
    }[kind]
    return f'<div class="mock">{rows}</div>'


def phone(kind, left, top, width, rot=0, back=False):
    return (f'<div class="phone{" back" if back else ""}" style="left:{left}px;top:{top}px;width:{width}px;transform:rotate({rot}deg)">'
            f'<div class="island"></div><div class="scr">{screen(kind)}</div></div>')


def trio(a, b, c, x0=96):
    """Three screens in reading order (RTL: a on the right). The middle one is larger and in front; the
    back ones are rotated and dimmed so depth reads physically."""
    return phone(c, x0, 312, 290, -7, True) + phone(a, x0 + 560, 312, 290, 7, True) + phone(b, x0 + 262, 236, 340)


# ---------------------------------------------------------------- slides
S = []

S.append(slide("blue", light("blue", "a") + """
<div class="who">اسم المؤلف<br>2026</div>
<div class="pre">عرض تقديمي</div>
<div class="giant">مسار</div>
<svg class="orbit" viewBox="0 0 800 520" aria-hidden="true">
  <defs><linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff3c4"/><stop offset=".45" stop-color="#d9a441"/><stop offset="1" stop-color="#8a5a12"/></linearGradient></defs>
  <ellipse cx="300" cy="300" rx="230" ry="150" fill="none" stroke="url(#gold)" stroke-width="34" transform="rotate(-18 300 300)"/>
  <ellipse cx="500" cy="260" rx="230" ry="150" fill="none" stroke="url(#gold)" stroke-width="34" transform="rotate(16 500 260)"/>
</svg>
<div class="sub"><b>تطبيق لتنظيم المذاكرة</b> · مثال توضيحي<br>Android و iOS · العربية والإنجليزية</div>""", "cover"))

CONTENTS = [("الفكرة", "المشكلة التي يحلها التطبيق ولمن.", "list"), ("رحلة<br>المستخدم", "من التسجيل حتى أول خطة.", "user"),
            ("الشاشات", "كل شاشة، وما يعمل خلفها.", "app"), ("المستويات", "كيف تكبر المزايا خطوة بخطوة.", "crown"),
            ("خطة<br>العمل", "أربع مراحل على 13 أسبوعًا.", "card"), ("الأسئلة", "ما نحتاج أن نتفق عليه.", "chat")]
S.append(slide("blue", light("blue", "b") + '<h1 class="ctitle">المحتويات</h1><div class="cgrid">' + "".join(
    f'<div class="ccard"><h3>{t}</h3><p>{d}</p><div class="cic">{icon(i, "#feefe8", 120, 1.4)}</div></div>' for t, d, i in CONTENTS) + "</div>", "contents"))

STEPS = [("user", "الحساب", "إيميل وكلمة مرور<br>وكود تحقق"), ("list", "الأهداف", "المواد والمواعيد<br>ووقت المذاكرة"),
         ("card", "الخطة", "جدول يومي<br>يتعدّل تلقائيًا"), ("heart", "التقدّم", "علامة لكل مهمة<br>ونسبة إنجاز"),
         ("chat", "التذكير", "إشعار قبل<br>كل جلسة"), ("crown", "المستوى", "مزايا إضافية<br>لمن يشترك")]
chev = '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="#ffd7c1" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg>'
S.append(slide("amber", light("amber", "b") + '<h2 class="jtitle">رحلة المستخدم داخل التطبيق</h2><div class="panel">' + chev.join(
    f'<div class="step"><div class="circ">{icon(i, "#e8833d", 110, 1.7)}</div><div class="lbl">{n:02d} . {t}</div><div class="sub2">{d}</div></div>'
    for n, (i, t, d) in enumerate(STEPS, 1)) + "</div>", "jr"))

S.append(slide("teal", light("teal", "a", glow=(560, 640, 420, 300)) + bar("teal", "الشاشات | الخطة اليومية") + '<div class="dev3">' + trio("form", "card", "list") + """</div>
<div class="info"><h2>الخطة اليومية</h2><p class="lede">يرى الطالب مهام اليوم مرتبة حسب الوقت، ويعلّم ما أنجزه بلمسة واحدة.</p><ul class="build">
  <li>جدول يومي يتعدّل عند تأجيل أي مهمة</li><li>علامة إنجاز ونسبة تقدّم لكل مادة</li><li>تذكير قبل كل جلسة مذاكرة</li>
  <li>تقارير أسبوعية لولي الأمر """ + tag("التقارير") + """</li></ul><p class="avail">(+) ميزة تأتي مع إضافة اختيارية بنفس الاسم.</p></div>"""
          + chips(["ux", "app", "db", "push"]) + '<p class="cap">شاشات توضيحية، والتصميم النهائي خاص بالمشروع.</p>', "scr"))

TIERS = [("01", "المجاني", "خطة يومية وتذكير لكل الطلاب.", "0", "للجميع", 126, 390, ""),
         ("02", "الأساسي", "تقارير أسبوعية، ومواد بلا حد.", "49", "شهريًا", 552, 330, ""),
         ("03", "المتقدم", "خطة ذكية تتعلم من أداء الطالب.", "99", "شهريًا", 978, 270, " pick"),
         ("04", "العائلي", "حتى خمسة طلاب بحساب واحد.", "179", "شهريًا", 1404, 210, "")]
arrows = "".join(f'<path d="M{1452 - k * 426} {378 - k * 60} C {1452 - k * 426} {278 - k * 60}, {1330 - k * 426} {264 - k * 60}, {1322 - k * 426} {310 - k * 60}"/>' for k in range(3))
S.append(slide("amber", light("amber", "a") + bar("amber", "المستويات | أربع خطوات") + f"""
<svg class="light" viewBox="0 0 1920 1080" aria-hidden="true"><defs><marker id="up" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#fff"/></marker></defs>
<g fill="none" stroke="#fff" stroke-width="5" stroke-dasharray="22 14" stroke-linecap="round" marker-end="url(#up)">{arrows}</g></svg>"""
          + "".join(f'<div class="tier{c}" style="right:{r}px;top:{t}px">' + ('<span class="rec">المقترح</span>' if c else "")
                    + f'<div class="n">{n}</div><div class="nm">{nm}</div><p>{d}</p><div class="price">{pr}<small> جنيه</small></div><div class="dur">{per}</div></div>'
                    for n, nm, d, pr, per, r, t, c in TIERS)
          + '<p class="lede2">كل مستوى يشمل ما قبله، ويضيف خطوة واحدة واضحة.</p><p class="note">أسعار توضيحية لمثال فقط.</p>', "pk"))

MODS = [("التقارير", "15,000", True, ["تقرير أسبوعي لكل طالب", "إرسال التقرير لولي الأمر"]),
        ("الخطة الذكية", "25,000", True, ["ترتيب المهام حسب الأداء", "اقتراح وقت المراجعة"]),
        ("المجموعات", "20,000", True, ["مذاكرة مع الأصدقاء", "تحديات أسبوعية"]),
        ("الاشتراكات", "30,000", True, ["كل المستويات مرة واحدة", "متابعة الاشتراكات في لوحة الإدارة"]),
        ("المحتوى", "35,000", False, ["دروس قصيرة لكل مادة", "اختبارات سريعة"]),
        ("المعلمون", "40,000", False, ["حسابات للمعلمين", "متابعة الفصل كاملًا"]),
        ("الذكاء الاصطناعي", "45,000", False, ["مساعد للأسئلة", "تلخيص الدروس"]),
        ("النمو", "20,000", False, ["كود دعوة الأصدقاء", "مكافآت الاستمرار"])]
ck = icon("check", "#3a1a06", 18, 3)
S.append(slide("amber", light("amber", "b") + bar("amber", "الإضافات | اختاروا ما تحتاجونه")
               + '<p class="mlede">ابدأوا بالأساس، وأضيفوا ما تحتاجونه الآن أو لاحقًا. كل إضافة تأتي بشاشاتها وبجزئها في لوحة الإدارة.</p><div class="adg">'
               + "".join(f'<div class="ad{" rec" if r else ""}"><div class="ah"><h4>+ {n}</h4><span>{p}<small>جنيه</small></span></div>'
                         + ('<i class="in3">ضمن المقترح</i>' if r else "") + "<ul>" + "".join(f'<li><span class="ck">{ck}</span>{x}</li>' for x in items) + "</ul></div>"
                         for n, p, r, items in MODS) + '</div><p class="adnote"><b>المقترح</b> = الأساس + الإضافات الأربع المعلَّمة.</p>', "diff"))

W = 1764 / 13
PH = [(3, "البداية والتصميم", ["تحديد المواصفات", "تصميم الشاشات", "جولتا تعديل"]), (5, "البرمجة", ["السيرفر ولوحة الإدارة", "الحساب والخطة", "التذكير والتقارير"]),
      (2, "الإضافات", ["الخطة الذكية", "المجموعات"]), (3, "الاختبار والنشر", ["اختبار على موبايلات", "الرفع على المتجرين"])]
x, done, ph = 1842, 0, ""
for i, (w, name, tasks) in enumerate(PH):
    left = x - w * W
    ph += (f'<div class="ph{" last" if i == 3 else ""}" style="left:{left + 5:.0f}px;width:{w * W - 10:.0f}px"><b>0{i + 1} . {name}</b>'
           f'<span>الأسبوع {done + 1} إلى {done + w}</span></div><ul class="tk" style="left:{left + 5:.0f}px;width:{w * W - 10:.0f}px">'
           + "".join(f"<li>{t}</li>" for t in tasks) + "</ul>")
    done += w; x = left
ticks = "".join(f'<i style="left:{1842 - (k + 0.5) * W - 20:.0f}px">{k + 1}</i>' for k in range(13))
pins = "".join(f'<div class="vl" style="left:{px - 1.5:.0f}px"></div><div class="pin {al}" style="left:{px:.0f}px"><i></i><div><b>{p}</b><span>{lab}</span></div></div>'
               for px, p, lab, al in [(1842, "35%", "البداية", "r"), (1842 - 3 * W, "25%", "اعتماد التصميم", "c"),
                                      (1842 - 10 * W, "25%", "نسخة تجريبية", "c"), (78, "15%", "النشر", "l")])
S.append(slide("blue", light("blue", "a") + bar("blue", "خطة العمل | ثلاثة عشر أسبوعًا")
               + '<p class="plede">أربع مراحل متتالية، وكل دفعة مرتبطة بشيء يمكن رؤيته.</p>'
               + f'<div class="ticks">{ticks}</div>{ph}<div class="payline"></div>{pins}<div class="after">ثم ضمان شهرين</div>', "plan"))

ROWS = [("البداية", "35%", "17,500", "35,000", "52,500"), ("اعتماد التصميم", "25%", "12,500", "25,000", "37,500"),
        ("نسخة تجريبية", "25%", "12,500", "25,000", "37,500"), ("النشر", "15%", "7,500", "15,000", "22,500")]
S.append(slide("teal", light("teal", "b") + bar("teal", "الدفع | أربع دفعات") + '<div class="ptab"><div class="hl"></div><table><thead><tr><th>المرحلة</th><td>النسبة</td><td>الأساس</td><td class="pk3">المقترح</td><td>الكامل</td></tr></thead><tbody>'
               + "".join(f"<tr><th>{a}</th><td class='pc'>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>" for a, b, c, d, e in ROWS)
               + "<tr class='tot'><th>الإجمالي بالجنيه</th><td class='pc'>100%</td><td>50,000</td><td>100,000</td><td>150,000</td></tr></tbody></table></div>"
               + '<p class="note2">أرقام توضيحية لمثال فقط.</p>', "pay"))

S.append(slide("blue", light("blue", "b") + '<div class="bye">شكرًا</div><div class="byw"><b>اسم المؤلف</b><br>سطر ختامي قصير</div>', "end"))

# ---------------------------------------------------------------- css
CSS = """
  @page { size: 1920px 1080px; margin: 0; }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  :root { --display: "Mohawla Typeface", "Lalezar", sans-serif; --text: "Tajawal", sans-serif; --peach-1: #feefe8; --peach-2: #ffd7c1; }
  html, body { background: #000; }
  body { color: #fff; font-family: var(--text); font-weight: 500; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  .slide { width: 1920px; height: 1080px; position: relative; overflow: hidden; page-break-after: always; break-after: page; }
  .light { position: absolute; inset: 0; width: 1920px; height: 1080px; pointer-events: none; }
  b { font-weight: 800; }
  .sbar { position: absolute; right: 0; top: 64px; width: 1220px; height: 118px; border-radius: 999px 0 0 999px; }
  .sbar span { position: absolute; right: 78px; top: 50%; transform: translateY(-46%); font-family: var(--display); font-size: 80px; line-height: 1; white-space: nowrap; }

  .cover .who { position: absolute; left: 78px; top: 70px; text-align: left; font-size: 34px; line-height: 1.3; }
  .cover .pre { position: absolute; right: 120px; top: 228px; font-size: 80px; font-weight: 800; }
  .cover .giant { position: absolute; left: 0; right: 0; top: 230px; font-family: var(--display); font-size: 600px; line-height: 1; text-align: center; }
  .cover .orbit { position: absolute; left: 560px; top: 560px; width: 800px; }
  .cover .sub { position: absolute; right: 120px; bottom: 70px; font-size: 32px; line-height: 1.5; text-align: right; }

  .ctitle { position: absolute; right: 78px; top: 36px; font-family: var(--display); font-size: 200px; line-height: 1; font-weight: 400; }
  .cgrid { position: absolute; right: 78px; left: 78px; top: 300px; bottom: 44px; display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(2, 1fr); gap: 58px 34px; }
  .ccard { position: relative; border-radius: 50px; padding: 34px 40px 0 0; background: linear-gradient(180deg, rgba(38,120,168,.26), rgba(14,58,84,.20)); }
  .ccard h3 { font-family: var(--display); font-weight: 400; font-size: 84px; line-height: .95; }
  .ccard p { font-size: 28px; line-height: 1.4; margin-top: 14px; width: 270px; }
  .cic { position: absolute; left: 40px; top: 50%; transform: translateY(-50%); }

  .jtitle { position: absolute; right: 78px; top: 72px; font-size: 60px; font-weight: 800; }
  .panel { position: absolute; right: 78px; left: 78px; top: 196px; height: 800px; border-radius: 56px; padding-top: 150px;
           background: linear-gradient(180deg, #b5622a 0%, #8a4316 12%, #2a1206 30%, #000001 50%, #0c1a2c 68%, #223f64 100%);
           display: flex; justify-content: center; align-items: flex-start; }
  .step { width: 248px; text-align: center; }
  .circ { width: 230px; height: 230px; border-radius: 50%; margin: 0 auto; background: linear-gradient(180deg, var(--peach-1), var(--peach-2)); display: grid; place-items: center; }
  .lbl { font-size: 38px; font-weight: 800; margin-top: 40px; white-space: nowrap; }
  .sub2 { font-size: 30px; font-weight: 700; line-height: 1.5; margin-top: 20px; }
  .chev { width: 46px; height: 46px; margin-top: 92px; flex: none; }

  .phone { position: absolute; aspect-ratio: 1080 / 2310; background: linear-gradient(135deg, #f4f4f6, #b9bbc2 45%, #eceef2); border-radius: 15% / 7%; padding: 2.6%; }
  .phone.back { filter: brightness(.8); }
  .phone .scr { width: 100%; height: 100%; border-radius: 13% / 6.2%; overflow: hidden; background: #0d1116; position: relative; }
  .phone .scr img { width: 100%; display: block; margin-top: -3.9%; }
  .phone .island { position: absolute; top: 3.2%; left: 50%; width: 30%; height: 2.6%; margin-left: -15%; background: #000; border-radius: 99px; z-index: 2; }
  .mock { position: absolute; inset: 0; padding: 22% 9% 0; display: flex; flex-direction: column; gap: 4%; }
  .mock .sk-h { height: 3%; width: 45%; align-self: center; border-radius: 99px; background: #2b3542; }
  .mock .sk-row { display: flex; gap: 6%; align-items: center; }
  .mock .sk-row i { width: 16%; aspect-ratio: 1; border-radius: 50%; background: #3d898f; }
  .mock .sk-row b { flex: 1; height: 10px; border-radius: 99px; background: #2b3542; }
  .mock .sk-hero { height: 34%; border-radius: 18px; background: linear-gradient(160deg, #3d898f, #15585d); }
  .mock .sk-chips { display: flex; gap: 5%; } .mock .sk-chips i { flex: 1; height: 22px; border-radius: 99px; background: #2b3542; }
  .mock .sk-l { height: 10px; border-radius: 99px; background: #2b3542; } .mock .sk-l.s { width: 60%; }
  .mock .sk-t { height: 16px; width: 70%; border-radius: 99px; background: #3a4656; }
  .mock .sk-in { height: 34px; border-radius: 12px; border: 2px solid #2b3542; }
  .mock .sk-btn { height: 38px; border-radius: 12px; background: #f2883d; margin-top: 6%; }
  .dev3 { position: absolute; left: 0; top: 0; width: 1060px; height: 1080px; }

  .info { position: absolute; right: 78px; top: 232px; width: 720px; }
  .info h2 { font-size: 64px; font-weight: 800; line-height: 1.12; }
  .lede { font-size: 29px; line-height: 1.5; margin-top: 14px; }
  .build { list-style: none; margin-top: 22px; }
  .build li { font-size: 26px; font-weight: 700; line-height: 1.45; padding: 10px 32px 10px 0; position: relative; border-top: 1px solid rgba(255,255,255,.14); }
  .build li::before { content: ""; position: absolute; right: 4px; top: 24px; width: 14px; height: 14px; border-radius: 50%; background: #68dae7; }
  .tg { font-style: normal; display: inline-block; font-size: 20px; font-weight: 800; border-radius: 999px; padding: 2px 14px; margin-right: 8px; vertical-align: 3px; white-space: nowrap; background: #f2883d; color: #2b1404; }
  .avail { font-size: 22px; font-weight: 700; opacity: .7; margin-top: 12px; }
  .svc { position: absolute; right: 78px; bottom: 50px; width: 720px; }
  .svc-l { font-size: 22px; font-weight: 700; opacity: .75; }
  .chips { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 12px; }
  .chip { display: inline-flex; align-items: center; gap: 10px; font-size: 24px; font-weight: 800; padding: 10px 20px 10px 18px; border-radius: 999px; background: rgba(255,255,255,.08); }
  .cap { position: absolute; left: 96px; bottom: 30px; font-size: 20px; font-weight: 700; opacity: .6; }

  .tier { position: absolute; width: 392px; height: 520px; border-radius: 50px; padding: 40px; background: linear-gradient(180deg, #010102 0%, #182433 38%, #2a3b50 62%, #24476b 100%); }
  .tier.pick { background: linear-gradient(180deg, #4a240c 0%, #763f18 22%, #c47a45 55%, #f2883d 100%); }
  .tier .rec { position: absolute; top: 0; left: 50%; transform: translate(-50%, -50%); white-space: nowrap; font-size: 26px; font-weight: 800; background: #fff; color: #3a1a06; border-radius: 999px; padding: 8px 26px; }
  .tier .n { font-size: 116px; font-weight: 800; line-height: .95; }
  .tier .nm { font-size: 46px; font-weight: 800; margin-top: 6px; }
  .tier p { font-size: 28px; line-height: 1.42; margin-top: 14px; }
  .tier .price { font-size: 80px; font-weight: 800; line-height: 1; margin-top: 22px; }
  .tier .price small { font-size: 32px; }
  .tier .dur { font-size: 26px; margin-top: 8px; }
  .lede2 { position: absolute; right: 78px; bottom: 40px; font-size: 30px; }
  .note, .note2 { position: absolute; left: 78px; bottom: 44px; font-size: 22px; opacity: .8; }

  .mlede { position: absolute; right: 78px; top: 222px; width: 1764px; font-size: 29px; line-height: 1.5; }
  .adg { position: absolute; right: 78px; left: 78px; top: 300px; bottom: 120px; display: grid; grid-template-columns: repeat(4, 1fr); grid-template-rows: 1fr 1fr; gap: 22px; }
  .ad { border-radius: 36px; padding: 24px 26px; background: linear-gradient(180deg, #010102 0%, #182433 45%, #24476b 100%); }
  .ad.rec { background: linear-gradient(180deg, #2a1206 0%, #5a2e10 45%, #a85d2a 100%); }
  .ad .ah { display: flex; justify-content: space-between; align-items: flex-start; gap: 10px; }
  .ad h4 { font-size: 28px; font-weight: 800; }
  .ad .ah span { flex: none; text-align: center; font-size: 22px; font-weight: 800; background: rgba(0,0,0,.32); border-radius: 18px; padding: 6px 12px; line-height: 1.2; }
  .ad .ah small { display: block; font-size: 18px; opacity: .85; }
  .ad .in3 { display: inline-block; font-style: normal; font-size: 17px; font-weight: 800; background: #ffd7c1; color: #3a1a06; border-radius: 999px; padding: 2px 12px; margin-top: 8px; }
  .ad ul { list-style: none; margin-top: 10px; }
  .ad li { display: flex; align-items: flex-start; gap: 10px; font-size: 22px; font-weight: 700; line-height: 1.35; padding: 4px 0; }
  .ck { flex: none; width: 28px; height: 28px; border-radius: 50%; background: linear-gradient(180deg, #feefe8, #ffd7c1); display: grid; place-items: center; }
  .adnote { position: absolute; right: 78px; bottom: 44px; font-size: 26px; font-weight: 700; }

  .plede { position: absolute; right: 78px; top: 222px; font-size: 29px; }
  .ticks i { position: absolute; top: 336px; width: 40px; text-align: center; font-style: normal; font-size: 22px; font-weight: 800; opacity: .7; }
  .ph { position: absolute; top: 376px; height: 120px; border-radius: 30px; padding: 18px 24px; background: linear-gradient(180deg, #0a1220 0%, #182433 40%, #2a4a70 100%); }
  .ph.last { background: linear-gradient(180deg, #4a240c 0%, #763f18 30%, #e07f38 100%); }
  .ph b { display: block; font-size: 29px; font-weight: 800; white-space: nowrap; }
  .ph span { font-size: 22px; font-weight: 700; opacity: .85; }
  .tk { position: absolute; top: 516px; list-style: none; padding-right: 8px; }
  .tk li { font-size: 25px; font-weight: 700; line-height: 1.6; }
  .vl { position: absolute; top: 500px; height: 296px; border-left: 3px dashed rgba(255,255,255,.3); }
  .payline { position: absolute; left: 78px; right: 78px; top: 812px; border-top: 4px dashed rgba(255,255,255,.55); }
  .pin { position: absolute; top: 796px; }
  .pin i { position: absolute; left: -16px; top: 0; width: 32px; height: 32px; border-radius: 50%; background: #ffd7c1; }
  .pin div { position: absolute; left: 0; top: 48px; white-space: nowrap; text-align: center; transform: translateX(-50%); }  /* left: 0, or RTL places it from the right */
  .pin.r div { transform: translateX(-100%); text-align: right; left: 16px; }
  .pin.l div { transform: none; text-align: left; left: -16px; }
  .pin b { display: block; font-size: 52px; font-weight: 800; line-height: 1; }
  .pin span { font-size: 23px; font-weight: 700; }
  .after { position: absolute; left: 78px; top: 968px; font-size: 25px; font-weight: 800; color: #ffd7c1; }

  .ptab { position: absolute; right: 78px; left: 78px; top: 260px; }
  .ptab table { width: 100%; border-collapse: collapse; position: relative; }
  .ptab th { text-align: right; font-size: 28px; font-weight: 700; height: 84px; }
  .ptab td { width: 260px; text-align: center; font-size: 32px; font-weight: 800; }
  .ptab tbody tr { border-top: 1px solid rgba(255,255,255,.14); }
  .ptab td.pc { color: #68dae7; }
  .ptab .hl { position: absolute; left: 260px; top: -8px; bottom: -8px; width: 260px; border-radius: 40px; background: linear-gradient(180deg, #4a240c 0%, #763f18 22%, #c47a45 60%, #f2883d 100%); }

  .bye { position: absolute; left: 0; right: 0; top: 200px; text-align: center; font-family: var(--display); font-size: 520px; line-height: 1; }
  .byw { position: absolute; right: 120px; bottom: 80px; font-size: 32px; line-height: 1.6; text-align: right; }
"""

html = f"""<!doctype html>
<html lang="ar" dir="rtl"><head><meta charset="utf-8"><title>Example Presentation</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lalezar&family=Tajawal:wght@500;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
{chr(10).join(S)}
</body></html>"""
(HERE / "deck.html").write_text(html.replace("Google Play", "Google Play").replace("App Store", "App Store"), encoding="utf-8")
print(len(S), "slides")
