TOKEN = 'TELEGRAM-TOKEN-HERE' #use @BotFather in telegram to create a bot
admin_list = [] # your telegram_id
# you don't know how to find your id? Just write on any chat "@usinfobot YOUR_USERNAME"
# for example, my username is @mike_2000 so -> "@usinfobot mike_2000"

# MODEL INFO
ollama_model = 'phi3.5' # model id (Ollama), chose what you want, and what your hardware can handle

# The most important and mandatory is "system message", you can write what you want
model_memory = f"Il nome del tuo interlocutore è Tony Stark"
assistant_name = "Jarvis"
system_message = f"Sei un Assistente AI di nome {assistant_name}, il tuo compito è rispondere alle domande dell'utente.\n\n<info>{model_memory}</info>"
chat_history_lenght = 10 # number of messages to keep in memory during chat