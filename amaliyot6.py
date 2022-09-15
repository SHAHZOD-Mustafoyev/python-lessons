# 1-MISOL: Foydalanuvchi ism va yoshini so`rab, uning tug`ilgan yilini
# hisoblaydigan funksiya yozing:

def t_yil_hisobla(ism,yosh ):
    """Foydalanuvchi ismi va yoshi orqali tug`ilgan yilini hisoblash."""
    print(f"{ism.title()} {2022 - yosh }-yilda tug`ilgan. ")

t_yil_hisobla(ism="Shahzod", yosh=22)

# 2-MISOL: Foydalanuvchidan son olib uning kvadratini va kubini
# konsolga chiqaruvchi funksiya yozing:
def kvadrat_kub_hisobla(son):
    """Sonning kvdrati va kubini konsolga chiaqruvchi funksiya: """
    print(f"{son} ning kvadrati {son ** 2} ga, kubi esa {son ** 3} ga teng. ")

kvadrat_kub_hisobla(4)

# 3-MISOL: Foydalanuvchidan son olib uning juft yoki toqligini
# konsolga chiqaruvchi funksiya yozing:

def juft_toq_hisobla(son):
    """Son juft toqligini tekshiradigan funksiya. """
    if son%2 == 0:
        print(f"{son} juft son:")
    else:
        print(f"{son} toq son:")
juft_toq_hisobla(6)
# 4-MISOL: Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga
# chiqaruvchi funksiya yozing. Agar sonlar teng bo`lsa "Sonlar teng" degan habar chiqsin.
def taqqosla(son1, son2):
    """Ikkta sonni taqqoslaydigan funksiya."""
    if son1 > son2:
        print(son1)
    elif son1 == son2:
        print("Sonlar teng!!! ")
    else:
        print(son2)
taqqosla(11, 11)
# 5-MISOL: Foydalanuvchidan x va y sonlar olib x ning y-darjasini
# hisoblaydigan funksiya yozing:
def daraja_hisobla(x,y):
    """x ning y-darajasini hisoblaydigan funksiya. """
    print(f"{x}ning {y}-darajasi {x**y}ga teng. ")

daraja_hisobla(2, 5)

# 6-MISOL: Yuqoridagi funksiyaga 2 standart qiymat bering.

def kvadrat_hisobla(x, y = 2):
    """Sonning kvdratini hisoblavchi dastur. """
    print(f"{x}ning kvdrati {x**y}ga teng. ")
#
# kvadrat_hisobla(8)
# 7-MISOL: Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo`lgan
# sonlarga qoldiqsiz bo`linishini tekshiruvchi funkisya yozamiz.


def bolinish_alomatlar(son):
    """Bo`linish almoatlarini tekshiradi. """
    for x in list(range(2, 11)):
        if son%x == 0:
            print(f"{son} {x} ga qoldiqsiz bo`linadi. ")

bolinish_alomatlar(70)




