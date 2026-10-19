# Feel Yourself Sugaring — site notes

Static website for Feel Yourself Sugaring, a home-based sugaring business in Winnipeg run by Pamela Delisle. Moved off Google Sites (www.feelyourselfsugaring.com) to GitHub Pages at https://github.com/JohnDelisle/feelyourselfsugaring. John (the user) maintains it; Pamela reviews and gives feedback through him.

**Start each session by reading `HANDOFF.md`.** It holds current status, decisions, open questions and the to-do list, and is updated at the end of each session.

## Layout

- `docs/` is the published site, served by GitHub Pages from `main` + `/docs`. Everything in it except `images/`, `favicon.ico`, `favicon-48/96/192.png`, `apple-touch-icon.png`, `styles.css`, `script.js` and `.nojekyll` is generated, including `sitemap.xml` and `robots.txt`.
- `build.py` at the root generates `docs/`. `media/` holds working materials. `README.md` and this file stay at the root.
- All of `media/` is committed, about 400 MB, on purpose: John wants the artifacts kept together in case the Google Drive copy is lost one day. The source was the business Google Drive, account john@feelyourselfsugaring.com, folder `FYS Media`. Don't add a gitignore for it.

## Rules

- Plain HTML/CSS/JS. No framework, no build step on GitHub. Keep it that way.
- `build.py` is the source of truth for page content and the shared header/footer. Make content changes in `build.py`, then run `python build.py` (on Windows; `python3 build.py` elsewhere). Don't hand-edit the generated `.html` files, or the next build will overwrite them.
- `build.py` writes UTF-8 with LF line endings on every platform. `.gitattributes` enforces LF in the repo. Keep both, or the en-dashes and curly quotes garble against the pages' declared UTF-8 charset.
- `docs/styles.css` holds all styling. Colours and fonts are CSS variables at the top. The variable names (`--pine`, `--honey`) are left over from the first palette; they now hold the noir pinks.
- Page filenames match the old Google Sites URLs (`/our-sugarist`, `/book-now`, etc.). Don't rename them. `home.html` and `why-us.html` are redirects for old links. `prices.html` and `new-clients.html` are new pages added in October 2026.
- Booking happens by text (204-557-5197) plus an embedded Google Form for the client profile.
- Google: the public Maps listing is `MAPS` in `build.py` (CID link; 5.0 stars, 89 reviews as of 2026-10-11; category "Hair removal service") and the write-a-review short link is `REVIEW` (from the Business Profile's "Ask for reviews" dialog). John's Business Profile dashboard is https://business.google.com/n/540640849903216367/profile (signed-in only; never link to it).
- Photos go in `docs/images/`, and only images the pages use live there. Missing photos show labelled placeholders. `pamela.jpg` and `studio-1/2/3.jpg` were cropped from the old Google Sites pages on 2026-10-10; full-resolution originals are in `media/photos/`. Logos are in `media/brand/`. Unused hero candidates and logo copies were removed from `docs/images/` on 2026-10-19 and are in git history. Published photos are sized to about twice their largest display size and saved at JPEG quality 82 with metadata stripped; resize new ones the same way. `share.jpg` (1200x630) is the social share image for every page.
- Search and sharing: `og:image`, `sitemap.xml` and `robots.txt` all use the www domain (`SITE`), so they only work once the domain points at GitHub Pages.
- Analytics: Cloudflare Web Analytics (cookieless, no banner needed), set up 2026-10-19 by John. `CF_BEACON` in `build.py` holds the site token; empty means no analytics script. The current token belongs to a Cloudflare site registered as `johndelisle.github.io`, and Cloudflare only counts visits from hostnames ending in the registered name. At cutover, add a site for `feelyourselfsugaring.com` (covers www) and swap in its token.
- Brand: two logos (hearts and hips), both by Pamela, in `media/brand/`. Brand colours from the old site's CSS: near-black #1C1C1C, blush #FACBD0, hot pink #F385AA, white; teal #1A9DA8 appears in the old banners. The favicon is Pamela's hearts mark.

## Design (chosen by Pamela, 2026-10-19)

In October 2026 the site carried switchable themes, hero art, photo sets and a second layout build so Pamela could compare. She picked the following, and the alternatives and the preview switcher were removed (they're in git history before 2026-10-19 if ever needed):

- **Noir theme**: pink on near-black with a blush band, folded into `:root` in `styles.css`. The header mark is the two hearts.
- **Home hero**: the photo of Pamela sugaring a leg (`images/hero-pamela.jpg`).
- **Photos on inner pages**: new-clients, why-sugar and wellness-tipping each have a photo.
- **Prices on their own page**: the home page has a short summary with a "See all prices" button; the full list is only on `prices.html`, and the nav's Prices link goes there.

## Audience and purpose

Most clients find Pamela through Google Maps while searching for sugaring or hair removal, then visit the site or text, and fill out the new-client form. Pamela wants the site to educate new clients and set expectations, hers and theirs. `new-clients.html` ("New here?") carries that in Pamela's fuller voice; the other pages stay tight.

## Hosting

- GitHub Pages, deploy from `main`, folder `/docs`, live at https://johndelisle.github.io/feelyourselfsugaring/. `docs/.nojekyll` is present so Pages serves the files as-is.
- Custom domain not set up yet. The github.io URL is being checked first.
- `docs/404.html` uses root-relative links (`/`, `/styles.css`), so it only looks right once the site is served from a domain root, not from the `/feelyourselfsugaring/` project path.
- Pushing: the gh CLI on John's machine has two accounts; see the memory note. Plain `git push` works once Git Credential Manager has a stored login.

## Open questions for Pamela

- Whether to use the hips logo anywhere.
- Cancellation, lateness and payment policies, parking and entry instructions, and age policy for tweens: none of these are on the old site, so the new-client page doesn't state them.
- The step-by-step description of what happens during an appointment on `new-clients.html` is written from standard sugaring practice and should be checked against what Pamela actually does.
- The 2024 pricing spreadsheet in Drive lists services the site doesn't (hydrojelly mask add-on, skin treatments, PCOS facial, five-session packages, first-visit aftercare gift). Are any still offered?
