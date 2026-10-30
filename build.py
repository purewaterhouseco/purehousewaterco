"""Static site generator for Pure House Water Co.

Edit the BUSINESS / AREAS data below, then run:  python3 build.py
Every .html page in this folder is regenerated from this file.
"""
from pathlib import Path

ROOT = Path(__file__).parent

# ---------------------------------------------------------------- business info
# TODO: replace placeholders with real details.
BUSINESS = {
    "name": "Pure House Water Co",
    "phone": "(972) 757-7011",
    "phone_href": "+19727577011",
    "email": "purehousewater@gmail.com",
    "hours": "Mon–Sat · 8am–6pm",
    "region": "North Texas",
}

# Counties/cities and their water facts live in areas_data.py.
from areas_data import COUNTIES, TOTAL_CITIES, slugify, CITY as CITY_WATER

AREAS = [(c["slug"], c["name"], [city[0] for city in c["cities"]]) for c in COUNTIES]

B = BUSINESS

# ---------------------------------------------------------------- layout
NAV = [
    ("Products", "products.html", [
        ("Whole Home Systems", "whole-home-systems.html"),
        ("Drinking Water Systems", "drinking-water-systems.html"),
    ]),
    ("Service Areas", "service-areas.html", None),
    ("Our Story", "about.html", None),
    ("Blog", "blog.html", None),
]


def header(active):
    links = []
    for label, href, sub in NAV:
        cls = ' class="active"' if href == active else ""
        if sub:
            items = "".join(f'<a href="{h}">{l}</a>' for l, h in sub)
            links.append(f'<div class="dropdown"><a href="{href}"{cls}>{label} ▾</a>'
                         f'<div class="dropdown-menu"><a href="{href}">All Products</a>{items}</div></div>')
        else:
            links.append(f'<a href="{href}"{cls}>{label}</a>')
    return f"""
<div class="topbar"><div class="container">
  <span>Locally owned in North Texas · Free water test · Garage installation included</span>
  <span>{B['hours']} · <a href="tel:{B['phone_href']}">{B['phone']}</a></span>
</div></div>
<header class="site-header"><div class="container">
  <a class="brand" href="index.html"><img src="assets/logo-transparent.png" alt="{B['name']} logo"></a>
  <button class="menu-toggle" aria-label="Open menu" aria-expanded="false">☰</button>
  <nav class="nav">{''.join(links)}<a class="btn btn-phone" href="tel:{B['phone_href']}">{icon("phone")}{B['phone']}</a><a class="btn btn-primary" href="quote.html">Free Quote</a></nav>
</div></header>"""


def footer():
    areas = "".join(f'<li><a href="service-areas/{s}.html">{n}</a></li>' for s, n, _ in AREAS[:6])
    return f"""
<footer class="site-footer"><div class="container">
  <div class="footer-grid">
    <div>
      <img src="assets/logo-transparent.png" alt="{B['name']}">
      <p>Whole-home filtration, softening and drinking water systems — tested, installed and supported by a local team.</p>
      <p><a href="tel:{B['phone_href']}">{B['phone']}</a><br><a href="mailto:{B['email']}">{B['email']}</a></p>
    </div>
    <div><h4>Products</h4><ul>
      <li><a href="whole-home-systems.html">Whole Home Systems</a></li>
      <li><a href="drinking-water-systems.html">Drinking Water Systems</a></li>
      <li><a href="quote.html">Free Water Test</a></li>
    </ul></div>
    <div><h4>Company</h4><ul>
      <li><a href="about.html">Our Story</a></li>
      <li><a href="blog.html">Blog</a></li>
      <li><a href="contact.html">Contact</a></li>
    </ul></div>
    <div><h4>Service Areas</h4><ul>{areas}<li><a href="service-areas.html">View all →</a></li></ul></div>
  </div>
  <div class="footer-bottom">
    <span>© <span data-year></span> {B['name']}. All rights reserved.</span>
    <span><a href="privacy-policy.html">Privacy Policy</a> · <a href="terms.html">Terms</a></span>
  </div>
</div></footer>"""


def page(filename, title, description, body, active=None):
    depth = filename.count("/")
    prefix = "../" * depth
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | {B['name']}</title>
<meta name="description" content="{description}">
<link rel="icon" href="assets/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
</head>
<body>
{header(active)}
<main>
{body}
</main>
{footer()}
<script src="assets/main.js"></script>
</body>
</html>
"""
    if prefix:
        # Rewrite root-relative links for nested pages.
        for attr in ('href="', 'src="'):
            html = html.replace(attr, attr + "§")
            html = html.replace(attr + "§http", attr + "http").replace(attr + "§tel:", attr + "tel:") \
                       .replace(attr + "§mailto:", attr + "mailto:").replace(attr + "§#", attr + "#")
            html = html.replace(attr + "§", attr + prefix)
    out = ROOT / filename
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print("wrote", filename)


def page_hero(title, text, crumb):
    return f"""<section class="page-hero"><div class="container">
  <div class="crumbs"><a href="index.html">Home</a> / {crumb}</div>
  <h1>{title}</h1><p>{text}</p>
</div></section>"""


def cta():
    return f"""<section class="section"><div class="container"><div class="cta-band">
  <div><h2>Find out what's really in your water.</h2>
  <p>Book a free, no-pressure in-home test and get a written recommendation the same day.</p></div>
  <div class="btn-row"><a class="btn btn-outline" href="tel:{B['phone_href']}">Call {B['phone']}</a>
  <a class="btn btn-white" href="quote.html">Book My Free Test</a></div>
