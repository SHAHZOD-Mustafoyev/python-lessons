# 1-MISOL: Foydalanuvchidan yaxshi ko`rgan kitobini kiritishini so`rang
# Foydalanuvchi "stop" so`zini yozishi bilan dastur to`xtasin
print("Siz yaxshi ko`rgan kitobni chiqaruvchi dastur: ")
savol = "Yoqtirgan kitobingizni kiritng>> "
savol += "Kitoblarni kiritb bo`lgach  'stop' deb yozing: "
kitob = ''
while kitob != 'stop':
    kitob = input(savol)
    if kitob != 'stop':
        print(f"Sizning yoqtirgan kitobingiz { kitob.upper() } kitobi: ")
    else:
        print("Dastur to`xtadi!!!!!!!! >>>>> ")
# 2-MISOL: Muzeyga krish narxi yoshga bog`liq bo`lsin: 7 dan yoshlarga
# kirish 2000, 7 dan katta 18 dan kichkanalarga 3000, 18 dan katta 65 dan
# kichkanalarga 10000 so`m, 65 dan kattalarga bepul deb kiritlsin
# foydalanuvchi 'exit' yoki 'quit' deb yozganida dastur to`xtasin:

print("Muzeydagi chipta narxi foydalanuvchi yoshiga bog`liq: ")
savol = "Yoshingizni kiriting: "
savol += "(Dasturni to`xtatish uchun 'exit' yoki 'quit' deb yozing: "

while True:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        break
    yosh = int(qiymat)

    if yosh < 7 :
        narx = 2000
    elif 7 <= yosh < 18:
        narx = 3000
    elif 18 <= yosh < 65:
        narx = 10000
    else:
        narx = 0
    if narx == 0:
        print("Sizga kirish bepul!!! ")
    else:
        print(f"Sizga kirish {narx} so'm ")

