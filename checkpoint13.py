def display_regular(message):
    print(f"{message}")
    return

def display_uppercase(message):
    print(f"{message.upper()}")
    return


def display_lowercase(message):
    print(f"{message.lower()}")
    return

mensaje = input(f"What is your message? ")

display_regular(mensaje)
display_uppercase(mensaje)
display_lowercase(mensaje)