#!/usr/bin/env python3
"""Builds the static pages of longshortnmargin.tech into ./docs (served by GitHub Pages). Run: python3 build.py"""
import json, os, html

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
SITE = "https://longshortnmargin.tech"
MAIL = "hello@longshortnmargin.tech"
WAITLIST = "mailto:waitlist@longshortnmargin.tech?subject=Early%20access"
REPO = "https://github.com/LongShortNMargin/mart-forge"
ORG = "https://github.com/LongShortNMargin"
LINKEDIN = "https://www.linkedin.com/in/vuduclong0309"
LINKEDIN_CO = "https://www.linkedin.com/company/longshortnmargin/"
UPDATED = "October 2026"

TITLE = "LongShortNMargin"
TAGLINE = "Automated strategy research for MetaTrader 5."
DESC = "Automated strategy research for MetaTrader 5. Claude agents research, build and test strategies, then grade them against prop-firm rules. In development."
LEGAL = ("LongShortNMargin builds research software. It is not a broker or investment adviser, and nothing on this site is investment advice. "
         "Trading leveraged products carries a high risk of loss.")


def page(path, title, desc, body, noindex=False):
    canonical = SITE + path
    head_extra = '<meta name="robots" content="noindex">' if noindex else f'<link rel="canonical" href="{canonical}">'
    ld = ""
    if path == "/":
        ld = '<script type="application/ld+json">' + json.dumps({
            "@context": "https://schema.org", "@type": "Organization",
            "name": "LongShortNMargin", "url": SITE + "/", "email": MAIL,
            "description": DESC, "foundingDate": "2025-08",
            "founder": {"@type": "Person", "name": "Long Vu Duc", "jobTitle": "Founder", "sameAs": LINKEDIN},
            "address": {"@type": "PostalAddress", "addressCountry": "VN"},
            "sameAs": [ORG, LINKEDIN_CO],
        }) + "</script>"
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
{head_extra}
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="LongShortNMargin">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/assets/site.css">
{ld}
</head>
<body>
<header class="top"><div class="wrap">
<a class="wordmark" href="/">LongShortNMargin</a>
<nav><a href="{REPO}" rel="noopener">GitHub</a><a href="mailto:{MAIL}">Contact</a></nav>
</div></header>
<main>
{body.strip()}
</main>
<footer><div class="wrap">
<div class="links"><a href="mailto:{MAIL}">{MAIL}</a><a href="{ORG}" rel="noopener">GitHub</a><a href="{LINKEDIN_CO}" rel="noopener">LinkedIn</a><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a></div>
<p class="legal">{html.escape(LEGAL)}</p>
<p class="legal">© 2026 LongShortNMargin · Vietnam</p>
</div></footer>
</body>
</html>
"""
    target = os.path.join(OUT, "404.html") if path == "/404.html" else os.path.join(OUT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(doc)
    print(os.path.relpath(target, OUT), os.path.getsize(target), "bytes")


home = f"""
<div class="hero wrap">
<h1>{TAGLINE}</h1>
<p class="lede">Claude agents research, build and test trading strategies end to end, then grade each one against the rules prop firms enforce. For developers who build MetaTrader 5 expert advisors.</p>
<p class="status">In development. Early access by waitlist.</p>
<p class="cta"><a class="btn" href="{WAITLIST}">Request early access</a></p>
<p class="fine">One email to <a href="{WAITLIST}">waitlist@longshortnmargin.tech</a>. You hear back when access opens.</p>
</div>

<section id="open-source"><div class="wrap">
<h2>Open source</h2>
<p><a href="{REPO}" rel="noopener">mart-forge</a> is how we contribute to open source: a Claude Code plugin pack for building Kimball data warehouses in phases, with linters that gate each phase. Four plugins, 21 skills, MIT licence.</p>
<pre><code>/plugin marketplace add LongShortNMargin/mart-forge</code></pre>
</div></section>

