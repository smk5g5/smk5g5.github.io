# Publish at https://smk5g5.github.io/

## Recommended repository arrangement

- PRIVATE `smk5g5/website`: upload the CONTENTS of `quarto-source/` here, including `.github/` and `.gitignore`.
- PUBLIC `smk5g5/smk5g5.github.io`: upload only the CONTENTS of `public-site/` here.

In the public repository, choose Settings → Pages → Deploy from a branch → main → /(root) → Save. No custom domain is necessary. Allow deployment to finish before checking the website.

Do not place `quarto-source/` inside the public repository. Its drafts and source history belong in the private repository.

## Easiest first publication

1. Extract the delivery ZIP.
2. Open `public-site/` on your computer.
3. Upload everything INSIDE it to the root of `smk5g5.github.io`, including `assets/`, `posts/`, `site_libs/`, CSS, generated HTML, XML, and `.nojekyll`.
4. Replace old generated files. Remove the obsolete `Saad-Khan-CV.pdf` and the former root `anatomy-method-header.webp` from the old HTML version if they still exist; the current banner is in `assets/`. Keep any unrelated files you intentionally maintain separately.
5. Enable Pages as above.

You can publish future updates manually by running `quarto render` in your private source checkout and uploading the CONTENTS of `_site/`. Avoid leaving withdrawn posts in the public repository.

## Optional: publish from the private source repository automatically

A manual GitHub Actions workflow is included at `.github/workflows/publish-public.yml`. It builds public output and pushes ONLY those generated files to `smk5g5/smk5g5.github.io`. It does not deploy draft previews.

One-time authorization is required. Create a repository-specific SSH deploy key locally:

```sh
ssh-keygen -t ed25519 -C "quarto-website-publisher" -f ~/.ssh/quarto-pages-deploy
```

For this automated key, leave the passphrase empty. Keep the private key out of Git and do not paste it into a chat.

1. In PUBLIC `smk5g5.github.io` → Settings → Deploy keys → Add deploy key, paste the contents of `~/.ssh/quarto-pages-deploy.pub` and enable Allow write access. This public key grants access only to the target repository.
2. In PRIVATE `website` → Settings → Secrets and variables → Actions → New repository secret, set name `PAGES_DEPLOY_KEY` and value to the complete contents of `~/.ssh/quarto-pages-deploy` (the private key).
3. Ensure the public repository already exists with a `main` branch and GitHub Pages configured for main/root.
4. In PRIVATE `website`, open Actions → Publish generated site to smk5g5.github.io → Run workflow.
5. Watch that workflow complete, then check the public repository's Pages deployment.

The publisher replaces the dedicated public repository's working files with fresh generated output, removing obsolete pages. It preserves an existing CNAME file. Keep unrelated projects out of this dedicated website repository. The workflow uses GitHub's HTTPS metadata endpoint to obtain GitHub SSH host keys and verifies the SSH server against those keys.

To publish on every source push later, add a `push: {branches: [main]}` trigger alongside `workflow_dispatch`; only do this if every push to main should publish approved content. Default publication is manual.

## Alternative: one public source repository

If you do not need private drafts, put the source project in `smk5g5.github.io`. Use `_examples/pages-single-repo.yml` as `.github/workflows/pages.yml`, remove `publish-public.yml`, and set Settings → Pages → Source → GitHub Actions. All source and draft text in that public repository will be public, even when Quarto omits the rendered draft.

## Cloudflare review previews

Cloudflare Access has not been configured by this package. A protected preview requires an account, a private source connection, and an email allowlist. Use the `preview` profile only after access protection is enabled and verified; never upload its output to GitHub Pages. Do not merge private draft content into a public source repository.
