# Library for requests
import requests
# PIL adds image processing capabilities
from PIL import Image
# StringIO allows to read and write strings as files
from StringIO import StringIO

# The URL to get the image from
target ='https://www.hackthissite.org/missions/prog/2/PNG/'

# Cookies 
cookieName1 = 'PHPSESSID'
cookieValue1 = 'phpsessidgoeshere'
cookies = {cookieName1: cookieValue1}

# Referer
referer = 'https://www.hackthissite.org/missions/prog/2/'

# Headers
headers = {'Referer': referer}

# Verifying we can connect
req = requests.get(target, cookies=cookies)
if req.status_code != requests.codes.ok:
        raise ValueError('Poof! Unable to connect to target t(X_X)t')
else:
        print('+++ Connected to target. Starting operation...\n')
 
# Get image
theImage = Image.open(StringIO(req.content))
img_width, img_height = theImage.size
img_pixel = theImage.load()
preposition = 0
morse_code = ""
answer = ""

# On Morse code: https://en.wikipedia.org/wiki/Morse_code 
char_morse_dict={
'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.',
'G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..',
'M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.',
'S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
'Y':'-.--','Z':'--..','0':'-----','1':'.----','2':'..---','3':'...--',
'4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',
'.':'.-.-.-',',':'--..--','?':'..--..',"'":'.----.','/':'-..-.','(':'-.--.-',
')':'-.--.-',':':'---...',';':'-.-.-.','=':'-...-','+':'.-.-.','-':'-....-',
'_':'..--.-','"':'.-..-.','$':'...-..-','':''
}
 
# Fetch ASCII code from the image
for y_point in range(img_height) :
    for x_point in range(img_width) :
        if img_pixel[x_point, y_point] == 1 :
            # Convert ASCII code to "dits" and "dahs" in morse code
            symbol = chr(x_point + 100 * y_point - preposition)
 
            if symbol != ' ' :
                morse_code += symbol
            else :
                # Decode morse code to character
                char = [key for key, value in char_morse_dict.iteritems() if value == morse_code][0]
                answer += char
                morse_code = ""
 
            preposition = x_point + 100 * y_point

print(answer)

# The URL to send our answer to
target = 'https://www.hackthissite.org/missions/prog/2/index.php'

# Submitting our answer
data = {'solution': answer}
headers.update({'submit': 'submit'})

# Sending our cookies, data and headers
req = requests.post(target, cookies=cookies, data=data, headers=headers)

print('+++ Successfully sent information.\n') 
print(req.content)


