#ism = input( "ismingiz nima?\n>>>>")
#print("Assalomu aleykum" + " " + ism.upper())
#yosh = input("nima ish qilasiz?\n>>>>")
#joy = input("nechanchi kurs?\n>>>>")

#kurs = input("uylanganmisiz?\n>>>>")
#if kurs == "yes":qachon
#vazifalar
kocha = "Bog'bon"
mahalla = "sog'bon"
tuman = "bodomzor"
viloyat = "samarqand"
manzil = f"{kocha} , {mahalla} , {tuman} , {viloyat}"
print(manzil.upper() + "da istiqomad qilaman".upper())
print(kocha.upper()  + " ko'chasida " +  mahalla.upper()  + " mahallasi " + tuman.lower() + " tumanida " + viloyat.lower() + " viloyatida istiqomad qilib kelmoqdaman ".title())


#input  bilan ishlash
print(kocha.upper())
print(mahalla.lower())
print(tuman.title())
print(viloyat.capitalize())


#sonlar bilan ishlash

a = 50
b = 140
c = 5.6
temp = 36.6
print(type(b))
aholi_soni = 7_594_376_000
print("aholi_soni:", aholi_soni)

z, x, c = 20, -15, 10.2
q = z*c
print(q)
r = 185/9
print(r)

#CONSTANT QIYMATLAR HAQIDA o'zgaruvchilarni katta hariflar bilan yozilgan bo'lsa bu o'zgarmaydigan qiymatlar bo'ladi!!!!
radius = 25
PI = 3.14159
diametr = 2*radius
print("aylana uzunligi=", PI*diametr)


ism = "nuriddin"
yosh =  42# bu yerga strni qo'shilsa keyinchalik bu ishlashda muammo bolishi mumkin
xabar = ism + " " + str(yosh) + "yoshda"
print(xabar)
# matn va raqamni birlashtirib ko'rsatish uchun str"yosh" degan holda yoziladi
#t_yil = int(input("tug'ulgan yilingizni kiriting: "))
#yosh = 2025 - t_yil
#print("siz ", yosh, "yoshda ekansiz ")
#input bu har qanday ozgaruvchini matn holatda saqlaydi

 #type()- bu o'zgartuvchining   turini aniqlab beradi
#ishlab_chiqarilgan_yil =  int(input("MASHINANGIZ ISHLAB CHIQARILGAN YIL>>>> "))
#necha = 2025 - ishlab_chiqarilgan_yil
#print("mashina olganingizga", necha, " yil bo'libdi ")
#print(PI)

#shga_kirgan_yil = int(input("qachon ishga kirgansiz????? "))
#vaqt = 2025 - ishga_kirgan_yil
#print("siz ishni boshlaganigizga " , vaqt, " shuncha yil to'libdi!!! ")
# raqamlarni saqlashda matn, son, string ko'rinishda saqlash mumkin
# a = int("10")
# b = float("9")
# temp = str
mevalar = ["olma", "nok", "behi", "uzum"]
narxlar = [10000, 12000, 13000, 14000]
mevalar[0] = "xurmq" # bu faqat o'zgartiradi
print(mevalar)
mevalar.append('tarvuz')# faqat ro'yxatni oxiriga qo'shadi iinsert esa hohlagan yerga
print(mevalar)
mevalar.insert(0, "banan")
print(mevalar)
#delmaxsus operator malum elementni o'chirib tashlashda ishlatiladi
cars = []
cars. append("honda")
cars.append("shevrolet")
cars.append("kia")
print(cars)
del cars [0]
print(cars)
#cars. remove( " honda " ) #agar royxatda bir nechata o'xshash bolsa ham faqa t 1chisini chiradi
print(cars)
narxlar [0] = narxlar [0] + 1000
print(narxlar)
print(cars)
oshna = " MUZAFFAR "
print(oshna.title() + "qayerdasan? kelasanmi?")