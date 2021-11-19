masukkansatu = float(input("Masukkan nilai rata-rata UG anda:"))
masukkandua = float(input("Masukkan nilai TTS anda:"))
masukkantiga = float(input("Masukkan nilai TAS UG anda:"))

nilai = (((masukkansatu * 0.7) + (masukkandua * 0.15) + (masukkantiga * 0.15)))

if nilai <= 44.9 and nilai >=0:
    print (f"Nilai anda: {nilai}")
    print("Nilai huruf anda: E")
elif nilai <= 54.9 and nilai >= 45:
    print (f"Nilai anda: {nilai}")
    print("Nilai huruf anda: D")
elif nilai <= 59.9 and nilai >= 55:
    print (f"Nilai anda: {nilai}")
    print("Nilai huruf anda: C")
elif nilai <= 64.9 and nilai >= 60:
    print (f"Nilai anda: {nilai}")
    print("Nilai huruf anda: C+")
elif nilai <= 69.9 and nilai >= 65:
    print (f"Nilai anda: {nilai}")
    print("Nilai huruf anda: B-")
elif nilai <= 74.9 and nilai >= 70:
    print (f"Nilai anda: {nilai}")
    print("Nilai huruf anda: B")
elif nilai <= 79.9 and nilai >= 75:
    print (f"Nilai anda: {nilai}")
    print("Nilai huruf anda: B+")
elif nilai <= 84.9 and nilai >= 80:
    print (f"Nilai anda: {nilai}")
    print("Nilai huruf anda: A-")
elif nilai <= 100:
    print (f"Nilai anda: {nilai}")
    print("Nilai huruf anda: A")
else:
    print ("Input Salah")
