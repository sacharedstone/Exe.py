import random

print('Bienvenue sur Exo.py')
print('Vous disposez de 5 jarres choisirez vous combien = 1, 2, 3, 4 ou 1000000')


# Random
snake_jar = random.randint(1, 10)

# Valeur Du Joueur
choix = int(input())

print("le joueur a mis le nombre", choix)
print(snake_jar)
