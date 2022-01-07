TOKEN = "1761635851:AAFkWG9yyhCoKtwpjuEwKth8Fp6QC_sQsvY"
REQUEST_KWARGS = {
    # t3 можно менять на t1 или t2
    'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'assert_hostname': 'False',
        'cert_reqs': 'CERT_NONE',
        'username': 'learn',
        'password': 'python'
    }
}
