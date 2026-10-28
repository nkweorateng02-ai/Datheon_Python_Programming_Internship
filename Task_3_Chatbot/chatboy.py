import json
import re
import os

try:#Searches for the json file
    
    base_dir = os.path.dirname(os.path.abspath(__file__))#Stores the folder
    json_path = os.path.join(base_dir, "sample_faq.json")# Joins the folder and the filename
    with open(json_path, "r") as f:#Opens the json file
        data = json.load(f)#Stores the data inside the json file
except FileNotFoundError:#Alerts user when the file does not exist
    print("Cannot find the json file")
    exit()

greetings = data.get("greetings", [])
faqs = data.get("faqs", [])

# Stores the keywords that willl trigger the response
INTENTS = {
    "greeting": r"\b(hello|hi|hey|good morning|good afternoon)\b",
    "hours": r"\b(hours|operation|open|close|timing|business hours|time)\b",
    "submit": r"\b(submit|submission|internship|project|github|repository)\b",
    "certificate": r"\b(certificate|certification|cert)\b",
    "exit": r"\b(bye|exit|quit|goodbye|thank you)\b"
}

def normalize(text):
    return text.lower().strip()#Removes extra spaces and make everything lowercase

def get_faq_answer(user_input):
    
    user_input = normalize(user_input)
    for item in faqs:
        q = item["question"].lower()
        #Loops through each word in the list
        keywords = re.findall(r'\w+', q) # Splits words
        for word in keywords:
            if len(word) >3 and word in user_input:# Ignores small words and checks for the keyword in user's input
                return item["answer"]#Returs the answer triggered by the keyword in the response
    return None

def get_intent(user_input):
    text = normalize(user_input)#Changes text to lower case
    for intent, pattern in INTENTS.items():
        if re.search(pattern, text, re.IGNORECASE):#Checks keywords
            return intent#REturns answer when there is a match
    return None#If there is no match the bot goes to fallback message

def chatbot():
    print("=========================================================")
    print("  Welcome to our customer support assistant Chatbot!")
    print("=========================================================")
    print("Hello! How can I help you today?")
    print("You can ask about hours, internship submission or certificate)")

    while True:
        user = input("\nYou: ").strip()#Accepts user's question
        if not user:
            continue

        normalized = normalize(user)
        intent = get_intent(normalized)

        
        if intent == "exit" or normalized in ["bye", "exit", "quit"]:#Searches for keywords that triggers the end of conversation
            print("Bot: Enjoy the rest of your day! Goodbye!")
            break

        # 2. Greeting
        if intent == "greeting":#Checks if you're greeting and responds
            print("Bot: Hello! I'm your support assistant. How can I help?")
            continue#skips the rest and goes to the while loop

        # 3. Hours
        if intent == "hours":
            # find answer from JSON
            for item in faqs:
                if "hours" in item["question"].lower():#Checks if the question has to do with time and gives relevant reply
                    print(f"Bot: {item['answer']}")
                    break
            continue#If you typed hours it skips everything and continues with the conversation(similar approach applies below with submit and certificate)

        if intent == "submit":
            for item in faqs:
                if "submit" in item["question"].lower():
                    print(f"Bot: {item['answer']}")
                    break
            continue

        if intent == "certificate":
            for item in faqs:
                if "certificate" in item["question"].lower():
                    print(f"Bot: {item['answer']}")
                    break
            continue

        # 6. Try generic FAQ matching
        faq_ans = get_faq_answer(normalized)
        if faq_ans:
            print(f"Bot: {faq_ans}")
            continue

     #Prints the following when there are no keywords
        print("Please ask about hours, internship submission or certificate ")
        print("Bot: You can ask about\n -certificate\n -business hours\n -project submission or\n -certificate ")

if __name__ == "__main__":
    chatbot()#Call the function
    input("\nPress ENTER to exit...")
