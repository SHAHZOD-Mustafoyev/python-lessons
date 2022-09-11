# 1-MISOL: Python izolhli lug`atini yarating va kamida 10 ta so`z qo`shing.
# Lug`atdagi har bir kalit va qiymatni for sikli yordamida, alfbo ketma ketligida
# chiroyli qilib konsolga chiqaring.

lugatlar = {
    'print': 'Amalni ekranga chiqarish funksiyasi',
    'for':'Biror amalni qayta qayta bajarish tsikli',
    'boolean':'Mantiqiy qiymat',
    'if':'shartlarni tekshirish operatori',
    'Elif':'Agar masa deb tarjima qilinadi',
    'Float':'O`nlik son',
    'Integer':'Butun son',
    'set':'Lug`atdagi bir xil elementlarni takrorlamaydigan funksiya',
    'none':'bo`sh bo`lgan obyektni qaytaradi',
    'def':'funksiya yaratishda ishlatiladi'
}
for key, value in sorted(lugatlar.items()):
    print(f"{key.title()}-{value}")

# 2-MISOL: Davlatlar va ularning poytaxtlari lug`atini tuzing. Avval
# lug`atdagi davlatlarni keyin poytaxtlarni alohida-alohida, alfbo
# ketma ketligida konsolga chiqaring:

coutries = {
    'Uzbekiston':'Toshkent',
    'America':'Washington',
    'Turkiya':'Istambul',
    'Rossiya':'Maskova',
    'Angliya':'London',
    'Norvegiya':'Oslo',
    'Afg`oniston':'Kabul',

}
print("Dunyo davlatlari:")
for key in sorted(coutries):
    print(key.upper())
print("\nDavlatlarning poytaxtlari")
for value in sorted(coutries):
    print(value.title())


# 3-MISOL: Foydalanuvchidan istlgan davlat nomini kiritishini so`rang
# va shu davlatni poytaxtini konsolga chiqaring. Agar foydalanuvchi
# lug`atda yuq davlat kiritsa "Kechirasiz bizda bunday ma`lumot yo`q"
# degan xabarni konsolga chiqaring:
countries = {
    'o`zbekiston' : 'toshkent',
    'amerika' : 'washington',
    'rossiya' : 'moskova',
    'turkiya' : 'istambul',
    'norvegiya' : 'oslo',
    'italiya' : 'rim',
    'angliya' : 'london'
}
capital = input("Qaysi davlat poytaxtini bilishni istaysiz?:  ").lower()
capitals = countries.get(capital)
if capitals == None:
    print("Kechirasiz bizda bu haqida ma`lumot yo`q: ")
else:
    print(f"{capital.upper()}ning poytaxti {capitals.title()} shahri. ")
# 4-MISOL: Restoran menyusi lug`atini tuzing. Foydalanuvchidan 3 ta toam
# kiritishini so`rang. Foydalanuvchi kiritgan toamlarni menu bilan solishtring
# agar toam menuda bo`lsa narxni ko`rsating aks holda "Kechirasiz! bizda bunday toam yo`q"
# deb konsolga chiqaring:

toamlar = {
    'osh': 10000,
    'jiz': 20000,
    'norin': 18000,
    'shashlik': 15000,
    'sho`rva': 12000,
    'manti': 25000,
    'somsa' : 28000
}
print("3 ta toam buyrutma bering: ")
buyrutmalar = []
for n in range(3):
    buyrutmalar.append(input(f"{n+1}-toam:").lower())
for buyrutma in buyrutmalar:
    if buyrutma in toamlar:
        print(f"{buyrutma.title()} {toamlar[buyrutma]}so`m")
    else:
        print(f"Kechirasiz bizda {buyrutma} yo`q. ")