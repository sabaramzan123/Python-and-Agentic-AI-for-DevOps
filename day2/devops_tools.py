from pathlib import Path
import subprocess
from collections import Counter


def read_log_file(path):
    """
    Read and return the complete content of a log file.
    """
    return Path(path).read_text(encoding="utf-8")


def count_log_levels(text):
    """
    Dynamically count all log levels found in the log file.

    The function does not use a predefined list of log levels.
    It extracts the log level from the third field of each log line.

    Example:
    2025-01-10 09:00:01 INFO Application started

    Here:
        tokens[0] = 2025-01-10
        tokens[1] = 09:00:01
        tokens[2] = INFO

    It also handles levels written as **ERROR**.
    """

    counter = Counter()

    for line in text.splitlines():

        # Ignore empty lines
        if not line.strip():
            continue

        tokens = line.split()

        # Make sure the line contains date, time and level
        if len(tokens) >= 3:

            # Extract the log level
            level = tokens[2].strip("*").upper()

            # Count the discovered level
            counter[level] += 1

    return dict(counter)


def show_docker_containers():
    """
    Show all Docker containers on the host machine.
    """
    return subprocess.run(
        ["docker", "ps", "-a"],
        capture_output=True,
        text=True
    )


if __name__ == "__main__":

    path = Path(r"C:\Python-for-DevOps\day2\app.log")

    text = read_log_file(path)

    print(count_log_levels(text))