</div></div></section>"""


# ---------------------------------------------------------------- icons
# Simple 24x24 line icons; colored by CSS via currentColor.
_ICON_PATHS = {
    "faucet": '<path d="M4 8h8a5 5 0 0 1 5 5v1"/><path d="M9 8V5"/><path d="M6 5h6"/><path d="M4 6v4"/><path d="M19 19.5a2 2 0 0 1-4 0c0-1.4 2-3.5 2-3.5s2 2.1 2 3.5z"/>',
    "shower": '<path d="M4 4l2.5 2.5"/><path d="M6.5 6.5a6 6 0 0 1 8.5 0l-8.5 8.5a6 6 0 0 1 0-8.5z"/><path d="M13 14l1.5 1.5"/><path d="M10 17l1.5 1.5"/><path d="M16 11l1.5 1.5"/><path d="M14 18l1.5 1.5"/><path d="M17 15l1.5 1.5"/>',
    "taste": '<path d="M4 9h10l-1.2 11.1a1 1 0 0 1-1 .9H6.2a1 1 0 0 1-1-.9z"/><path d="M4.6 13h8.8"/><path d="M17 3.5c1.2 1.2 1.2 2.3 0 3.5s-1.2 2.3 0 3.5"/><path d="M20.5 3.5c1.2 1.2 1.2 2.3 0 3.5s-1.2 2.3 0 3.5"/>',
    "heater": '<rect x="6" y="2.5" width="12" height="18" rx="2"/><circle cx="12" cy="8" r="2.5"/><path d="M12 8l1.5-1.5"/><path d="M12 18.5c-1.2 0-2-.8-2-1.9 0-1.2 2-3.1 2-3.1s2 1.9 2 3.1c0 1.1-.8 1.9-2 1.9z"/><path d="M8.5 20.5v1"/><path d="M15.5 20.5v1"/>',
    "dollar": '<circle cx="12" cy="12" r="9"/><path d="M15 9.2c-.6-.9-1.7-1.4-3-1.4-1.7 0-3 .9-3 2.1s1.2 1.8 3 2.1 3 .9 3 2.1-1.3 2.1-3 2.1c-1.4 0-2.6-.6-3.2-1.5"/><path d="M12 6v1.8"/><path d="M12 16.2V18"/>',
    "recycle": '<path d="M20 12a8 8 0 0 1-13.7 5.7"/><path d="M4 12A8 8 0 0 1 17.7 6.3"/><path d="M18 2.5v4h-4"/><path d="M6 21.5v-4h4"/>',
    "glass": '<path d="M6 3h12l-1.6 17.1a1 1 0 0 1-1 .9H8.6a1 1 0 0 1-1-.9z"/><path d="M6.7 10c1.8-1 3.5-1 5.3 0s3.5 1 5.3 0"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
    "wrench": '<path d="M14.5 3.5a5 5 0 0 0-4.6 6.9L3.5 16.8a1.8 1.8 0 0 0 2.5 2.5l6.4-6.4a5 5 0 0 0 6.9-4.6l-3 3-3-.5-.5-3z"/>',
    "shield": '<path d="M12 3l7 3v5c0 4.5-3 8.3-7 10-4-1.7-7-5.5-7-10V6z"/><path d="M9 12l2 2 4-4"/>',
    "phone": '<path d="M5 4h3.5l1.7 4.3-2.2 1.4a11 11 0 0 0 6.3 6.3l1.4-2.2L20 15.5V19a1.5 1.5 0 0 1-1.6 1.5A16 16 0 0 1 3.5 5.6 1.5 1.5 0 0 1 5 4z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5l8.5 6.5 8.5-6.5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>',
    "flask": '<path d="M9 3h6"/><path d="M10 3v6.5L4.8 18.6A1.6 1.6 0 0 0 6.2 21h11.6a1.6 1.6 0 0 0 1.4-2.4L14 9.5V3"/><path d="M7.5 15h9"/>',
    "chat": '<path d="M5 5h14a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H9l-5 4V6a1 1 0 0 1 1-1z"/><path d="M8 10h8"/><path d="M8 13h5"/>',
    "gem": '<path d="M6 3h12l4 6-10 12L2 9z"/><path d="M2 9h20"/><path d="M9 3l3 18 3-18"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="M4.9 4.9l1.4 1.4"/><path d="M17.7 17.7l1.4 1.4"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="M4.9 19.1l1.4-1.4"/><path d="M17.7 6.3l1.4-1.4"/>',
}


def icon(name):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_ICON_PATHS[name]}</svg>')


# ---------------------------------------------------------------- shared content
PROBLEMS = [
    ("faucet", "Crusty fixtures & spotty dishes", "Hard-water minerals leave white scale on faucets, glass shower doors and every dish that comes out of the dishwasher."),
    ("shower", "Dry skin & dull hair", "Chlorine and dissolved minerals strip natural oils, so showers leave skin tight and hair harder to manage."),
    ("taste", "Off taste & odor", "A pool-like smell, metallic aftertaste or earthy flavor is a sign something in the supply needs to be treated."),
    ("heater", "Shorter appliance life", "Scale builds up inside water heaters, coffee makers and washing machines, cutting efficiency and lifespan."),
]

# Current packages. Images live in assets/products/ (web-sized copies of assets/pics/).
# (slug, tag, image, name, subtitle, price, was_price or None, features)
PRODUCTS = [
    ("complete-home", "40% Off", "assets/products/complete-home.jpg",
     "Complete Home Filtration System",
     "Whole-home water softener plus a reverse osmosis drinking water system — one package for the entire house.",
     "$2,650", "$4,599",
     ["Whole-home water softener with smart digital control valve",
      "Reverse osmosis drinking water system with dedicated faucet",
      "Advanced filtration that removes harmful contaminants",
      "Protects your plumbing, fixtures & appliances",
      "Garage installation included"]),
    ("dual-tank", "40% Off", "assets/products/dual-tank.jpg",
     "Dual Tank System",
     "A two-tank softening and filtration system designed specifically for Texas water.",
     "$2,900", None,
     ["Two dedicated treatment tanks for hardness and filtration",
      "Smart digital control valve",
      "Built for the hard, treated water common across North Texas",
      "Brine tank included",
      "Garage installation included"]),
]

FAQS = [
    ("Is the water test really free?", "Yes. A technician comes to your home, tests your tap water on the spot, explains the results in plain language and leaves you a written recommendation. There's no charge and no obligation."),
    ("How long does installation take?", "Most whole-home systems are installed in about half a day. Under-sink drinking water systems usually take one to two hours. We clean up and walk you through the system before we leave."),
    ("What's the difference between a softener and a filter?", "A softener removes hardness minerals (calcium and magnesium) that cause scale. A filter removes things like chlorine, chloramine, sediment and odors. Both of our packages handle softening and filtration."),
    ("How much maintenance is involved?", "Softeners need salt added every few weeks, and filters are replaced on a schedule based on your usage. We can set up reminders or handle it for you with a maintenance plan."),
    ("Do you offer financing?", "Yes — we offer monthly payment options with approved credit. Ask your technician for details during your free test."),
    ("What warranty comes with the system?", "Every system includes manufacturer coverage on tanks and valves plus our own workmanship guarantee on installation. Your technician will give you the exact terms in writing."),
]


def faq_html(items=FAQS):
    return '<div class="faq">' + "".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items) + "</div>"


def price_html(price, was):
    was_html = f'<span class="was">{was}</span>' if was else ""
    return f'<div class="price">{was_html}<span class="now">{price}</span><span class="incl">Garage install included</span></div>'


def product_cards(items=PRODUCTS):
    out = []
    for slug, tag, img, name, sub, price, was, feats in items:
        li = "".join(f"<li>{f}</li>" for f in feats)
        out.append(f"""<div class="card product-card" id="{slug}">
  <div class="media"><span class="tag">{tag}</span><img src="{img}" alt="{name}" loading="lazy"></div>
  <div class="body"><h3>{name}</h3><p>{sub}</p>{price_html(price, was)}<ul class="checklist">{li}</ul>
  <a class="btn btn-primary" href="quote.html">Claim This Offer</a></div></div>""")
    return '<div class="grid grid-2">' + "".join(out) + "</div>"


def product_feature(product, flip=False, extra_imgs=()):
    slug, tag, img, name, sub, price, was, feats = product
    li = "".join(f"<li>{f}</li>" for f in feats)
    thumbs = "".join(f'<img src="{i}" alt="{name}" loading="lazy">' for i in extra_imgs)
    thumbs_html = f'<div class="thumbs">{thumbs}</div>' if thumbs else ""
    visual = f'<div><img class="feature-img" src="{img}" alt="{name}">{thumbs_html}</div>'
    text = f"""<div><span class="eyebrow">{tag} · Limited-time offer</span><h2>{name}</h2>
  <p class="lead">{sub}</p>{price_html(price, was)}
  <ul class="checklist">{li}</ul>
  <div class="btn-row"><a class="btn btn-primary" href="quote.html">Claim This Offer</a>
  <a class="btn btn-outline dark" href="tel:{B['phone_href']}">Call {B['phone']}</a></div></div>"""
    return f'<div class="container split" id="{slug}">' + (text + visual if flip else visual + text) + "</div>"


def category_cards():
    cats = [
        ("Whole Home Systems", "Softened, filtered water from every faucet, shower and appliance.", "whole-home-systems.html", "90% 30%"),
        ("Drinking Water Systems", "Bottled-quality water straight from your kitchen tap.", "drinking-water-systems.html", "75% 60%"),
    ]
    return '<div class="grid grid-2">' + "".join(
        f'<a class="card cat-card" href="{h}" style="--pos:{p}"><div class="body"><h3>{t}</h3><p>{d}</p><span class="more">Explore →</span></div></a>'
        for t, d, h, p in cats) + "</div>"


STEPS = [
    ("Book your free test", "Pick a time that works for you online or by phone."),
    ("We test at your tap", "A technician checks hardness, chlorine, TDS, pH and more — right in your kitchen."),
    ("Get a clear recommendation", "We explain the numbers and suggest only what your water actually needs."),
    ("Professional install", "Our own team installs, tests and walks you through your new system."),
]


def steps_html():
    return '<div class="grid grid-4 steps">' + "".join(
        f'<div class="card step"><h3>{t}</h3><p>{d}</p></div>' for t, d in STEPS) + "</div>"


def lead_form(heading="Request your free water test"):
    # Submissions are emailed to B["email"] via FormSubmit (see assets/main.js).
    return f"""<div class="form-card">
  <h3>{heading}</h3>
  <form data-lead-form data-email="{B['email']}" class="form-grid">
    <input type="hidden" name="_subject" value="New website request: {heading}">
    <input type="hidden" name="Form" value="{heading}">
    <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
    <div><label for="fn">First name</label><input id="fn" name="First name" required></div>
    <div><label for="ln">Last name</label><input id="ln" name="Last name" required></div>
    <div><label for="ph">Phone</label><input id="ph" name="Phone" type="tel" required></div>
    <div><label for="em">Email</label><input id="em" name="email" type="email" required></div>
    <div class="full"><label for="ad">Home address</label><input id="ad" name="Address" required></div>
    <div><label for="src">Water source</label><select id="src" name="Water source"><option>City water</option><option>Well water</option><option>Not sure</option></select></div>
    <div><label for="int">Interested in</label><select id="int" name="Interested in"><option>Complete Home Filtration System</option><option>Dual Tank System</option><option>Not sure yet</option><option>Just the free water test</option></select></div>
    <div class="full"><label for="msg">Anything we should know?</label><textarea id="msg" name="Message" rows="3"></textarea></div>
    <div class="full"><button class="btn btn-primary btn-block" type="submit">Schedule My Free Test</button>
    <p class="form-note">No cost, no obligation. We'll call to confirm a time.</p>
    <div class="form-success">Thanks! We received your request and will call you shortly to confirm.</div>
    <div class="form-error">Sorry, something went wrong. Please call us at <a href="tel:{B['phone_href']}">{B['phone']}</a>.</div></div>
  </form>
