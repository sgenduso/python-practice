import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + 'jpg'
    urllib.request.urlretrieve(url, full_name)


download_web_image(http://lh3.googleusercontent.com/iSCcQ3KiaCPUHY0EFbS-qgovGcfuTJCLDe2WFWvl3fV-ijUOfwGHK88FjRTB5P6rZiNesbUP7wl-0lcj5TlWUw)
