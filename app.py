# app.py
import time
import logging
import random
import socket
import os

# Ensure log directory exists
log_dir = "/var/log/myapp"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, "app.log")

hostname = socket.gethostname()

# Configure logging: write to file + stdout
logging.basicConfig(
    level=logging.INFO,
    format=f"%(asctime)s - {hostname} - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

messages = [
    "User logged in",
    "File uploaded",
    "Payment processed",
    "Cache miss",
    "Connection error",
    "Job completed successfully"
]

if __name__ == "__main__":
    while True:
        msg = random.choice(messages)
        logging.info(msg)
        time.sleep(2)