</div>"""


# Add real customer reviews as (name, city, text). While empty, the site shows a Google review prompt.
REVIEWS = []
GOOGLE_REVIEWS_URL = "#"  # TODO: your Google Business review link


def reviews_html(items=REVIEWS):
    if not items:
        return (f'<div class="card center narrow"><div class="stars">★★★★★</div>'
                f'<h3>Had a Pure House install?</h3><p>We\'d love to hear how your water has changed. Your review helps other North Texas families find honest water advice.</p>'
                f'<a class="btn btn-primary" href="{GOOGLE_REVIEWS_URL}">Review Us on Google</a></div>')
    return (''
            '<div class="grid grid-3">' + "".join(
                f'<div class="card review"><div class="stars">★★★★★</div><p>“{t}”</p><div class="who">{n}</div><div class="where">{c}</div></div>'
                for n, c, t in items) + "</div>")


GALLERY = [("Whole-home install", "88% 50%"), ("Under-sink RO", "78% 70%"), ("Garage system", "95% 40%"),
           ("Kitchen faucet", "100% 70%"), ("Water test", "0% 30%"), ("Well treatment", "92% 45%"),
           ("Clean install", "70% 30%"), ("Final walkthrough", "5% 60%")]


def gallery_html(n=8):
    return (''
            '<div class="gallery">' + "".join(
                f'<div class="shot" style="--pos:{p}"><span>{t}</span></div>' for t, p in GALLERY[:n]) + "</div>")


def areas_html():
    return '<div class="grid grid-3">' + "".join(
        f'<a class="card area-card" href="service-areas/{s}.html"><h3>{n} <span>→</span></h3><p class="cities">{", ".join(c)}</p></a>'
        for s, n, c in AREAS) + "</div>"


def kind_badge(kind):
    cls = {"City water": "city", "Mostly private wells": "well"}.get(kind, "mixed")
    return f'<span class="kind {cls}">{kind}</span>'


def city_cards(county):
    return '<div class="grid grid-3">' + "".join(
        f'''<a class="card city-card" href="service-areas/{county['slug']}/{slugify(name)}.html">
  <h3>{name} <span>→</span></h3><div class="supplier">💧 {utility}</div>{kind_badge(kind)}</a>'''
        for name, utility, source, kind, note in county["cities"]) + "</div>"


def facts_box(rows, title="Water at a glance"):
    items = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows if v)
    return f'<div class="facts"><h3>{title}</h3><dl>{items}</dl></div>'


def contact_section(heading="Request your free water test", intro="Tell us a little about your home and we'll call you to set up a time."):
    return f"""<section class="section contact-section" id="contact"><div class="container">
  <div class="contact-panel">
    <div class="contact-info">
      <span class="eyebrow">Free water test</span>
      <h2>{heading}</h2>
      <p>{intro}</p>
      <ul class="perks">
        <li><span>{icon("flask")}</span><div><strong>Free in-home water test</strong><br>Results explained on the spot, yours to keep.</div></li>
        <li><span>{icon("wrench")}</span><div><strong>Garage installation included</strong><br>Installed by our own local team.</div></li>
        <li><span>{icon("chat")}</span><div><strong>No pressure, no obligation</strong><br>We only recommend what your water needs.</div></li>
      </ul>
      <a class="phone-card" href="tel:{B['phone_href']}"><span>{icon("phone")}</span><div><small>Prefer to talk? Call or text</small><strong>{B['phone']}</strong></div></a>
      <p class="privacy">Your details are only used to contact you about your water — we never sell your information. <a href="privacy-policy.html">Privacy policy</a></p>
    </div>
    {lead_form("Book your free water test")}
  </div>
