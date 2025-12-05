# from colorsys import yiq_to_rgb
#
# mexmon =  ['akram ','Bohodir','abdumalik','Muzaffar','mirfozil','nurmuhammad']
# #print("salom" , mexmon[2])#[] ichida belgilangan raqamdagi uzgaruvchiga ishlaydi
# for mexmonlar in mexmon:
#     #print("salom" , mexmon)
#     print(f"hurmatli do'stim {mexmonlar}, sizni 20 fevral kuni bolib o'tadigan  tadbirga taklif etaman")
#     print("hurmat bilan, Abdulqosimovlar oilasi!!!\n")# etiborliroq --------------------------------------------------------------------------------------------------------------bu joyda for dan keyingi uzgaruvchini yoziladi
# sonlar = list(range(1,41))
# print (sonlar)
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**3} ga teng bulsa kerak")
# #print (sum(sonlar))
# #sonlar_kvadrati = []#yangi bosh uzgaruvchi ochadi
# #for son in sonlar:
#  #   sonlar_kvadrati.append(son**4)#hamma raqamlarni 4 ni korsaatadi
# #print(sonlar_kvadrati)
# #dostlar =  []
# #print("5 ta eng yaqin dostingiz kim?")
# #for n in range(5):
#  #   dostlar.append(input(f"{n+1}-do'stlaringiz ismini kiriting:-->>>"))#n+1 da berilishini sababi ruyxat 1 dan boshlashi uchun agar n+2 bolganda 2 chi dost deb chiqarardi
# #print (dostlar)<<<<<<< -------------  shu yerda ishlab ketmasligi uchun # quyildi
#
#  ################ yangi mavzu <<<<<<  if - elif - else  >>>>. faqat 1 ta shartni tekshirsa buladi holos
#
# son = 50
# if son<0:
#      print("manfiy son")
# else:
#      print("musbat son")
# yosh =  int(input('yoshingiz nechida?'))
# if yosh<14:
#     print("sizga kirish bepul.")# orada yana qoshimcha qilib elif qilib qushimcha qilsa buladi
# elif yosh<=18:
#     print("sizga kirish 10000 so\'m")
# elif yosh >30:
#     print("sizga kirish 50000 so\'m")
# else:
#     print("sizga kirish 20000 so\'m")
#
#
#
#
#
#
#
#     # bus usulni qisqaroq usuli bor kodlarni qayta qayta yozmaslik uchun'
# yosh = int(input('yoshingiz nechida?'))
# if yosh<=18:
#     narh = 0
# elif yosh<=30:
#     narh = 150000
# elif yosh<=50:
#     narh = 250000
# elif yosh<=90:#uje 90dan detasi 1 somga chiqardi 90 bilan teng yoki kichik
#     narh = 100000
# else:
#     narh =1
# print(f"sizga kirish {narh} so'm")# shu usulda ozroq yozsa buladi kamchilik faqat 1 ta
#
#
# # or operatori
# #+++++++++++++++++++++++++++++++
#
# kun = input("Bugun nima kun?")
# if kun.lower() == "shanba" or kun.lower() == "yakshanba":
#     print("bugun uyga vodiyga borish kuni")
# else:
#     print("bugun uchrashuvga borish kuni!ish")
#
# day = input("Bugun nima kun?")
# harorat = float(input("havo harorati qanday?"))# AND BILAN OR NING FARQI UNDA 2 LA SHART HAM TUGRI BOLISHI KERAK
#
# # if day.lower() == "shanba" or day.lower()== "yakshanba" and harorat >=30:
# #     print("Chomilib bir dam olaylik!!!")
# # elif day.lower() == "shanba" or day.lower()=="yakshanba" and harorat <30:
# #     print("uyda miriqib uxlaymiz!!!!")
#
#
#
#
#
# #guvohnoma =input("haydovchilik guvohnomangiz bormi?"))
# #if guvohnoma = yoq:
#  #   print("sizga shtraf solamiz!!!")
# #else guvohnoma = bor:
#  #   print("ketishingiz mumkin!!!")
#
#
#
# #BOOOLEAN -------------------- YANGI MALUMOTLAR TURI
from math import trunc

# narh = 15000# mijor 15 minga ovqat sotib oldi
# choy = True# mijoz choy ham oldi
# salat = True#False#mijoz salat oldi
#
# if choy and salat:#agar mijooz salat ham choy ham olgan bulsa
#     narh = narh + 10000#narxga 10000 sum qushamiz
# elif choy or salat:#agar choy yoki salat olgan bulsa
#     narh = narh + 5000# narhga 5000 som ham qushamiz
# print(f"Jammi {narh} so\'m")#yakuniy barxni chiqaramiz
#
# menyu = ['osh', 'qozonkabob', 'manti', 'lag\'mon', 'shashlik', 'norin', 'somsa']
# ovqat = input('Nima yeysiz?>>')
# narx = (15000, 20000, 30000, 40000, 50000, 60000, 45000)
# # if ovqat.lower() in menyu:
# #     print('Buyurtma qabul qilindi!')
# # else:
# #     print('Afsuski bizning oshxonada bunday ovqat yo\'q!!!')
#     # bizda keyingii kod not in bulib buni ishlatilsa buyurtma pastga afsuski esa tepaga chiqadi
# if ovqat.lower() not in menyu:
#     print('Afsuski bizning oshxonada bunday ovqat yo\'q!!!')
# else:
#     print('Buyurtma qabul qilindi!')
# menyu = ['osh', 'qozonkabob', 'manti', 'lag\'mon', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'qozonkabob', 'manti', 'lag\'mon']#biz qolda yozdik
# for taom in buyurtmalar:
#     if taom in menyu:
#         print(f'menuda {taom} bor')
#     else:
#         print(f'Kechirasiz, menuda {taom} yo\'q')# ikkita ruyxatni bir bilan solishtirildi
# menyu = ['osh', 'qozonkabob', 'manti', 'lag\'mon', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'qozonkabob', 'manti', 'lag\'mon']  # biz qolda yozdik
#
#     ###############################print(f'menuda {len(buyurtmalar)} ta taom bor')
#
#
# menyu = ['osh', 'qozonkabob', 'manti', 'lag\'mon', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'qozonkabob', 'manti', 'lag\'mon']  # biz qolda yozdik
# if buyurtmalar:
#     for taom in buyurtmalar:
#        if taom in menyu:
#           print(f'menuda {taom } bor')
#     else:
#           print(f"kecirasiz menuda {taom} yo\'q")# menuda 4 ta taom bor javo shunaqa chiqadi
# else:
#     print("savatchangi bo\'sh")

