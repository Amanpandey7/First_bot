
url = "https://api.telegram.org/bot1762612777:AAF4tgycJOrBuhwE2f3yMpL8qAo40UcBoGw/"

#creating function to get chat id

def get_chat_id(update):
    chat_id = update['message']["chat"]["id"]
    return chat_id

#create a function to get message text
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text

#create a function to get last update
def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json
    result = 