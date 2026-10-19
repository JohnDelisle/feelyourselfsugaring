# Generates the static HTML pages into docs/, which GitHub Pages serves. Output is plain HTML.
#
# Layout: docs/ is the published site; media/ holds working materials (originals, logos);
# this script and the notes stay at the repo root.
import json, os, re
SITE_DIR = "docs"
SITE = "https://www.feelyourselfsugaring.com/"
PHONE_HREF = "sms:+12045575197"
PHONE = "204-557-5197"
INSTAGRAM = "https://www.instagram.com/feelyourselfsugaring/"
MAPS = "https://maps.google.com/?cid=16458464166340835351"          # public Google Maps listing
REVIEW = "https://g.page/r/CRe4PWf1NWjkEBM/review"                 # "write a review" link from the Business Profile
CF_BEACON = ""                                                    # Cloudflare Web Analytics token; empty = no analytics
FORM = "https://docs.google.com/forms/d/e/1FAIpQLSeQs9sJO3A9PlhY3qhilEIwmsSzeXqD-X9Zkp8nebxhRqmKyg/viewform"

# Brand mark: echoes Pamela's two-hearts logo.
HEART = "M0 20C-14 8-20 2-20-6c0-7 5-11 11-11 4 0 7 2 9 5 2-3 5-5 9-5 6 0 11 4 11 11 0 8-6 14-20 26z"
HEARTS = (f'<svg class="mark" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="31" fill="#1C1C1C"/>'
          f'<path d="{HEART}" fill="#FACBD0" transform="translate(25 29) scale(.66)"/>'
          f'<path d="{HEART}" fill="#F385AA" transform="translate(40 35) scale(.66)"/></svg>')

# ---------------- Shared content ----------------
popular = [("Brazilian","For people with a vulva. Includes inner glutes.",50),("Bikini line, extended","",35),
  ("Legs, full","",90),("Legs, half","",45),("Legs, quarter","",20),("Chest or back","",50),
  ("Face, full","Includes a brow touch-up.",40),("Arms, full","",40),("Arms, half","",25),
  ("Bum cheeks","",25),("Underarms","",20),("Abdomen, full","",20),("Ears","",20)]
addons = [("Ingrown hair extraction","15 minutes.",10),("Upper and lower lip","",10),("Chin","Includes lower lip.",10),
  ("Brow touch-up","",10),("Nape of the neck","",10),("Abdomen trail","",10),("Areolas","",10)]

def plist(items):
    out=[]
    for n,note,p in items:
        s = f"<small>{note}</small>" if note else ""
        out.append(f'<li><span class="name">{n}{s}</span><span class="amt">${p}</span></li>')
    return '<ul class="price-list">\n'+"\n".join(out)+"\n</ul>"

def price_block():
    return f'''    <p class="price-note">2026 prices, taxes included. Every service is gender-inclusive. Prices are starting points and may change with the time and product a service needs.</p>
    <div class="prices">
      <div>
        <h3>Most popular</h3>
{plist(popular)}
      </div>
      <div>
        <h3>Add-ons</h3>
{plist(addons)}
        <p class="price-note" style="margin-top:1.25rem">Don't see what you need? <a href="{PHONE_HREF}">Text Pamela</a> about a custom service.</p>
      </div>
    </div>
    <h3 style="margin-top:3rem">Ways to save</h3>
    <div class="offers">
      <div class="offer"><h3>Leave a Google review</h3><p>Rate and review us on Google and get $10 off your next service. <a href="{REVIEW}">Write a review</a>.</p></div>
      <div class="offer"><h3>Refer a friend</h3><p>When someone new books on your recommendation, you both get $10 off your next service.</p></div>
    </div>'''

ld = {"@context":"https://schema.org","@type":"BeautySalon","name":"Feel Yourself Sugaring",
      "description":"Home-based body sugaring hair removal in Winnipeg's Charleswood/Tuxedo neighbourhood.",
      "url":SITE,"telephone":"+1-204-557-5197","sameAs":[INSTAGRAM, MAPS],"hasMap":MAPS,
      "founder":{"@type":"Person","name":"Pamela Delisle"},
      "address":{"@type":"PostalAddress","streetAddress":"31 Woodview Bay","addressLocality":"Winnipeg","addressRegion":"MB","addressCountry":"CA"},
      "areaServed":"Winnipeg, MB","priceRange":"$10–$90"}

