Dasha, Igor, Kirill = map(float, input().split())
D = 305
C = 5

# Находим вероятность хорошего исхода за 1 день для каждого
Dasha = pow((1-Dasha), 1/C)
Igor = pow((1-Igor), 1/C)
Kirill = pow((1-Kirill), 1/C)

# D дней все хорошо
Dasha = Dasha**D
Igor = Igor**D
Kirill = Kirill**D

# У Даши цунами!
answ = (1 - Dasha) * Igor * Kirill
print(answ)
