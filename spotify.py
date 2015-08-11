import string
import random
import requests
from bs4 import BeautifulSoup
from fng import FakeNameGenerator

def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

full_email = raw_input("What is your email? ")
submits = raw_input("How many accounts to create? ")
email_split = full_email.split("@")
handle = email_split[0]
domain = email_split[1]

for i in range(int(submits)):
    # create a fake profile
    person = FakeNameGenerator('random', 'us', 'us')

    # set initial headers when visiting registration page
    get_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': 'www.spotify.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }
    # cache details
    username = person.username + id_generator()
    password = person.password
    email = "{}+{}@{}".format(handle, id_generator(), domain)
    # registration data
    form_data = {
        'sp_csrf': '',
        'form_token': '',
        'creation_flow':' ',
        'forward_url': '/us/download/',
        'signup_pre_tick_eula': 'true',
        'username': username,
        'password': password,
        'email': email,
        'confirm_email': email,
        'dob_month': '03',
        'dob_day': '1',
        'dob_year': '1980',
        'gender': 'female'
    }
    # start request session
    spotify = requests.Session()
    # set headers
    spotify.headers.update(get_headers)
    # get request registration page
    get_registration = spotify.get('https://www.spotify.com/us/signup/')
    # parse html
    html = BeautifulSoup(get_registration.text)
    # update form data
    form_data['sp_csrf'] = spotify.cookies['sp_csrf']
    form_data['form_token'] = html.select('input[name="form_token"]')[0]['value']
    # post request to registration page
    post_registration = spotify.post('https://www.spotify.com/us/xhr/json/sign-up-for-spotify.php', data=form_data)

    json_data = post_registration.json()
    if json_data.get('errors'):
        print "Errors!"
        for code in json_data['errors']:
            print json_data['errors'][code]['message']
    else:
        print "account registered!"
        fo = open("spotify_accounts.txt", "a+")
        fo.write("{}\n{}:{}\n\n".format(email, username, password));
        fo.close()
