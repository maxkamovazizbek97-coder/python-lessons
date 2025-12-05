import pandas as pd
import os

print("Hammasi ishlayapti ✅")
os.chdir(r"C:\Users\user\Downloads")
print("Hozirgi papka:", os.getcwd())
all_students = pd.read_excel("all_students.xlsx")
real_time = pd.read_excel("real_time.xlsx")
print(all_students.columns)
print(real_time.columns)
all_students.columns = all_students.columns.str.strip()
real_time.columns = real_time.columns.str.strip()
# Bo‘sh kataklarni tozalash
all_students["Name"] = all_students["Name"].fillna("")
real_time["Name"] = real_time["Name"].fillna("")

# Holat ustunini yaratish
all_students["Holat"] = all_students["Name"].apply(
    lambda x: "Hozir o‘qiydi" if x in real_time["Name"].values else "Tamomlagan"
)

# Natijani ko‘rish
print(all_students.head())
import pandas as pd

# Fayllarni o‘qish
all_students = pd.read_excel(r"C:\Users\user\Downloads\all_students.xlsx")
real_time = pd.read_excel(r"C:\Users\user\Downloads\real_time.xlsx")

# Har ikkala fayl ustunlarini tekshirish
print("All_students ustunlari:", all_students.columns)
print("Real_time ustunlari:", real_time.columns)
all_students["Name"] = all_students["Name"].fillna("")
real_time["Name"] = real_time["Name"].fillna("")
all_students ["Holat"] = all_students["Name"].apply(
    lambda x: "Hozir o‘qiydi" if x in real_time["Name"].values else "Tamomlagan"
)
print(all_students.head(10))   # birinchi 10 ta o‘quvchini chiqaradi
all_students.to_excel(r"C:\Users\user\Downloads\students_with_status.xlsx", index=False)
print("Yangi fayl yaratildi ✅")
print(all_students.head(10))  # dastlabki 10 qatorni tekshirish
# Hozir o‘qiyotganlar va tamomlaganlar soni
print("Hozir o‘qiyotganlar soni:", (all_students["Holat"]=="Hozir o‘qiydi").sum())
print("Tamomlaganlar soni:", (all_students["Holat"]=="Tamomlagan").sum())
# Hozir o‘qiyotganlar va tamomlaganlar soni
print("Hozir o‘qiyotganlar soni:", (all_students["Holat"]=="Hozir o‘qiydi").sum())
print("Tamomlaganlar soni:", (all_students["Holat"]=="Tamomlagan").sum())
# Kurs bo‘yicha tahlil (agar 'Course' ustuni bo‘lsa)
import pandas as pd
# Faylni o‘qish
real_time = pd.read_excel(r"C:\Users\user\Downloads\real_time.xlsx")
# Bo‘sh kataklarni tozalash
real_time["Name"] = real_time["Name"].fillna("")
real_time["Group Name"] = real_time["Group Name"].fillna("Ma'lumot yo'q")
real_time["Group Course"] = real_time["Group Course"].fillna("Ma'lumot yo'q")
# Kurs va guruh bo‘yicha hozir o‘qiyotganlar soni
kurs_guruh_tahlil = real_time.groupby(["Group Course", "Group Name"])["Name"].count()
print("Hozir o‘qiyotganlar kurs va guruh bo‘yicha taqsimoti:")
print(kurs_guruh_tahlil)
# kurs va guruh bo‘yicha tahlil
kurs_guruh_tahlil = real_time.groupby(["Group Course", "Group Name"])["Name"].count()
# DataFrame ga aylantirish
kurs_guruh_df = kurs_guruh_tahlil.reset_index()
kurs_guruh_df.rename(columns={"Name": "Student Count"}, inplace=True)
kurs_guruh_df.to_excel(r"C:\Users\user\Downloads\real_time_analysis.xlsx", index=False)
print("Natija faylga saqlandi ✅")
real_time.groupby(["Group Course", "Group Name"])["Name"].count()
import pandas as pd
# Faylni o‘qish
real_time = pd.read_excel(r"C:\Users\user\Downloads\real_time.xlsx")
# Bo‘sh kataklarni tozalash
real_time["Name"] = real_time["Name"].fillna("")
real_time["Group Name"] = real_time["Group Name"].fillna("Guruh yo'q")
real_time["Group Course"] = real_time["Group Course"].fillna("Ma'lumot yo'q")
# Guruh bo‘yicha tahlil (faqat guruh raqami mavjudlar)
guruhli = real_time[real_time["Group Name"] != "Guruh yo'q"]
guruh_tahlil = guruhli.groupby(["Group Course", "Group Name"])["Name"].count().reset_index()
guruh_tahlil.rename(columns={"Name": "Student Count"}, inplace=True)
# Guruhi bo‘lmaganlarni alohida ko‘rsatish
guruhsiz = real_time[real_time["Group Name"] == "Guruh yo'q"]
# Natijalarni faylga saqlash
guruh_tahlil.to_excel(r"C:\Users\user\Downloads\grouped_students.xlsx", index=False)
guruhsiz.to_excel(r"C:\Users\user\Downloads\ungrouped_students.xlsx", index=False)
print("Guruhli va guruhsiz o‘quvchilar alohida fayllarga saqlandi ✅")
guruh_tahlil = guruhli.groupby(["Group Course", "Group Name"])["Name"].count().reset_index()
guruh_tahlil.rename(columns={"Name": "Student Count"}, inplace=True)
print("Guruh bo‘yicha tahlil:")
print(guruh_tahlil)
print("Guruhi bo‘lmagan o‘quvchilar:")
print(guruhsiz)
guruh_tahlil.to_excel(r"C:\Users\user\Downloads\grouped_students.xlsx", index=False)
guruhsiz.to_excel(r"C:\Users\user\Downloads\ungrouped_students.xlsx", index=False)
print("Jami hozir o‘qiyotganlar:", len(real_time))
print(real_time.groupby("Group Course")["Name"].count())
# Bu faqat bosqichni konsolda ko‘rsatadi, lekin shart emas
print("✅ 1. Fayllarni o‘qish bajarildi")
print("✅ 2. Bo‘sh kataklarni tozalash bajarildi")
import matplotlib.pyplot as plt
# Kurs bo‘yicha bar chart
real_time["Group Course"].value_counts().plot(kind="bar")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
# Faylni o'qish
real_time = pd.read_excel(r"C:\Users\user\Downloads\real_time.xlsx")
# Bo'sh kataklarni tozalash
real_time["Name"] = real_time["Name"].fillna("")
real_time["Group Name"] = real_time["Group Name"].fillna("Guruh yo'q")
real_time["Group Course"] = real_time["Group Course"].fillna("Ma'lumot yo'q")
# Guruhli o'quvchilar
guruhli = real_time[real_time["Group Name"] != "Guruh yo'q"]
# Kurs bo'yicha bar chart
kurs_counts = guruhli["Group Course"].value_counts()
kurs_counts.plot(kind="bar", color="skyblue")
plt.title("Hozir o'qiyotganlar kurs bo'yicha taqsimoti")
plt.xlabel("Kurs")
plt.ylabel("O'quvchilar soni")
plt.show()
# Guruh bo'yicha bar chart
guruh_counts = guruhli.groupby("Group Name")["Name"].count()
guruh_counts.plot(kind="bar", color="lightgreen")
plt.title("Hozir o'qiyotganlar guruh bo'yicha taqsimoti")
plt.xlabel("Guruh")
plt.ylabel("O'quvchilar soni")
plt.show()
import matplotlib.pyplot as plt
import seaborn as sns  # qo‘shimcha kutubxona
# Zamonaviy rang palitrasi
sns.set(style="whitegrid", palette="pastel")
# Kurs bo‘yicha bar chart
plt.figure(figsize=(10,6))
sns.barplot(x=kurs_counts.index, y=kurs_counts.values)
plt.title("Hozir o'qiyotganlar kurs bo‘yicha taqsimoti", fontsize=16)
plt.xlabel("Kurs", fontsize=12)
plt.ylabel("O'quvchilar soni", fontsize=12)
plt.xticks(rotation=30)
plt.show()
import plotly.express as px
fig = px.bar(guruhli,
             x="Group Course",
             y="Name",
             color="Group Name",
             labels={"Name": "O'quvchilar soni"},
             title="Kurs va guruh bo‘yicha o‘quvchilar")
