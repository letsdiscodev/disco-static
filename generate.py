import os
import markdown2

print("Generating site")

DIST_DIR = "dist" # /code/dist
PAGES_PATH = "pages"

if not os.path.isdir(DIST_DIR):
    os.makedirs(DIST_DIR)

def generate_html_file(md_filename: str) ->  None:
    with open(f"{PAGES_PATH}/{md_filename}", encoding="utf-8") as f:
        md = f.read()
    html = f"""<!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    </head>
    <body>
    {markdown2.markdown(md)}
    </body>
    </html>"""
    html_filename = md_filename.replace(".md", ".html")
    with open(f"{DIST_DIR}/{html_filename}", "w", encoding="utf-8") as f:
        f.write(html)

generate_html_file("index.md")

print("Done generating site")
