import random
frases = [
    "No dejes para mañana lo que puedes lograr hoy.",
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
    "Cree en ti y todo será posible.",
    "Cada día es una nueva oportunidad para mejorar.",
    "La disciplina es el puente entre metas y logros.",
    "El tiempo no es más que una forma de contar los hechos, nunca es tarde para empezar.",
    "No importa que hagas siempre habrá algo de lo que te arrepientas, asi que no temas experimentar."
]
frases2 = [
    "hoy es tu dia!",
    "mañana todo ira mejor!",
    "nadie puede detenerte!",
    "eres admirable!",
    "Henry Calvin estaria orgulloso de ti!"
]
def generar_frase():
    return random.choice(frases)
def generar_segunda_frase():
    return random.choice(frases2)
if __name__ == "__main__":
while True:
    pregunta = input("quieres leer algo? ").lower()
    if pregunta == "si":
            print("Frase del día:")
            print(generar_frase())
            print("______________")
            print(generar_segunda_frase())
    elif pregunta == "no":
        print("vale, exito!")
        break
    else:
        print("no entiendo, por favor coloca 'si' o 'no' ")