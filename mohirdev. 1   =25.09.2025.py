from matplotlib import pyplot as plt

print("Hello world!")
print(10+25)
print("assalomu aleykum")
print ("""hello, World sdsdasdsadsadasd  
sdsadasa dsdsdsds""")
print ("men data analitika \n kursini urganmoqdaman")
print ('men albatta \n yaxshi kadr bo\'laman')
print (4**4) # sonni darajaga oshirish
print (30//7) # sonni bo'lganda qoldiqni tashlab yuborish
print (30/7) # qoldiq bilan ko'rsatish

# dars o'zgaruvchilar (variables)
# o'zgaruvchilar 2 ta so'zdan iborat bo'lmasligi kerak va raqam bilan boshlamaslik kerak _ ishlatish mumkin
# ism_sharif =  'maxkamov azizbek'
# sana 25/09/2025
# qo'pol qilib aytganda nom berish va nom bilan chaqirish keyinchalik ism fayldagi malumotni chiqar desa vhiqatib beradi
ism = "Azizbek"
yosh = 28
print (ism)
print ( yosh)
# veriable explore da o'zgaruvchilarni saqlanadi va uni ichida strings (str) bu matn  int  esa raqam size da nechtaligi

y = 2025
x = 1997
a = 2003
b = 2025
q = 2025
z = 2026

print (y - x)
print (b - a)
print (q - z)

print ((x + a )**2)

ism_familya = "maxkamov azizbek"
print(ism_familya)
sms = "azizbek"
sms = "makhkamov"
sms = "mukhtorjon ugli"
print (sms)

xabar = "hello world"
print(xabar)


#print("")
#radiuso = 15
#pi = 9.42477
#aylana_markazi = pi * radiuso**2

#print("radiusi" , radiuso, "ga teng aylananing yuzi=", aylana_markazi)
#radius = 5
#pi = 3.14159
#aylanma_yuzi = pi * radius**2
#print("Radiusi" , radius, "ga teng aylananing yuzi= ", aylanma_yuzi)
en = 4
uzunlik = 8
xona_kvadrati = en * uzunlik
print("xona_kvadrati" , en, "x", uzunlik, "ko'paytirsa natija", xona_kvadrati , "ga teng bo'ladi")
# class den nomlangan o'zgaruvchi yarating, unga biror qiymat bering va konsolga chiqaring (siz kutgan natija chiqdimi?)
# O'zgaruvchini class deb nomlash mumkin emas, sababi class bu maxsus kalit so'z.




print(ism_familya ,"☺")
print ("men yaxshi o'rganishim lozim " + "xona_kvadrati" , en, "x", uzunlik, "ko'paytirsa natija", xona_kvadrati , "ga teng bo'ladi" )

f = "Azizbek"
d = "Maxkamov"
print( f + d)
print( f +" " + d )
smile1 = " ☺ "


#f string usuli:
#ism = "Azizbek"
familya = "Maxkamov"
sharif = "muxtorjon ugli"
ism_sharif = f"{ism} {familya} {sharif}"
print(ism_sharif)


#ism = "James"
familya = "Bond"
print(f"Salom, mening ismim {familya}, {ism} {familya}!")
print("hello world")
print("hello \tworld")
print("hello \nworld")
print(smile1)


#STRING METODLAR
# o'zgaruvchiga agar kichik karif bilan saqlangan bulsa katta harif bilan uzgartirib saqlaydi
# lower bulsa bunda kichik harf bilan saqlaydi
# bu  metodlar qollanganda faqat natija o'zgaradi holos o'zgaruvchi ichida saqlab quyilgan malumot o'zgarmaydi
#upper())
#lower())
#title()) bu faqat bosh hariflarni katta qilib ko'rsatadi'
#
#ism = 'James'
#familya = 'Bond'
#sharif = 'rikardo'
ism_sharif = f"{ism} {familya} {sharif}"
ism_sharif = ism_sharif.upper()
print(ism_sharif.upper())
print(ism_sharif.lower())
print(ism_sharif.title())
meva = "    olma    "
#meva = ("        olma")
print(      meva    )
print(meva)
print("Men " + meva.lstrip() +  ism_sharif + " judayam yaxshi ko'raman ")
print("men " + meva.rstrip() + " judayam yaxshi ko'raman ")
print("men " + meva.lstrip() + " judayam yaxshi ko'raman ")
print("men " + meva.strip() + " judayam yaxshi ko'raman ")

#input
meva =  "anor"
print("bIZNING UYDA" + meva.lstrip() + " ko'chatlari juda ko'p, \nhosil beradi")
print("bizning uyda mevali " + meva.rstrip() + " ko'chatlari \tjuda ham ko'p ekilgan ")
# exit
print("bizning uyda juda ko'p " + meva.upper() + " ko'chatlari mavjud ".upper())
# agar kod yozilsa va qo'shtirnoq ichida biz o'zimiz kiritgan suzdan sung . upper qilinsa bu qavs ichiga to'liq tasir qiladi
print("bizning uyda juda ko'p " + meva.upper().rstrip()  + " ko'chatlari mavjud ")
#print("bizning uyda juda ko'p " + meva.title()  + " ko'chatlari mavjud ")


#input kamandasidan foydalanishda biz o'zimiz kiritadigan emas balki foydalanuvchi tomondan kiritiladi
#ism = input("qanday ish bilan mashg'ulsiz?")
#print("assalomu aleykum" + ism + "kuningizdan mamnunmisiz?")
#print("assalomu aleykum")
# qaytadan
#ism = input("ismingiz nima?")
#print(ism)

#print("isming nima?")
#name =  input()
#print("salom", name)
#
#
#ish = input("nima ish qilasiz?\n>>>")
#print("Salom, " + ish.upper()  )
#joy = input("qayerda o'qiysiz?)\t>>>")
#print(joy)
#joy = joy.upper()
#3print(joy)


#list
#haqida 1 ta o'zgaruvchi ichida kop malumotlartrni saq
mevalar = ["olma", "anor", "behi", "nok"]
#bularni chaqirib olishda tartib raqamiga boglanamiz [] shunday idex orqali foydalanamiz
narxlar = [12000, 13000, 14000, 15000] #narxlar ro'yxati (sonlar)'
print(mevalar[1], narxlar[1])# mevalarni 1 elementi narxlarni 1 elementi deb atasa ham bo'ladi
# bo'sh ro'yxat yaratish usuli sonlar = [] qilinsa consoldayam bu o'zgaruvchida o turadi
print(narxlar[1], mevalar[1])
#mevalar [0]da 1  chi meva chiqadi pythonda 0dan boshlab sanaladi -1 qilinsa oxiridagi mevani olib keladi

print(mevalar[1].upper())
print(mevalar[2].lower())
print(mevalar[2].title())
#agar mevalarni qiymatini o'zgartirmoqchi bo'lsa mevalar [0] = 'olxo'ri'
#mevalar[0] = "xurmo"
#print(mevalar)
#mevalar[-1] = "xurmo"
#mevalar[1] = 'xurmo'
#mevalar.append("uzum")
mevalar. insert(0, "xurmo")
