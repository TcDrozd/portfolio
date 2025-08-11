Backend/Automation Portfolio — Starter Kit & Deploy Guide

A clean, fast-loading, and maintainable portfolio template for backend & automation engineers.

Features
	•	Static + Simple — No frameworks required; HTML + TailwindCSS.
	•	Data-Driven Projects — Projects loaded from a single data/projects.json file.
	•	Tag Filtering — Quick client-side filter by tech tags.
	•	Ready to Deploy Anywhere — GitHub Pages, Cloudflare Pages, or self-host via Docker.
	•	Dark Theme — Minimal and modern design.

Quick Start

# Clone the repo
git clone https://github.com/yourname/portfolio.git
cd portfolio

# Local dev (simple HTTP server)
make serve
# → visit http://localhost:8080

# Or self-host with Docker (Nginx)
docker compose up -d
# → visit http://<host-ip>:8080

Customize
	1.	Edit data/projects.json with your projects.
	2.	Update links and contact info in index.html.
	3.	Add your resume.pdf to public/.
	4.	(Optional) tweak styling in styles.css.

Deployment Options
	•	GitHub Pages — Free, zero-maintenance.
	•	Cloudflare Pages — Free, CDN, TLS.
	•	Oracle VM / VPS — Use provided Nginx or Caddy Docker config.

License

MIT — Use, modify, and deploy freely.