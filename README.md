# Anatomy of a Method — Research Portfolio

A static website with separate Research, Publications, Software, Blog, Contact, and About pages. Only the selected page's content is displayed. Every page shares the illustrated header and navigation. No build step or installation is needed.

## Files

- `index.html`: Research homepage
- `publications.html`: searchable publications and author/preprint filters
- `software.html`: software and resources
- `blog.html`: blog page (no posts published yet)
- `contact.html`: contact information and profile links
- `about.html`: biography, professional background, expandable research experience, skills, education, talks, and service
- `anatomy-method-header.webp`: required illustrated banner

## Preview

Extract the ZIP and double-click `index.html`. Keep all files in the same directory. Links between pages also work locally.

## Publish on GitHub Pages

1. Create a public repository called `smk5g5.github.io` under the `smk5g5` account. If it already exists, use the existing repository without deleting unrelated content.
2. Upload ALL extracted files at the repository root, including the six HTML pages and image. Upload files, not the ZIP or its containing folder.
3. Commit to `main`.
4. Go to Settings → Pages. Choose Deploy from a branch, main, and /(root). Save.
5. Wait for the deployment to complete. The user website will be available at https://smk5g5.github.io/.

If you use a different repository name, such as `portfolio`, the project website will instead be https://smk5g5.github.io/portfolio/. Relative links support both locations.



## Edit

Each HTML file contains its own embedded CSS; edit corresponding pages for content changes. Publication data is in the `publications` JavaScript array in `publications.html`.  The About page is transcribed from the supplied LaTeX. The header image comes from the supplied illustrated header HTML.

## Publication list

The Publications page contains 17 journal papers, 3 preprints for which no full journal version was identified, and 3 book chapters/conference papers. It is rendered directly in HTML, with browser-side search and category/first-author filters. `publications-data.json` retains bibliographic data and source links for editing/reference; the page does not fetch it at runtime. Edit both files when changing entries.

The list was expanded from the supplied CV using publisher/Crossref, PubMed, and author/lab records. Google Scholar blocked direct retrieval on October 28, 2026, so this is not certified as an exhaustive export of that profile. Conference abstracts, datasets, and duplicate preprint versions of published articles are not included in the journal-paper count. The earlier m6A preprint is represented by its 2026 Cancers publication. The TREM2 paper is dated 2023 (the journal record), rather than 2024 in the supplied CV.

The CV download option has been removed; the PDF is not included in this website package. The Research introductory sentence requested for removal is absent.
