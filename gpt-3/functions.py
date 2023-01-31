# functions.py
import openai
def ask_question(prev_answer, question):
    prompt = (f"{question}" if prev_answer == "" else f"{prev_answer}\n\n{question}")
    model_engine = "text-davinci-003"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024*2,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = completions.choices[0].text
    return answer
def askAPI():
    api_key = input("请输入您的OPENAI API 钥匙来使用程序: ")
    return api_key

