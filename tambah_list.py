print("===== Menambah List =====")
print()
x=['A', 'B', 'C', 'D']
y=['E', 'F', 'G', 'H']
print("List X :", x, "\nList Y :", y)
print()

#Mengambil 2 Bagian Dari List Pertama dan Jadikan List ke-2
print("Mengambil 2 Bagian Dari List X dan Jadikan List Y :")
y.append(x[0:2])
print(y)
print()

#Menambah List Y Dengan Nilai String
print("Menambah List Y Dengan Nilai String :")
y.append('I')
print(y)
print()

#Menambah List Y Dengan 3 Nilai
print("Menambah List Y Dengan 3 Nilai :")
print(y+['J', 'K', 'L'])
print()

#Menambah List Y Dengan List X
print("Menambah List Y Dengan List X :")
print(x+y)