perks = [
 ("Flexible hours","Daytime, evening, weekday and weekend appointments."),
 ("Unrushed appointments","Longer sessions if you'd like a more relaxed pace."),
 ("Mobile service","Pamela can come to you, on your own or with a group."),
 ("The forest next door","Take a walk in Assiniboine Forest and Park before or after your appointment."),
 ("Plants and art","14 plants and 8 original artworks, including screen prints by Manitoba artist Eric Ouimet."),
 ("Curated products","Shop a small selection of exfoliating and hydrating products for aftercare at home."),
 ("Little surprises","Aftercare gifts, plus stress balls and candy to keep your mind busy."),
 ("Your playlist","Music chosen to suit your mood."),
 ("Gender-inclusive pricing","Prices are based on the service, not on your gender."),
 ("Scent-free and pet-free","No artificial scents, and no fur or feathers for anyone with allergies."),
 ("Made by Pamela","One-of-a-kind promo material, designed by Pamela herself."),
]

groups = [
 ("Easier on your skin",[
   ("Gentler than waxing","The paste comes off in small sections, in the direction your hair grows, so it hurts less."),
   ("Good for sensitive skin","Sugar sticks only to hair and dead skin, not live skin, and it's applied at body temperature, so there's no risk of burns."),
   ("Fewer ingrown hairs","Sugaring clears away dead skin and pulls hair out the way it grows, so less hair breaks off and gets trapped."),
   ("Very precise","It removes hair as short as 1/16 of an inch, so you can come in sooner than you could for waxing."),
 ]),
 ("Better over time",[
   ("Results that build","Initial results last 3 to 4 weeks. With regular appointments, hair grows back slower, finer and softer, and over time it may stop growing back. Each visit gets easier."),
   ("Put down the razor","Shaving undoes the progress by letting hair grow back strong and thick from the root."),
   ("Works almost anywhere","Every part of the body can be sugared."),
   ("Priced like waxing","Sugaring takes more training, but costs about the same as waxing."),
 ]),
 ("Good for you",[
   ("Simple, natural paste","Just sugar, lemon and water. It's sanitary, biodegradable and wipes off with a damp cloth."),
   ("Thousands of years of safe use","Sugaring dates back to ancient Egypt."),
   ("Gender affirming","Removing hair can help your body match your authentic self, and boost your confidence."),
   ("Feel at home in your body","Smooth skin can add new sensations and new ways to appreciate your body."),
   ("A self-care ritual","Following your sugarist's before-and-after advice builds habits that feel good, and can lead to other healthy choices."),
 ]),
]

stages = [
 ("Before your appointment",[
   ("Fill out your client profile.",'Complete the <a href="book-now.html#form">Client Profile and Consent Form</a> before your first visit.'),
   ("Let your hair grow.","Aim for 1/16 to 1/4 of an inch. Longer hair can be sugared, but it takes more time and is less comfortable. Trim longer hair with a #2 guard."),
   ("Exfoliate and moisturize","the day before for the best results."),
   ("Drink plenty of water","in the days leading up to your appointment."),
   ("Practice slow breathing.","It really does help with any discomfort."),
   ("Time it with your cycle.","If you menstruate, sugaring tends to hurt less between the last day of bleeding and the day before you ovulate. On a 28-day cycle with 4 to 5 days of bleeding, that's about days 5 to 13."),
 ]),
 ("On the day",[
   ("Keep the day calm","if you can."),
   ("Feeling nervous is normal.","Tell Pamela. She's there to support you."),
   ("Drink water,","and skip caffeine and alcohol."),
   ("Avoid acidic foods","before your appointment."),
   ("Come with clean skin:","no makeup, deodorant, perfume, cologne or lotion on the area."),
   ("Wear loose, clean clothes.",""),
   ("Consider a pain reliever.","If your doctor says it's OK, take one 30 minutes before your appointment."),
 ]),
 ("During your appointment",[
   ("Speak up.","Share any questions, concerns or needs as they come up."),
   ("Remember it's brief.","Any discomfort passes quickly, and the results are worth it."),
   ("Use your tools:","slow breathing, or one of the studio's stress balls."),
   ("Wearing a tampon?","Tuck the string inside for the appointment."),
   ("Book your next visit","before you leave. Appointments are usually 3 to 6 weeks apart, depending on the service."),
 ]),
 ("The first 48 hours",[
   ("Expect some redness.","Redness, swelling and tiny spots of blood are normal and should fade within a few hours."),
   ("Use a cold compress","if your skin needs soothing."),
   ("Protect the area","from heat, friction, and dirty hands or clothing."),
   ("Take a break","from sex, heavy exercise, saunas, steam rooms, hot showers, pools, lakes and hot tubs."),
   ("Skip skincare products,","including deodorant, unless Pamela recommends them."),
   ("Stay out of the sun","and tanning beds."),
   ("Wait to exfoliate","until your skin feels normal again."),
 ]),
 ("Until your next appointment",[
   ("Reach out","to Pamela with any questions or concerns."),
   ("Keep drinking water","for healthy skin."),
   ("Moisturize daily","with a natural, fragrance-free moisturizer."),
   ("Exfoliate 2 to 3 times a week","to keep skin smooth and ingrown-free."),
   ("Avoid tight clothes","that rub on sugared areas."),
   ("Don't shave.","It sets back the progress sugaring makes."),
   ("Leave ingrown hairs alone.","Exfoliate or use an ingrown serum instead of picking."),
 ]),
]

