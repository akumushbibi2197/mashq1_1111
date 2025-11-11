#1-misol
lugat = eval(input("Lug‘at kiriting: "))
print("Kalitlar ro‘yxati:", list(lugat.keys()))

#2-misol
lugat = eval(input("Lug‘at kiriting: "))
print("Qiymatlar yig‘indisi:", sum(lugat.values()))

#3-misol
lugat = eval(input("Lug‘at kiriting: "))
kalit = input("Qaysi kalitni tekshirmoqchisiz? ")
print("Kalit mavjudmi?", kalit in lugat)

#4-misol
lugat = eval(input("Lug‘at kiriting: "))
saralangan = dict(sorted(lugat.items(), key=lambda x: x[1]))
print("Saralangan lug‘at:", saralangan)

#5-misol
satr = input("Satr kiriting: ")
natija = {}
for harf in satr:
    natija[harf] = natija.get(harf, 0) + 1
print("Harf takrorlanishi:", natija)
