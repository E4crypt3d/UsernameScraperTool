import requests as r

red = "\u001b[6;31m"
green = "\u001b[1;32m"
reset = '\u001b[0m'

print(f'\t\t{green}Username Scraper Tool by @E4CRYPT3D{reset}\n')
print(f"{red}NOTE:This might not be 100% accurate...\n")
print(f"NOTE: Use this for only educational purpose{reset}\n")
from social_sites import social_sites,username

for social, social_link in social_sites.items():
    try:
        get_social = r.get(social_link)
        status_code = get_social.status_code
    except r.exceptions.TooManyRedirects:
        print("Too Many Redirects")
        break
    except r.exceptions.ConnectionError:
        continue
    except r.exceptions.Timeout:
        continue
    except KeyboardInterrupt:
        print("\nThanks For Using our tool")
        break
    if status_code == 404:
        continue
    print('____________________________________________________________________')
    print('|  '+social.upper() +' '+'\t\t| ' + 'Username = '+username +'\t\t| '+ social_link+' |')