</div></section>"""


# ---------------------------------------------------------------- pages
def build_home():
    problems = "".join(f'<div class="card"><div class="icon">{icon(i)}</div><h3>{t}</h3><p>{d}</p></div>' for i, t, d in PROBLEMS)
    body = f"""
<section class="hero hero-split"><div class="bubbles" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></div><div class="container">
  <div class="hero-copy">
    <span class="pill">🔥 Limited time · Up to 40% off complete systems</span>
    <h1>Every tap in your home.<br><span>Cleaner, softer, better.</span></h1>
    <p>Pure House installs whole-home softening, filtration and reverse osmosis drinking water systems for families across North Texas — starting with a free in-home water test and finishing with a clean, professional garage install.</p>
    <div class="btn-row"><a class="btn btn-white" href="quote.html">Book My Free Water Test</a>
    <a class="btn btn-outline" href="tel:{B['phone_href']}">{icon("phone")}{B['phone']}</a></div>
    <ul class="hero-checks"><li>Free in-home water test</li><li>Garage installation included</li><li>Locally owned in North Texas</li><li>No-pressure recommendations</li></ul>
  </div>
  <figure class="hero-video">
    <div class="video-card">
      <video id="intro-video" preload="none" playsinline poster="assets/video/poster.jpg">
        <source src="assets/video/purehouse-intro.mp4" type="video/mp4">
      </video>
      <button class="video-overlay" type="button" aria-label="Play the Pure House video">
        <span class="play-btn">▶</span>
        <span class="video-title">See how Pure House works</span>
        <span class="video-cta">▶ Watch the 2-minute intro</span>
      </button>
    </div>
    <figcaption>A quick look at what hard, treated water does to your home — and how we fix it.</figcaption>
  </figure>
