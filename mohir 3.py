#listni davomi
bozorlik = ["un", "yog'", "piyoz", "go'sht"]
#.pop(1,2...) qandaydir elementni sug'urib olishda qol keladi
#maxsulot = bozorlik.pop(2)
#print("men " + maxsulot + "sotib oldim ") #agar " ichida joy tashlamasdan yozsam maxsulot bilan birlashtirib quyadi
#print("olinmagan maxsulotlar".upper(), bozorlik)
#print("akam " + maxsulot + "sotib olgani ketdi" + "men " + maxsulot + "olamanmi???")
#print("men" + maxsulot.title() + "ni "+ str( bozorlik ) + "bozorlik ruyxatida yuqligi uchun uzim olaman")
##pop metodidan foydalanilgandan agar pop() ichga raqam quyilmasa eng oxiridagi elementni oladi!!!
#narxlar = [10000, 12000, 13000, 14000]
#narxlar [0] = narxlar [0] + 1000   # shu holatda qushsa buladi
#print(narxlar)
#print(narxlar[1] + narxlar[2]) shu usulda ham qushsa buladi

#ro'yxatlar(list metodilaridan biri)
# teslari tartib
#asl royxatga tegamagan holda royxatni tartiblash
cars = ['bmw', 'mers', 'gm', 'Labar', 'Porsh', 'bugati' , 'zikir', 'audi']
#cars.sort()
print(cars)
#odatda jadvaldagi katta harflar oldinda turadi
print(cars)
#reverse= true bu ruyxatni teskari tartibda taxla degani
cars.sort(reverse=True)#jadvalni teskari taritibda joyla degan buyruq
print(cars)
#sorted degan funksiyasi tartiblangan ruyxatni o'zgatirmasdan konsolga olib chiqaradi
print(sorted(cars))
#odatda sortedda asosoiy ozgaruvchilar o'zgarmaydi lekin #sort orqali cars.sort() qilish orqali ozgartirilgan ozgaruvchini qaytadan saqlab quyiladi (o'zgargan shakilda)
cars.sort()
print(cars)
sonlar =  [5, 1, 2, 3, 11, -11, 28, -1]
print(sonlar)
print(sorted(sonlar ))#oqami ketinlik bilan tariblandi
sonlar.sort(reverse=True)# bu hoaltda sonlar kattadan kichikga teskari tartibda saralanadi
print(sonlar)
len(sonlar)# bu ruyxat uzunligini korsatadi nechta soz yoki raqamlar borligini korsatadi
uzunlik = len (cars)# shu holatda uzunli o'zgaruvchisi ichida cars ichida nechta ruyxat borligini alohida o'zgaruvchi ichiga saqlab quyadi
#range bu funksiyada malum oraliqdagi sonlarni qaytaradi
#range()
sonlar = list(range(0, 20))
print(sonlar)#shu holatda odan boshlab 20 gacha sonlarni ruyxatini tuzadi 20 kirmaydi 19 gacha qiladi
#30.10.2025 yangi come back
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num)
num.sort (reverse=True)
print(num)
# bizda qiziqarli malumot agar numb deb raqamlarda () ishlatilsa unda ishlamadi (tupleda faqat listda ishlaydi deb chiqdi men agar raqamlar bilan uzgaruvchi qilsam uni [] ichiga yozganim ishlaydi faqat)
#len(num) uzunligini hisoblab beradi len() — bu Python’dagi ro‘yxat (list), matn (string), tuple, dictionary va hokazolar uzunligini (elementlar sonini) hisoblaydigan standart funksiya. va unis pythonda ishlatishda print(len(num)) deb kiritsa ishlaydi
#range(0,30) bunda hosil bulgan natijani ruyxataga utkazish uchun raqamlar =  list (range(0,30)) deb yoziladi
sonlar = list(range(0, 30))#lekin oxirgi raqam kirmaydi 30 emas balki 29 da tugatiladi
print(sonlar)
juft_sonlar = list(range(0,10,2))# 0dan 10gacha 2 qadam bilan sonlarni oladi
print(juft_sonlar)
sanash = list(range(0,100,3))
print(sanash)
sanash.sort(reverse=True)
print(sanash) # shu usul bilan teskari shakilda korish mumkin
max_qiymat = max (sanash)
print(max_qiymat) #maxda shu berilgan ichidagi eng katta qiymatni korsatadi

