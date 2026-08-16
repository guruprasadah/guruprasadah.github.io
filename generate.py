import os

from markdown_it import MarkdownIt
from markupsafe import escape
import frontmatter

from pathlib import Path

md = MarkdownIt("gfm-like")
default_fence = md.renderer.fence # type: ignore

def render_fence(self, tokens, idx, options, env):
    token = tokens[idx]

    if token.info.strip() == "mermaid":
        return f'<div class="not-prose"><div class="mermaid">{escape(token.content)}</div></div>\n'

    return default_fence(tokens, idx, options, env)

md.add_render_rule("fence", render_fence)

def render_document(text):
    post = frontmatter.loads(text)

    html = md.render(post.content)

    return {
        "metadata": post.metadata,
        "html": html,
    }

directory = Path('./posts')

public_posts = Path("./public/posts")
public_posts.mkdir(parents=True, exist_ok=True)

posts = {}

for file in directory.iterdir():
    if file.is_file() and file.suffix == ".md":
        with open(file, "r") as f:
            doc = render_document(f.read())
            post_name = file.name.removesuffix(".md")
            post_path = f"public/posts/{post_name}.html"
            posts[post_name] = (post_path, doc["metadata"]["published"])
            with open(f"public/posts/{post_name}.html", "w") as p:
                p.write(f"""
    <div id='content' class='w-full pt-5 flex flex-col items-center'>
        <div class='w-full flex justify-end px-2'>
            <a class='text-blue-600' hx-get='/public/posts.html' hx-target='#content' hx-swap='outerHTML'>&crarr; home</a>
        </div>
        <div class='prose'>
            <h1>{file.name.removesuffix(".md")}</h1>
            <span>Published {doc["metadata"]["published"]}</span>
            <div>{doc["html"]}</div>
        </div>
    </div>""")

sorted_posts = sorted([(key, value[0], value[1]) for key, value in posts.items()], key=lambda x: x[2])

post_list = "".join([f"<span class='flex justify-between w-full'><a hx-get='{x[1]}' hx-target='#content' hx-swap='outerHTML' class='text-blue-600'>{x[0]}</a> <span>{x[2]}</span></span>" for x in sorted_posts])
with open("./public/posts.html", "w") as f:
    f.write(f"<div id='content' class='px-2 w-full'>{post_list}</div>")