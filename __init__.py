import random


class ProxySelectionException(Exception):
    pass


class RobinRoundProxy:

    def __init__(self, proxies: list, seed_int=42, https=True):
        random.seed(seed_int)
        self.proxies = random.shuffle(proxies)
        self.__index = 0
        self.__https = https

    def __call__(self):
        proxy = self.proxies[self.__index % len(self.proxies)]
        self.__index += 1
        if self.__https:
            return {'http': proxy, 'https': proxy}
        else:
            return {'http': proxy}


class RandomProxy:

    def __init__(self, proxies, seed_int=42, https=True):
        random.seed(seed_int)
        self.proxies = random.shuffle(proxies)
        self.__https = https

    def __call__(self):
        proxy = random.choice(self)
        if self.__https:
            return {'http': proxy, 'https': proxy}
        else:
            return {'http': proxy}


class RandomProxies:

    def __init__(self, proxies, number, seed_int=42, https=True):
        random.seed(seed_int)
        self.number = number
        self.proxies = random.shuffle(proxies)
        self.__https = https

    def __call__(self, *args, **kwargs):
        number = kwargs.get('number', self.number)
        proxies = random.choices(self.proxies, k=number)
        if self.__https:
            return [{'http': proxy, 'https': proxy} for proxy in proxies]
        else:
            return [{'http': proxy} for proxy in proxies]


class WeightedProxy:

    def __init__(self, proxies, weights, seed_int=42, https=True):
        random.seed(seed_int)
        if len(proxies) != len(weights):
            raise ProxySelectionException('Weights must be the same length as your provided proxies')
        self.proxies = proxies
        self.weights = weights
        self.__https = https

    def __call__(self, *args, **kwargs):
        proxy = random.choices(self.proxies, weights=self.weights)
        if self.__https:
            return {'http': proxy, 'https': proxy}
        else:
            return {'http': proxy}
