# Simple Python Port Scanner

A sequential port scanner written in Python to discover open ports on a target host.

---
## Features

* **Scans IP addresses or hostnames.**
* Accepts a **custom port range** (1-1024) or a list of specific ports (80,443,8080).
* **Service Detection**: Identifies common services running on open ports (e.g., HTTP, SSH).

---
## Usage

You must run the script from your command line. The `host` argument is required.

**Basic Scan (default ports 1-1024)**
```bash
python port_scanner.py scanme.nmap.org