# talaba_0 = {
#     'ism':'alijon',
#     'familya':'shamsiyev',
#     'yosh':'22',
#     'fakultet':'matematika',
#     'kurs': 4 # etibor beramiz raqamga " shart bo;'lmadi
#      }
# print(talaba_0.items())#dict_items([('ism', 'alijon'), ('familya', 'shamsiyev'), ('yosh', '22'), ('fakultet', 'matematika'), ('kurs', 4)]) natija shu tartibda juda tushunarsiz chiqdi
# for key, value in talaba_0.items():
#     print(f"kalit: {key}")
#     print(f"qiymat: {value} \n")#key va value da yozishda etiborli bolishkerak adshtirishi mumkin
# # -----------------------------------Lugat so'zlar  dictionary
# car_0 = {'model':'ferrari', 'rang':'qizil'}# rangning : qiymati qizil
# print(car_0['model'])
# print(car_0['rang'])
# en_uz = {'apple':'olma', 'apricot':'o\'rik', 'banana': 'banan'}
# print(en_uz['apple'])# shu uslubda lugat yaratdik
# mevalar = {'olma':'10000', 'o\'rik':'15000', 'banan': '25000'}
# print(f" olma narhi {mevalar['olma']} so'm")
# talaba_0 = {'ism':'murod olimov', 'yosh':'24', 't_yil':2000}
# print(f"{talaba_0['ism'].title()},\
#       {talaba_0['t_yil']}- yilda tug'ilgan,\
#       {talaba_0['yosh']} yoshda")
# # yangi kalit so'z bemalol qo'shish mumkin
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'informatika'
# talaba_0['ism'] = 'abdulloh'# ismni o'zgartirib quydi
# print(talaba_0)
# #bo'sh lugat yaratish yoli
# talaba_1 = {}# shu usul bilab bosh lugat yaratiladfi
# talaba_1['ism'] = ' abdusator abdusatorov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 21
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
#       #natija Talaba  Abdusator Abdusatorov 3-kurs shu ko'rinishda bo'ladi
# talaba_1['kurs'] = 4                                                                      #yuqoridagi talaba _1 ga o'zgartirishlar kiritish yo'llari
#
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")#Talaba  Abdusator Abdusatorov 4-kurs natija shu koprinishda buladi



#__________________ kalit so'z qiymatini o'chirib tashlash del orqali amalga oshiriladi
# talaba_0 = {'ism': 'murod olimov', 'yosh': '24', 't_yil': 2000}# natijada {'ism': 'murod olimov', 't_yil': 2000} shu korinishda boladi
# del talaba_0['yosh']
# print(talaba_0)
# en_uz = {'apple':'olma', 'apricot':'o\'rik', 'banana': 'banan'}
# del en_uz['banana']
# print(en_uz)
# #luga'tlar juda katta bolsa' und aelementlar kop bolsa
# #{}qavs yordamida amalga oshiriladi
#
#
# #__________________________________get metodi haqida
# telefon = {#--------------------------------------------------------------------------------------------------------pastroqda huddi shu uzgaruvchini ishga solingan
#     'ali': 'iphone X',
#     'vali':'samsung 22',
#      'olim':'mi 13 pro',
#     'husan':'lg',
#     'xolid':'iphone X',
#      'nodir':'samsung 22'
#       }
# for k, q in telefon.items():
#     print(f"{k.title()}ning telefoni {q}")
# #     Alining telefoni iphone X
# #     Valining telefoni samsung22
# #     Olimning telefonimi13pro
# # Husanning    telefoni lg Javoblr huddi shunday chiqadi
# phone = telefon.get('hasan', 'Bunday odam mavjud emas')
# print(phone)
# meva = en_uz.get('apple', 'o\'rik')
# print(meva)

#__________________.keys()  metodi har bir kalitni qaytaradi
# maxsulotlar = {
#     'olma':10000,
#     'anor':25000,
#     'behi':9000,
#     'uzum':15000,
#     'shaftoli':28000
# }
# # print(maxsulotlar.keys())
# # print('do\'kondagi maxsulotlar')
# # for maxsulot in maxsulotlar.keys():#agar lugatga in maxsulotlar desa ham chiqadi yani topib beradi
# #     print(maxsulot.title())
#
# bozorlik = ['anor','behi','uzum', 'LIMON']
# for maxsulot in maxsulotlar:
#     if maxsulot in bozorlik:
#         print(f"{maxsulot.title()} {maxsulotlar[maxsulot]} so'm")#maxsulot → string ("non", "cola" kabi) maxsulotlar → dict ({"non":5000, "cola":9000"} kabi) Bu — string ichidan dictionary bilan index olishga urinish, bu esa xato.
#
# for buyum in bozorlik:
#     if buyum not in maxsulotlar:
#         print(f"iltimos do'konigizga {buyum} ham olib keling!!!")
# print("Do'konigizdagi maxsulotlar")
# for maxsulot in sorted(maxsulotlar):#sorted yordamida faqat kalitlarni tartiblab chiqaradi
#     print(maxsulot.title())
#
# print(telefon.values()) # shu pasdagi royxatdan faqat kalitni chiqardi
# # 'ali': 'iphone X',
# # 'vali': 'samsung 22',
# # 'olim': 'mi 13 pro',
# # 'husan': 'lg'
# # }
# print('foydalanuvchilar quyidagi telefonlarni ishlatadi:')
# for tel in set(telefon.values()):#set yordamioda bir nechta birxillardan faqat 1 tadan qoldi
#     print(tel)
# toys = {"ball", "car", "lamop", "ball", "car"}# birxillardan faqat 1 tadan korsatdi
# print(toys)
# python_words = {
#     'integer':'butun son',
#     'float':'o\'nlik son',
#     'boolean':'mantiqiy qiymat',
#     'for':'biror amalni qayta- qayta bajarish sikli',#-----------------------------------------------------------------------------------------------------------------------------<<<<< takrorlashga uxshagan yaxshi eslatmalar
#     'if':'shartlarni tekshirish operatori'
# }
# for key, value in sorted(python_words.items()):
#     print(F"{key.title()} - {value}")
# davlatlar = {
#     "o'zbekiston":"toshkent",
#     "AQSh":"washington d.c.",
#     "rossiya":"moskva",
#     "tojikiston":"dushanbe",
#     "qirg'iziston":"bishkek",
#     "singapur":"sxungapur",
#     "italiya":"rim"
# }
# print("Dunyo davlatlari:")
# for davlat in sorted(davlatlar):
#     print(davlat.upper())# shu joyda davlatlar desam ishlamadi menda davlatlar lugat yani dict korinishda edi shu joyda menda yechim to'g'ri chiqarish uchun uni davlat shakilda ishlatildi
#
# print('\nDavlatlarning poytaxtlari')
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())
# coutry = input('Qaysi davlatning poytaxtini bilishni hohlaysiz?:').lower()
# capital = davlatlar.get(coutry)
# if capital==None:
#     print('Kechirasiz bizda bu davlat haqida malumot yo\'q!')
# else:
#     print(f"{coutry.title()} ning poytaxti {capital.title() } shaxri")#title bizda javobning shriflarini katta yoki kichik yoki bosh harifi katta bolishini amalga oshiorib berdi
# menu = {
#     'osh':20000,
#     'lagmon':30000,
#     'manti':25000,
#     'shashlik':16000,
#     'somsa':12000
# }
# print('3 ta taom buyurtma bering!!!')
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom").lower())
#
# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} {menu [buyurtma]} so'm")
#     else:
#         print(f"kECHIRASIZ, BIZDA {buyurtma} yo'q.")

