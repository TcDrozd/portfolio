## Quick Start

```bash
# Clone the repo
git clone https://github.com/yourname/portfolio.git
cd portfolio

# Local dev (simple HTTP server)
make serve
# → visit http://localhost:8080
```

## Customize

1. Edit `data/projects.json` to add/update projects.
2. Update links and contact info in `index.html`.
3. Add `public/resume.pdf` (optional).
4. Tweak styling in `styles.css`.

## Projects JSON Shape (canonical)

Each project must conform to this schema (empty strings are OK):

```json
{
  "title": "",
  "description": "",
  "highlights": [],
  "tech": [],
  "impact": "",
  "links": {
    "repo": "",
    "demo": "",
    "loom": ""
  }
}
```

## Deployment

This is a static site. You can host it anywhere that serves files.

### Option A — Static hosting (recommended)
- GitHub Pages
- Cloudflare Pages
- Any CDN / object storage static hosting

### Option B — Self-host
Serve the repository root (or the built artifact) with your web server of choice.

Important: ensure `data/projects.json` is served as a static file (no SPA rewrite rules should intercept `/data/*`).

License

MIT — Use, modify, and deploy freely.