</div></section>

<section class="section alt"><div class="container">
  <div class="section-head"><span class="eyebrow">Sound familiar?</span><h2>Signs your water needs attention</h2>
  <p class="lead">Most homes deal with at least one of these — and most homeowners assume it's normal.</p></div>
  <div class="grid grid-4">{problems}</div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="eyebrow">Special offers</span><h2>Save up to 40% on a complete system</h2>
  <p class="lead">Limited-time pricing on our two most popular packages — professional garage installation included.</p></div>
  {product_cards()}
</div></section>

<section class="section alt"><div class="container">
  <div class="section-head"><span class="eyebrow">Shop by category</span><h2>Solutions for the whole house</h2></div>
  {category_cards()}
</div></section>

<section class="section dark"><div class="container">
  <div class="section-head"><span class="eyebrow">How it works</span><h2>Four simple steps to better water</h2>
  <p class="lead">No pushy sales pitch — just honest answers about your water.</p></div>
  {steps_html()}
</div></section>

<section class="section"><div class="container split">
  <div><span class="eyebrow">Free water test</span><h2>Know your numbers before you buy anything.</h2>
  <p class="lead">Every recommendation we make starts with real data from your own tap. In about 30 minutes, we'll test for:</p>
  <ul class="checklist"><li>Hardness (grains per gallon)</li><li>Chlorine & chloramine</li><li>Total dissolved solids (TDS)</li><li>pH, iron and more for well owners</li></ul>
  <p>You keep the results whether you buy from us or not.</p></div>
  {lead_form()}
</div></section>

<section class="section alt"><div class="container split">
  <div class="visual logo"></div>
  <div><span class="eyebrow">Our story</span><h2>A local company built around one idea: honest water advice.</h2>
  <p>Pure House Water Co was started by people who were tired of seeing homeowners oversold on equipment they didn't need. We test first, recommend only what your water calls for, and install everything with our own team.</p>
  <p>We're North Texas locals, and we treat every home like it's our own family's — clear answers, fair pricing and work we're proud to put our name on.</p>
  <a class="btn btn-primary" href="about.html">Read Our Story</a></div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="eyebrow">Where we work</span><h2>Proudly serving {B['region']}</h2>
  <p class="lead">Don't see your city? Call us — we may still cover you.</p></div>
  {areas_html()}
</div></section>

<section class="section alt"><div class="container">
  <div class="section-head"><span class="eyebrow">FAQ</span><h2>Common questions</h2></div>
  {faq_html()}
</div></section>
{cta()}"""
    page("index.html", "Water Filtration & Softening", f"Whole-home water filtration, softeners and reverse osmosis systems in {B['region']}. Book a free in-home water test.", body)


def build_products():
    body = page_hero("Water Treatment Systems", "Two complete packages built for North Texas water — each with professional garage installation included.", "Products") + f"""
<section class="section"><div class="container">{product_cards()}</div></section>
<section class="section alt"><div class="container"><div class="section-head"><h2>Browse by category</h2></div>{category_cards()}</div></section>
{cta()}"""
    page("products.html", "Products", "Complete Home Filtration System and Dual Tank System packages from Pure House Water Co, with garage installation included.", body, "products.html")


def build_whole_home():
    body = page_hero("Whole Home Systems", "Treat water once at the point it enters your home, so every shower, sink and appliance gets the benefit.", '<a href="products.html">Products</a> / Whole Home') + f"""
