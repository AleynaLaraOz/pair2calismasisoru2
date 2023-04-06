sayı1 = float(input("ilk sayıyı giriniz"))
sayı2 = float(input("ikinci sayıyı giriniz."))
islem = input("Bir işlem seçiniz:")

if islem == "+":
    print(sayı1 + sayı2)
elif islem == "-":
    print(sayı1 - sayı2)
elif islem == "*":
    print(sayı1 * sayı2)
elif islem == "/":
    print(sayı1 / sayı2)
else:
    print("Yanlış bir değer girdiniz.")



