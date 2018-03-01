import urllib.request

URL_IP = 'http://httpbin.org/ip'


def use_simple_urlib():
    response = urllib.request.urlopen(URL_IP)
    print(response.info())

    print(''.join([str(line) for line in response.readlines()]))


if __name__ == '__main__':
    use_simple_urlib()
