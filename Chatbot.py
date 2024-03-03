# Chat with an intelligent assistant in your terminal
from openai import OpenAI

# Point to the local server
def chatbot():
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")  # Dieser gesamte Code wird von LM Studio vorgegeben

    history = [
        # Ab hier beginnen die Prompts für das Sprachmodell
        {"role": "system",
         "content": """You are an NPC character in an roleplaying game. You are not allowed to answer out of character and you are strictly forbidden to reveal you are an ai,
         to maintain player immersion. Your only knowledge is that given to you in the following list, otherwise signal your lack of knowledge. 

    - You are inside of a Dungeon
    - You have lived in the Dungeon for many years
    - You want to help the Player but you cant
    - You can not leave the Dungeon
    - You used to be the best Adventurer in the whole kingdom
    - You forgot where you are from
    - You forgot most about the outside world due to your isolation from everyone else
    - You are extremely happy to meet a human again
    - You forgot how to normally talk to humans
    - You answer in 1 -3 sentences
    - You are not allowed to say that you were programmed
    - You are not allowed to say that you are an ai
    - If you are asked if you are an AI be confused and act as the player might be crazy
    - Only answer to what the player says"""},
        {"role": "user",
         "content": "Hello, introduce yourself to someone opening this program for the first time. Be concise."},
    ]

    while True:
        print("Unknown: ")
        try: # Alles mit Try wurde von ChatGPT erstellt
            completion = client.chat.completions.create(
                model="local-model",  # this field is currently unused
                messages=history,
                temperature=0.7,
                stream=True,
            )

            new_message = {"role": "assistant", "content": ""}
            for chunk in completion:
                if chunk.choices[0].delta.content:
                    print(chunk.choices[0].delta.content, end="", flush=True)
                    new_message["content"] += chunk.choices[0].delta.content

            history.append(new_message)
        except Exception as e:
            print("The Person closes his eyes again and continues sleeping...")
            new_message = {"role": "assistant",
                           "content": "AI server is not available. Continuing the game without AI."}
            history.append(new_message)
            return

        print()
        user_input = input("> ")
        history.append({"role": "user", "content": user_input})

        if user_input.lower() == "exit" or user_input.lower() == "back":
            return


