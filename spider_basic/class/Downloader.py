class Downloader:
    def __init__(self, delay=5, user_agent='wswp',
                 proxies=None, num_retries=1, cache=None):
        self.user_agent = user_agent
        self.proxies = proxies
        self.num_retries = num_retries
        self.cache = cache

    def __call__(self, url):
        result = None
