# https://api.telegram.org/bot/1807912789:AAFAdGju6F6q_nBJ9HoI8CG8alsvfe7BisY/getUpdates
# chatID: -557968202
# https://api.telegram.org/bot1807912789:AAFAdGju6F6q_nBJ9HoI8CG8alsvfe7BisY/sendMessage?chat_id=-557968202&text='Just a test'
import requests
import time

jokes = ['Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.',
         'Why do we tell actors to “break a leg?” Because every play has a cast.',
         'Helvetica and Times New Roman walk into a bar. “Get out of here!” shouts the bartender. “We don’t serve your type.”',
         'Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.']

for joke in jokes:
    baseurl = 'https://api.telegram.org/bot1807912789:AAFAdGju6F6q_nBJ9HoI8CG8alsvfe7BisY/sendMessage?chat_id=-557968202&text="{}"'.format(joke)
    requests.get(baseurl)
    time.sleep(5)