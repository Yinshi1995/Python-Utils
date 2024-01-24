# My Personal Utils

This repository contains a collection of python utility scripts and tools that I've developed for my own needs. Feel free to explore and use them if they fit your requirements.

## Proxy Manager

The Proxy Manager is a utility for managing and rotating proxy configurations. It allows you to load proxy information from a TOML file, and provides methods to retrieve random or sequentially rotated credentials and proxy details.

### Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Use it for fetching
    ```python
    import ProxyManager

    file_path = 'credentials_and_proxies.toml'

    proxy_manager = ProxyManager(file_path)

    credentials_and_proxy = proxy_manager.get_random_credentials_and_proxy()
    print(f"Using proxy {random.choice(credentials_and_proxy['proxies'])} with credentials {credentials_and_proxy['username']}:{credentials_and_proxy['password']} for the first request.")

    for _ in range(5):
        credentials_and_proxy = proxy_manager.get_next_credentials_and_proxy()
        print(f"Using proxy {random.choice(credentials_and_proxy['proxies'])} with credentials {credentials_and_proxy['username']}:{credentials_and_proxy['password']} for the next request.")
    ```
    > Replace print with fetch url with needed params


## Make Executable

The `make_executable.py` script is a utility to make a Python script executable on Windows by modifying file permissions. It uses the `subprocess` module to run the `icacls` command, granting read (R) and execute (X) permissions to everyone.

### Usage

1. Open a terminal.

2. Run the script by providing the path to the Python script you want to make executable:
   ```bash
   python make_executable.py your_script.py
   ```
