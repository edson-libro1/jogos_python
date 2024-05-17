import random
print("bem vindo ao jogo letra secreta!")
letras_possiveis = ["a", "l", "b", "c"]
letra = random.choice(letras_possiveis)
chute = input("digite uma letra!")
if chute == letra:
    print("você acertou")
else:
    print(f"Você errou. A letra secreta era '{letra}'.")