"""Notre programme permet à l'utilisateur d'entrer 2 mots,
en suite le programme à l'aide de la classe set renvoyera
differemment les elements suivants:les lettres communes, les lettres
manquantes dans le deuxième mot par rapport au premier mot et
les lettres manquantes dans le premier mot par rapport au
deuxième mot"""

x = set(input("\ntaper le premier mot:..."))
y = set(input("\ntaper le deuxième mot:..."))

print("\nles lettres communes aux deux mots entrés sont:",x&y)

print("\nles lettres du deuxièmes mot manquantes dans le premier sont:",y-x)

print("\nles lettres du premier mot manquantes dans le deuxième sont:",x-y)

print("\n\nFIN DU PROGRAMME.")






