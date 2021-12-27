#
#   Copyright (C) 2021 xyzuan, Jody Yuantoro
#

rev = "rev1.0.confidental"

import os
from selenium import webdriver
from selenium.webdriver.common.by import By

loop = 0
web = "https://infokhs.umm.ac.id"

nim_db = open("nim.txt","r")
pic_db = open("pic.txt","r")

os.system('cls')
nim = nim_db.read()
pic = pic_db.read()

nim_db.close()
pic_db.close()

os.system('cls')
print("================================================")
print("\n Bot Sistem Presensi")
print(  " Developed by xyzuan\n")
print(  " Software rev\t : ", rev)
print(  " Site Target\t : ", web)
print("\n================================================\n")
print(  " User information :")
print(  " NIM\t : ", nim)
print(  " PIC\t :  ************")
print("\n================================================")
print("\n 1. Pancasila\t\t 2. Olahraga\n 3. Pemdas\t\t 4. Orkom\n 5. Kalkulus\t\t 6. PTI\n 7. Bahasa Indonesia\n")
menu = input("Pilih mata kuliah : ")

# Login Page
absen = webdriver.Edge(executable_path=r'msedgedriver.exe')
absen.get(web)
absen.find_element(By.NAME, "username").send_keys(nim)
absen.find_element(By.NAME, "password").send_keys(pic)
absen.find_element(By.CLASS_NAME, "btn.btn-default.submit").click()

# Pancasila
if menu == "1":
    while loop <= 1:
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/893011/558758')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/893011/558759')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/893011/558760')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/893011/558761')
    
# Olahraga
if menu == "2":
    while loop <= 1:
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892939/554022')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892939/554023')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892939/554024')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892939/554025')

# Pemrograman Dasar
elif menu == "3":
    while loop <= 1:
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892987/553988')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892987/553989')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892987/553990')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892987/553991')

# Orkom
elif menu == "4":
    while loop <= 1:
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892951/554262')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892951/554263')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892951/554264')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892951/554265')

# Kalkulus
elif menu == "5":
    while loop <= 1:
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892975/553926')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892975/553927')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892975/553928')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892975/553929')

# PTI
elif menu == "6":
    while loop <= 1:
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892963/553718')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892963/553719')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892963/553720')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/892963/553721')

# Bahasa Indonesia
elif menu == "7":
    while loop <= 1:
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/893023/554214')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/893023/554215')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/893023/554216')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/893023/554217')
        absen.get('https://infokhs.umm.ac.id/jadwal-kuliah/202120221/proses/893023/554218')

elif menu != "":
      print("Inputan salah !!!") 