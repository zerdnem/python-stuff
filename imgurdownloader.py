#!/usr/bin/env python
"""Parse and download images from an ImgUr gallery.

The creation of this script was inspired by Methos25's rice [1]. I loved the
wallpaper he was using, and looking on the ImgUr gallery [2] he told us he got
the image, I had the idea to create a script to download all images from there
and randomly pick one to set as wallpaper.

Well, this script do the first part, following the KISS philosophy. The second
part will be done later on.

[1] https://www.reddit.com/r/unixporn/comments/4mtww2/i3gaps_a_little_materialistic/  # noqa
[2] https://imgur.com/gallery/SwhjO
"""

import os
import re
import sys

from urllib2 import urlopen
from HTMLParser import HTMLParser
from argparse import ArgumentParser

__author__ = "Rodrigo Oliveira"
__version__ = "1.0.0"
__maintainer__ = "Rodrigo Oliveira"
__email__ = "rodrigo@deadbodyoutline.com"


class Arguments():
    url = None
    path = None

    def __init__(self):
        self._parse_args()

    def _parse_args(self):
        parser = ArgumentParser()

        parser.add_argument("url",
                            type=str,
                            metavar='N',
                            nargs=1,
                            help="ImgUr gallery URL")
        parser.add_argument("--path",
                            "-p",
                            type=str,
                            default=os.getcwd(),
                            help="Path to save images (default: current)")
        parser.add_argument("--limit",
                            "-l",
                            type=int,
                            default=0,
                            help="Limit the number of images to download\
                            (default: 0, all images)")
        parser.add_argument("--print-to-file",
                            "-f",
                            action="store_true",
                            default=False,
                            help="Log messages to '~/.imgurme.log'. Note that\
                            this file will be replaced at each run\
                            (default: false)")

        args = parser.parse_args()

        self.url = args.url[0].strip()
        self.path = args.path.strip()
        self.limit = args.limit
        self.log = args.print_to_file


class ImgUrParser(HTMLParser):

    def __init__(self):
        # disclaimer: HTMLParser is old style class, do not support 'super'
        # initialization style :/
        HTMLParser.__init__(self)

        self._images = []
        self._scheme = None

    def _validate_url(self, url):
        regex = ur'http[s]?://(?:w{3}\.)?imgur.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]\
                |[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))*'  # neat

        return re.match(regex, url)

    def _validate_image(self, image):
        """Check if parsed image name has one of the supported extensions

        Currently supporting JPG and PNG. Do ImgUr support any other?

        :param image: the image string to validate
        """
        regex = ur'.*(?:.png|.jpg)$'

        return re.match(regex, image)

    def parse(self, url):
        p = PrintOut.instance()

        if not self._validate_url(url):
            p.out("URL '%s' doesn't seems to be a valid ImgUr address" % url)
            return

        self._scheme = url.split(":")[0]
        p.out("Parsing %s" % url)

        try:
            f = urlopen(url)
            html = f.read()
            f.close()
        except Exception as e:
            p.out(">> Error; is it a valid URL? (%s)" % e)
            return

        try:
            html = self.unescape(html)
        except Exception as e:
            p.out(">> Error: %s" % e)
            return

        try:
            self.feed(html)
        except Exception as e:
            p.out(">> Error: %s" % e)
            return

        p.out("Found %s images" % len(self._images), 4)

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr, value in attrs:
                if attr == "href" and self._validate_image(value):
                    self._images.append("%s:%s" % (self._scheme, value))

    def images(self):
        return self._images


class Downloader():

    def __init__(self, path, name):
        self._path = path if path != str() else "./"
        self._name = name

        self._download_path = os.path.join(path, dir_name)

    def download(self, images=[], limit=0):
        p = PrintOut.instance()

        if not images:
            return

        if not os.path.exists(self._path):
            p.out("> Path '%s' doesn't exist" % self._path)
            return

        if not os.path.exists(self._download_path):
            p.out("Creating %s/ on %s" % (self._name, self._path))
            try:
                os.mkdir(self._download_path)
            except Exception as e:
                p.out(">> Error: %s" % e)
                return

        p.out("Downloading images to %s/" % self._download_path)
        if limit > 0:
            images = images[:limit]
            p.out("(limiting download to %s images)" % limit, 4)

        num_images = len(images)
        for index, image in enumerate(images):
            image_file = image.split('/')[-1]

            p.out("(%s/%s) %s..." % (index + 1, num_images, image_file), 4)

            image_file = os.path.join(self._download_path, image_file)
            if os.path.isfile(image_file):
                p.out("File already exists, skipping...", 8)
                continue

            try:
                f = open(image_file, 'wb')
                f.write(urlopen(image).read())
                f.close()
            except Exception as e:
                p.out(">> Error: %s" % e)
                return


class PrintOut(object):
    _instance = None
    _where = sys.stdout

    def __del__(self):
        if type(self._where) is file:
            self._where.close()

    @classmethod
    def instance(self):
        if self._instance is None:
            self._instance = self()

        return self._instance

    def set_output(self, file=None):
        if file is None:
            self._where == sys.stdout
            return

        self._where = open(file, 'w+')

    def out(self, str, indent=0):
        print >> self._where, str.rjust(len(str) + indent)

        if type(self._where) is file:
            self._where.flush()

if __name__ == '__main__':
    arguments = Arguments()

    log_file = os.path.join(os.path.expanduser('~'), 'imgurme.log')
    p = PrintOut.instance()
    p.set_output(log_file if arguments.log else None)

    url = arguments.url

    parser = ImgUrParser()
    parser.parse(url)

    dir_name = url.split('/')[-1]

    downloader = Downloader(arguments.path, dir_name)
    downloader.download(parser.images(), arguments.limit)
