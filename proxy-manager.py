import random
import toml

class ProxyManager:
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.credentials_and_proxies = toml.load(file)['credentials_and_proxies']
        self.current_credentials_index = None

    def get_random_credentials_and_proxy(self):
        credentials = random.choice(self.credentials_and_proxies)
        return credentials

    def get_next_credentials_and_proxy(self):
        if self.current_credentials_index is None:
            self.current_credentials_index = random.randint(0, len(self.credentials_and_proxies) - 1)
        else:
            self.current_credentials_index = (self.current_credentials_index + 1) % len(self.credentials_and_proxies)

        return self.credentials_and_proxies[self.current_credentials_index]
