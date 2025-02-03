import os
import sys

def get_size(start_path='.'):
    """Recursively calculates the total size of files in a given directory."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                total_size += os.path.getsize(file_path)
            except FileNotFoundError:
                # Skip files that are not found
                continue
    return total_size

def analyze_disk_usage(path='.'):
    """Analyzes disk usage and reports on space consumption by files and folders."""
    if not os.path.exists(path):
        print(f"Error: The path '{path}' does not exist.")
        return

    if not os.path.isdir(path):
        print(f"Error: The path '{path}' is not a directory.")
        return

    print(f"Analyzing disk usage for: {path}")
    print(f"{'Name':<40} {'Size (MB)':>10}")
    print("="*50)

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            size = get_size(item_path) / (1024 * 1024)  # Convert size to MB
            print(f"{item:<40} {size:>10.2f}")
        elif os.path.isfile(item_path):
            size = os.path.getsize(item_path) / (1024 * 1024)  # Convert size to MB
            print(f"{item:<40} {size:>10.2f}")

if __name__ == "__main__":
    dir_to_analyze = sys.argv[1] if len(sys.argv) > 1 else '.'
    analyze_disk_usage(dir_to_analyze)