# SSH/FTP Brute-forcer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/language-python-blue)

A multithreaded brute-force tool for SSH and FTP protocols. Designed for CTF challenges, security research, and authorized penetration testing.

## Features

- Support for both SSH (via pxssh) and FTP (via ftplib)
- Configurable multithreading using ThreadPoolExecutor
- Progress bar with tqdm
- Customizable connection timeout and thread delay
- Clean success output with credential details
- Proper error handling and input validation

## Security Disclaimer
This tool is intended for authorized security testing, CTF exercises, and legitimate system administration purposes only.  
Unauthorized use against systems without explicit permission is illegal and may violate applicable laws  
(including the Computer Fraud and Abuse Act in the US or equivalent legislation in other jurisdictions).  
The author bears no responsibility for any misuse or damage caused by this tool.

## Installation

```bash
git clone https://github.com/VeirHannon/ssh-ftp-brute.git
cd ssh-ftp-brute
pip install -r requirements.txt
python3 ssh_ftp_brute.py
```

## Requirements

Python 3.8+
pexpect
tqdm

## Usage
``` Bash  
python ssh_ftp_brute.py <mode> <host> <username> <wordlist> [OPTIONS]
```

## Options

| **Argument** | **Short** | **Description**                         | **Default** |
| :------ | :-----------: | :----------------------: | -------------: |
| mode         | \-        | Attack mode \(ssh or ftp\)              | \-          |
| host         | \-        | Target host IP or hostname              | \-          |
| username     | \-        | Username to brute\-force                | \-          |
| wordlist     | \-        | Path to password wordlist               | \-          |
| \-\-threads  | \-t       | Number of concurrent threads            | 10          |
| \-\-timeout  | \-T       | Connection timeout in seconds           | 8           |
| \-\-delay    | \-        | Delay between thread starts \(seconds\) | 0\.1        |


## Examples:
```Bash
SSH brute force
python ssh_ftp_brute.py ssh 192.168.1.100 admin passwords.txt -t 20

FTP brute force
python ssh_ftp_brute.py ftp 10.10.10.50 user rockyou.txt --threads 15 --delay 0.05

SSH with increased timeout
python ssh_ftp_brute.py ssh target.local root wordlist.txt -T 12
```
