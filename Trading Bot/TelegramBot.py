# Insert the Bot Father API TOKEN you created
# https://api.telegram.org/bot{API TOKEN}/getUpdates

# Add the bot username you created with Bot father to the group and get the ID
# chatID: {CHAT ID}

# The url below is will help test if the message 'Just a test' is sent to your group
# https://api.telegram.org/bot{API TOKEN}/sendMessage?chat_id={CHAT ID}&text='Just a test'

import requests
import time

jokes = ['Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.',
         'Why do we tell actors to “break a leg?” Because every play has a cast.',
         'Helvetica and Times New Roman walk into a bar. “Get out of here!” shouts the bartender. “We don’t serve your type.”',
         'Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.']

for joke in jokes:
    baseurl = 'https://api.telegram.org/bot{API TOKEN}/sendMessage?chat_id={CHAT ID}&text="{}"'.format(joke)
    requests.get(baseurl)
    time.sleep(5)
