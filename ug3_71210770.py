kalimat = input("Masukkan kalimat: ")

kata = kalimat.split()
kalimat = ''.join(a for a in kalimat if a.isalnum() or a.isspace())

frekuensi = {}
for i in kata:
    if i in frekuensi:
        frekuensi[i] += 1
    else:
        frekuensi[i] = 1


print("Maka Outputnya adalah:")
for i, k in frekuensi.items():
    print(i, "=", k)
total_kata = sum(frekuensi.values())
print("Total kata =", total_kata)
print("Kata unik =", len(frekuensi))