# ---------------- Builder ----------------
def build(outdir):
    """Write the complete set of pages into outdir."""
    NAV = [("index.html","Home"),("new-clients.html","New here?"),("prices.html","Prices"),
           ("our-sugarist.html","Our sugarist"),("our-studio.html","Our studio"),
           ("why-sugar.html","Why sugar"),("wellness-tipping.html","Wellness tipping"),("advice.html","Advice")]

    def photo(src, label, cls=""):
        return (f'<figure class="{" ".join(["photo", cls]).strip()}" data-label="{label}"><img src="images/{src}" alt="{label}" loading="lazy" '
                f'onerror="this.parentNode.classList.add(\'missing\');this.remove()"></figure>')

    def page(slug, title, desc, body, extra_head=""):
        nav = "\n".join(
            f'<a href="{h}"{" aria-current=\"page\"" if h==slug else ""}>{t}</a>' for h,t in NAV)
        book_cur = ' aria-current="page"' if slug=="book-now.html" else ""
        full_title = "Feel Yourself Sugaring | Sugaring hair removal in Winnipeg" if slug=="index.html" else f"{title} | Feel Yourself Sugaring"
        url = SITE if slug=="index.html" else SITE + slug.replace(".html","")
        beacon = (f"\n<script defer src=\"https://static.cloudflareinsights.com/beacon.min.js\" "
                  f"data-cf-beacon='{{\"token\": \"{CF_BEACON}\"}}'></script>") if CF_BEACON else ""
        return f'''<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}images/share.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Pamela sugaring a client's leg, beside the Feel Yourself Sugaring logo">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{url}">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" href="favicon-48.png" type="image/png" sizes="48x48">
<link rel="icon" href="favicon-96.png" type="image/png" sizes="96x96">
<link rel="icon" href="favicon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Newsreader:ital,opsz,wght@0,6..72,400..600;1,6..72,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<script>document.documentElement.classList.add('js')</script>{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html">{HEARTS}Feel Yourself Sugaring</a>
    <nav class="nav" id="site-nav" aria-label="Main">
{nav}
    </nav>
    <a class="btn header-book" href="book-now.html"{book_cur}>Book now</a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h2>Contact</h2>
        <p>Text <a href="{PHONE_HREF}">{PHONE}</a></p>
        <p>31 Woodview Bay, Winnipeg<br>Charleswood/Tuxedo, beside Assiniboine Forest</p>
        <p><a href="{MAPS}">Open in Google Maps</a></p>
      </div>
      <div>
        <h2>Hours</h2>
        <p>By appointment only, no walk-ins.</p>
        <p>Daytime, evening and weekend appointments.</p>
      </div>
      <div>
        <h2>Follow</h2>
        <p><a href="{INSTAGRAM}">Instagram</a></p>
        <p><a href="{REVIEW}">Leave a Google review</a></p>
        <p><a href="book-now.html">Book an appointment</a></p>
      </div>
    </div>
    <p class="land">Feel Yourself Sugaring is located on Treaty 1 Territory, the stolen land of the Anishinaabe, Cree, Oji-Cree, Dakota and Dene peoples, and the homeland of the Métis Nation.</p>
  </div>
</footer>
<script src="script.js"></script>{beacon}
</body>
</html>
'''

    pages = {}

    # ---------------- HOME ----------------
    prices_section = f'''<section class="section rule" id="prices">
  <div class="wrap split">
    <h2>Services and prices</h2>
    <div>
      <p class="lead">2026 prices, taxes included, and the same price for everyone. A Brazilian is $50, full legs are $90, underarms are $20, and add-ons like lip, chin or brows are $10 each.</p>
      <p>Prices are starting points and may change with the time and product a service needs. Leave a Google review or refer a friend and you get $10 off your next visit.</p>
      <div class="actions"><a class="btn btn-primary" href="prices.html">See all prices</a><a class="btn" href="{PHONE_HREF}">Ask about a custom service</a></div>
    </div>
  </div>
</section>'''

    pages["index.html"] = page("index.html","Home",
     "Gentle, unrushed sugaring hair removal in Winnipeg, a gentler alternative to waxing. Home studio beside Assiniboine Forest. Everyone welcome.",
    f'''<section class="hero">
  <div class="wrap">
    <div>
      <h1>Feel yourself.</h1>
      <p class="lead">Gentle, unrushed sugaring hair removal in a home studio beside Assiniboine Forest in Winnipeg. Everyone is welcome.</p>
      <div class="actions">
        <a class="btn btn-primary" href="book-now.html">Book an appointment</a>
        <a class="btn" href="{PHONE_HREF}">Text Pamela</a>
      </div>
      <p class="hero-note">New to sugaring? <a href="new-clients.html">Start here</a>.</p>
    </div>
    <div class="hero-art">
      <figure class="photo"><img src="images/hero-pamela.jpg" alt="Pamela sugaring a client's leg in the studio"></figure>
    </div>
  </div>
</section>

<section class="section rule">
  <div class="wrap split">
    <h2>Soft skin, and a lift in your spirits.</h2>
    <div>
      <p class="lead">Pamela Delisle is the owner and only sugarist at Feel Yourself Sugaring. She works from a calm, scent-free studio in her Charleswood/Tuxedo home.</p>
      <p>Tweens to seniors, 2SLGBTQ+ folks, every body size and background: you'll get the same care and attention, free of judgment. Pamela keeps training with new certifications and private lessons so your results keep getting better.</p>
      <p><strong>New to sugaring, or a little nervous?</strong> Text Pamela to set up a meet and greet. You can tour the studio and ask questions before you book.</p>
      <p><a href="our-sugarist.html">Meet Pamela</a></p>
    </div>
  </div>
</section>

{prices_section}

<section class="section band">
  <div class="wrap split">
    <h2>Every tip helps someone else get sugared.</h2>
    <div>
      <p class="lead">Pamela gives 100% of her tips to clients who want to be sugared but have no self-care budget.</p>
      <p>If cost is what's stopping you from booking, ask about a Wellness Spot.</p>
      <div class="actions"><a class="btn" href="wellness-tipping.html">How wellness tipping works</a></div>
    </div>
  </div>
</section>''',
     extra_head='\n<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>')

    # ---------------- PRICES ----------------
    pages["prices.html"] = page("prices.html","Prices",
     "2026 gender-inclusive sugaring prices at Feel Yourself Sugaring in Winnipeg, from $10 add-ons to full legs.",
    f'''<section class="page-head">
  <div class="wrap">
    <h1>Services and prices</h1>
    <p class="lead">Every service is priced the same for everyone. Nervous or new to sugaring? Text Pamela for a meet and greet before you book.</p>
  </div>
</section>
<section class="section rule">
  <div class="wrap">
{price_block()}
    <div class="actions" style="margin-top:2.5rem"><a class="btn btn-primary" href="book-now.html">Book an appointment</a><a class="btn" href="wellness-tipping.html">Can't afford it? Wellness Spots</a></div>
  </div>
</section>''')

    # ---------------- NEW CLIENTS ----------------
    pages["new-clients.html"] = page("new-clients.html","New to sugaring?",
     "What sugaring is, what an appointment at Feel Yourself Sugaring is like, and how to get ready for your first visit.",
    f'''<section class="page-head">
  <div class="wrap">
    <div class="with-photo">
      <div>
        <h1>New to sugaring? Start here.</h1>
        <p class="lead">Most people find Pamela while searching for hair removal near them. If that's you, this page explains what sugaring is, what an appointment is like, and how to get ready, so there are no surprises for either of us.</p>
      </div>
      {photo("hero-pamela.jpg","Pamela sugaring a client's leg")}
    </div>
  </div>
</section>

<section class="section rule">
  <div class="wrap split">
    <h2>What sugaring is</h2>
    <div>
      <p class="lead">Sugaring removes hair with a soft paste made of nothing but sugar, lemon and water. Pamela applies it by hand at body temperature, then flicks it off in small sections, in the direction your hair grows.</p>
      <p>That direction matters. Waxing pulls against the grain and sticks to live skin. Sugar paste sticks only to hair and dead skin cells, so it takes the hair out whole, root and all, with much less tugging on your skin. There's no heat, so there's no risk of burns, and it's gentle enough for sensitive skin and for areas like the face and bikini line.</p>
      <p>It's also precise. Sugaring removes hair as short as 1/16 of an inch, so you can come in sooner than you could for waxing, and because hair comes out the way it grows, less of it breaks off and gets trapped. That means fewer ingrown hairs.</p>
      <p>The paste is sanitary, biodegradable and wipes off with a damp cloth. People have used it safely since ancient Egypt. Sugaring takes more training than waxing, but costs about the same.</p>
      <p><strong>What results to expect.</strong> Your first results last about 3 to 4 weeks. With regular appointments, hair grows back slower, finer and softer, and as the root weakens it may stop growing back altogether. Every appointment gets easier and more comfortable than the last. Shaving between appointments undoes that progress, because it lets the hair grow back strong and thick from the root.</p>
      <p>Every part of the body can be sugared. <a href="why-sugar.html">More reasons people stick with sugaring</a>.</p>
    </div>
  </div>
</section>

<section class="section rule">
  <div class="wrap split">
    <h2>What to expect from Pamela</h2>
    <div>
      <p class="lead">Feel Yourself Sugaring is a home-based studio at 31 Woodview Bay in Charleswood/Tuxedo, beside Assiniboine Forest. Pamela is the owner and the only sugarist, so you'll see her every time.</p>
      <dl class="perks">
        <div><dt>A welcome for everyone</dt><dd>Tweens to seniors, 2SLGBTQ+ folks, people of every body size and background. The studio is discrimination-free, and the well-being of each person comes first.</dd></div>
        <div><dt>Someone on your side</dt><dd>Sugaring doesn't have to be intimidating when the person doing it cares about you. Pamela listens to what you need, puts your comfort first, and explains what she's doing as she goes.</dd></div>
        <div><dt>Unrushed</dt><dd>Appointments are never hurried. If you'd like a slower pace or a longer session, just ask.</dd></div>
        <div><dt>Scent-free, pet-free</dt><dd>No artificial scents in the studio, and no fur or feathers in the home, for anyone with allergies or sensitivities.</dd></div>
        <div><dt>A calm room</dt><dd>Plants, original art, a playlist chosen for your mood, stress balls and candy to keep your mind busy, and a small gift for aftercare.</dd></div>
        <div><dt>A "sugar nerd"</dt><dd>Pamela was certified in May 2023 with specialized training in Brazilian and facial sugaring, and keeps adding certifications and private training so you get the best technique and premium products.</dd></div>
        <div><dt>Aftercare you can take home</dt><dd>You'll leave with advice for the first 48 hours and beyond, and the studio stocks exfoliating and hydrating products if you want them.</dd></div>
        <div><dt>Mobile service</dt><dd>Pamela can also come to you, on your own or with a group.</dd></div>
      </dl>
    </div>
  </div>
</section>

<section class="section rule">
  <div class="wrap split">
    <h2>What Pamela asks of you</h2>
    <div>
      <p class="lead">A few things make your appointment go smoothly, for you and for her.</p>
      <ol class="steps">
        <li><strong>Fill out the <a href="book-now.html#form">Client Profile and Consent Form</a> before your first appointment.</strong> It covers your health history, skin, medications and consent, so Pamela can look after you safely.</li>
        <li><strong>Let your hair grow to between 1/16 and 1/4 of an inch.</strong> Longer hair can be sugared, but it takes more time and is less comfortable. Trim longer hair with a #2 guard. Don't shave in the weeks before.</li>
        <li><strong>Arrive with clean skin.</strong> No makeup, deodorant, perfume, cologne or lotion on the area. Wear loose, clean clothes.</li>
        <li><strong>Tell her how you're feeling.</strong> Being nervous is normal. Say so, and speak up during the appointment about anything you need.</li>
        <li><strong>Book by text, and come at your booked time.</strong> The studio is in a family home, by appointment only, with no walk-ins.</li>
      </ol>
      <p>The full preparation and aftercare list is on the <a href="advice.html">Advice</a> page.</p>
    </div>
  </div>
</section>

<section class="section rule">
  <div class="wrap split">
    <h2>Your first appointment, step by step</h2>
    <div>
      <ol class="steps">
        <li><strong>Text Pamela at <a href="{PHONE_HREF}">{PHONE}</a></strong> with the service you'd like and a few times that work. Daytime, evening and weekend appointments are available.</li>
        <li><strong>Fill out the client profile</strong> online before you arrive.</li>
        <li><strong>Get ready</strong> in the days before: exfoliate and moisturize the day before, drink plenty of water, and practice slow breathing. If you menstruate, appointments tend to hurt less between the last day of bleeding and the day before you ovulate.</li>
        <li><strong>At the studio,</strong> Pamela will go over your form, answer your questions and get you settled. She cleanses and preps the area, sugars it section by section, then soothes the skin. Any discomfort is brief, and you can use your breathing or a stress ball. If you're wearing a tampon, tuck the string inside.</li>
        <li><strong>Afterward,</strong> expect some redness, swelling and tiny spots of blood for a few hours. For 48 hours, keep the area away from heat, friction, sun, pools, hot tubs, heavy exercise and skincare products. Then moisturize daily and exfoliate 2 to 3 times a week.</li>
        <li><strong>Book your next visit</strong> before you leave, usually 3 to 6 weeks out depending on the service. The second appointment is easier than the first.</li>
      </ol>
    </div>
  </div>
</section>

<section class="section rule">
  <div class="wrap split">
    <h2>Prices and paying for it</h2>
    <div>
      <p class="lead">Prices are the same for everyone and include tax. Add-ons start at $10, a Brazilian is $50, and full legs are $90. <a href="prices.html">See all prices</a>.</p>
      <p>If cost is what's stopping you, ask about a Wellness Spot. Pamela gives 100% of her tips to clients who want to be sugared but have no self-care budget, and nobody has to prove anything. <a href="wellness-tipping.html">How wellness tipping works</a>.</p>
      <p><a href="{REVIEW}">Leave a Google review</a>, or refer a friend, and you get $10 off your next service.</p>
    </div>
  </div>
</section>

<section class="section band">
  <div class="wrap split">
    <h2>Still nervous? Come for a meet and greet.</h2>
    <div>
      <p class="lead">Text Pamela to set up a short visit. Tour the studio, ask anything, and learn about sugaring before you book. No obligation.</p>
      <div class="actions"><a class="btn" href="{PHONE_HREF}">Text Pamela</a><a class="btn" href="book-now.html">Book an appointment</a></div>
    </div>
  </div>
</section>''')

    # ---------------- OUR SUGARIST ----------------
    pages["our-sugarist.html"] = page("our-sugarist.html","Our sugarist",
     "Meet Pamela Delisle, certified sugarist and owner of Feel Yourself Sugaring in Winnipeg.",
    f'''<section class="page-head">
  <div class="wrap">
    <h1>Hi, I'm Pamela.</h1>
    <p class="lead">I'm the owner and only sugarist at Feel Yourself Sugaring, and I'd love to pamper you at my home studio next to Assiniboine Forest.</p>
  </div>
</section>
<section class="section rule">
  <div class="wrap split">
    <div>
      {photo("pamela.jpg","Pamela Delisle")}
      <ul class="facts" style="margin-top:1.25rem">
        <li>Certified sugarist since May 2023</li>
        <li>Specialized training in Brazilian and facial sugaring</li>
        <li>Started her career at White Elm Spa, River Heights</li>
        <li>Scent-free studio in a fur- and feather-free home</li>
      </ul>
    </div>
    <div>
      <p class="lead">I was sugared for the first time in 2022. The results beat my expectations, and making time for it reminded me that I was worth the pampering.</p>
      <p>I wanted to share that feeling, so I trained. I was certified in May 2023, started as a sugarist at White Elm Spa in River Heights that July, and founded Feel Yourself Sugaring at the same time. I keep adding certifications and private training so every appointment gets my best technique and premium products.</p>
      <p>I also bring my background as a women's health social worker, an artist, a spouse and a parent. All of it shapes the care I give.</p>
      <h2 style="margin-top:2rem">What matters most to me</h2>
      <p>The connection. Showing up for an appointment takes trust, and I don't take that lightly. You're not just a client. You're someone who deserves care.</p>
      <p>I'll listen to what you need, put your comfort first, and send you home with aftercare advice so your results last. With someone on your side, sugaring stops feeling intimidating.</p>
      <p>Everyone is welcome here: tweens to seniors, 2SLGBTQ+ folks, and people of every body size and background.</p>
      <div class="actions"><a class="btn btn-primary" href="book-now.html">Book with Pamela</a><a class="btn" href="{PHONE_HREF}">Text a question</a></div>
    </div>
  </div>
</section>''')

    # ---------------- OUR STUDIO (absorbs old "Why us") ----------------
    dl = "\n".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a,b in perks)
    pages["our-studio.html"] = page("our-studio.html","Our studio",
     "A calm, plant-filled home studio in Charleswood/Tuxedo, Winnipeg, steps from Assiniboine Forest.",
    f'''<section class="page-head">
  <div class="wrap">
    <h1>The studio</h1>
    <p class="lead">A calm, plant-filled room in Pamela's Charleswood/Tuxedo home, a short walk from Assiniboine Forest.</p>
    <div class="gallery">
      {photo("studio-1.jpg","The studio")}
      {photo("studio-2.jpg","Plants and artwork in the studio")}
      {photo("studio-3.jpg","Aftercare products")}
    </div>
  </div>
</section>
<section class="section" id="why-us">
  <div class="wrap">
    <h2>What makes it different</h2>
    <dl class="perks">
{dl}
    </dl>
  </div>
</section>''')

    # ---------------- WHY SUGAR ----------------
    gh = ""
    for g,items in groups:
        dl = "\n".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a,b in items)
        gh += f'<div class="group"><h2>{g}</h2>\n<dl class="perks">\n{dl}\n</dl></div>\n'
    pages["why-sugar.html"] = page("why-sugar.html","Why sugar",
     "Sugaring is a gentler alternative to waxing and shaving: kinder to sensitive skin, fewer ingrown hairs, and results that build over time.",
    f'''<section class="page-head">
  <div class="wrap">
    <div class="with-photo">
      <div>
        <h1>Why sugar?</h1>
        <p class="lead">Sugaring removes hair with a warm paste of sugar, lemon and water. Here's why people who try it tend to stick with it.</p>
      </div>
      {photo("sugar-skin.jpg","Sugar paste on skin, mid-appointment")}
    </div>
  </div>
</section>
<section class="section rule">
  <div class="wrap">
{gh}
    <div class="actions"><a class="btn btn-primary" href="book-now.html">Try sugaring</a></div>
  </div>
</section>''')

    # ---------------- WELLNESS TIPPING ----------------
    pages["wellness-tipping.html"] = page("wellness-tipping.html","Wellness tipping",
     "100% of tips at Feel Yourself Sugaring fund sugaring for people with no self-care budget.",
    f'''<section class="page-head">
  <div class="wrap">
    <h1>Wellness tipping</h1>
    <p class="lead">100% of tips go to people who want to be sugared but don't have a self-care budget.</p>
  </div>
</section>
<section class="section rule">
  <div class="wrap split">
    <div><h2>How it works</h2>{photo("tipping.jpg","Tip money beside a Feel Yourself Sugaring pin","wide")}</div>
    <div>
      <p>Wellness services like sugaring should be open to everyone, whatever their budget. So every tip Pamela receives pays for appointments for people who self-declare as having no money for self-care.</p>
      <p>Nobody has to prove anything. If you say you need a spot, that's enough.</p>
    </div>
  </div>
</section>
<section class="section rule">
  <div class="wrap split">
    <h2>If you can tip</h2>
    <div>
      <p>If you have room in your self-care budget, please consider tipping after your appointment. Your tip says thanks, and it gives someone else in our community the same care you just had.</p>
      <p>That's the point: healthier, happier neighbourhoods, where everyone's well-being matters.</p>
    </div>
  </div>
</section>
<section class="section band">
  <div class="wrap split">
    <h2>If cost is in the way</h2>
    <div>
      <p class="lead">Ask about a Wellness Spot. We'll work out something that puts your well-being first.</p>
      <div class="actions"><a class="btn" href="{PHONE_HREF}">Text Pamela about a Wellness Spot</a></div>
    </div>
  </div>
</section>''')

    # ---------------- ADVICE ----------------
    sh = ""
    for title, tips in stages:
        lis = "\n".join(f"<li><strong>{a}</strong> {b}".rstrip()+"</li>" for a,b in tips)
        sh += f'<li class="stage"><div><h2>{title}</h2>\n<ul class="tips">\n{lis}\n</ul></div></li>\n'
    pages["advice.html"] = page("advice.html","Advice",
     "How to prepare for sugaring and care for your skin afterward, from the week before to your next appointment.",
    f'''<section class="page-head">
  <div class="wrap">
    <h1>Before and after</h1>
    <p class="lead">A little preparation makes sugaring more comfortable and helps your results last.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <ol class="stages">
{sh}
    </ol>
  </div>
</section>''')

    # ---------------- BOOK NOW ----------------
    pages["book-now.html"] = page("book-now.html","Book now",
     "Book a sugaring appointment with Pamela by text, and fill out your client profile before your first visit.",
    f'''<section class="page-head">
  <div class="wrap">
    <h1>Book an appointment</h1>
    <p class="lead">Appointments are by text, with daytime, evening and weekend times available.</p>
    <ol class="steps">
      <li><strong>Text Pamela at <a href="{PHONE_HREF}">{PHONE}</a></strong> with the service you'd like and a few times that work for you.</li>
      <li><strong>Fill out the Client Profile and Consent Form below</strong> before your first appointment.</li>
    </ol>
    <div class="actions"><a class="btn btn-primary" href="{PHONE_HREF}">Text to book</a></div>
    <p class="muted" style="margin-top:1.25rem">Not sure yet? Ask for a meet and greet: tour the studio and learn about sugaring first. <a href="new-clients.html">New to sugaring? Start here.</a></p>
  </div>
</section>
<section class="section rule" id="form">
  <div class="wrap">
    <h2>Client Profile and Consent Form</h2>
    <p class="muted">Your answers go only to Pamela. She uses them to sugar you safely, because your health history, skin and medications affect how she works. They're kept in the business's Google account and never shared or sold. Text Pamela any time to see, correct or delete what you've sent.</p>
    <p>Trouble with the form? <a href="{FORM}">Open it in a new tab</a>.</p>
    <iframe class="form-frame" src="{FORM}?embedded=true" title="Client Profile and Consent Form" loading="lazy"></iframe>
  </div>
</section>''')

    # Redirects for old Google Sites URLs
    def redirect(target):
        return f'''<!doctype html><html lang="en-CA"><head><meta charset="utf-8"><title>Moved</title>
<meta http-equiv="refresh" content="0; url={target}"><link rel="canonical" href="{target}"></head>
<body><p>This page has moved to <a href="{target}">{target}</a>.</p></body></html>
'''
    pages["home.html"] = redirect("index.html")
    pages["why-us.html"] = redirect("our-studio.html#why-us")

    nf = page("404.html","Page not found","This page doesn't exist.",
    '''<section class="page-head"><div class="wrap"><h1>Page not found</h1>
<p class="lead">That page doesn't exist, or it moved when the site was rebuilt.</p>
<div class="actions"><a class="btn btn-primary" href="/">Go to the home page</a><a class="btn" href="/book-now">Book an appointment</a></div></div></section>''')
    # 404 is served from any path, so it needs root-relative asset links
    nf = nf.replace('href="styles.css"','href="/styles.css"').replace('src="script.js"','src="/script.js"').replace('href="favicon','href="/favicon').replace('href="apple-touch-icon.png"','href="/apple-touch-icon.png"')
    nf = re.sub(r'href="([a-z0-9-]+\.html)', r'href="/\1', nf)
    pages["404.html"] = nf

    # Search engines: only meaningful at the domain root, so these start working at cutover
    urls = "\n".join(f"  <url><loc>{SITE if n=='index.html' else SITE + n.replace('.html','')}</loc></url>"
                     for n in pages if n not in ("home.html","why-us.html","404.html"))
    pages["sitemap.xml"] = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
'''
    pages["robots.txt"] = f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n"

    os.makedirs(outdir, exist_ok=True)
    for name, html in pages.items():
        open(os.path.join(outdir, name), "w", encoding="utf-8", newline="\n").write(html)
    print(f"built {len(pages)} files in {outdir}")

build(SITE_DIR)
