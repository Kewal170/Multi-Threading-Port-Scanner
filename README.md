---

# Port Scanner

A multi-threaded port scanner that detects open TCP ports on a specified IP address. This script uses Python's `socket` library for network communication, `threading` for concurrent scanning, and `colorama` for colorful console output. Results are logged in a file for later review.

## Features

- **Multi-threaded Scanning**: Efficiently scans a range of ports using multiple threads.
- **Colorful Output**: Uses `colorama` to color-code console output for better readability.
- **Logging**: Logs open ports and their associated services to a file (`scan_results.log`).
- **Configurable**: Easily adjustable parameters for IP address, port range, number of threads, and verbosity.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/port-scanner.git
   cd port-scanner
   ```

2. **Install dependencies:**

   Ensure you have Python installed, then install the required Python packages:

   ```bash
   pip install colorama
   ```

## Usage

1. **Edit Configuration:**

   Open the script and set the `IP_ADDRESS` and `PORT_RANGE` variables as needed:

   ```python
   IP_ADDRESS = '192.168.137.1'
   PORT_RANGE = range(1, 1001)  # Adjust port range as necessary
   ```

2. **Run the Script:**

   Execute the script using Python:

   ```bash
   python port_scanner.py
   ```

   - The script will display a banner with the IP address being scanned.
   - Only open ports will be shown in the console output.
   - Results are saved in `scan_results.log`.

## Example

```bash
$ python port_scanner.py
```

**Console Output:**

```
----------------------------------------------------------------------------------------------------
[*] Scanning 192.168.137.1
----------------------------------------------------------------------------------------------------
[+] Port 22 :: ssh
[+] Port 80 :: http
----------------------------------------------------------------------------------------------------
Finished scanning
Results are saved in 'scan_results.log'
```

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements. Please ensure your contributions align with the project's coding standards and include tests where appropriate.

## Acknowledgments

- **Python Documentation**: For the extensive library support.
- **Colorama**: For providing a way to add color to console output.

---

Feel free to adjust the URLs, details, or instructions based on your specific project setup and preferences.
