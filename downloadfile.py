import os
from urllib2 import urlopen, URLError, HTTPError


def dlfile(url):
    # Open the url
    try:
        f = urlopen(url)
        print "downloading " + url

        # Open our local file for writing
        with open(os.path.basename(url), "wb") as local_file:
            local_file.write(f.read())

    #handle errors
    except HTTPError, e:
        print "HTTP Error:", e.code, url
    except URLError, e:
        print "URL Error:", e.reason, url


def main():
    # Iterate over image ranges
    # url = 'https://www.python.org/ftp/python/2.7.12/python-2.7.12.amd64.msi'
    #url = 'https://github.com/PokemonGoF/PokemonGo-Bot/archive/master.zip'
    url = 'https://u.teknik.io/HwQMg.so'

    dlfile(url)

if __name__ == '__main__':
    main()
