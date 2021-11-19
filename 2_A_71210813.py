print('############################')
print('Kalkulator Advance Sederhana')
print('############################')
print('  1. Menghitung sisa hasil bagi')
print('  2. Membulatkan ke bawah hasil pembagian')
print('  3. Mencari akar kubik sebuah bilangan')

menu = input('Masukkan menu yang anda pilih: ')
if menu == '1':
    dibagi_1 = float(input('Masukkan bilangan yang ingin dibagi: '))
    pembagi_1 = float(input('Masukkan bilangan pembagi: '))
elif menu == '2':
    dibagi_2 = float(input('Masukkan bilangan yang ingin dibagi: '))
    pembagi_2 = float(input('Masukkan bilangan pembagi: '))
elif menu == '3':
    pembagi_3 = eval(input('Masukkan bilangan yang ingin dicari akar kubiknya: '))
else:
  print('Menu yang anda pilih tidak tersedia')
        
if menu == '1':
  penyelesaian_1 = dibagi_1 % pembagi_1
  print(f'Sisa hasil bagi {dibagi_1} dibagi dengan {pembagi_1} adalah {penyelesaian_1}')
elif menu == '2':
  penyelesaian_2 = dibagi_2 // pembagi_2
  print(f'Hasil pembagian {dibagi_2} dibagi dengan {pembagi_2} dibulatkan kebawah adalah {penyelesaian_2}')
elif menu == '3':
  penyelesaian_3 = sqrt=pembagi_3**(1/3) 
  print(f'Akar kubik dari {pembagi_3} adalah = {penyelesaian_3}')

