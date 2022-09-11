# LUG`ATLAR BILAN ISHLASH
# 1-misol: Otam (onam, akam, ukam va hokozo) degan lug`at yarating va
# va shu inson haqida kamida 3 ta ma`lumot kiriting (ismi, t-yili, shahri va hokozo)
# Lug`atning malumotini matn shaklida konsolga chiqaring.

otam  = {
    'ismi' : 'Jasur',
    'familiyasi' : 'Boytanov',
    't_yili' : 1975,
    't_joyi' : 'Baxmal'
    }
onam = {
    'ismi' : 'Fazilat',
    'familiyasi' : 'Boytanova',
    't_yili' : 1978,
    't_joyi' : 'baxmal'
}
ukam = {
    'ismi' : 'Sherzod',
    'familiyasi' : 'Mustafoyev',
    't_yili' : 2002,
    't_joyi' : 'baxmal'
}
print(f"Otamning ismi {otam['ismi'].title()},\
 familiyasi {otam['familiyasi'].title()}, \
{otam['t_yili']}-yilda, {otam['t_joyi']}da tug'ilgan" )
print(f"Onamning ismi {onam['ismi'].title()},\
 familiyasi {onam['familiyasi'].title()}, {onam['t_yili']}-yilda,\
{onam['t_joyi'].title()}da tug'ilgan." )
print(f"Ukamning ismi {ukam['ismi'].title()},\
 familiyasi {ukam['familiyasi'].title()}, {ukam['t_yili']}-yilda,\
{ukam['t_joyi'].title()}da tug'ilgan")


# 2-Misol: Oilangiz az`olarining sevimli toamlar ro`yxatini tuzing.
# Lug`at kamida 5 ta ism-toam juftligi bo`lsin, kamida 3 kishining sevimli
# toamini konsolga chiqaring:

s_toamlar = {
    'ali' : 'manti',
    'vali': 'norin',
    'hasan':'kabob',
    'husan':'osh',
    'olim':'chipsi',
    'zokir':'gumma'
}
print(f"Alining sevimli toami:  {s_toamlar['ali'].title()}")
print(f"Valining sevimli toami:  {s_toamlar['vali'].title()}")
print(f"Hasanning sevimli toami:  {s_toamlar['hasan'].title()}")
print(f"Husanning sevimli toami:  {s_toamlar['husan'].title()}")
print(f"Olimning sevimli toami:  {s_toamlar['olim'].title()}")

# 3-Misol: Python izohli lug`atini tuzing: Lug`atda shu kunga qadar o`rgangan
# 10 so`zni kiriting (masalan: integer, float, string, if, else va h.k) va
# har birining qisqacha tarjimasini yozing.

p_izohlar = {
    'string':'matn ',
    'float':'o`nlik son',
    'integer':'butun son',
    'false':'yolg`on',
    'true':'rost',
    'none':'bo`sh obyekt',
    'if':'agar',
    'else':'aks holda',
    'print':'konsolga chiqarish',
    'import':'kutubxona chaqirish'
}
print(f"Quyida izohlar bajaradigan vazifasi keltrilgan {p_izohlar}")

# 4-Masala: Foydalanuvchidan biror so`z kiritishni so`rang
# va so`zning tarjimasini yuqoridagi lug`atdan chiqarib bering.
# Agar so`z lug`atda mavjud bo`lmasa, "Bunda so'z mavjud emas"  degan xabarni chiqaring.


p_izohlar = {
    'string':'matn ',
    'float':'o`nlik son',
    'integer':'butun son',
    'false':'yolg`on',
    'true':'rost',
    'if':'agar',
    'else':'aks holda',
    'print':'konsolga chiqarish',
    'import':'kutubxona chaqirish'
}
kalit = input("Kalit so`z kiriting: ").lower()
# print(p_izohlar.get(kalit, "Bunday so`z mavju emas"))
tarjima = p_izohlar.get(kalit)
if tarjima == None:
    print("Bunday so`z mavjud emas. ")
else:
    print(f"{kalit}ning tarjimasi {tarjima}")

