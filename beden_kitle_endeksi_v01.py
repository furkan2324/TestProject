print("""************** 
Beden kitle endeksi ölçümü
****************
""")

a = float(input("boyunuzu giriniz:"))
b = int(input("kilonuzu giriniz:"))

c = b / (a**2)

if (c < 18.5) :
    print("zayıfsın")
elif (18.5 < c < 25):
    print("normal")
elif (25 < c < 30):
    print("fazla kilolu")
elif (c > 30):
    print("obezsin")
