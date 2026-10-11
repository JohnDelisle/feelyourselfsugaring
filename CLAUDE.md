# Feel Yourself Sugaring — site notes

Static website for Feel Yourself Sugaring, a home-based sugaring business in Winnipeg run by Pamela Delisle. Moved off Google Sites (www.feelyourselfsugaring.com) to GitHub Pages at https://github.com/JohnDelisle/feelyourselfsugaring. John (the user) maintains it; Pamela reviews and gives feedback through him.

## Rules

- Plain HTML/CSS/JS. No framework, no build step on GitHub. Keep it that way.
- `build.py` is the source of truth for page content and the shared header/footer. Make content changes in `build.py`, then run `python build.py` (on Windows; `python3 build.py` elsewhere). Don't hand-edit the generated `.html` files, or the next build will overwrite them.
- `build.py` writes UTF-8 with LF line endings on every platform. Keep it that way, or the en-dashes and curly quotes garble against the pages' declared UTF-8 charset.
- `styles.css` holds all styling. Colours and fonts are CSS variables at the top, with the alternate themes right below them.
- Page filenames match the old Google Sites URLs (`/our-sugarist`, `/book-now`, etc.). Don't rename them. `home.html` and `why-us.html` are redirects for old links. `prices.html` and `new-clients.html` are new pages added in October 2026.
- Booking happens by text (204-557-5197) plus an embedded Google Form for the client profile.
- Photos go in `images/` (`pamela.jpg`, `studio-1.jpg`, `studio-2.jpg`, `studio-3.jpg`). Missing photos show labelled placeholders. All four were pulled from the old Google Sites pages on 2026-10-10. `logo.png` (the two-hearts brand mark) and `sugaring-hero.jpg` (old home banner) are also there but unused so far.

## Review variants and themes (October 2026, temporary)

Pamela is choosing between options. Until she decides, the repo carries:

- **Colour themes** in `styles.css`, selected by `html[data-theme]`: `pine` (default: forest green, honey, blush), `brand` (the old Google Sites palette: near-black #1C1C1C, blush #FACBD0, hot pink #F385AA, white), `teal` (the teal #1A9DA8 from the old site's banners, pink accents), `noir` (dark, pink on near-black, like the logo). Open any page with `?theme=name`, or use the switcher. The honey-blob header mark shows in `pine`; the two-hearts mark shows in the other themes.
- **A preview switcher** at the bottom of `script.js`. It appears only on github.io, localhost, or with `?preview` in the URL, so it vanishes once the custom domain is live. It remembers the theme in localStorage and links to the same page in the other structural variant.
- **Structural variant** `variants/prices-page/`: a full second build where the price list is off the home page and only on `prices.html`. The root build keeps prices on the home page (`/#prices`) and also has `prices.html`. Variant pages are `noindex` and canonical to the root. To retire a variant, delete its folder and its `build()` line at the bottom of `build.py`.

To make a theme permanent: set `data-theme="name"` on the `<html>` tag in `build.py`'s page template (or copy that theme's variables into `:root`), delete the other theme blocks, and remove the switcher block from `script.js` and the `.preview` CSS.

## Audience and purpose

Most clients find Pamela through Google Maps while searching for sugaring or hair removal, then visit the site or text, and fill out the new-client form. Pamela wants the site to educate new clients and set expectations, hers and theirs. `new-clients.html` ("New here?") carries that in Pamela's fuller voice; the other pages stay tight.

## Hosting

- GitHub Pages, deploy from `main`, root folder, live at https://johndelisle.github.io/feelyourselfsugaring/. `.nojekyll` is present so Pages serves the files as-is.
- Custom domain not set up yet. The github.io URL is being checked first.
- `404.html` uses root-relative links (`/`, `/styles.css`), so it only looks right once the site is served from a domain root, not from the `/feelyourselfsugaring/` project path.

## Open questions for Pamela

- Which theme and which prices layout to keep.
- Cancellation, lateness and payment policies, parking and entry instructions, and age policy for tweens: none of these are on the old site, so the new-client page doesn't state them.
- The step-by-step description of what happens during an appointment on `new-clients.html` is written from standard sugaring practice and should be checked against what Pamela actually does.
- The Google Business Profile / Maps link, for a "leave a review" link and schema.
