# GPT-6.2 Astra 100 HTML Files

A collection of **100 self-contained HTML visual studies** generated with **GPT-6.2 Astra** — still-life instruments, paper objects, quiet interfaces and animated scenes. Every piece is a single HTML file with all CSS and JS inline (no external fonts, images or libraries), and ships with its original generation prompt and a rendered screenshot.

**Browse the gallery:** https://miaai-lab.github.io/GPT-6.2-Astra-100-HTML-Files/

## Structure

```
├── index.html            ← gallery index (screenshot + description + prompt per study)
├── thumbs/               ← rendered screenshots (001–100, web-optimized JPEG)
├── NNN-*.html            ← the 100 standalone studies
├── NNN-*.txt             ← original prompt, description, techniques and interaction notes
├── generate_index.py     ← regenerates index.html from the studies + thumbs
└── shot_playwright.py    ← regenerates thumbs/ (headless Chromium captures)
```

## Gallery features

- One card per study: screenshot, number, title, description
- **Open** — loads the piece in a new tab
- **Prompt** — expands to the full original generation prompt and its prompt file
- Search across numbers, titles, descriptions and prompt text, with a live result count

## Rebuilding

```bash
python3 shot_playwright.py
python3 generate_index.py
```

Part of MiaAI Lab's LLM front-end capability evaluations: same prompt-style briefs, different model, same 100-slot budget.
