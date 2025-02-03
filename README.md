# SyncPress

SyncPress is a Python program that analyzes disk usage and reports on space consumption by different files and folders in a specified directory on Windows. This tool helps users understand how their disk space is being used, allowing for better disk management and cleanup.

## Features

- Recursively calculates the total size of files within directories.
- Reports the size of both files and folders in a human-readable format (MB).
- Handles errors gracefully, such as missing files or incorrect paths.

## Requirements

- Python 3.x
- Windows Operating System

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/syncpress.git
   ```
2. Navigate to the directory:
   ```bash
   cd syncpress
   ```

## Usage

To analyze disk usage, run the program from the command line:

```bash
python syncpress.py [directory_path]
```

- If no directory path is provided, the current directory will be analyzed.
- The program outputs a table showing the name and size (in MB) of each file and folder within the specified directory.

Example:

```bash
python syncpress.py C:\Users\YourUsername\Documents
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.

## Issues

If you encounter any issues, please report them in the [issue tracker](https://github.com/yourusername/syncpress/issues).

## Acknowledgements

- This project was inspired by the need for simple disk space analysis tools on Windows.