# import avto_info_mod
#
# avto1 = avto_info_mod.avto_info("gm", "malibu", "qora", "avtomat", 2020, 40000)
# avto_info_mod.info_print(avto1)
from idlelib.multicall import r

# # BU ESA QISQA ISM BERISH USULI IKKISI HAM 1 TA KOD
# import avto_info_mod as aim
#
# avto1 = aim.avto_info("gm", "malibu", "qora", "avtomat", 2020, 40000)
# aim.info_print(avto1)

# yanada qisqa uslubi
# from avto_info_mod import avto_info, info_print
# avto1 = avto_info("gm", "malibu", "qora", "avtomat", 2020, 40000)
# info_print(avto1)
#
# #++++++++++++++++++++++++++++++++++++++++++++++++++ 3ta usulda hammasi 1 ta anatija chiqdi
# #Qora GM]MALIBU, avtomat karobka, 2020-yil, 40000$
# #agar kop uxshash funksiyalar bulsa unda shu yordamida nomini uazgartiramiz
# from avto_info_mod import avto_info as ainfo, info_print as iprint
# avto1 = ainfo("gm", "malibu", "qora", "avtomat", 2020, 40000)
# iprint(avto1)

#yuqoridagilarni hammasi 1 ta javobga har hil yechim  va qisqartirish usuli va nomini uzgartirishva hokozolar



#from avto_info_mod import *#shuni ichidagi hamma funksiyani chaqirib oladi yani 3 ta funksiyani hammasini chaqiradi
#lekin bu usul tavfsiya qilinmaydi chunki ularni ichidagi hamma uzgaruvchilar qorishib ketadi


# import math # nu modulni chqirib olsak
# x=400#ni kvadrat qiymatini hisoblaydi
# print (math.sqrt(x))
# print(math.pow(5,3))#5ning kubi#sonning malum bir darajasini hisoblaydi 5ning kubini va kvadratini hisoblaydi
# print(math.pi)#ning qiymatini aniqlik bilan korsatadi #bu ozgaruvchi hisoblanadi
# print(math.log2(8))#2 asosli logorifm
# print(math.log10(100))
# # bu modullarni hammsini python modulle indexdan tosa va yuklab olsa buladi

#yana bir modul bu random moduli
# import random as r
# #modulga qisqa nom bersa va undan qaytib foydalanmaslik kerak xato beradi
# son = r.randint(0,100)#shu oraliqdagi istalgan sonlarni random qaytaraveradi
# print(son)

# import random as r
# #choice haqwida urganamiz
# ismlar = ['olim', 'anvar', 'husan', 'qodir', 'shokir']
# ism = r.choice(ismlar)#RUYXATNI ICHIODAGI ISMLARDAN RANDOM CHOIS DEB TANLAB BER DEB BUYRUQ BERILDI
# print(ism)
# print(r.choice(ism))

# import random as r
# x = list(range(0,51,5))#51gacha bulgan sonlarni 5 qadam bilan sanaydi va tasodifiy qiymatni tanlab beradi
# print(x)
# print(r.choice(x))



# shuffler funksiyasi haqida


import random as r
x = list(range(11))#51gacha bulgan sonlarni 5 qadam bilan sanaydi va tasodifiy qiymatni tanlab beradi
print(x)
r.shuffle(x)
print(x)#tasodifiy tartib bulib o'zgaraveradi
