<section id="company"><div class="wrap">
<h2>Company</h2>
<dl>
<dt>Founded</dt><dd>August 2025, Vietnam</dd>
<dt>Stage</dt><dd>Bootstrapped, founder-led</dd>
<dt>Founder</dt><dd><a href="{LINKEDIN}" rel="noopener">Long Vu Duc</a>, data engineer since 2019, M.Sc. Financial Engineering.</dd>
<dt>Contact</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd>
</dl>
</div></section>
"""

privacy = f"""
<div class="hero wrap">
<h1>Privacy</h1>
<p class="lede">What LongShortNMargin collects through this site, and what it does with it. Last updated {UPDATED}.</p>
</div>
<section><div class="wrap">
<h2>Email</h2>
<p>If you join the waitlist or write to us, your message and address are kept in the company mailbox. Waitlist addresses are used for one purpose: telling you when early access opens. Write to <a href="mailto:{MAIL}">{MAIL}</a> to be removed.</p>
</div></section>
<section><div class="wrap">
<h2>Visits</h2>
<p>The site is static. It sets no cookies and runs no analytics. The hosting and network providers process request data such as your IP address to serve the page. The typeface loads from Google Fonts, which receives your IP address under Google's privacy policy.</p>
</div></section>
<section><div class="wrap">
<h2>Links</h2>
<p>GitHub and LinkedIn have their own privacy policies.</p>
</div></section>
"""

terms = f"""
<div class="hero wrap">
<h1>Terms</h1>
<p class="lede">This site describes LongShortNMargin and software in development. It is provided for information, as is, and may change without notice. Last updated {UPDATED}.</p>
</div>
<section><div class="wrap">
<h2>Scope</h2>
<p>LongShortNMargin builds research and evaluation software. It is not a broker, investment adviser or asset manager. It does not manage money, sell signals or trade on anyone's behalf. Nothing on this site is investment advice or an offer to buy or sell any financial instrument. Trading leveraged products carries a high risk of loss, and past performance, actual or simulated, does not indicate future results.</p>
</div></section>
<section><div class="wrap">
<h2>Early access</h2>
<p>Joining the waitlist creates no obligation on either side. Early access, when offered, comes with its own terms.</p>
</div></section>
<section><div class="wrap">
<h2>Trademarks and licences</h2>
<p>mart-forge is published under the MIT licence; the licence file in the repository governs its use. MetaTrader is a trademark of MetaQuotes. Claude is a trademark of Anthropic. LongShortNMargin is independent and not affiliated with, sponsored by or endorsed by either.</p>
</div></section>
"""

notfound = f"""
<div class="hero wrap">
<h1>No page here.</h1>
<p class="lede"><a href="/">Back to the front page</a>, or write to <a href="mailto:{MAIL}">{MAIL}</a>.</p>
</div>
"""

page("/", f"{TITLE} · {TAGLINE.rstrip('.')}", DESC, home)
page("/privacy/", f"Privacy · {TITLE}", "What longshortnmargin.tech collects when you visit or join the waitlist, what it is used for, and how to be removed.", privacy)
page("/terms/", f"Terms · {TITLE}", "Terms for longshortnmargin.tech: what LongShortNMargin is and is not, early access, trademarks and licences.", terms)
page("/404.html", f"Page not found · {TITLE}", "That page does not exist.", notfound, noindex=True)

with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for p in ("/", "/privacy/", "/terms/"):
        f.write(f"<url><loc>{SITE}{p}</loc></url>\n")
    f.write("</urlset>\n")
with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
with open(os.path.join(OUT, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="6" fill="#16181a"/>'
            '<text x="16" y="22" text-anchor="middle" font-family="Inter,Helvetica,Arial,sans-serif" font-size="17" font-weight="600" fill="#fbfaf7">LS</text></svg>')
open(os.path.join(OUT, ".nojekyll"), "w").close()
