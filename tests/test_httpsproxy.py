from os import environ as env

import requests
import requests_httpsproxy


proxy = env['TEST_HTTPS_PROXY']

assert proxy.startswith('https')

proxies = {
    'http': proxy,
    'https': proxy,
}

def test_httpsproxy():
    proxies
    r = requests.get('https://httpbin.org/status/204', proxies=proxies)
    assert r.status_code == 204
