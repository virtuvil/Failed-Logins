import sys
import re
from collections import defaultdict

# Regular expression patterns to match events of interest
failed_login_pattern = r'Failed login attempt.*?from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
# Add more patterns for other events if needed

def analyze_log(log_file_path):
    # Dictionary to store events and their counts
    events = defaultdict(int)

    # Read the log file
    with open(log_file_path, 'r') as file:
        log_data = file.read()

    # Find failed login attempts
    failed_login_matches = re.findall(failed_login_pattern, log_data, re.DOTALL)
    for ip_address in failed_login_matches:
        events[f"Failed login from {ip_address}"] += 1

    # Add more event processing logic for other patterns

    # Print the report
    print("Log Analysis Report:")
    for event, count in events.items():
        print(f"{event}: {count} occurrences")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_analysis.py <log_file_path>")
        sys.exit(1)

    log_file_path = sys.argv[1]
    analyze_log(log_file_path)

