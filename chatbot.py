import re
import random

# Define a list of patterns and responses
rules = [
    (r'hi|hello|hey', ["Hello!", "Hi there!", "Hey!"]),
    (r'how are you ?', ["I'm doing well, thank you!", "I'm great, how about you?", "I'm fine, thanks!"]),
    (r'what is your name ?', ["My name is Chatbot.", "I'm Chatbot, your virtual assistant.", "You can call me Chatbot."]),
    (r'good', ["Happy to hear", "Great", "Nice!How can I help?"]),
    (r'what (.*)do you like ?', ["I like chatting with people!", "I enjoy talking to you.", "I like helping users like you."]),
    (r'(.*)weather', ["I'm not sure, but you can check the weather on a weather website.", "I don't have access to weather information right now."]),
    (r'(.*)time ', ["I don't have a watch, but you can check the time on your device.", "Time is a concept, and I am timeless."]),
    (r'bye|goodbye|see you', ["Goodbye!", "See you later!", "Bye! Have a great day!"]),
    (r'(.*)', ["I'm not sure I can not understand you.", "Could you rephrase that?", "Let's talk about something else."])
]

def match_rule(user_input):
    for pattern, responses in rules:
        if re.match(pattern, user_input):
            return random.choice(responses)
    return "I'm not sure I understand you."

# Start the conversation
def chat():
    print("Hi! I'm a chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("> ").lower()
        if user_input in ["bye", "goodbye", "exit"]:
            print("Goodbye!")
            break
        response = match_rule(user_input)
        print(response)

if __name__ == "__main__":
    chat()