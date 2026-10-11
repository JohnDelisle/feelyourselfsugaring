# Feel Yourself Sugaring — site notes

Static website for Feel Yourself Sugaring, a home-based sugaring business in Winnipeg run by Pamela Delisle. Moved off Google Sites (www.feelyourselfsugaring.com) to GitHub Pages at https://github.com/JohnDelisle/feelyourselfsugaring. John (the user) maintains it; Pamela reviews and gives feedback through him.

## Layout

- `docs/` is the published site, served by GitHub Pages from `main` + `/docs`. Everything in it except `images/`, `favicon.png`, `apple-touch-icon.png`, `styles.css`, `script.js` and `.nojekyll` is generated.
- `build.py` at the root generates `docs/`. `media/` holds working materials. `README.md` and this file stay at the root.
- All of `media/` is committed, about 400 MB, on purpose: John wants the artifacts kept together in case the Google Drive copy is lost one day. The source was the business Google Drive, account john@feelyourselfsugaring.com, folder `FYS Media`. Don't add a gitignore for it.

## Rules

- Plain HTML/CSS/JS. No framework, no build step on GitHub. Keep it that way.
- `build.py` is the source of truth for page content and the shared header/footer. Make content changes in `build.py`, then run `python build.py` (on Windows; `python3 build.py` elsewhere). Don't hand-edit the generated `.html` files, or the next build will overwrite them.
- `build.py` writes UTF-8 with LF line endings on every platform. `.gitattributes` enforces LF in the repo. Keep both, or the en-dashes and curly quotes garble against the pages' declared UTF-8 charset.
- `docs/styles.css` holds all styling. Colours and fonts are CSS variables at the top, with the alternate themes right below them.
- Page filenames match the old Google Sites URLs (`/our-sugarist`, `/book-now`, etc.). Don't rename them. `home.html` and `why-us.html` are redirects for old links. `prices.html` and `new-clients.html` are new pages added in October 2026.
- Booking happens by text (204-557-5197) plus an embedded Google Form for the client profile.
- Photos go in `docs/images/` (`pamela.jpg`, `studio-1.jpg`, `studio-2.jpg`, `studio-3.jpg`). Missing photos show labelled placeholders. All four were cropped from the old Google Sites pages on 2026-10-10; full-resolution originals are in `media/photos/`. `logo.png` (hearts, on black), `logo-hips.png` (the second logo: a hips silhouette with "FYS") and `sugaring-hero.jpg` (old home banner) are also there but unused by the pages so far.
- Brand: two logos (hearts and hips), both by Pamela, in `media/brand/`. Brand colours from the old site's CSS: near-black #1C1C1C, blush #FACBD0, hot pink #F385AA, white; teal #1A9DA8 appears in the old banners. The favicon is Pamela's hearts mark.

## Review variants and themes (October 2026, temporary)

Pamela is choosing between options. John's own pick (2026-10-11): noir theme, prices on the home page. Until Pamela decides, the repo carries:

- **Colour themes** in `docs/styles.css`, selected by `html[data-theme]`: `pine` (default: forest green, honey, blush), `brand` (old Google Sites palette), `teal`, `noir` (dark). Open any page with `?theme=name`, or use the switcher. The honey-blob header mark shows in `pine`; the two-hearts mark shows in the other themes.
- **Hero art options** on the home page, selected by `html[data-hero]`: `blob` (default, the animated honey blob), `hearts` (hearts logo), `hips` (hips logo), `pamela` (Pamela sugaring a leg), `sugar` (a ball of paste in her hand), `legs` (legs on the zebra rug), `studio` (treatment table), `none` (text only). All candidates are in the HTML with `loading="lazy"`, so only the chosen one downloads. Pamela didn't love the blob, hence the options.
- **Extra inner-page photos** (`.photo.extra` on new-clients, why-sugar and wellness-tipping), hidden by `html[data-photos="fewer"]`.
- **A preview switcher** at the bottom of `docs/script.js` with rows for theme, hero, photos and layout, plus a "copy share link" that encodes the current choices as `?theme=…&hero=…&photos=…`. It appears only on github.io, localhost, or with `?preview` in the URL, so it vanishes once the custom domain is live. It remembers the theme in localStorage and links to the same page in the other structural variant.
- **Structural variant** `docs/variants/prices-page/`: a full second build where the price list is off the home page and only on `prices.html`. The main build keeps prices on the home page (`/#prices`) and also has `prices.html`. Variant pages are `noindex` and canonical to the main site. To retire a variant, delete its folder and its `build()` line at the bottom of `build.py`.

To make choices permanent: set `data-theme`, `data-hero` and `data-photos` on the `<html>` tag in `build.py`'s page template (or fold the chosen theme's variables into `:root`), delete the other theme blocks and unused hero candidates, drop unused images from `docs/images/`, and remove the switcher block from `script.js` and the `.preview` CSS.

## Audience and purpose

Most clients find Pamela through Google Maps while searching for sugaring or hair removal, then visit the site or text, and fill out the new-client form. Pamela wants the site to educate new clients and set expectations, hers and theirs. `new-clients.html` ("New here?") carries that in Pamela's fuller voice; the other pages stay tight.

## Hosting

- GitHub Pages, deploy from `main`, folder `/docs`, live at https://johndelisle.github.io/feelyourselfsugaring/. `docs/.nojekyll` is present so Pages serves the files as-is.
- Custom domain not set up yet. The github.io URL is being checked first.
- `docs/404.html` uses root-relative links (`/`, `/styles.css`), so it only looks right once the site is served from a domain root, not from the `/feelyourselfsugaring/` project path.
- Pushing: the gh CLI on John's machine has two accounts; see the memory note. Plain `git push` works once Git Credential Manager has a stored login.

## Open questions for Pamela

- Which theme and which prices layout to keep, and whether to use the hips logo anywhere.
- Cancellation, lateness and payment policies, parking and entry instructions, and age policy for tweens: none of these are on the old site, so the new-client page doesn't state them.
- The step-by-step description of what happens during an appointment on `new-clients.html` is written from standard sugaring practice and should be checked against what Pamela actually does.
- The Google Business Profile / Maps link, for a "leave a review" link and schema.
- The 2024 pricing spreadsheet in Drive lists services the site doesn't (hydrojelly mask add-on, skin treatments, PCOS facial, five-session packages, first-visit aftercare gift). Are any still offered?
