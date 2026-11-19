
# Network Diagnostics Tool

A Python-based command-line tool for performing basic network diagnostics, testing host connectivity, and checking DNS resolution.

## Features

- Ping an IP address or domain name
- Send four ICMP Echo Requests
- Display ping results and response times
- Calculate approximate average response time
- Check DNS resolution
- Perform basic internet connectivity checks
- Interactive menu for selecting operations

## Technologies Used

- Python 3
- subprocess module
- socket module
- re module
- Windows Ping utility

## How to Run

1. Install Python 3.
2. Clone the repository.
3. Open a terminal in the project folder.
4. Run:

    python network_diagnostics.py

5. Choose an option from the menu.

## Menu Options

1. Ping a host
2. Check DNS
3. Check internet connectivity
4. Exit

## How It Works

The tool uses Python's subprocess module to execute Windows ping commands and capture their output. It extracts response times using regular expressions and calculates an approximate average.

It also uses Python's socket module to resolve domain names into IPv4 addresses.

## Learning Outcomes

- ICMP and network connectivity testing
- DNS resolution
- Python subprocess and socket modules
- Regular expressions
- Functions and loops
- Basic network troubleshooting

## Limitations

- Designed for Windows.
- Ping may fail when ICMP traffic is blocked.
- The internet connectivity check is not a complete test of internet access.
- Average response time is approximate.
- DNS lookup returns one IPv4 address.

## Future Improvements

- Packet-loss reporting
- More reliable ping result detection
- Cross-platform support
- Network diagnostic reports
