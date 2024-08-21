import ollama
from util.common import get_user_interactions, save_interaction
import config

def generate_answer(prompt: str, user_id: int):
    messages = [{"role": "system", "content": config.system_message}]
    
    if config.chat_history_lenght <= 0:
        chat_history = []
    else:
        chat_history = get_user_interactions(user_id)[-(config.chat_history_lenght):]
    

    for item in chat_history:
        obj = {"role": item[2], "content": item[3]}
        messages.append(obj)
    
    try:
        last = chat_history[-1]
        counter = int(last[4]) + 1
    except:
        counter = 1

    messages.append({"role": "user", "content": prompt})


    save_interaction(user_id, "user", prompt, counter)
    response = ollama_generate(messages)
    save_interaction(user_id, "assistant", response, counter)
    
    return response



def ollama_generate(messages):
    response = ollama.chat(model=config.ollama_model, messages=messages)
    return response['message']['content']