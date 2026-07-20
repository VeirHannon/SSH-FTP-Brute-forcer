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
If you're defending infrastructure and found this while researching the attack side, the mitigations that neutralize this whole class  
of tool are: key-based auth instead of passwords, fail2ban / rate limiting, account lockout, and not exposing SSH/FTP to the public internet unnecessarily.  

## Installation

```bash
git clone https://github.com/VeirHannon/SSH-FTP-Brute-forcer.git
cd SSH-FTP-Brute-forcer
pip install -r requirements.txt
python3 ssh_ftp_brute.py
```

## Requirements

- Python 3.8+
- pexpect
- tqdm

## Usage, Examples and Options  
Intended for authorized lab targets only. See --help for options.
