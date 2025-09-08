import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CowrieHandler(FileSystemEventHandler):
    def __init__(self, analyze_callback):
        self.analyze_callback = analyze_callback

    def on_modified(self, event):
        if event.src_path.endswith("cowrie.json"):
            print("[INFO] New logs detected! Running analysis...")
            self.analyze_callback()

def start_monitor(log_dir, analyze_callback):
    observer = Observer()
    observer.schedule(CowrieHandler(analyze_callback), path=log_dir, recursive=False)
    observer.start()
    print("[INFO] Monitoring started... Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
