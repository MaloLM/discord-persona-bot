from GPTpersona import Chat

def main():
    chat = Chat()

    persona_answer = chat.send("Zelda", 'Mais père ?')

    print("Persona answer: ", persona_answer)

    chat.close()

if __name__ == "__main__":
    main()