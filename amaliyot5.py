# 1-MISOL: Foydalanuvchidan buyrutma qabul qiluvchi dastur tuzing.
# Mahsulot nomini birma-bir qabul qilib yangi ro`yxatga joylang:

goods = []
while True:
    mahsulot = input("Mahsulot nomini kiritng: ")
    goods.append(mahsulot)
    javob = input("Yangi mahsulot qo`shasizmi: ha/yo`q ")
    if javob != 'ha':
        print("Siz kiritgan mahsulotlar ro`yxati: ")
        print(goods)
        break

#2-MISOL: Elektron bozor uchun mahsulot va ularning narxlarini lug`atini
# shakillantiruvchi dastur tuzing. Foydalanuvchidan unga bir nechta
# element (tovar va narx)ini kiritishni so`rang.

mahsulotlar = {}
ishora = True
while ishora:
    tovar = input("Tovar nomini kiriting: ")
    narx = input(f"{tovar.title()} ning narxini kiritng. ")
    mahsulotlar[tovar] = int(narx)

    javob = input("Yana tovar qo`shishni hohlaysizmi: ha/yo`q ")
    if javob != 'ha':
        ishora = False
for tovar, narx in mahsulotlar.items():
    print(f"{tovar.title()} ning narxi {narx} so`m. ")

# 3-MISOL: Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi
# buyurtmasi ro`yxatidagi har bir mahsulotni e-bozordagi mahsulotlar
# bilan solishitiring (tayyor ro`yxat ishlatishingiz mumkin).
# Agar mahsuot e-bozorda mavjud bo`lsa mahuslot narhini chiqaring,
# aks holda "Bizda bu mahsulot yo'q" degan xabarni kor`sating.


buyrutmalar = ['olma', 'anjir', 'uzum', 'qovun']
mahsulotlar = {
    'olma' : 15000,
    'shaftoli' : 7000,
    'tarvuz' : 3000,
    'uzum' : 7000
}
while buyrutmalar:
    buyrutma = buyrutmalar.pop()
    if buyrutma in mahsulotlar.keys():
        narx = mahsulotlar[buyrutma]
        print(f"{buyrutma.title()} - {narx} so`m. ")