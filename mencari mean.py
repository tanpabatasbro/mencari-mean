import statistics

inputan = input("Masukkan Deret Angka (Pisahkan Dengan Tanda Koma (,) ) :")
data = []

for bilangan in inputan.split(','):
    data.append(int(bilangan))
    
rerata = statistics.mean(data)
print(f"Data -> {data}")
print(f"Mean -> {rerata}")