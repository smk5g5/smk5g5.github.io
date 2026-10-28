# Anatomy of a Method — Research Portfolio

A static website with separate Research, Publications, Software, Blog, Contact, and About pages. Only the selected page's content is displayed. Every page shares the illustrated header and navigation. No build step or installation is needed.

## Files

- `index.html`: Research homepage
- `publications.html`: searchable publications and author/preprint filters
- `software.html`: software and resources
- `blog.html`: blog page (no posts published yet)
- `contact.html`: contact information and profile links
- `about.html`: biography, HTML CV, expandable research experience, skills, education, talks, and service
- `anatomy-method-header.webp`: required illustrated banner
- `Saad-Khan-CV.pdf`: downloadable CV

## Preview

Extract the ZIP and double-click `index.html`. Keep all files in the same directory. Links between pages also work locally.

## Publish on GitHub Pages

1. Create a public repository called `smk5g5.github.io` under the `smk5g5` account. If it already exists, use the existing repository without deleting unrelated content.
2. Upload ALL extracted files at the repository root, including the six HTML pages, image, and PDF. Upload files, not the ZIP or its containing folder.
3. Commit to `main`.
4. Go to Settings → Pages. Choose Deploy from a branch, main, and /(root). Save.
5. Wait for the deployment to complete. The user website will be available at https://smk5g5.github.io/.

If you use a different repository name, such as `portfolio`, the project website will instead be https://smk5g5.github.io/portfolio/. Relative links support both locations.

The uploaded CV will be public; review its contact and reference details before publishing.

## Edit

Each HTML file contains its own embedded CSS; edit corresponding pages for content changes. Publication data is in the `publications` JavaScript array in `publications.html`. Replace the PDF using the same filename to update the downloadable CV. The About page is transcribed from the supplied LaTeX. The header image comes from the supplied illustrated header HTML.
