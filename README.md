# Feel Yourself Sugaring

Static website for Feel Yourself Sugaring, hosted on GitHub Pages. Plain HTML and CSS, no build step needed.

## Files

- `index.html`, `our-sugarist.html`, `our-studio.html`, `why-sugar.html`, `wellness-tipping.html`, `advice.html`, `book-now.html`: the pages
- `styles.css`: all styling. Colours and fonts are set at the top.
- `script.js`: mobile menu
- `home.html`, `why-us.html`: redirects so old Google Sites links keep working
- `404.html`: page-not-found page
- `build.py`: optional. Regenerates every page from one script, so the shared header and footer stay in sync. Run `python3 build.py`.

Old URLs like `/our-sugarist` and `/book-now` work unchanged, because GitHub Pages serves `our-sugarist.html` at `/our-sugarist`.

## Before going live

1. **Add photos** to `images/`. Until they're added, each photo slot shows a labelled placeholder.
   - `pamela.jpg`: portrait for the Our Sugarist page (portrait orientation, 4:5)
   - `studio-1.jpg`: main studio photo (large)
   - `studio-2.jpg`: plants and artwork
   - `studio-3.jpg`: aftercare products
   Keep each file under about 500 KB; resize to around 1600px wide.
2. **Fix the Instagram link.** Set `INSTAGRAM` in `build.py` to the real profile URL and run `python3 build.py`, or find and replace `https://www.instagram.com/` in the HTML files.

## Publish on GitHub Pages

1. Create a repo (for example `feelyourselfsugaring`) and push these files to the `main` branch.
2. In the repo, go to **Settings → Pages**. Under "Build and deployment", choose **Deploy from a branch**, then `main` and `/ (root)`.
3. After a minute, the site is live at `https://<your-username>.github.io/feelyourselfsugaring/`. Check every page there.

## Move the domain over (cutover)

Do this only when the GitHub version looks right.

1. In **Settings → Pages → Custom domain**, enter `www.feelyourselfsugaring.com` and save. GitHub adds a `CNAME` file to the repo.
2. At the domain registrar, update DNS:
   - `www` → CNAME record pointing to `<your-username>.github.io`
   - The bare domain `feelyourselfsugaring.com` → four A records: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - Remove the old records that point to Google Sites.
3. Once the certificate is issued (can take up to a day), tick **Enforce HTTPS**.
4. In Google Sites, remove the custom domain from the old site and unpublish it.
