
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def plot_attack_graphs(ips, creds, commands, times):
    try:
        # Convert lists to pandas Series safely
        ips_series = pd.Series(ips) if len(ips) > 0 else pd.Series(dtype='str')
        creds_series = pd.Series([f"{u}:{p}" for u, p in creds]) if len(creds) > 0 else pd.Series(dtype='str')
        commands_series = pd.Series(commands) if len(commands) > 0 else pd.Series(dtype='str')
        times_series = pd.to_datetime(pd.Series(times)) if len(times) > 0 else pd.Series(dtype='datetime64[ns]')

        # Top 10 Attacker IPs
        if not ips_series.empty:
            ip_counts = ips_series.value_counts().head(10)
            ip_counts.plot(kind="bar", title="Top 10 Attacker IPs", color='skyblue')
            plt.xlabel("IP Address")
            plt.ylabel("Attempts")
            plt.tight_layout()
            plt.savefig("top_ips.png")
            plt.close()

        # Top 10 Failed Credentials
        if not creds_series.empty:
            cred_counts = creds_series.value_counts().head(10)
            cred_counts.plot(kind="bar", title="Top 10 Failed Credentials", color='salmon')
            plt.xlabel("Username:Password")
            plt.ylabel("Attempts")
            plt.tight_layout()
            plt.savefig("top_credentials.png")
            plt.close()

        # Top 10 Commands
        if not commands_series.empty:
            cmd_counts = commands_series.value_counts().head(10)
            cmd_counts.plot(kind="bar", title="Top 10 Commands", color='lightgreen')
            plt.xlabel("Command")
            plt.ylabel("Count")
            plt.tight_layout()
            plt.savefig("top_commands.png")
            plt.close()

        # Attack Frequency by Hour
        if not times_series.empty:
            hour_counts = times_series.dt.hour.value_counts().sort_index()
            hour_counts.plot(kind="bar", title="Attack Frequency by Hour", color='orange')
            plt.xlabel("Hour of Day")
            plt.ylabel("Number of Attacks")
            plt.tight_layout()
            plt.savefig("attack_by_hour.png")
            plt.close()

        print("[INFO] Graphs saved: top_ips.png, top_credentials.png, top_commands.png, attack_by_hour.png")

    except Exception as e:
        print("[WARNING] Failed to plot graphs:", e)
