a = int(input("A : "))
b = int(input("B : "))
c = int(input("C : "))
if(a <= 0 or b <= 0 or c <= 0):
	print("Tidak Ada Segitiga Dapat Dibangun")
elif(a >= b + c or b >= a + c or c >= a + b):
	print("Tidak Ada Segitiga Dapat Dibangun")
elif((a == b and a != c) or (b == c and b != a) or (a == c and a != b)):
	print("Segitiga SAMA KAKI")
elif(a == b and b == c):
	print("Segitiga SAMA SISI")
elif(a * a or b * b or c * c):
	print("Segitiga SIKU-SIKU")
else:
	print("Segitiga BEBAS")
