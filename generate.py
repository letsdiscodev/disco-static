import os

print("Generating site")

DIST_DIR = os.environ.get("DISCO_DIST_PATH")
COMMIT = os.environ.get("DISCO_COMMIT")

assert DIST_DIR is not None
assert COMMIT is not None

HTML = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
    <h1>Hello!</h1>
    <p>This is the commit {COMMIT}</p>
    <p>DIST_DIR: {DIST_DIR}</p>
</body>
</html>"""

if not os.path.isdir(DIST_DIR):
    os.makedirs(DIST_DIR)

with open(f"{DIST_DIR}/index.html", "w", encoding="utf-8") as f:
    f.write(HTML)

print("Done generating site")
