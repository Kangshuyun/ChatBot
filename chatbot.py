
from chatterbot import ChatBot 

chatbot = ChatBot("Chatpot")

exit_condition =("q" ,"Exit", "quit")

while True:
    query =input(">   ")
    if query in exit_condition:
        break
    else:
     print(f" {chatbot.get_response(query)}")     