a = 5
b = 6
c = 3

print(a+b)

fruit = ["mangue","pomme","letchis","avocat"]
print(fruit[1])
fruit.append("orange")
print(fruit)
fruit.insert(0,"ananas")
print(fruit)
#____________________________________________
panier = {"mangue" : 5,"ananas" : 10}
print(panier)
panier["mangue"] = 6
print(panier)
panier.pop("mangue")
print(panier)
panier["avocat"] = 3
print(panier)
print(panier)



for i in fruit:
    print(i)

if a < b and b > c:
    print("ok")
else:
    print("nok")
#______________________________________
place_cinema_dispo = 50
place_cinema_vendu = 39

while place_cinema_vendu < place_cinema_dispo:
    place_cinema_vendu += 1
    print(f"on a vendu {place_cinema_vendu} places") 
    if place_cinema_vendu == place_cinema_dispo:
        print("on est complet maintenant")

import random as rd
print(rd.random())
print(rd.uniform(3,5))
