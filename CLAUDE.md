# Feel Yourself Sugaring — site notes

Static website for Feel Yourself Sugaring, a home-based sugaring business in Winnipeg run by Pamela Delisle. Moved off Google Sites (www.feelyourselfsugaring.com) to GitHub Pages at https://github.com/JohnDelisle/feelyourselfsugaring.

## Rules

- Plain HTML/CSS/JS. No framework, no build step on GitHub. Keep it that way.
- `build.py` is the source of truth for page content and the shared header/footer. Make content changes in `build.py`, then run `python build.py` (on Windows; `python3 build.py` elsewhere). Don't hand-edit the generated `.html` files, or the next build will overwrite them.
- `build.py` writes UTF-8 with LF line endings on every platform. Keep it that way, or the en-dashes and curly quotes garble against the pages' declared UTF-8 charset.
- `styles.css` holds all styling. Colours and fonts are CSS variables at the top.
- Page filenames match the old Google Sites URLs (`/our-sugarist`, `/book-now`, etc.). Don't rename them. `home.html` and `why-us.html` are redirects for old links.
- Booking happens by text (204-557-5197) plus an embedded Google Form for the client profile.
- Photos go in `images/` (`pamela.jpg`, `studio-1.jpg`, `studio-2.jpg`, `studio-3.jpg`). Missing photos show labelled placeholders. All four were pulled from the old Google Sites pages on 2026-10-10. `logo.png` (brand mark) and `sugaring-hero.jpg` (old home banner) are also there but unused so far.

## Hosting

- GitHub Pages, deploy from `main`, root folder. `.nojekyll` is present so Pages serves the files as-is.
- Custom domain not set up yet. The github.io URL is being checked first.
- `404.html` uses root-relative links (`/`, `/styles.css`), so it only looks right once the site is served from a domain root, not from the `/feelyourselfsugaring/` project path.

## Open to-dos

- Real Instagram URL (`INSTAGRAM` placeholder at the top of `build.py`).
