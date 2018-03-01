import requests

URL_IP = 'http://httpbin.org/ip'

URL_GET = 'http://httpbin.org/get'


def use_simple_requests():
    response = requests.get(URL_IP)
    print('>>>>>Response Headers:')
    print(response.headers)
    print('>>>>>Response Status:')
    print(response.status_code)
    print('>>>>>Response content:')
    print(response.text)


def use_get_requests():
    params = {'param1': 'hello', 'param2': 'world'}
    response = requests.get(URL_GET, params=params)
    print('>>>>>Response Headers:')
    print(response.headers)
    print('>>>>>Response Status:')
    print(response.status_code)
    print(response.reason)
    print('>>>>>Response content:')
    print(response.text)
    print(response.json())


if __name__ == '__main__':
    # use_simple_requests()
    use_get_requests()