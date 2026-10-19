# Feel Yourself Sugaring

Static website for Feel Yourself Sugaring, hosted on GitHub Pages. Plain HTML, CSS and a little JavaScript. No framework, no build step on GitHub.

## Layout

- `docs/`: the published site. GitHub Pages serves this folder from the `main` branch. Don't hand-edit the HTML in here; it's generated.
  - `index.html`, `new-clients.html`, `prices.html`, `our-sugarist.html`, `our-studio.html`, `why-sugar.html`, `wellness-tipping.html`, `advice.html`, `book-now.html`: the pages
  - `styles.css`: all styling. Colours and fonts are CSS variables at the top.
  - `script.js`: mobile menu toggle
  - `images/`: photos and logos used by the pages
  - `favicon.png`, `apple-touch-icon.png`: Pamela's hearts favicon
  - `home.html`, `why-us.html`: redirects so old Google Sites links keep working
  - `404.html`: page-not-found page
- `build.py`: generates everything in `docs/` from one script, so the shared header and footer stay in sync. Run `python build.py` after any content change.
- `media/`: working materials, copied from the `FYS Media` folder in the business Google Drive.
  - `brand/`: logos and favicons (committed)
  - `photos/`: original phone photos from the studio shoots
  - `old-site/`: banners from the old Google Sites pages
  - `instagram/`: Instagram's official glyph pack
  All of it is committed on purpose, as a backup of the Drive folder.

Old URLs like `/our-sugarist` and `/book-now` work unchanged, because GitHub Pages serves `our-sugarist.html` at `/our-sugarist`.

## Publish on GitHub Pages

In the repo, go to **Settings → Pages**. Under "Build and deployment", choose **Deploy from a branch**, then `main` and `/docs`. The site is live at `https://johndelisle.github.io/feelyourselfsugaring/` a minute or two after each push.

## Move the domain over (cutover)

Do this only when the GitHub version looks right.

1. In **Settings → Pages → Custom domain**, enter `www.feelyourselfsugaring.com` and save. GitHub adds a `CNAME` file to `docs/`; commit it.
2. At the domain registrar, update DNS:
   - `www` → CNAME record pointing to `johndelisle.github.io`
   - The bare domain `feelyourselfsugaring.com` → four A records: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - Remove the old records that point to Google Sites.
3. Back in **Settings → Pages**, tick **Enforce HTTPS** once the certificate is issued.
4. Unpublish the Google Site.
