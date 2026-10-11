# Handoff — where things stand (written 2026-10-11, end of session)

Read this with CLAUDE.md. CLAUDE.md holds the standing rules and layout; this file holds the current state, decisions so far, open questions, and the to-do list. Update it at the end of each session.

## Status

- The site is live on GitHub Pages at https://johndelisle.github.io/feelyourselfsugaring/ from `main` + `/docs`. Custom domain not moved yet; www.feelyourselfsugaring.com still serves the old Google Site.
- All work is committed and pushed. `media/` (about 400 MB) is in git on purpose as a backup of the Drive folder.
- Pamela has seen the first version and liked the tighter content and structure. She didn't love the yellow honey blob on the home page. She's worried the tightened copy drops messages she cares about (educating new clients, setting expectations).
- John's own picks so far: **noir** theme, **prices on the home page** (the main build, not the variant). Pamela hasn't chosen yet.

## What's built for her to choose from

All of it is switchable on the live site with the corner switcher (github.io only) or URL parameters, and "Copy share link" in the switcher gives a URL that captures the choices.

- Themes: `pine` (default), `brand`, `teal`, `noir`.
- Hero art on the home page: `blob` (default), `hearts`, `hips`, `pamela`, `sugar`, `legs`, `studio`, `none`.
- Extra inner-page photos: `photos=more` (default) or `fewer`.
- Layout: prices on home page (main) vs. `docs/variants/prices-page/`.
- New pages: `new-clients.html` ("New here?", Pamela's fuller voice for Google Maps arrivals) and `prices.html` (direct link to prices).

When Pamela decides, make the choices permanent and strip the rest; CLAUDE.md says how. Do that before the domain cutover so the site goes lean.

## Open questions for Pamela

1. Theme, hero, photos, and prices layout. Also whether the hips logo should appear anywhere.
2. Policies the old site never stated, for the new-client page: cancellation and lateness, payment methods, parking and how to enter the home studio, age rule for tweens (parent present?), and whether mobile service has a travel fee.
3. Check the "at the studio" step of the appointment walkthrough on `new-clients.html`. It's written from standard sugaring practice, not from Pamela.
4. The 2024 price sheet in Drive lists services the site doesn't: hydrojelly mask add-on after Brazilian/bikini, "Feel Your Skin Pampered" and "Nurtured" treatments, PCOS facial hair removal, five-session packages, first-visit aftercare gift. Still offered?
5. The review offer says "$10 off for a Google review." Google's policy forbids incentivized reviews. Suggest rewording to a thank-you after the fact, and ask Pamela how she wants it handled.

## Google Business Profile: findings and suggestions

Findings (2026-10-11): 5.0 stars from 89 reviews, category "Hair removal service", LGBTQ+ friendly attribute, Pamela replies to reviews. Competitors on the "people also search for" row: Nude Sugar Bar 4.8/180, Bare Body Sugaring 4.8/381, Sweet Secrets 4.6/275, LA Sugaring 4.3/94. Best rating, fewest reviews. Review keywords Google surfaces: "sugarist", "waxing appointment", "no ingrown hairs", "brow shaping". Dashboard says profile strength "Looks good", 672 customer interactions. Third-party listings exist on Fresha (says "Elmhurst", 8 a.m. to 10 p.m.), BookBeauty and Wheree.

Gaps: no booking/appointment link, no public business description, no services list, no posts, no exterior/arrival photo, hours show "Closed" outside 8 a.m. to whatever, holiday hours not set.

Suggested, in order of payoff:

1. Set the appointment URL (dashboard → Bookings) to the Book Now page.
2. Use the review link and QR code (dashboard → Ask for reviews) at checkout or in the post-appointment text. Review volume is the gap versus competitors.
3. Write the business description (750 chars, no links). Can be drafted from the site copy.
4. Add services with prices (dashboard → Edit services). Map from `popular` and `addons` in `build.py`.
5. Fix hours: real availability, or "By appointment" attribute, so "Closed" stops showing at times she'd take a booking.
6. Add photos: Pamela at work (`docs/images/hero-pamela.jpg`), the portrait, and an exterior/entry photo.
7. Posts and offers: the referral offer as an "Offer" post; a post every few weeks.
8. Check attributes: Women-owned, Appointment required, accessibility, mobile service.
9. Seed Q&A with the questions clients text most (what to wear, hair length, pain, do you take men). Answers exist on the new-client page.

Site-side follow-ups from this: add "the gentler alternative to waxing" phrasing to titles/new-client page since searchers say "waxing"; reword the review offer (see open question 5).

Offered but not yet done: a paste-ready document with the description, the services list with prices, and five Q&A pairs for the dashboard.

## Technical notes for the next session

- `python build.py` regenerates `docs/` and `docs/variants/`. Run it after any content change and commit the output.
- Local preview: `cd docs && python -m http.server 8765` then open http://127.0.0.1:8765/. The switcher shows on localhost.
- Chrome screenshots through the extension were flaky this session (timeouts on the first capture after a navigation). JavaScript queries on the page worked; a second screenshot attempt often worked. Not a site bug.
- Google Drive connector: the business account (john@feelyourselfsugaring.com) is now the connected identity. It returns image bytes as base64 text, so it's only practical for small files. The full FYS Media folder is already in `media/`.
- Links: Maps listing and review link are `MAPS` and `REVIEW` in `build.py`. The dashboard URL (business.google.com/n/540640849903216367) is private; never put it on the site.
- Still to do at cutover: custom domain in Pages settings, DNS at the registrar (README has the records), enforce HTTPS, unpublish the Google Site, strip unchosen variants.
