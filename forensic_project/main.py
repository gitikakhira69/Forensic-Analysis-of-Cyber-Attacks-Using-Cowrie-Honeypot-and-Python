import os
from log_parser import parse_cowrie_logs
from geoip_map import generate_geo_map
from report_generator import create_pdf_report
from ml_anomaly import detect_anomalous_ips, detect_anomalous_commands
from real_time_monitor import start_monitor
from graphs import plot_attack_graphs

# -----------------------
# CONFIGURATION
# -----------------------
LOG_PATH = "../cowrie/var/log/cowrie/cowrie.json"
LOG_DIR = os.path.dirname(LOG_PATH)

print(f"[INFO] Checking if log file exists at: {LOG_PATH}")
if not os.path.exists(LOG_PATH):
    print("[ERROR] Cowrie log file not found. Please check LOG_PATH.")
    exit(1)
else:
    print("[INFO] Log file found.")

# -----------------------
# MAIN ANALYSIS FUNCTION
# -----------------------
def analyze_logs():
    try:
        print("[INFO] Parsing Cowrie logs...")
        ips, creds, commands, times = parse_cowrie_logs(LOG_PATH)
        print(f"[INFO] Top Attacker IPs: {ips[:10]}")
        print(f"[INFO] Top Failed Credentials: {creds[:10]}")
        print(f"[INFO] Top Commands: {commands[:10]}")

        # Plot attack graphs
        plot_attack_graphs(ips, creds, commands, times)

        # Generate GeoIP map
        print("[INFO] Generating GeoIP map...")
        generate_geo_map(set(ips))
        print("[INFO] Map saved as attack_map.html")

        # Generate PDF report
        print("[INFO] Generating PDF report...")
        create_pdf_report(ips, creds, commands)
        print("[INFO] PDF report saved as forensic_report.pdf")

        # ML-based anomaly detection
        print("[INFO] Detecting anomalous IPs...")
        anomalous_ips = detect_anomalous_ips(ips)
        if anomalous_ips is not None and not anomalous_ips.empty:
            print(anomalous_ips)

        print("[INFO] Detecting anomalous commands...")
        anomalous_cmds = detect_anomalous_commands(commands)
        if anomalous_cmds is not None and not anomalous_cmds.empty:
            print(anomalous_cmds)

    except Exception as e:
        print("[ERROR] Failed during analysis:", e)


# -----------------------
# ENTRY POINT
# -----------------------
if __name__ == "__main__":
    # Run initial analysis
    analyze_logs()

    # Start real-time monitoring
    if not os.path.exists(LOG_DIR):
        print(f"[ERROR] Log directory for monitoring not found: {LOG_DIR}")
    else:
        print("[INFO] Starting real-time log monitoring...")
        try:
            start_monitor(LOG_DIR, analyze_logs)
        except Exception as e:
            print("[ERROR] Real-time monitoring failed:", e)
