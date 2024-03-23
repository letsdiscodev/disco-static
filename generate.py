import os

print("Generating site")

REPO_PATH = os.environ.get("DISCO_REPO_PATH")
DIST_DIR = os.environ.get("DISCO_DIST_PATH")
COMMIT = os.environ.get("DISCO_COMMIT")

assert REPO_PATH is not None
assert DIST_DIR is not None
assert COMMIT is not None

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
