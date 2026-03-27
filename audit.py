import json
import platform
import shutil
import subprocess
import sys
from collections import defaultdict

from rich.console import Console
from rich.table import Table
from rich import box
from rich.text import Text
from rich.panel import Panel

console = Console()

# ── Section 1: Config Loader ──────────────────────────────────────────────────

def load_tools(path="tools.json"):
    try:
        with open(path) as f:
            return json.load(f)["tools"]
    except FileNotFoundError:
        console.print(f"[red]Error:[/red] Could not find '{path}'.")
        sys.exit(1)
    except json.JSONDecodeError:
        console.print(f"[red]Error:[/red] '{path}' is not valid JSON.")
        sys.exit(1)

# ── Section 2: OS Detection ───────────────────────────────────────────────────

def get_os():
    system = platform.system().lower()
    if system == "darwin":
        return "mac"
    elif system == "windows":
        return "windows"
    else:
        return "linux"

def get_fix(tool, os_key):
    return tool["fix"].get(os_key, "Check the project README")

# ── Section 3: Tool Checker ───────────────────────────────────────────────────

def check_tool(tool):
    name = tool["name"]
    cmd = tool["version_cmd"].split()

    if shutil.which(name) is None:
        return {"status": "missing", "version": None}

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=5
        )
        output = result.stdout.strip() or result.stderr.strip()
        version = output.split("\n")[0] if output else "installed"
        return {"status": "ok", "version": version}
    except subprocess.TimeoutExpired:
        return {"status": "error", "version": "timed out"}
    except Exception as e:
        return {"status": "error", "version": f"error: {e}"}

# ── Section 4: Run All Checks ─────────────────────────────────────────────────

def run_audit(tools):
    results = {}
    with console.status("[bold cyan]Scanning your environment...[/bold cyan]"):
        for tool in tools:
            results[tool["name"]] = {
                **check_tool(tool),
                "category": tool["category"],
                "fix": tool["fix"]
            }
    return results

# ── Section 5: Report Printer ─────────────────────────────────────────────────

def print_report(results, os_key):
    by_category = defaultdict(list)
    for name, data in results.items():
        by_category[data["category"]].append((name, data))

    installed = sum(1 for d in results.values() if d["status"] == "ok")
    missing   = sum(1 for d in results.values() if d["status"] == "missing")
    errors    = sum(1 for d in results.values() if d["status"] == "error")
    total     = len(results)

    summary = (
        f"[green]{installed} installed[/green]  "
        f"[red]{missing} missing[/red]  "
        f"[yellow]{errors} errors[/yellow]  "
        f"[dim]out of {total} tools[/dim]"
    )
    console.print(Panel(summary, title="[bold]Audit Summary[/bold]", expand=False))
    console.print()

    for category, items in sorted(by_category.items()):
        table = Table(
            title=f"[bold]{category.title()}[/bold]",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold dim",
            expand=False,
            min_width=60
        )
        table.add_column("Tool",           style="bold", width=12)
        table.add_column("Status",         width=12)
        table.add_column("Version / Fix",  overflow="fold")

        for name, data in items:
            if data["status"] == "ok":
                status = Text("Installed", style="green")
                detail = Text(data["version"], style="dim")
            elif data["status"] == "missing":
                status = Text("Missing", style="red")
                fix    = data["fix"].get(os_key, "See README")
                detail = Text(f"Fix: {fix}", style="yellow")
            else:
                status = Text("Error", style="yellow")
                detail = Text(data["version"], style="dim")

            table.add_row(name, status, detail)

        console.print(table)
        console.print()

# ── Section 6: Main Entry Point ───────────────────────────────────────────────

def main():
    console.print(Panel.fit(
        "[bold cyan]Dev Environment Audit Tool[/bold cyan]\n"
        "[dim]Checks your machine for common developer tools[/dim]",
    ))
    console.print()

    os_key = get_os()
    console.print(f"[dim]Detected OS: {os_key}[/dim]\n")

    tools   = load_tools("tools.json")
    results = run_audit(tools)
    print_report(results, os_key)

if __name__ == "__main__":
    main()