#__________________________________________________NEsting haqida nimadir ichida nimadirni saqlash_________________++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++qaysi biring ketsang ketlaring zayka qildilaring
car0 = {
    'model':'honda',
    'rangi':'oq',
    'yil':2017,
    'narx':8000,
    'km':140000,
    'karobka':'avtomat'
}
car1 = {
    'model':'testla',
    'rangi':'qora',
    'yil':2018,
    'narx':12000,
    'km':11000,
    'karobka':'avtomat'
}
car2 = {
    'model':'porsh',
    'rangi':'ko\'k',
    'yil':2019,
    'narx':18000,
    'karobka':'mexanika'
}
car = car2#shu joydagi raqamni uzgartira kelib chiqaveradi
print(f"{car['model'].title()},"
      f"{car['rangi']} rangi, "#bizda shu joyda rang deb yozib quyganim uchun hato krlib chiqdi bizda esa rangi edi
      f"{car['yil']}- yil, {car["narx"]}$")
#endi biz osonroq uslubdan foydalanamiz
# buning uchun bir 1 chi ruyxat yaratamiz
cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()},"
          f"{car['rangi']} rangi, "
          f"{car['yil']}- yil, {car['narx']}$ "

    )# qoshtirnoq va qavsga etiborlirroq bulgan holda amalga oshirish kerak
# endi lugatlarga alohida murojat qilsih uchun
print(cars[0]['model'])#honda javob shu tarzda buldi endi biz alohida alohida qilib javob olish uchun shu tarzda yondashamiz
print(f"{cars[2]['model'].lower()}"
      f"{cars[2]['rangi'].upper()}")#porshKO'K javob shu korinishda buldi

malibus = []
for n in range(10):
    new_car = {
        'model':'malibu',
        'rang':'none',#rangi noaniq None
        'yil':2020,
        'km':0,
        'narx':19000,
        'karobka':'avtomat'
    }
    malibus.append(new_car)
    #endi biz o'zgartirishlarni kiritamiz !!!!
for malibu in malibus[ :3]:
    malibu['rang']='qizil'
for malibu in malibus[3:6]:
    malibu['rang']='qora'
for malibu in malibus[6:]:
    malibu['rang']='kulrang'
    malibu['karobka']='mexanika'
for malibu in malibus:# shu joyi vapshe zor chiqdi ______________________________ajoyib yechim bilan ishlandi

    if malibu['karobka'] == 'avtomat':
        malibu['narx']=40000
    else:
        malibu['narx']=33000
        print(malibus)
dasturchilar = {
    'ali': ['python', 'c++'],
    'husan':['c++', 'java'],
    'vali':['python', 'c++', 'java'],
    'nur':['python', 'java']
}
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())
 # Ali
        # quyidagi
        # dasturlash
        # tillarini
        # biladi:
        # PYTHON
        # C + +
        #
        # Husan
        # quyidagi
        # dasturlash
        # tillarini
        # biladi:
        # C + +
        # JAVA
        #
        # Vali
        # quyidagi
        # dasturlash
        # tillarini
        # biladi:
        # PYTHON
        # C + +
        # JAVA
        #
        # Nur
        # quyidagi
        # dasturlash
        # tillarini
        # biladi:
        # PYTHON
        # JAVA ---------------------------------------javoblar shu tarzda chiqdi


# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#             print(f'{til.upper()} ', end=' ')#oxirida keyingi qatorga otmasda qilib beriladi
    # PYTHON
    # C + +
    # Husan
    # quyidagi
    # dasturlash
    # tillarini
    # biladi:
    # C + +  JAVA
    # Vali
    # quyidagi
    # dasturlash
    # tillarini
    # biladi:
    # PYTHON
    # C + +  JAVA
    # Nur
    # quyidagi
    # dasturlash
    # tillarini
    # biladi:
    # PYTHON
    # JAVA bu holatda oradan katta joy tashlamay zichroq qilib amalga oshiradi
# hamkasblar = {
#     'ali':{'familya':'valiyev',
#            'tyil':1999,
#            'malumot':'oliy',
#             'tillar':['python', 'java']
#            },
#     'husan':{'familya':'nuriddinov',
#             'tyil':1999,
#             'malumot':'oliy',
#             'tillar':['python', 'c++']
#              },
#     'vali':{'familya':'jabborov',
#             'tyil':1999,
#             'malumot':'oliy',
#             'tillar': ['python', 'htm']
#             },
#     'nur':{'familya':'shamsiyev',
#             'tyil':1993,
#             'malumot':'oliy',
#             'tillar':['C++', 'java']# skob va qavslar notogri quyilsa topomay qiynalinadi etibor kerak
#            }
# }
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familya'].title()},"
#           f"{info['tyil']} - yilda tug'ulgan."
#           f"malumoti:{info['malumot']}.\n"
#           "quyidagi dasturlash tillarni biladi:")
#     for til in info['tillar']:# shu oxirgi 2 qatorda dasturlash tillari haqida buladi
#         print(til.upper())# shu orqali har bir malumot alohida alohida bulib chiqdi
#
#
#

