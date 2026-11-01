# Log Analyzer

A simple Python script that analyzes an authentication log and detects
suspicious login activity.

## What it does
- Reads and analyzes login records from the auth.log file.
- Counts failed login attempts per IP address and per username
- Flags any IP or user that exceeds a threshold (default: 3 failed attempts)
- Raises an alert when an IP logs in successfully after exceeding the threshold
- Saves the suspicious entries to `conteo.txt`

## How to run
Requires Python 3 only.

    python analyzer.py

## About the sample data
`auth.log` is a fictional sample. It contains no real users, passwords or IPs.
The IP addresses belong to ranges reserved for documentation.

## Limitations
- The fixed threshold can cause false positives (e.g. many users behind one IP).
- Failed attempts are counted per user, regardless of the source IP.
- The script only reports; it does not block anything.
