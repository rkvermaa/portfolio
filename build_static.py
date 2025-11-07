"""
Build static HTML version of the portfolio for GitHub Pages
"""
import os
from pathlib import Path
from main import app, rt

def build_static():
    """Generate static HTML files"""
    # Create build directory
    build_dir = Path("docs")
    build_dir.mkdir(exist_ok=True)

    # Copy static files
    import shutil
    if Path("static").exists():
        shutil.copytree("static", build_dir / "static", dirs_exist_ok=True)

    # Generate index.html
    from starlette.testclient import TestClient
    client = TestClient(app)

    response = client.get("/")

    with open(build_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    print(f"✅ Static site built in {build_dir}/")
    print(f"📄 Files: {list(build_dir.glob('*'))}")

if __name__ == "__main__":
    build_static()
