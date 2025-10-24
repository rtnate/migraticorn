# src/migraticorn/cli.py
import sys

def main():
    print("🦄  Migraticorn — A Majestic Static Site Deployment Tool")
    if len(sys.argv) < 2:
        print("Usage: migraticorn [deploy|status|rollback]")
        sys.exit(0)

    cmd = sys.argv[1]
    if cmd == "deploy":
        print("Deploying static site…")
    elif cmd == "status":
        print("Checking migration status…")
    elif cmd == "rollback":
        print("Rolling back to previous release…")
    else:
        print(f"Unknown command: {cmd}")
