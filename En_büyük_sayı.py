a = int(input("birinci sayıyı giriniz:"))
b = int(input("ikinci sayıyı giriniz:"))
c = int(input("üçüncü sayıyı giriniz:"))

if a>b and a>c:
    print("birinci sayı en büyüktür.")

elif b>a and b>c:
    print("ikinci sayı en büyüktür.")

elif c>a and c>b:
    print("üçüncü sayı en büyüktür.")

else:
    print("bütün sayılar eşittir....")