<section class="section">{product_feature(PRODUCTS[0], extra_imgs=("assets/products/complete-home-2.jpg", "assets/products/complete-home-3.jpg"))}</section>
<section class="section alt">{product_feature(PRODUCTS[1], flip=True, extra_imgs=("assets/products/dual-tank-2.jpg",))}</section>
<section class="section"><div class="container">
  <div class="section-head"><h2>Compare packages</h2></div>
  <table class="spec"><tr><th>Feature</th><th>Complete Home</th><th>Dual Tank</th></tr>
  <tr><td>Price</td><td><strong>$2,650</strong> <s>$4,599</s></td><td><strong>$2,900</strong></td></tr>
  <tr><td>Whole-home water softening</td><td>✓</td><td>✓</td></tr>
  <tr><td>Reverse osmosis drinking water</td><td>✓</td><td>—</td></tr>
  <tr><td>Two-tank treatment design</td><td>—</td><td>✓</td></tr>
  <tr><td>Smart digital control valve</td><td>✓</td><td>✓</td></tr>
  <tr><td>Garage installation included</td><td>✓</td><td>✓</td></tr></table>
</div></section>
{cta()}"""
    page("whole-home-systems.html", "Whole Home Systems", "Whole-home water softener and filtration systems for city and well water.", body, "products.html")


def build_drinking():
    body = page_hero("Drinking Water Systems", "Crisp, clean water for drinking and cooking — right from your kitchen faucet. No more hauling cases of bottles.", '<a href="products.html">Products</a> / Drinking Water') + f"""
<section class="section"><div class="container split">
  <img class="feature-img" src="assets/products/complete-home-3.jpg" alt="Pure House reverse osmosis system">
  <div><span class="eyebrow">Reverse osmosis</span><h2>Included with the Complete Home Filtration System</h2>
  <p class="lead">Our Complete Home package pairs a whole-home softener with an under-sink reverse osmosis system, so you get crisp, great-tasting water for drinking and cooking right at the kitchen sink.</p>
  {price_html(PRODUCTS[0][5], PRODUCTS[0][6])}
  <ul class="checklist"><li>Crisp, clean, great-tasting water</li><li>Compact under-sink unit</li><li>Dedicated drinking water faucet</li><li>Professional installation</li></ul>
  <a class="btn btn-primary" href="whole-home-systems.html#complete-home">See the Full Package</a></div>
</div></section>
<section class="section alt"><div class="container">
  <div class="section-head"><h2>Why switch from bottled water?</h2></div>
  <div class="grid grid-3">
    <div class="card"><div class="icon">{icon("dollar")}</div><h3>Save money</h3><p>Filtered water at home costs pennies per gallon compared with buying bottles every week.</p></div>
    <div class="card"><div class="icon">{icon("recycle")}</div><h3>Less plastic</h3><p>Cut hundreds of single-use bottles out of your household's trash every year.</p></div>
    <div class="card"><div class="icon">{icon("glass")}</div><h3>Always on tap</h3><p>No more running out or storing cases in the garage — it's there whenever you need it.</p></div>
  </div>
</div></section>
{cta()}"""
    page("drinking-water-systems.html", "Drinking Water Systems", "Reverse osmosis drinking water, included with the Pure House Complete Home Filtration System.", body, "products.html")


def build_addons():
    body = page_hero("Add-Ons", "Upgrades that pair with your Pure House system to fine-tune taste and add extra protection.", '<a href="products.html">Products</a> / Add-Ons') + f"""
<section class="section"><div class="container"><div class="grid grid-2">
  <div class="card"><div class="icon">{icon("gem")}</div><h3>Remineralization Filter</h3><p>Adds back healthy calcium and magnesium after reverse osmosis for a smoother, balanced taste and a more neutral pH.</p><ul class="checklist"><li>Improves flavor of RO water</li><li>Easy inline installation</li><li>Simple annual replacement</li></ul><a class="btn btn-primary more" href="quote.html">Ask About This</a></div>
  <div class="card"><div class="icon">{icon("sun")}</div><h3>UV Disinfection</h3><p>Ultraviolet light neutralizes bacteria and viruses without adding chemicals — a smart safeguard, especially for well water.</p><ul class="checklist"><li>Chemical-free protection</li><li>Whole-home or point-of-use</li><li>Lamp-life alarm built in</li></ul><a class="btn btn-primary more" href="quote.html">Ask About This</a></div>
</div></div></section>
{cta()}"""
    page("add-ons.html", "Add-Ons", "Remineralization and UV disinfection add-ons for your water system.", body, "products.html")


def build_areas():
    jump = "".join(f'<a href="#{c["slug"]}">{c["name"]}</a>' for c in COUNTIES)
    sections = "".join(f"""
<section class="section{' alt' if i % 2 else ''}" id="{c['slug']}"><div class="container">
  <div class="county-head"><div><span class="eyebrow">{len(c['cities'])} cities</span><h2>{c['name']}</h2>
  <p class="lead">{c['overview']}</p></div>
  <a class="btn btn-outline dark" href="service-areas/{c['slug']}.html">{c['name']} water details →</a></div>
  {city_cards(c)}
</div></section>""" for i, c in enumerate(COUNTIES))
    body = page_hero("Where We Work", f"Pure House installs and services water systems across {B['region']}. Find your city to see where your water comes from and what we typically find in it.", "Service Areas") + f"""
<section class="stats-bar"><div class="container">
  <div><strong>{TOTAL_CITIES}</strong><span>Cities served</span></div>
  <div><strong>{len(COUNTIES)}</strong><span>Counties</span></div>
  <div><strong>Free</strong><span>In-home water test</span></div>
