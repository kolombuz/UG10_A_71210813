menu = input('Mendatar/Menurun?: ')
if menu == 'Mendatar':
    angka = eval(input('Masukkan kolom: '))
elif menu == 'Menurun':
    angka = eval(input('Masukkan baris: '))
else:
  print('Pola tidak dikenali')
print('#' * angka)


