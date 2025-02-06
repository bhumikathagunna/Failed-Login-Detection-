import re
from collections import defaultdict

# Define the log file path
LOG_FILE = "auth.log"

# Threshold for failed attempts (can be customized)
FAILED_ATTEMPT_THRESHOLD = 5

def parse_log():
    failed_login_attempts = defaultdict(int)
    
    # Regular expression to match failed login attempts and extract the IP
    login_failure_pattern = re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)")

    try:
        with open(LOG_FILE, "r") as file:
            for line in file:
                match = login_failure_pattern.search(line)
                if match:
                    ip_address = match.group(1)
                    failed_login_attempts[ip_address] += 1
    except FileNotFoundError:
        print(f"Log file '{LOG_FILE}' not found.")
        return None

    return failed_login_attempts

def check_brute_force(failed_login_attempts):
    for ip, count in failed_login_attempts.items():
        if count >= FAILED_ATTEMPT_THRESHOLD:
            print(f"[ALERT] Potential brute-force attack detected from IP: {ip} with {count} failed attempts")

def main():
    failed_login_attempts = parse_log()
    if failed_login_attempts:
        check_brute_force(failed_login_attempts)
    else:
        print("No failed login attempts found or log file is empty.")

if __name__ == "__main__":
    main()
