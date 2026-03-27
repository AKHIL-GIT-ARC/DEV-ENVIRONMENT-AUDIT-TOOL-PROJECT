<div align="center">
```ascii
██████╗ ███████╗██╗   ██╗      █████╗ ██╗   ██╗██████╗ ██╗████████╗
██╔══██╗██╔════╝██║   ██║     ██╔══██╗██║   ██║██╔══██╗██║╚══██╔══╝
██║  ██║█████╗  ██║   ██║     ███████║██║   ██║██║  ██║██║   ██║   
██║  ██║██╔══╝  ╚██╗ ██╔╝     ██╔══██║██║   ██║██║  ██║██║   ██║   
██████╔╝███████╗ ╚████╔╝      ██║  ██║╚██████╔╝██████╔╝██║   ██║   
╚═════╝ ╚══════╝  ╚═══╝       ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝   ╚═╝  
```

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
```
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

┌─────────────────────────────────────────────────────────────┐
│  Audit Summary                                              │
│  7 installed   2 missing   0 errors   out of 10 tools       │
└─────────────────────────────────────────────────────────────┘

╭─ Version Control ────────────────────────────────────────────╮
│ Tool     Status       Version / Fix                         │
│ ──────── ──────────── ──────────────────────────────────    │
│ git    ● Installed    git version 2.43.0                    │
│ gh     ✗ Missing      Fix: sudo apt install gh              │
╰─────────────────────────────────────────────────────────────╯

╭─ Language ───────────────────────────────────────────────────╮
│ Tool     Status       Version / Fix                         │
│ ──────── ──────────── ──────────────────────────────────    │
│ python ● Installed    Python 3.12.0                         │
│ node   ● Installed    v20.11.0                              │
╰─────────────────────────────────────────────────────────────╯
```

---

## ❯ Features
```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         │
  │   ● Detects 10+ common dev tools out of the box        │
  │   ● Shows exact version of every installed tool        │
  │   ● Per-OS fix commands  (Linux / Mac / Windows)       │
  │   ● Groups tools by category for clean output          │
  │   ● Runs in under 3 seconds                            │
  │   ● Zero config needed to get started                  │
  │   ● Fully customizable via tools.json                  │
  │                                                         │
  └─────────────────────────────────────────────────────────┘
```
