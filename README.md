# SSH/FTP Brute-forcer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/language-python-blue)

A multithreaded brute-force tool for SSH and FTP protocols. Designed for CTF challenges, security research, and authorized penetration testing.

## Context and scope
This tool exists for one purpose: learning how online brute-force attacks work against services you own or are explicitly authorized to test.  
It was written and used exclusively in controlled, self-authorized environments — local vulnerable VMs and self-hosted CTF labs   
(VulnHub images and custom lab setups). It has never been pointed at third-party infrastructure.  
Online password guessing against systems you do not own or have explicit written permission to test is illegal in most jurisdictions
(e.g. the Computer Fraud and Abuse Act in the US, and equivalent laws elsewhere).
Do not use it anywhere you are not authorized. The author takes no responsibility for misuse.

## Mitigations

This class of attack is trivially defeated by standard hardening. If you're
defending infrastructure, any of the following will neutralize online
brute-forcing:

- **Key-based authentication** - disable password auth for SSH entirely; there's
  nothing to guess.
- **Rate limiting / fail2ban** - ban or throttle an IP after a few failed
  attempts, making exhaustive guessing impractical.
- **Account lockout** - temporarily lock an account after N failed logins.
- **Don't expose SSH/FTP publicly** - keep them behind a VPN or restricted to
  trusted networks when internet access isn't required.
- **Strong, unique passwords** - where password auth is unavoidable, length and
  randomness push brute-force time beyond feasibility.

## Installation

```bash
git clone https://github.com/VeirHannon/SSH-FTP-Brute-forcer.git
cd SSH-FTP-Brute-forcer
pip install -r requirements.txt
python3 ssh_ftp_brute.py
```

## Requirements

- **Python 3.8+**
- **pexpect**
- **tqdm**

## Usage, Examples and Options  
Intended for authorized lab targets only. See --help for options.  
``` python
# Against a local lab target
python3 ssh_ftp_brute.py --target 127.0.0.1 --service ssh --userlist users.txt --passlist pass.txt
```