fig.show()
# Matplotlib bar chart – kurs bo‘yicha
plt.figure(figsize=(10,6))
kurs_counts = guruhli["Group Course"].value_counts()
kurs_counts.plot(kind="bar", color="skyblue")
plt.title("Hozir o'qiyotganlar kurs bo'yicha taqsimoti", fontsize=16)
plt.xlabel("Kurs", fontsize=12)
plt.ylabel("O'quvchilar soni", fontsize=12)
plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
# Seaborn bar chart – kurs va guruh bo‘yicha
plt.figure(figsize=(12,6))
sns.countplot(data=guruhli, x="Group Course", hue="Group Name", palette="Set2")
plt.title("Kurs va guruh bo'yicha o'quvchilar", fontsize=16)
plt.xlabel("Kurs", fontsize=12)
plt.ylabel("O'quvchilar soni", fontsize=12)
plt.legend(title="Guruh")
plt.show()# Plotly interaktiv bar chart – kurs va guruh bo‘yicha
fig = px.bar(guruhli,
             x="Group Course",
             y="Name",
             color="Group Name",
             labels={"Name":"O'quvchilar soni"},
             title="Kurs va guruh bo‘yicha hozir o‘qiyotganlar (interaktiv)")
fig.show()
# Plotly – interaktiv bar chart
fig = px.bar(guruhli,
             x="Group Course",
             y="Name",
             color="Group Name",
             labels={"Name":"O'quvchilar soni"},
             title="Kurs va guruh bo‘yicha hozir o‘qiyotganlar (interaktiv)")
