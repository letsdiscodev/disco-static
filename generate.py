import os

print("Generating site")

REPO_PATH = os.environ.get("DISCO_REPO_PATH")
DIST_DIR = f"{REPO_PATH}/dist"
COMMIT = os.environ.get("DISCO_COMMIT")

HTML = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
    <h1>Hello!</h1>
    <p>This is the commit {COMMIT}
</body>
</html>"""

if not os.path.isdir(DIST_DIR):
    os.makedirs(DIST_DIR)

with open(f"{DIST_DIR}/index.html", "w", encoding="utf-8") as f:
    f.write(HTML)

print("Done generating site")