</div></section>
<section class="section flush-bottom"><div class="container"><div class="county-jump">{jump}</div></div></section>
{sections}
{contact_section()}"""
    page("service-areas.html", "Service Areas", f"Water softener and filtration installation in {TOTAL_CITIES} cities across {len(COUNTIES)} {B['region']} counties.", body, "service-areas.html")

    for c in COUNTIES:
        crumb = f'<a href="service-areas.html">Service Areas</a> / {c["name"]}'
        body = page_hero(f"Water Softeners & Filtration in {c['name']}", c["overview"], crumb) + f"""
<section class="section"><div class="container split align-start">
  <div><span class="eyebrow">Your water</span><h2>What's in {c['name']} water?</h2>
  <p class="lead">Every utility and every well is a little different, so we never rely on a county-wide average. Here's the big picture — your free in-home test fills in the details for your address.</p>
  <ul class="checklist"><li>Hardness that leaves scale on fixtures and inside appliances</li><li>Disinfectant taste and smell from treated city water</li><li>Iron, sulfur and sediment on many private wells</li></ul>
  <a class="btn btn-primary" href="#contact">Book My Free Test</a></div>
  {facts_box(c['facts'], f"{c['name']} at a glance")}
</div></section>
<section class="section alt"><div class="container">
  <div class="section-head"><span class="eyebrow">Cities we serve</span><h2>Choose your city</h2>
  <p class="lead">See who supplies your water and what we usually find in it.</p></div>
  {city_cards(c)}
</div></section>
<section class="section"><div class="container"><div class="section-head"><span class="eyebrow">Special offers</span><h2>Our packages in {c['name']}</h2></div>{product_cards()}</div></section>
{contact_section(f"Free water test in {c['name']}")}"""
        page(f"service-areas/{c['slug']}.html", f"{c['name']} Water Softeners & Filtration", f"Water softeners and filtration in {c['name']}, TX. Local water facts and a free in-home water test.", body, "service-areas.html")

        for name, utility, source, kind, note in c["cities"]:
            nearby = "".join(f'<a href="service-areas/{c["slug"]}/{slugify(n)}.html">{n}</a>' for n, *_ in c["cities"] if n != name)
            rows = [("Water utility", utility), ("Water source", source), ("Water type", kind_badge(kind)), ("County", c["name"])]
            crumb = f'<a href="service-areas.html">Service Areas</a> / <a href="service-areas/{c["slug"]}.html">{c["name"]}</a> / {name}'
            body = page_hero(f"Water Softeners & Filtration in {name}, TX", f"Homes in {name} get their water from {utility}. We'll test yours for free and show you exactly what's in it.", crumb) + f"""
<section class="section"><div class="container split align-start">
  <div><span class="eyebrow">Your water in {name}</span><h2>What to know about {name} water</h2>
  <p class="lead">{note}</p>
  <p>{'Private wells are common around ' + name + ', and well water is completely different from city supply — iron, sulfur and high hardness are all possible. ' if kind != CITY_WATER else ''}Water can vary street to street, so a city-wide report only tells part of the story. Our free in-home test checks hardness, chlorine/chloramine, TDS and pH right at your kitchen sink.</p>
  <div class="btn-row"><a class="btn btn-primary" href="#contact">Book My Free Test</a><a class="btn btn-outline dark" href="tel:{B['phone_href']}">Call {B['phone']}</a></div></div>
  {facts_box(rows, f"{name} water at a glance")}
</div></section>
<section class="section alt"><div class="container"><div class="section-head"><span class="eyebrow">Special offers</span><h2>Popular packages in {name}</h2></div>{product_cards()}</div></section>
{contact_section(f"Free water test in {name}")}
<section class="section flush-top"><div class="container">
  <h3>Nearby cities we serve in {c['name']}</h3><div class="county-jump">{nearby}<a href="service-areas/{c['slug']}.html">All of {c['name']} →</a></div>
</div></section>"""
            page(f"service-areas/{c['slug']}/{slugify(name)}.html", f"{name}, TX Water Softeners & Filtration", f"Water softener and filtration installation in {name}, TX. Supplied by {utility}. Free in-home water test.", body, "service-areas.html")


def build_about():
    body = page_hero("Our Story", "A local water treatment company that tests first and recommends only what you need.", "Our Story") + f"""
<section class="section"><div class="container split">
  <div class="visual logo"></div>
  <div><span class="eyebrow">Who we are</span><h2>Clean water shouldn't come with a sales trick.</h2>
  <p>Pure House Water Co was founded in North Texas to give homeowners a straightforward way to get better water. Too many families were being sold oversized systems or locked into confusing contracts, and we knew there was a better way to do it.</p>
  <p>Our approach is simple: show homeowners what's actually in their water, explain it clearly, and install quality equipment that's sized correctly the first time.</p></div>
</div></section>
<section class="section alt"><div class="container">
  <div class="section-head"><h2>What we stand for</h2></div>
  <div class="grid grid-3">
    <div class="card"><div class="icon">{icon("search")}</div><h3>Transparency</h3><p>Your test results, your pricing and your options — all in writing, with nothing hidden.</p></div>
    <div class="card"><div class="icon">{icon("wrench")}</div><h3>Craftsmanship</h3><p>Our own trained team handles every install. No subcontractors, no shortcuts.</p></div>
    <div class="card"><div class="icon">{icon("shield")}</div><h3>Long-term support</h3><p>We're local, we answer the phone, and we're here for service long after install day.</p></div>
  </div>
</div></section>
{cta()}"""
    page("about.html", "Our Story", "Learn about Pure House Water Co and how we approach water treatment.", body, "about.html")


def build_gallery():
    body = page_hero("Install Gallery", "A look at recent Pure House installations across our service area.", "Gallery") + f"""
