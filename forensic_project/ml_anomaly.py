import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalous_ips(ips):
    """
    Detects anomalous IP addresses using IsolationForest
    """
    if not ips:
        print("[INFO] No IP data to analyze.")
        return pd.DataFrame()

    # Count attempts per IP
    ip_counts = pd.Series(ips).value_counts().reset_index()
    ip_counts.columns = ["IP", "count"]

    try:
        # Train IsolationForest
        clf = IsolationForest(contamination=0.1, random_state=42)
        ip_counts["anomaly"] = clf.fit_predict(ip_counts[["count"]])

        anomalous_ips = ip_counts[ip_counts["anomaly"] == -1]

        if not anomalous_ips.empty:
            print("[INFO] Anomalous IPs Detected:")
            print(anomalous_ips)
        else:
            print("[INFO] No anomalous IPs detected.")

        return anomalous_ips
    except Exception as e:
        print("[WARNING] Failed to detect anomalous IPs:", e)
        return pd.DataFrame()


def detect_anomalous_commands(commands):
    """
    Detects anomalous commands using IsolationForest
    """
    if not commands:
        print("[INFO] No command data to analyze.")
        return pd.DataFrame()

    # Count command frequency
    cmd_counts = pd.Series(commands).value_counts().reset_index()
    cmd_counts.columns = ["Command", "count"]

    try:
        clf = IsolationForest(contamination=0.1, random_state=42)
        cmd_counts["anomaly"] = clf.fit_predict(cmd_counts[["count"]])

        anomalous_cmds = cmd_counts[cmd_counts["anomaly"] == -1]

        if not anomalous_cmds.empty:
            print("[INFO] Anomalous Commands Detected:")
            print(anomalous_cmds)
        else:
            print("[INFO] No anomalous commands detected.")

        return anomalous_cmds
    except Exception as e:
        print("[WARNING] Failed to detect anomalous commands:", e)
        return pd.DataFrame()
