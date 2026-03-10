idade = 3
"""
if idade < 4:
    print("Seu ticket custa $0")
elif idade < 18:
    print("Seu ticket custa $5")
else:
    print("SEu ticket custa $10")
"""
price = 0
if idade < 4:
    price = 0
elif idade < 18:
    price = 5
else:
    price = 10

print("Seu ticket custa $", str(price), ".")
