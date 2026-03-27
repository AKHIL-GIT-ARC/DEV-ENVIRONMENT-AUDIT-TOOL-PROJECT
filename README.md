<div align="center">

# 🛠️ Dev Audit Tool

**Know your machine. Fix your setup. Ship faster.**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-a855f7?style=flat-square)](CONTRIBUTING.md)
[![Made with Rich](https://img.shields.io/badge/Made%20with-Rich-orange?style=flat-square)](https://github.com/Textualize/rich)

</div>

---

## ❯ What is this?

Ever set up a new machine and spent hours figuring out what's missing?  
Ever onboarded a teammate who couldn't run the project because of a missing tool?

**Dev Audit** fixes that. One command. Instant answer.
```bash
python audit.py
```

It scans your machine, checks every dev tool you care about, and gives you a clean colored report — what's installed, what's missing, and exactly how to fix it for your OS.

---

## ❯ Demo
```
╭──────────────────────────────────────────────╮
│          Dev Environment Audit Tool          │
│   Checks your machine for developer tools    │
╰──────────────────────────────────────────────╯

  Detected OS: linux

  Audit Summary
  7 installed   2 missing   0 errors   out of 10 tools

  Version Control
  ─────────────────────────────────────────────
  git    ✔ Installed    git version 2.43.0
  gh     ✘ Missing      Fix: sudo apt install gh

  Language
  ─────────────────────────────────────────────
  python ✔ Installed    Python 3.12.0
  node   ✔ Installed    v20.11.0
```

---

## ❯ Features

- ✅ Detects 10+ common dev tools out of the box
- ✅ Shows exact version of every installed tool
- ✅ Per-OS fix commands — Linux / Mac / Windows
- ✅ Groups tools by category for clean output
- ✅ Runs in under 3 seconds
- ✅ Zero config needed to get started
- ✅ Fully customizable via `tools.json`

---

## ❯ Getting Started

**1 — Clone the repo**
```bash
git clone https://github.com/AKHIL-GIT-ARC/dev-audit-tool.git
cd dev-audit-tool
```

**2 — Create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate        # Mac / Linux
venv\Scripts\activate           # Windows
```

**3 — Install dependencies**
```bash
pip install -r requirements.txt
```

**4 — Run it**
```bash
python audit.py
```

No API keys. No accounts. No config required.

---

## ❯ Project Structure
```
dev-audit-tool/
│
├── audit.py            ← main script (run this)
├── tools.json          ← add / remove tools here
├── requirements.txt    ← just one dependency: rich
├── .gitignore
└── README.md
```

---

## ❯ Customize It

Want to add or remove tools? Open `tools.json` and add a block like this:
```json
{
  "name": "rust",
  "version_cmd": "rustc --version",
  "category": "language",
  "fix": {
    "linux": "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
    "mac": "brew install rust",
    "windows": "https://rustup.rs"
  }
}
```

Save the file, run `python audit.py` again. Done.

---

## ❯ Tools Checked by Default

| Tool | Category | Why it matters |
|------|----------|----------------|
| `git` | Version Control | You can't dev without it |
| `gh` | Version Control | GitHub from the terminal |
| `python` | Language | Runs this very script |
| `node` | Language | JS runtime |
| `npm` | Package Manager | Node packages |
| `pip` | Package Manager | Python packages |
| `docker` | Container | Containerized environments |
| `curl` | Networking | API calls, downloads |
| `wget` | Networking | File downloads |
| `make` | Build Tool | Build automation |

---

## ❯ Contributing

The easiest way to contribute? **Add a tool to `tools.json`.**
```
1. Fork this repo
2. Add your tool to tools.json
3. Test it: python audit.py
4. Open a pull request
```

All skill levels welcome — if you've never made a PR before, this is a great first one.

---

## ❯ Roadmap

- [x] Core audit engine
- [x] Per-OS fix suggestions
- [x] Category grouping
- [ ] `--json` flag for piping output
- [ ] `--fix` flag to auto-install missing tools
- [ ] Config profiles — frontend / backend / devops
- [ ] GitHub Action to audit CI environments

---

## ❯ License

MIT — do whatever you want with it.  
Built by [AKHIL](https://github.com/AKHIL-GIT-ARC)

---

<div align="center">
<sub>If this saved you time, drop a ⭐ — it helps more people find it.</sub>
</div>
