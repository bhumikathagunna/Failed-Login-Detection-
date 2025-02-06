Failed Login Detection Script

This Python script is designed to analyze a server's auth.log file and detect multiple failed login attempts from the same IP address. It's useful for identifying potential brute-force attacks or unauthorized login attempts.

Features

Detects failed login attempts: Analyzes the auth.log file to detect failed login attempts.
Identifies suspicious activity: Flags IP addresses that have exceeded the threshold for failed login attempts.
Customizable: You can modify the failed attempt threshold in the script.
Requirements

Python v - 3.8 or above
No external dependencies required (uses built-in libraries)
Setup

Clone the repository or download the script to your local machine.
git clone using - (https://github.com/bhumikathagunna/Failed-Login-Detection-.git)
Ensure that you have an auth.log file in the same directory as the script, or adjust the script to point to the correct log file location.
Usage

Save the Python script as detect_failed_logins.py.
Place your auth.log file in the same directory as the script, or change the file path in the script to your log file.
Run the script using the following command:
python3 detect_failed_logins.py
The script will parse the auth.log file and display the IP addresses that have exceeded the set threshold for failed login attempts.
Configuration

The script checks for failed login attempts and flags any IP that exceeds 5 failed login attempts (you can change this threshold).

To change the threshold for failed login attempts:

Open the detect_failed_logins.py file.
Modify the threshold variable in the script:
threshold = 5  # Set your desired threshold
Example

For a auth.log file that contains the following entries:

Feb  6 12:34:56 server sshd[1234]: Failed password for invalid user admin from 192.168.1.100 port 45678 ssh2
Feb  6 12:34:57 server sshd[1235]: Failed password for invalid user root from 192.168.1.101 port 45679 ssh2
Feb  6 12:34:58 server sshd[1236]: Failed password for invalid user guest from 192.168.1.102 port 45680 ssh2
Feb  6 12:34:59 server sshd[1237]: Failed password for invalid user admin from 192.168.1.100 port 45681 ssh2
Feb  6 12:35:00 server sshd[1238]: Failed password for invalid user root from 192.168.1.101 port 45682 ssh2
The script will output:

Suspicious IP address: 192.168.1.100 has 2 failed login attempts
Suspicious IP address: 192.168.1.101 has 2 failed login attempts
