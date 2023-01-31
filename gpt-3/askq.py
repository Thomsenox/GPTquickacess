import openai
from functions import ask_question, askAPI

openai.api_key = askAPI()

def interactive_chat():
    prev_answer = ""
    print("哈喽, 这是OPENAI的大型语言模型, 请问您想问些什么?(输入 '退出' 来退出程序)")
    while True:
        # Ask the question
        question = input("我的提问: ")
        if question == "退出":
            print("很高兴能与人类交流! 谢谢!!")
            break
        prev_answer = ask_question(prev_answer, question)
        print(f"AI的回答: {prev_answer}")
        print("__________________________________________")
interactive_chat()
