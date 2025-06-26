import time
import subprocess
import sys

TRATE = 20  # Set the interval in minutes

print(f"[SCHEDULER] Running sollax.py every {TRATE} minutes. Press Ctrl+C to stop.")

while True:
    print("[SCHEDULER] Starting sollax.py...")
    result = subprocess.run([sys.executable, "sollax.py"])
    if result.returncode != 0:
        print(f"[SCHEDULER] sollax.py exited with code {result.returncode}")
    print(f"[SCHEDULER] Waiting {TRATE} minutes for next run...")
    time.sleep(TRATE * 60)
