import urllib.request
import urllib.error


# urllib.request.build_opener

def download(url):
     print('Downloading...' + url)
     headers = {'User-agent':'dsws'}
     try:
         if not url == '':
            req = urllib.request.Request(url, headers=headers)
            html = urllib.request.urlopen(req).read()
         else:
            html = None
     except urllib.error.HTTPError as e:
         print(e.reason)
         print(e.code)
         html = None
     except urllib.error.URLError as e:
         print(e.reason)
         html = None
     return html

if __name__ == '__main__':
    print(download(''))