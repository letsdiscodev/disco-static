import os
import randomname

print("Generating site")

DIST_DIR = "dist" # /code/dist

HTML = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
    <h1>Hello!</h1>
    <p>This is a random name for this deployment:</p>
    <p>{randomname.get_name()}</p>
</body>
</html>"""

if not os.path.isdir(DIST_DIR):
    os.makedirs(DIST_DIR)

with open(f"{DIST_DIR}/index.html", "w", encoding="utf-8") as f:
    f.write(HTML)

print("Done generating site")