print(sanash)
sanashi = [2000, 2200, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
print(sanashi)
kichik = min(sanashi)
katta = max(sanashi)
jami = sum(sanashi)
print("ENG KICHIK", kichik, "eng katta", katta, "hammasi", jami) # shu tartibda ketadi va shu joylarni yaxshiroq etibor bergan holda qilish kerak
sabzavotlar = ["kartoshka" , "sabzi", "oshqovoq", "lavlagi", "baqlajon"]
print(sabzavotlar[0:3])# shu usul bilan ruyxatdan 1dan 3 gacha bulganini qoldirdi
print(cars)
#cars = my_mashina bu holatda 1 ta uzgaruvchilar ruyxatiga 2 ta nom berildi 1 tasi uzgarsa 2chisi ham uzgaradi
my_mashina = cars
print(my_mashina)
cars.remove("bmw")
cars[0] =  "lasetti"
print(cars)
print(my_mashina)
my_mashina = cars[:]# shu holatga carsdagi boshidan oxirigacha nusha olib my mashina ichiha joyla (nusxa ol degan)
print(my_mashina)
print(cars)
cars.remove("Porsh")
print(cars)
print(my_mashina)
#TUPLe -  bu o'zgarmas ruyhat
toys = ("bus", "car", "animals", "fruits") #etibor beramiz () ishlatildi [] emas
print(toys[-1])
print(toys[0])
print(toys[2:])
#toys[0] = "teddy" qilib yangi element qushmoqchi bulinsa bulmaydi
#toys.remove("car") shunda ham olib bulmaydi
# agar uzgartirish kerak bulsa
print(type(toys)) # bunda turiga kora tuple yani uzgarmas degani
toys = list(toys)
print (toys)
print(type(toys))# bu yerda listga uzgartirilganini tekshirdim
mexmonlar = ['akram', 'mirfozil' , 'Abdumalik' , 'Doniyor' , 'muzaffar' , 'Nurmuhammad' , 'bohodir' , 'shohrux']
mexmonlar.sort()
print(mexmonlar)
mexmonlar.sort(reverse=True)
print(mexmonlar)
print("sorted() qaytargan ruyxat:" , sorted(mexmonlar))#<<<<<<-------- shu joylarga etibor berish kerak
print("asl ruyxat o'zgarmay qoldi:" , mexmonlar)
print(sorted(mexmonlar , reverse=True))#bu xolatda ham teskari ruyxat hosil buladi
ages = [25, 60, 75, 15, 9, 35, 45, 50]
ages.reverse() # shu joyda sort(reverse=true) kabi teskari qilib chiqaradi
print(ages)
meva = ["olma", "banan" , "nok" , "apelsin" , "uzum"]
print("elementlar soni:" , len(meva))#elementlar soni deb: ruyxatning uzunligi yani nechtaligini sonini quyib beradi
muchal = list(range(1997,2400,12))
print("muchal nishonlanadigan kunlar:" , muchal)
kunlar = [1997, 2009, 2021, 2033, 2045, 2057, 2069, 2081, 2093, 2105, 2117, 2129, 2141, 2153, 2165, 2177, 2189, 2201, 2213, 2225, 2237, 2249, 2261, 2273, 2285, 2297, 2309, 2321, 2333, 2345, 2357, 2369, 2381, 2393]
eng_birinchi = min(kunlar)
eng_oxirgi = max(kunlar)
hammasi = sum(kunlar)
print("eng birinchi nishonlanish sanasi", eng_birinchi , "eng oxirgi nishonlanish sanasi", eng_oxirgi, "hammasini qushilsa" , hammasi)
# sikil yangi mavzul
#malum kodlar qayta qayta qaytarilgani uchun
print("salom" , mexmonlar[0])
for mexmonlar in mexmonlar:
    print("hush kelibsiz" , mexmonlar)
    print("hush ko'rdik" , mexmonlar)
print(max(kunlar)-min(kunlar))
print(f"hurmatli {mexmonlar} , sizni 19 chi yanvar kungi oshga taklif qilamiz")
print("hurmat bilan , polonchiyevlar oilasi\n")
kunlar = list(range(1997,2393))
for kunlar in kunlar:
    print(f"{kunlar} ning kvadrati {kunlar**2} ga teng")# umuman bumba narsa ekan yanada chuqurroq urganish kerak
numb = list(range(1,40))
print(numb)
numb.append(40)
print(numb)
numb_kvadrati = []
for numb in numb:
    numb_kvadrati.append(numb**3)
#print(numb_kvadrati)
#print(numb)# kvadrat va kub haqida bir oz malumotlarni urganish\
#druglar = []
#print("5 ta eng yaqin dostingiz kim?")# judayam qiziqarli bulib borvati
#for n in range(5):
    #druglar.append(input(f"{n+1}- do'stingizni ismini kiriting ---->\n"))#n +1 ga etibor beramiz chunki n ni o'zi bolib qolsa 1 chi drugni emas balki 0 drugni kiriting deydi chunki python tarti bo'yicha boladi
#print(druglar)
#tarmoqlanish
#avtolar = ['bmw' , 'hunday' , 'cruz' , 'subaru' , 'porsh']
#for avto in avtolar#agar biz hamma uzgaruvchilarni bosh hariflarni katta harfda ko'rsatadi
 #   print(avto.title())
  #  if avto == 'bmw':
   #     print(avto.upper())
    #else:
     #   print(avto.title())mexmonlar = ('akram', 'mirfozil' , 'Abdumalik' , 'Doniyor' , 'muzaffar' , 'Nurmuhammad' , 'bohodir' , 'shohrux')
print(mexmonlar)
#for mexmon in mexmonlar:
 #   print ("salom" , mexmonlar)
