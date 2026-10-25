# guruprasadah.me

A small static blog: Markdown posts are rendered by `generate.py` into full HTML
pages, and htmx swaps the `#content` region so in-site navigation still feels
like a single-page app.

## Writing a post

Add a Markdown file to `posts/`. Frontmatter is required:

```yaml
---
published: 20260816
title: Optional title, defaults to the filename
slug: optional-url-slug
description: Optional meta description
---
```

The URL for a post is `/posts/<slug>/`. If `slug` is omitted, it is generated
from the title (or filename). Slugs must be lowercase letters, numbers, and
single hyphens.

`index.html` and `posts/<slug>/index.html` are generated; edit
`src/layout.html` for shared page structure and `generate.py` for rendering
logic.

## Building

```sh
uv sync
npm install
npm run build
```

`npm run generate` only regenerates HTML. `npm run build` also rebuilds the
Tailwind stylesheet.
