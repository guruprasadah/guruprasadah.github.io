# guruprasadah.me

A small static blog: Markdown posts are rendered by `generate.py` into full HTML
pages, and htmx swaps the `#content` region so in-site navigation still feels
like a single-page app.

## Writing a post

Each post is a directory in `posts/` named after its URL slug. The post itself
is `index.md` in that directory:

```text
posts/
└── my-post/
    ├── index.md
    └── images/
        └── diagram.png
```

Frontmatter is required:

```yaml
---
published: 20260816
title: My post
description: Optional meta description
---
```

The URL for a post is `/posts/<slug>/`, where `<slug>` is the directory name.
Slugs must be lowercase letters, numbers, and single hyphens. `title` defaults
to the slug if omitted. A `slug` field is allowed only if it matches the
directory name.

Set `wip: true` in the frontmatter to keep a post in the repository without
publishing it. Work-in-progress posts are left out of the home page, and any
previously generated page for them is removed on the next build.

`index.html` and `posts/<slug>/index.html` are generated; edit
`src/layout.html` for shared page structure and `generate.py` for rendering
logic.

## Images and other post assets

Keep assets in the post's directory, preferably under `images/`, and reference
them with a path relative to `index.md`:

```markdown
![A diagram](images/diagram.png)
```

The generator checks that local images exist and stay inside the post
directory. Root-absolute paths (`/images/...`) and paths that escape the
directory (`../...`) are rejected. Use a full `https://` URL for externally
hosted images.

Because the generated `index.html` lives beside `index.md`, the same relative
paths work in the browser, when previewing the Markdown, and when the site is
opened directly from disk.

`index.html` can be opened from the filesystem for a quick look. htmx needs
HTTP, so on `file://` URLs the generated pages automatically fall back to
normal full-page navigation. Run a local server when testing htmx navigation.

## Building

```sh
uv sync
npm install
npm run build
```

`npm run generate` only regenerates HTML. `npm run build` also rebuilds the
Tailwind stylesheet.
