def f(x):
    return x**3 + 4*x**2 - 10

def ikiye_bolme_metodu(a, b, epsilon):
    if f(a) * f(b) > 0:
        print("Belirtilen aralıkta kök yok.")
        return None
    iterasyon = 1
    while (b - a) / 2 > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iterasyon += 1
    return (a + b) / 2, iterasyon
cozum, iterasyonlar = ikiye_bolme_metodu(1, 2, 1e-6)

print(f"Bulunan çözüm: {cozum}")
print(f"Iterasyon sayısı: {iterasyonlar}")
