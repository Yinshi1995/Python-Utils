import argparse
import subprocess

def make_executable(file_path):
    try:
        subprocess.run(["icacls", file_path, "/grant", "*S-1-1-0:(RX)"], check=True, capture_output=True)
        print(f"Added execute permission to {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error adding execute permission to {file_path}: {e.stderr.decode()}")

def main():
    parser = argparse.ArgumentParser(description="Make a Python script executable on Windows by modifying file permissions.")
    parser.add_argument("file_path", type=str, help="Path to the Python script you want to make executable")

    args = parser.parse_args()
    make_executable(args.file_path)

if __name__ == "__main__":
    main()
