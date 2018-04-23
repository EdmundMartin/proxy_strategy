# proxy_strategy

## Round Robin Proxy
```python
from proxy_strategy import RoundRobinProxy

proxies = ['143.104.238.70:80', '35.196.89.215:80', '35.196.143.234:80', '47.206.51.67:8080']
r = RoundRobinProxy(proxies)
proxy = r()
```

## RandomProxy
```python
from proxy_strategy import RandomProxy

proxies = ['143.104.238.70:80', '35.196.89.215:80', '35.196.143.234:80', '47.206.51.67:8080']
r = RandomProxy(proxies)
proxy = r()
```

## To-Do
* Add more complicated strategies
* Add comprehensive type hinting
* Package for PyPi
* Add better documentation