#________________________________________________________________________while sikli yangi mavzu    ______input va while
# ism = input("ismingiz nima?")
# print(ism)# shu joyda etiborliroq yani ism deb va ismni print qilinganda ismingiz nima deb savol beradi va bu savolga javob bersangiz shu o'zgaruvchini qiymatini o'zingiz berasiz
# savol = f"salom, {ism.title()}. yoshingiz nechida?"
# yosh = input(savol)# shu tarazda ozingiz javob berasiz va uni input saqlab beradi
# #yoshni input dunksiyasi string holatda saqlaydi va aslida raqam integer bolishi kerak edi lekin input sting shakilda ishladi
# # endi uni integerga o'tkazish uchun
# yosh = int(yosh)# shu shakilda otadi va keyingida bu raqamlar ustida matemetik amallarni bajarsa buladi
# heiht = input("bo'yingiz necha metr?")
# heiht = float(heiht)# bushakilda ham float o'nlik son shakliga o'tkazib olindi
# # hozirgacha bajarilganda shartlar faqat 1 marta amalga oshirildi endi bu shartlarni while yordamida (toki) yordamida belgilangan shartlar bajarilmaguncha qayta qayta amalga oshiraveradi



# while
# son =  1# songa 1 qiymatini beramiz
# while son <=5:# toki son 5 dan kichik yoki teng ekan
#     print(son, end='')# sonni konsolga chiqaramiz
#     son += 1# songa 1 ni qo'shamiz
# print('dastur tugadi')# 1dan 5 gacha sanaydigan dastur yasaldi


# while va input
# print("kiritilgan sonni kvadratini qaytaruvchi dastur!")
# savol = "istalgan sonni kiriting "
# savol += "(dasturni tugatish uchun 'exit' deb yozing): "#+= istalgan sonni kiriting deb dasturni tugatish degan matinni ham qo'shdik
# qiymat = ''
# while qiymat != 'exit':# toki qiymat exitga ! teng bolmasa != teng bo'lmasa deman manoda ishladi
#     qiymat = input(savol)#biz foydalanuvchidan qiymat kiritishni soraymiz
#     if qiymat != 'exit':    # agar qiymat foydalanuvchi yuklagan ga teng bolmasa
#         print(float(qiymat)**2)# unda biz bu qiymatni kvadratini hisoblaymiz
# print('dastur tugadi')# exit deb yozmaguncha bu uyin tugamaydi

# uyin tugatish uchun shartlar kop boladi bunday shartlarni tekshirish uchun iroralar buladi ularni flaglar deyiladi

# print("kiritilgan sonni kvadratini qaytaruvchi dastur!")
# savol = "istalgan sonni kiriting "
# savol += "(dasturni tugatish uchun 'exit' deb yozing):"
# ishora = True #qiymat = ''# shui qismni orniga biz ishora deb qushib ketdik
# while ishora:# ishora true bulguncha kodlar bajarilaveradi
#     qiymat = input(savol)#
#     if qiymat == 'exit':    #
#         ishora = False
#     else:
#         print(float(qiymat)**2)#
# print('dastur tugadi')#

# break (for) va ()while >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# print("kiritilgan sonni kvadratini qaytaruvchi dastur!")
# savol = "istalgan sonni kiriting "
# savol += "(dasturni tugatish uchun 'exit' deb yozing):"
#
# while True:# abadiy tsikl bolib qoladi
#      qiymat = input(savol)#
#      if qiymat == 'exit':    #
#          break#tsiklni toxtatib beradi
#      else:
#          print(float(qiymat)**2)#
# print('dastur tugadi')


#break haqida+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#    print(f"{son} ning kvadrati {son**2} ga teng")




#continue haqida
#breakni teskarisi
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")# natijda 5 ni tashlab ketdi unchalik tushunarli emas mujmal




   #endi continue va wile haqida bir biri bilan ishlatish
# son = 0
# while son < 10: # toki son 10dan kichkina ekan 1 ni qushadi
#     son += 1
#     if son%2!=0:#% sonni qoldi borligini tekshiradigan aperaton hisoblanadi # sonni qoldigi bolmasa yana boshiga qaytib ketadi
#         continue
#     else:
#         print(son)#sonni qoldigi bolsa uni consolga olib chiqadi
#
#
# son = 0
# while son < 10:
#     son += 1
#     if son%2==0:#shu ozgartirish orqali endi toq sonlani korsatadi
#         continue
#     else:
#         print(son)


#infinite loop bu abadiy sikl bolib u mantiqiy hato sababli kelib chiqadi
# son = 0
# while son < 10:# shu joyda son>0 qilib quysa ham hatolik kelib chiqadi
#     #son +=1 shu qism qolib ketgani uchun hatolik
#     if son%2!=0:#shu ozgartirish orqali endi toq sonlani korsatadi
#         continue
#     else:
#         print(son)# buni tuxtatish uchun tepadagi qizilni bosiladi yoki ctrl +c ni bosiladi






# while va ro'yxatlar bilan ishlash(ruyxatni toldirish)
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# ismlar = []
# n=1# ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}- do'stingiz ismini kiriting:"
#     ism = input (savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ishm qo'shasizmi? (ha/yo'q)")
#     n+=1
#     if takrorlash != 'ha':
#         break
#
#
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())
#while sikli yordamida lugatni toldiramiz
# print("Do'stlaringiz yoshini saqlaymiz:")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("do'stingiz ismini kiriting:")
#     yosh = input(f"{ism.title()} ning yoshini kiriting:")
#     dostlar[ism] = int(yosh) # bu yerda ism kalit yosh esa qiymat bo'ladi
#
#     javob = input("yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False
#
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

#while sikl yordamida birnechta qiymatni o'chirib tashlash'   agar ro'yxatning ichida 3 ta nexia qiymati bo'sa remove faqat 1 tasini o'chirtib tashlaydi
# cars = ['laseti', 'nexia', 'kobalt', ' jentra', 'nexia', 'tiko']# shu joyda qoshimcha qili tagidan car deb yoziladi
# while 'nexia' in cars: # shu buyruq tufayli carsdagi hamma nexialar o'chib ketdi
#     cars.remove('nexia')
# print(cars)

