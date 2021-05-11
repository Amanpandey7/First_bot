from pip._vendor import requests
import random
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
    response = response.json()
    result = response["result"]
    total_updates = len(result)-1
    return result[total_updates] #get last record of message update


#create function to let bot send message to the user
def send_messgae(chat_id, message_text):
    params = {"chat_id": chat_id,"text": message_text}
    response = requests.post(url + "sendMessage", data=params)
    return response

#create main function to navigate or reply message back
def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            if get_message_text(update).lower() == "hi" or get_message_text(update).lower() == "hello":
                send_messgae(get_chat_id(update),'Hello welcome to our bot. Type "Play" to roll the dice!')
            elif get_message_text(update).lower() == "play":
                _1= random.randint(1,6)
                _2= random.randint(1,6)
                _3= random.randint(1,6)
                send_messgae(get_chat_id(update),'You have ' + str(_1) + " , " + str(_2) + " , " + str(_3) + ". The sum is "+ str(_1+_2+_3) + "!!!" )

            else:
                send_messgae(get_chat_id(update), "try again")

            update_id +=1

#calling function
main()