fig.write_html(r"C:\Users\user\Downloads\kurs_guruh_plotly.html")
fig.show()
print("✅ Grafiklar saqlandi: Matplotlib & Seaborn PNG, Plotly HTML")
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
# Fayllarni o'qish
all_students = pd.read_excel(r"C:\Users\user\Downloads\all_students.xlsx")
real_time = pd.read_excel(r"C:\Users\user\Downloads\real_time.xlsx")
# Bo'sh kataklarni tozalash
all_students["Name"] = all_students["Name"].fillna("")
real_time["Name"] = real_time["Name"].fillna("")
real_time["Group Name"] = real_time["Group Name"].fillna("Guruh yo'q")
real_time["Group Course"] = real_time["Group Course"].fillna("Ma'lumot yo'q")
# Holat ustuni
all_students["Holat"] = all_students["Name"].apply(
    lambda x: "Hozir o'qiydi" if x in real_time["Name"].values else "Tamomlagan"
)
# Guruhli va guruhsiz
guruhli = real_time[real_time["Group Name"] != "Guruh yo'q"]
guruhsiz = real_time[real_time["Group Name"] == "Guruh yo'q"]
# Kurs bo'yicha tahlil
kurs_counts = guruhli.groupby("Group Course")["Name"].count().reset_index()
kurs_counts.rename(columns={"Name":"Hozir o'qiydi"}, inplace=True)
# Guruh bo'yicha tahlil
guruh_counts = guruhli.groupby("Group Name")["Name"].count().reset_index()
guruh_counts.rename(columns={"Name":"Hozir o'qiydi"}, inplace=True)
# Dashboard yaratish
fig = go.Figure()
# Kurs bo'yicha bar chart
fig.add_trace(go.Bar(
    x=kurs_counts["Group Course"],
    y=kurs_counts["Hozir o'qiydi"],
    name="Kurs bo'yicha",
    marker_color='skyblue'
))
# Guruh bo'yicha bar chart
fig.add_trace(go.Bar(
    x=guruh_counts["Group Name"],
    y=guruh_counts["Hozir o'qiydi"],
    name="Guruh bo'yicha",
    marker_color='lightgreen'
))
fig.update_layout(
    title="Hozir o'qiyotganlar: Kurs va Guruh bo'yicha taqsimoti",
    xaxis_title="Kurs / Guruh",
    yaxis_title="O'quvchilar soni",
    barmode='group'
)
# Dashboardni HTML fayl sifatida saqlash va ko‘rsatish
fig.write_html(r"C:\Users\user\Downloads\dashboard.html")
fig.show()
all_students["Holat"] = all_students["Ism"].apply(
    lambda x: "Hozir o‘qiydi" if x in real_time["Ism"].values else "Tamomlagan"
)
all_students["Name"] = all_students["Name"].fillna("")
real_time["Name"] = real_time["Name"].fillna("")
all_students["Name"] = all_students["Name"].astype(str)
real_time["Name"] = real_time["Name"].astype(str)
# Bo'sh kataklarni tozalash va stringga aylantirish
all_students["Name"] = all_students["Name"].fillna("").astype(str)
real_time["Name"] = real_time["Name"].fillna("").astype(str)
# Holat ustuni
all_students["Holat"] = all_students["Name"].apply(
    lambda x: "Hozir o‘qiydi" if x in real_time["Name"].values else "Tamomlagan"
)
print(all_students.columns)
print(real_time.columns)
# Misol: agar ustun 'Name' deb yozilgan bo‘lsa
all_students["Holat"] = all_students["Name"].apply(
    lambda x: "Hozir o'qiydi" if x in real_time["Name"].values else "Tamomlagan"
)
all_students["Name"] = all_students["Name"].fillna("").astype(str)
real_time["Name"] = real_time["Name"].fillna("").astype(str)
print(all_students.columns)
print(real_time.columns)
all_students["Holat"] = all_students["Name"].apply(
    lambda x: "Hozir o'qiydi" if x in real_time["Name"].values else "Tamomlagan"
)