# shu joyda qoshimcha qili tagidan car deb yoziladi

# cars = ['laseti', 'nexia', 'kobalt', ' jentra', 'nexia', 'tiko']# shu joyda qoshimcha qili tagidan car deb yoziladi
# car = 'laseti'
# #'nexia', 'kobalt', ' jentra', 'nexia', 'tiko'] bu esa natija
# while car in cars: #
#     cars.remove(car)
# print(cars)

# talabalar = ['hasan', 'abu', 'zuhriddin', 'nodir', 'javlon']# talabalar ustida qandaydir amal bajarib va bu elemetlarni boshqa ruyxatga yoki lugatga o'tkazib ko'ramiz
# baxolangan_talabalar = {}
# while talabalar:#toki talabalr degar ro'yxatning ichida 1 ta bolsaxam element bulsa pasdagi 4 qator sikilni bajar degan buyruqa
#     talaba = talabalar.pop()# bu ozgaruvchi ichidagi 1 ta elentni sugurib (pop) odatda ruyxatydagi oxirgi elentdan boshlaydi
#     baho = input(f"{talaba.title()} ning baxosini kiriting:")# o'qituvchi talabani baxosini kiritadi va bu baho boho uzgaruvchisiga joylanadi
#     print(f"{talaba.title()} baxolandi")
#     baxolangan_talabalar[talaba] = int(baho)#integer bu baholar butun sonda bulgani uchun
# #    Javlon ning baxosini kiriting:5
# # Javlon baxolandi
# # Nodir ning baxosini kiriting:4
# # Nodir baxolandi
# # Zuhriddin ning baxosini kiriting:3
# # Zuhriddin baxolandi
# # Abu ning baxosini kiriting:4
# # Abu baxolandi
# # Hasan ning baxosini kiriting:5
# # Hasan baxolandi                -                ------- natija shu korinishda buldi
# print(baxolangan_talabalar)  # bu esa natija {'javlon': 4, 'nodir': 5, 'zuhriddin': 5, 'abu': 45, 'hasan': 5}


#====================================AMALIYOT
# savat = []# shu joyda {} belgisi sababli append hato berdi chunki u faqat lit uchun ishlaydi u joyda [] quyish kerak{} esa faqat lug'at uchun ishlaydi
# while True:
#     mahsulot = input("savatga maxsulot qo'shing:")
#     savat.append(mahsulot)
#     javob = input("yana mahsulot qo\'shasizmi?(ha/yo\'q)")
#     if javob != 'ha':
#         break
# buyurtmalar = ['olma', 'nok', 'sabzi', 'uzum', 'hurmo']
# mahsulotlar = {'olma':15000,
#                'behi':12000,
#                'qovun':16000,
#                'uzum':19000,
#                'hurmo':14000}
#
# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh = mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()} - {narh} so'm")
#     else:
#         print(f"Bizda {buyurtma} yo'q")
#     Hurmo - 14000 so'm #NATIJALAR
#     Uzum - 19000
#     so
#     'm
#     Bizda
#     sabzi
#     yo
#     'q
#     Bizda
#     nok
#     yo
#     'q
#     Olma - 15000
#     so
#     'm

# yangi mavzu __________________FUNKSIYA 11.25 malum bir kodlarning yigindisi shu qismga kelgan da ## belgisi yuqoridagi kodlarni ishlatilganda degan manoda sal tepparoqdagi degan manoda ishlatdim
# def salom_ber():
#     """salom beruvchi funksiya"""#shu ikki qator funksiyani badani'''funksiya haqida malumot
#     print("Assalomu aleykum")
# salom_ber()#consolda salom berdi
# #misol sifatida Print ham bir funksiya
# def salom_ber(ism):#foydalanuvchidan talab qilinadigan qiymat parametr deyiladi (ism)
#     """foydalanuvchi ismni qabul qilib, unga salom beruvchi funksiya"""#shu ikki qator funksiyani badani'''funksiya haqida malumot
#     print(f"Assalomu aleykum, hurmatli {ism.title()}!")
# salom_ber('hasan')
# salom_ber('abu')
# Assalomu aleykum, hurmatli Hasan!# bu esa natija shu tariqada chiqadi
# Assalomu aleykum, hurmatli Abu!# agar bunga qiymat bermasa eror chiqadi salom ber() shu tariqada yozilsa

# print(print.__doc__)# shu haqida maulot chiqadi
#
#
#
# def toliq_ism(ism, familya):#
#     """foydalanuvchi ismni va familyasini jamlab chiqaruvchi funksiya"""# shu qismni tushunarli qilib yozish kerak chunki keyinchalik kerak bulib qolsa salom_ber( shu tariqada konsolda yozilganda malumot qismi korinadi va ishlatishga qulay buladi va buni dog string deyiladfi
#     print(f"foydalanuvchi ismi: {ism.title()}!\n"
#          f"foydalanuvchi familyasi: {familya.title()}")
#
# toliq_ism('olim', 'hakimov')#argument
# foydalanuvchi ismi: Olim!
# foydalanuvchi familyasi: Hakimov shu natija


# def yosh_hisobla(ism, tugulgan_yil):
#     """Foydalanuvchi ismini hisoblaydigan funksiya"""
#     print(f"{ism.title()} {2020- tugulgan_yil} yoshda")
#
# #yosh_hisobla('olim', 1997)#agr shu joyda birinch yilni yozsa xato chiqadi
# # bu esa natija shu shakilda chiqdi
# #agr shu joyda birinch yilni yozsa xato chiqadi buni oldini olish uchun alohida kamanda beriladi ---------->>>>>>>>>>>>>>>>>>>>>>
# yosh_hisobla(tugulgan_yil= 1997, ism= "olim")# shu uslub orqali aniq qiymat berilsa endi hato chiqmaydi yani parametrga aniq argument berildi
# ##toliq_ism(familya='hakimov', ism='olim')#argument yuqoridagi funksiyada ham shunday shu tarzda shunaqa qilib argumetlar berilsa qaysi birini oldin sorasa ham, javob chiqadi

# def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
#     """foydalanuvchi tugilgan yilidan uning yoshini hisoblaydi"""
#     print(f"siz {joriy_yil-tugilgan_yil} yoshdasiz!")
#
# #yosh_hisobla(1995, 2020)
# #yosh_hisobla(1993) # ikkalasini amalga oshirsa ham hato chiqmaydi chunki biz joriy yilga standart qiymat kiritib keltdik shu sabab muammo bulkmaydi

