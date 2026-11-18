#!/usr/bin/env python3
"""Capture viewport JPEG thumbs for every study HTML file."""
from __future__ import annotations

import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
THUMBS = ROOT / "thumbs"
WIDTH, HEIGHT = 1280, 800


def main() -> None:
    wanted = {Path(a).name for a in sys.argv[1:]} if len(sys.argv) > 1 else None
    files = sorted(ROOT.glob("[0-9][0-9][0-9]-*.html"))
    if wanted:
        files = [p for p in files if p.name in wanted]
    THUMBS.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
            viewport={"width": WIDTH, "height": HEIGHT},
            device_scale_factor=1,
        )
        for i, html_path in enumerate(files, 1):
            dest = THUMBS / f"{html_path.stem}.jpg"
            url = html_path.resolve().as_uri()
            try:
                page.goto(url, wait_until="load", timeout=15000)
                page.wait_for_timeout(700)
                page.screenshot(path=str(dest), type="jpeg", quality=82, full_page=False)
                print(f"[{i:03}/{len(files)}] {dest.name}  {dest.stat().st_size // 1024}k")
            except Exception as exc:
                print(f"[{i:03}/{len(files)}] FAIL {html_path.name}: {exc}")
        browser.close()


if __name__ == "__main__":
    main()
