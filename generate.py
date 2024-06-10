import os
import markdown2

print("Generating site")

DIST_DIR = "dist" # /code/dist
PAGES_DIR = "pages"

if not os.path.isdir(DIST_DIR):
    os.makedirs(DIST_DIR)

def generate_html_file(md_filename: str) ->  None:
    with open(f"{PAGES_DIR}/{md_filename}", encoding="utf-8") as f:
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

for filename in os.listdir(PAGES_DIR):
    print(f"Generating {filename}")
    generate_html_file(filename)

print("Done generating site")