#+++++++++++++++++++++++++++++ shu dars buyicha vazsifalar
# def salom_ber(ism):
#     """foydalanuvchidan ism qabul qilib unga salom beradigan funksiya yaratamiz"""
#     print(f"assalomu aleykum {ism.title()}!")
# salom_ber('olim')# ishladi(olim shu joyda argument)
# print(salom_ber.__doc__)#foydalanuvchidan ism qabul qilib unga salom beradigan funksiya yaratamiz natija shu korinishdda buli bundan maqsad funksiya haqda malumot olish uchun bladi
# def salom_ber_yil(ism, yosh):
#     """salom berib yoshni ko'rsatadigan funksiya"""
#     print(f"{ism.title()} {2025-yosh} yoshda")
# salom_ber_yil('ali', 1997)# muvaffaqiyatli amalga oshdi
# def kvadrat(son):
#     """foydalanuvchidan son olib uni kvadratini konsolga olib chiqadigan funksiya"""
#     print(f"{son} ning kvadrati {son**2} ga, kubi {son**3} ga teng!!!")
# kvadrat(5)#5 ning kvadrati 25 ga, kubi 125 ga teng!!! bu esa natija

#3333333
# def juftmi(son):
#     """foydalanuvchidan son olib uni  toq yoki juftligini konsolda korsatadigan funksiya"""
#     if son%2:
#         print(f"{son} toq son")
#     else:
#         print(f"{son} just son")
# juftmi(20)



# def solishtirish(x,y):
#     """ikki sonni solishtirish funksiyasi"""
#     if x > y:
#         print(f"{x}>{y}")
#     elif x<y:
#         print(f"{x}<{y}")
#     else:
#         print(f"{x}={y}")
# solishtirish(15,42)
# solishtirish(12453,453511)


#foydalanuvchidan x va y sonlarni olib, x^y ni konsolga chiqaruvchi funksiya yozing
# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
# def daraja(x,y=2):
#     print(f"{x} ning {y}- darajasi {x**y} ga teng")
#
# daraja(2, 2)#2 ning 2- darajasi 4 ga teng natija



# foydalanuvchidan son qabul qilib  sonni 2,3,4, va 5 ga qoldiqsiz bulinishini tekshirish
# funksiya yozing
# natija konsolga chiqarish("15 soni 3 ga qoldiqsiz bo'linadi" ko'rinishida)

# def bolinish_alomatlari(son):
#     for n in range(2,11):
#         if not son%n:
#             print(f"{son} {n} ga qoldiqsiz bo'linadi")
#
# bolinish_alomatlari(20)
#
# def bolinish_belgisi(son):
#     for n in range (1,20):
#         if not son%n:
#             print(f"{son} {n} ga qoldiqsiz bo'linadigan son")#==================================================================== shu formulani aniqlashtirish kearak
# bolinish_belgisi(20)




############################################ bu yangi mavzu funksiyada qiymat qaytarish

# def toliq_ism_yasa(ism, familya):
#     """toliq ism qqaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familya}"
#     print(toliq_ism)
# toliq_ism_yasa('ali', 'husanov')


# def toliq_ism_yasa(ism, familya):
#     """toliq ism qqaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familya}"
#     return toliq_ism#toliq ozgaruvchini qiymatini qaytaradi bu funksiyani ichida qolib ketadi
#
# talaba = toliq_ism_yasa('ali', 'husanov')
# print(talaba)   # bu joyda faqat print qilsa javob chiqadi ichida saqlanib turadi tipa ozgaruvchiga uxshab


# def toliq_ism_yasa(ism, familya):
#     """toliq ism qqaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familya}"
#     return toliq_ism#toliq ozgaruvchini qiymatini qaytaradi bu funksiyani ichida qolib ketadi
#
# talaba = toliq_ism_yasa('ali', 'husanov')
# talaba1 = toliq_ism_yasa('jasur', 'buriddinov')
# print(f"darsga jkelmagan talabalar: {talaba1} va {talaba} ")
# print(f"{talaba1}  darsga kechikib keldi")   # bu joyda faqat print qilsa javob chiqadi ichida saqlanib turadi tipa ozgaruvchiga uxshab




# def toliq_ism_yasa(ism, familya, otasining_ismi=''):# otasining ismiga standart qiymat berib quydik otasining ismiga qiymat berildi agar bulmasa bush qolaveradi
#     """toliq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familya}"
#     else:
#         toliq_ism = f"{ism} {familya}"
#     return toliq_ism.title()# agar return ichkariroq surilib qolsa natinada none bulib qolishi mumkin
# talaba1 = toliq_ism_yasa('ali', 'husanov')
# talaba2 = toliq_ism_yasa('jasur', 'buriddinov', 'abrorovich')
#
#
# print(f"darsga kelmagan talabalar: {talaba1} va {talaba2 }")



# def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):#bizda ozgaruvchiga  hech qanday qiymat bermaslikni hohlasak biz shunda NOne deb ketishinmiz mumkin
#     avto = {'kompaniya': kompaniya,
#             'model': model,
#             'rangi': rangi,
#             'karobka': karobka,
#             'yili': yili,
#             'narhi': narhi}
#     return avto
# avto1 = avto_info('GM', 'nexia', 'qora', 'mexanika', 2020)
# avto2 = avto_info('BMW', 'G30', 'oq', 'avtomat', 2022 )
# avto3 = avto_info('mers', 'banan', 'kuilrang', 'avtomat', 2024)
# avtolar = [avto1, avto2, avto3]
# print(f"online bozordagi mavjud mashinalar:")
# for avto in avtolar:
#     if avto['narhi']:
#         narhi = avto['narhi']
#     else:
#         narhi = "Noma'lum"
#     print(f"{avto['rangi']} {avto['model']}. Narhi: {narhi}")#natijalar quyidagicha
#     # online
    # bozordagi
    # mavjud
    # mashinalar:
    # qora
    # nexia.Narhi: Noma
    # 'lum
    # oq
    # G30.Narhi: Noma
    # 'lum
    # kuilrang
    # banan.Narhi: Noma
    # 'lum

