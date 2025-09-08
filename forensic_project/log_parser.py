import json
import pandas as pd
from collections import Counter
import datetime

def parse_cowrie_logs(file_path):
    with open(file_path) as f:
        logs = [json.loads(line) for line in f if line.strip()]

    # Extract IPs, credentials, commands
    ips = [log["src_ip"] for log in logs if "src_ip" in log]
    creds = [(log.get("username"), log.get("password")) for log in logs if log.get("eventid") == "cowrie.login.failed"]
    commands = [log.get("input") for log in logs if log.get("eventid") == "cowrie.command.input"]

    # Extract timestamps
    times = []
    for log in logs:
        if "timestamp" in log:
            ts = log["timestamp"].replace("Z", "")
            try:
                times.append(datetime.datetime.fromisoformat(ts))
            except:
                pass

    df_times = pd.Series(times)
    return ips, creds, commands, df_times
