from sgmllib import SGMLParser
import urllib, re, os
dirs = []
pages = []
check = True
total = 0
count = 0
length = 40
def mkdir():
    global DLlocation
    DLlocation = raw_input('Enter download folder:\n')
    if DLlocation:
        root,  tail = os.path.splitdrive(DLlocation)
        os.chdir(root+os.sep)
        try:
            os.makedirs(DLlocation)
            os.chdir(DLlocation)
            DLlocation = os.getcwd()
        except:
            try:
                os.path.exists(DLlocation)
                os.chdir(DLlocation)
                DLlocation = os.getcwd()
            except:
                print "Entered bad pathname."
                mkdir()
    else:
        print "Did not enter pathname."
        mkdir()
def getimgs():
    site = raw_input('Enter photobucket gallery:\n')
    if site:
        site = re.split('[a-zA-Z0-9_.?=-]*$',site)[0]
        try:
            scanpages(site)
        except:
            print "Entered bad URL."
            getimgs()
        try:
            for page in pages:
                print "Downloading pictures from page "+str(pages.index(page)+1)+"..."+" "*15+"\n"
                getpics(page)
            print "\nCompleted downloading all "+str(count)+" images in gallery."+" "*10+"\n"
        except:
            print "Error downloading images."
            getimgs()
    else:
        print "Did not enter URL."
        getimgs()
def dlbar():
    barnum = count*length/total
    blanknum = length-barnum
    bars = '='*barnum
    blanks = ' '*blanknum
    return "["+bars+blanks+"]"
def DLpic(url,filename):
    sock = urllib.urlopen(url)
    img = sock.read()
    location = open(DLlocation+os.sep+filename, "wb")
    location.write(img)
    location.close()
def getpics(site):
    sock = urllib.urlopen(site)
    parser = Parser()
    parser.feed(sock.read())
    parser.close()
    sock.close()
    images = []
    imgName = re.compile('th_[a-zA-Z0-9_-]+.[a-z]+$')
    for url in parser.imgs:
        idx = parser.imgs.index(url)
        try:
            img = imgName.search(url)
            file = img.group()
            fullimg = file.replace('th_',  '')
            url = url.replace(file, fullimg)
            file = file.replace('th_', '')
            images.append(url)
        except:
            continue
    if len(images) == 0:
        print "No images on page."
        getimgs()
    images = images[5:]
    for url in images:
        global count
        count = count + 1
        idx = images.index(url)
        regx = re.compile('[a-zA-Z0-9_-]+.[a-z]+$')
        fullimg = regx.search(url)
        done = str(idx+1)
        file = fullimg.group()
        if int(done) < len(images):
            print('\033[AImage '+str(done)+'/'+str(len(images))+' on current page. '+str(count)+'/'+str(total)+' total.'+' '*5)
        else:
            pagenum = count/20
            if count%20:
                pagenum=pagenum+1
            print('\033[A\033[AAll images on page '+str(pagenum)+' downloaded.'+' '*20)
        print(dlbar()+'\033[A')
        DLpic(url,file)
def scanpages(site):
    num = 0
    print "Scanning for end page..."
    while True:
        imgs = []
        link = site+'?start='
        usock = urllib.urlopen(link+str(num))
        parser = Parser()
        parser.feed(usock.read())
        parser.close()
        for url in parser.imgs:
            imgName = re.compile('th_[a-zA-Z0-9_-]+.[a-z]+$')
            try:
                img = imgName.search(url)
                file = img.group()
                imgs.append(file)
            except:
                continue
        if not len(imgs) == 25:
            global total
            total = len(imgs)-5+num
            pages.append(link+str(num))
            print "Found end page: "+str(num/20+1)
            break
        pages.append(link+str(num))
        num = num + 20
    return
class Parser(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.imgs = []
    def start_img(self, attrs):
        src = [v for k, v in attrs if k=='src']
        if src:
            self.imgs.extend(src)
mkdir()
getimgs()

