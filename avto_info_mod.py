# # 3 ta funksiya mavzuga oid shu joydan boshladi
#
#
# #main papka bilan boglangan
#
#
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
#     print(f"{avto_info['rangi'].title()} {avto_info['kompaniya'].upper()}]"
#     f"{avto_info['model'].upper()}, {avto_info['karobka']} karobka, "
#     f"{avto_info['yili']}-yil, {avto_info['narhi']}$")
