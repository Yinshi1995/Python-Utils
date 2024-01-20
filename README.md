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
    file_path = 'credentials_and_proxies.toml'

    proxy_manager = ProxyManager(file_path)

    credentials_and_proxy = proxy_manager.get_random_credentials_and_proxy()
    print(f"Using proxy {random.choice(credentials_and_proxy['proxies'])} with credentials {credentials_and_proxy['username']}:{credentials_and_proxy['password']} for the first request.")

    for _ in range(5):
        credentials_and_proxy = proxy_manager.get_next_credentials_and_proxy()
        print(f"Using proxy {random.choice(credentials_and_proxy['proxies'])} with credentials {credentials_and_proxy['username']}:{credentials_and_proxy['password']} for the next request.")
    ```
    > Replace print with fetch url with needed params