<section class="section"><div class="container">{gallery_html()}</div></section>{cta()}"""
    page("gallery.html", "Gallery", "Photos of recent Pure House water system installations.", body, "gallery.html")


def build_reviews():
    body = page_hero("Customer Reviews", "Hear from homeowners who made the switch to Pure House water.", "Reviews") + f"""
<section class="section"><div class="container">{reviews_html(REVIEWS * 2)}
{f'<div class="center section-foot"><a class="btn btn-primary" href="{GOOGLE_REVIEWS_URL}">Leave Us a Google Review</a></div>' if REVIEWS else ''}</div></section>{cta()}"""
    page("reviews.html", "Reviews", "Customer reviews for Pure House Water Co.", body, "reviews.html")


POSTS = [
    ("Hard Water", "5 signs you have hard water (and what to do about it)", "From spotty glasses to dry skin — how to tell if hardness is the culprit.", "10% 40%"),
    ("Drinking Water", "Reverse osmosis vs. pitcher filters: an honest comparison", "What each one actually removes and when an upgrade makes sense.", "85% 70%"),
    ("Well Water", "A homeowner's guide to testing well water", "What to test for, how often, and what the results mean.", "92% 45%"),
    ("Maintenance", "How often should you change your water filters?", "A simple schedule for softeners, carbon tanks and RO cartridges.", "78% 60%"),
    ("City Water", "Chlorine vs. chloramine: why it matters for your filter", "Not all carbon is equal — here's what to look for.", "40% 30%"),
    ("Home", "How hard water shortens the life of your water heater", "Scale build-up costs more than you think. Here's the math.", "95% 30%"),
]


def build_blog():
    cards = "".join(
        f'<article class="card post-card"><div class="media" style="--pos:{p}"></div><div class="meta">{c}</div><h3>{t}</h3><p>{d}</p><a class="more" href="#">Read article →</a></article>'
        for c, t, d, p in POSTS)
    body = page_hero("Water Wise Blog", "Plain-language guides on water quality, treatment and maintenance.", "Blog") + f"""
<section class="section"><div class="container">
<div class="grid grid-3">{cards}</div></div></section>{cta()}"""
    page("blog.html", "Blog", "Water quality tips and guides from Pure House Water Co.", body, "blog.html")


def build_quote():
    body = page_hero("Get Your Free Quote", "Start with a free in-home water test. We'll show you the results and give you a written quote — no pressure.", "Free Quote") + f"""
<section class="section"><div class="container split">
  <div><h2>What happens next?</h2>{steps_html().replace('grid-4', 'grid-2')}</div>
  {lead_form("Tell us about your home")}
</div></section>"""
    page("quote.html", "Free Quote", "Request a free in-home water test and quote from Pure House Water Co.", body)


def build_contact():
    body = page_hero("Contact Us", "Questions about your water or an existing system? We're happy to help.", "Contact") + f"""
<section class="section"><div class="container split">
  <div><h2>Get in touch</h2>
  <div class="grid grid-tight">
    <div class="card"><div class="icon">{icon("phone")}</div><h3>Call or text</h3><p><a href="tel:{B['phone_href']}">{B['phone']}</a></p></div>
    <div class="card"><div class="icon">{icon("mail")}</div><h3>Email</h3><p><a href="mailto:{B['email']}">{B['email']}</a></p></div>
    <div class="card"><div class="icon">{icon("clock")}</div><h3>Hours</h3><p>{B['hours']}</p></div>
  </div></div>
  {lead_form("Send us a message")}
</div></section>"""
    page("contact.html", "Contact", "Contact Pure House Water Co.", body)


def build_legal():
    privacy = page_hero("Privacy Policy", "How we collect and use your information.", "Privacy Policy") + f"""
<section class="section"><div class="container prose">
<h2>Information we collect</h2><p>When you request a water test or contact us, we collect the details you provide, such as your name, phone number, email and address.</p>
<h2>How we use it</h2><p>We use your information to schedule appointments, provide quotes and service, and respond to your questions. We do not sell your personal information.</p>
<h2>Cookies & analytics</h2><p>Our website may use cookies and analytics tools to understand how visitors use the site.</p>
<h2>Contact</h2><p>Questions about this policy? Email <a href="mailto:{B['email']}">{B['email']}</a>.</p>
</div></section>"""
    page("privacy-policy.html", "Privacy Policy", "Pure House Water Co privacy policy.", privacy)
    terms = page_hero("Terms of Service", "The terms that apply to using this website.", "Terms") + f"""
<section class="section"><div class="container prose">
<h2>Use of this site</h2><p>Content on this website is provided for general information. Product specifications and pricing may change without notice.</p>
<h2>Quotes & services</h2><p>All quotes are provided in writing after an in-home water test. Installation and warranty terms are governed by your signed service agreement.</p>
<h2>Contact</h2><p>Questions? Call <a href="tel:{B['phone_href']}">{B['phone']}</a>.</p>
</div></section>"""
    page("terms.html", "Terms", "Pure House Water Co terms of service.", terms)


if __name__ == "__main__":
    build_home(); build_products(); build_whole_home(); build_drinking()
    build_areas(); build_about(); build_blog()
    # Hidden for now — add back to NAV/footer and call these to re-enable:
    # build_gallery(); build_reviews(); build_addons()
    build_quote(); build_contact(); build_legal()