#endi funksiyadan ruyxat qaytarish ko'rib chiqamiz
#range dan qaytganlarni ruxatga olish uchun listdan foydalaniladi list(range(0,10)) shaklida foydalaniladi
# def oraliq(min,max):#
#     sonlar = []# shu ruyxat icjhioga joylanadi
#     while min < max:#toki minimum maksimumdan kichik ekan sonlarni ichiga minimumni qushiladi
#         sonlar.append(min)
#         min += 1 #minimumga 1 ni qushdik 0+1=1, 1+1=2........
#     return sonlar
# print(oraliq(10,20))
# print(oraliq(0,33))
# print(oraliq(100,120))



# def oraliq(min,max,qadam=2):#
#     sonlar = []# shu ruyxat icjhioga joylanadi
#     while min < max:#toki minimum maksimumdan kichik ekan sonlarni ichiga minimumni qushiladi
#         sonlar.append(min)
#         min += 2 #minimumga 2 ni qushdik 0+1=1, 1+1=2..shu shakilda buladi va qadam 2 bilan harakatlanadi......
#     return sonlar
# print(oraliq(10,20))
# print(oraliq(0,33))
# print(oraliq(100,120))


# def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):#bizda ozgaruvchiga  hech qanday qiymat bermaslikni hohlasak biz shunda NOne deb ketishinmiz mumkin
#     avto = {'kompaniya': kompaniya,
#             'model': model,
#             'rangi': rangi,
#             'karobka': karobka,
#             'yili': yili,
#             'narhi': narhi}
#     return avto
# print("saytimizdagi avtolar ruyxatini shakillantiramiz.")#har bir avtolar haqidagi ruyxatni lugat shaklida saqlaydi
# avtolar = []# hammaruyxat shunga tushadi
# while True:
#     print("\nQuyidagi malumotlarni kiriting:")
#     kompaniya = input("ishlab chiqaruvchi:")
#     model = input("modeli:")
#     rangi = input("rangi:")
#     karobka = input("karobka:")
#     yili = input("ishlab chiqarilgan yili:")
#     narhi = input("narhi:")
#     # foydalanuvchi har bir kiritgan malumotdan avto_info yordamida
#     #lugat shakillantirib, har bir lugatni ruyxatga qushadi
#     avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narhi))
#     #yana avto qoshish yoki qushmasligini so'raymiz
#     javob = input("yana avto qo\'shasizmi? (yes/no):")
#     if javob == 'no':
#         break
# print("\nsalonimizdagi avtolar:")
# for avto in avtolar:
#     if avto['narhi']:
#         narh = avto['narhi']
#     else:
#         narh = "nomalum"
#     print(f"{avto['rangi'].title()} {avto['model'].title()}, {karobka} karobka. Narhi: {narhi}")

################################################################## print("\nQuyidagi malumotlarni kiriting:") shu joyda oxirida end='' qilib quyganim uchun menga input sifatida qayta qayta chiqdi



# YANGI MAVZU #####################FUNKSIYAGA RUYXAT UZATISH

# def bahola(ismlar):#ismlar bu ruyxat
#     baholar = {}#bush ruyxat
#     while ismlar:#ismlarni while orqali tekshiryabmiz agar ruyxatni ichida 1 elemet bulsa ham treu qaytaradi
#         ism = ismlar.pop()#pop metodi yoramida 1 elementni sugurib olyabdi anashu qiymatni ism degan uzgaruvchiga yuklaydi
#         baho = input(f"Talaba {ism.title()} ning bahosi:")#talabaga baho kiritilsa uni bahoga joylaydi ism kluch
#         baholar[ism]=(baho)#shu joyda videoda int(baholar edi lekin ) vazifalarda int yuq va shu sababli eror chiqarmadi
#     return baholar
# talabalar = ['ali', 'vali', 'nur', 'jasur']
# baholar = bahola(talabalar)
# print(baholar)
# print(talabalar)
#eslatma bizdagi tlalabalar uzgaruvchisi oxirida bush bulib qoladi vhuni haqiqiy aasli bilan ishladi pop metodi
#ismlar va talabalar ikki ismli va 1 uzgaruchi yaratib quyddik

# ------------------------shu qatorlar darslikni ichidan olingan
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar
#
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)

#endi alohida alohida 2 ta yaratish uchun yani nusxasini funksiyaga uizatish uchun

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()#
#         baho = input(f"Talaba {ism.title()} ning bahosi:")#
#         baholar[ism]=(baho)#
#     return baholar
# talabalar = ['ali', 'vali', 'nur', 'jasur']
# baholar = bahola(talabalar[:])# faqt shu yerdsa uzgarish buldi yani ruyxatdan nusxa olish funksiyasi
# print(baholar)
# print(talabalar)


### ARGS VA KWARGS HAQIDA YANGI DARS
# def summa(*sonlar):
#     """kiritilgan sonlar yigindisini hisoblaydigan funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
#
# print(summa(1,2))
# print(summa(1,2,3,4,5))#istagancha qiymat kirgizsa buladi va sonlar degan ozgaruvchiga tushadi va ozgarmas uzgaruvchi sifatida saqlanadi(tuple sifatida)


# def summa(*sonlar):
#     """kiritilgan sonlar yigindisini hisoblaydigan funksiya"""
#     return sum(sonlar)
#
# print(summa(1,2))
# print(summa(1,2,3,4,5))# bu ham yuqoridagi bilan bir xil ishlaydi

#!!!!!!!!!!!!!!!!!!!!!!!!!
# def summa(x,y,*sonlar):
#     """kiritilgan sonlar yigindisini hisoblaydigan funksiya"""
#     return x+y+sum(sonlar)
#
#
# print(summa(1, 2))
# print(summa(1, 2, 3, 4, 5))  # bu ham yuqoridagi bilan bir xil ishlaydi
# print(summa(2))# agar shu tarzda 1 ta son sozzam eror beradi chunki sen dY ni qiymatini kiritmading deydi
# #TypeError: summa() missing 1 required positional argument: 'y'


###############################################################################################################################
# def avto_info(kompaniya, model,**malumotlar):
#     """avto haqidagi malumotlarni lugat shaklida qaytaruvchi funksiya"""
#     malumotlar ['kompaniya']=kompaniya
#     malumotlar ['model']=model
#     return malumotlar
#
#
#
# avto1 = avto_info("gm", "maligu", rang ="qora", yil = 2018)
# avto2 = avto_info("kia", "k5", rang ="qizil", yil = 2019)
# print(avto1)# shu joyda = quyib ketganim uchun eror chiqdi 30 soatni uvol qildi1023


# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar
#
#
#
# avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
# avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)

# shu mavzu buyicha vazifalar
# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
# Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.


# def multiply(*sonlar):
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma *= son
#     return kopaytma
#
# print(multiply(4,5,6))

# def talaba_info(ism, familya, **kwargs):
#     kwargs['ism']=ism
#     kwargs['familya']=familya
#     return kwargs
#
# talaba=talaba_info('olim', 'olimov', tyil=1994, fakultet='IT', yonalish='At')
# print(talaba)
# # ozim yasadi qarqab
# def oquvchi(ism, familya, **kwargs):
#     kwargs['ism']=ism
#     kwargs['familya']=familya
#     return kwargs
# oquvchi_info=oquvchi('zokir', 'dolimov', tyil=1993, soha='biologiya')
# print(oquvchi_info)

########################################### yana yangi mazu MODULLAR haqida
#funksiyalarda foydalanish maqsadi kodni kaltaroq qilish
#  mavzu dasturni modullarga  bulish yani yanada tozalash


#uzun kodlarni alohida fayillarga bulib chiqish va tartiblash

# import avto_info_mod# as avtoil



# 3 ta funksiya mavzuga oid shu joydan boshladi
# def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):#bizda ozgaruvchiga  hech qanday qiymat bermaslikni hohlasak biz shunda NOne deb ketishinmiz mumkin
#     avto = {'kompaniya': kompaniya,
#             'model': model,
#             'rangi': rangi,
#             'karobka': karobka,
#             'yili': yili,
#             'narhi': narhi}
#     return avto
#
#
# def avto_kirit():
#     """foydalanuvchiga avto_info yordamida bir nechta avtolar haqida malumotni papkaga joylaydi"""
#     avtolar = []
#     while True:
#         print("\nQuyidagi malumotlarni kiriting:", end=' ')
#         kompaniya=input()
#         kompaniya=input("ishlab chiqaruvchi:")
#         model=input("modeli:")
#         rangi=input("rangi:")
#         karobka=input("karobka:")
#         yili=input("ishlab chiqarilgan yili:")
#         narhi=input("narhi:")
#         avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narhi))
#         javob = input("yana avto qo\'shasizmi? (yes/no):")
#         if javob == 'no':
#             break
#     return avtolar
#
# def info_print(avto_info):
#     """avtolar haqidagi malumotlar saqlagan lugatni komnsolga chiqaruvchi funksiya"""
#     print(f"{avto_info['rangi'].title()} {avto_info['kompaniya'].upper()}]")
#           f"{avto_info['model'].upper()}, {avto_info['karobka']} karobka, "
#           f"{avto_info['yili']}-yil, {avto_info['narhi']}$")


#SHU MAVZUDA MAIN VA AVTO INFO FAYLI YARATILGAN


#NOMSIZ FUNKSIYA LAMBDA NOMLI
import math

# def nom(argument):
#     return ifoda # biz funksiyalarni yaratishda shu usuldan foydalanib kelayotgan edik
#defni orniga lambda deb yoziladi va tana bitta buladi
# lambda argument1, argument2:ifoda=argument1+argument2 # tarzda amalga oshiriladi

# uzunlik = lambda pi,r : 2*pi*r
# print(uzunlik(math.pi,10))#62.83185307179586 natija shu shakilda amalga oshirildi
#
#
# kvadrat = lambda x, y : x**y
# print(kvadrat(3, 2))# javob 9 bulib chiqdi



# def daraja(n):
#     return lambda x: x**n
# print(daraja(3))# agar shu holatda run qilsak shu shakilda javob qaytadi <function daraja.<locals>.<lambda> at 0x00000225F9CCC900>
# #funksiya yasaydigan funksiya buldi

# def daraja(n):
#     return lambda x: x**n
#
# kvadrat = daraja(5)
# print(kvadrat(5)) #shu tarzda amalga oshirilib chiqadi
# #lambda orqali boshqa funksiyalar ichida ishlatish qulay

# def daraja(n):
#     return lambda x: x**n
#
# kvadrat = daraja(5)
# kub = daraja(6)
# print(f"3- ning kvadrati {kvadrat(3)} ga, "
#       f"kubi {kub(3)} ga teng")
# # natija esa 3- ning kvadrati 243 ga, kubi 729 ga teng shu korinishda buladi


from math import sqrt#kvadrat ildizi
# sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar))# endi mapning vazifasi  2argumet qabul qilib  sonlardagi har bir songa sqrt formulasini qullab uni list holatda bizga taqdim etadi list allabtda berish kerak chunki map obyekt qaytarmaydi
# print(ildizlar)# bu esa natija +++++++=======[0.0, 1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.0, 3.1622776601683795]

 #yana yangi

# sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar))
#
# def daraja2(x):
#     """berilgan sonlarning kvadaratini qaytaruvchi funksiya"""
#     return x*x
# print(list(map(daraja2, sonlar)))
#
# #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100] bu esa natija


# endi shu funksiyani lambda orqali osonro qilish
# kvadratlar = list(map(lambda x:x*x,sonlar))#1 chi xni x*x kopaytiradi va ruyxat bu sonlar degan ruyxat va lambda x ning kvadratini qaytaradi va
# print(kvadratlar)


# import random as r
#
# sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar#0DAN 99 GACHA SONLAR ORASIDA TASODIFIY 10 TANI OLADI
#
# def juftmi(x):
#     """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
#     return x%2==0
#
# juft_sonlar = list(filter(juftmi,sonlar))
# print(sonlar)
# print(juft_sonlar)

# import random as r
#
# sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
# juft_sonlar = list(filter(lambda son: son%2==0,sonlar))
#
# print(sonlar)
# print(juft_sonlar)#TASODIFIY 10 TA SONLAR ORASIDAN JUSTLARNI AJRATIB OLADI


# mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]
# #
# # mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))#BU startswich  bu ichida belgilangan harib bor sozlarni ajratib beradi
# # print(mevalar_b)
# mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))# bu metod yordamida mevalar ichida 5 ta yoki 5tadan kam harifli sozlarni ajratib oladi
# print(mevalar2)
# a = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
# print (a)# bu metod yordamida a dan boshlab r da tugaydigan so'zlarni ajratib oladi



# data sciense ga kirish boshlanishlar muhim qismlar