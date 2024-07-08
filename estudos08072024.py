altura = int(input("Digite sua altura em centimetros: "))
peso = float(input("Digita seu peso em quilos: "))


altura_metros = altura / 100

calcImc = peso / (altura_metros * altura_metros)


# Exibe os resultados com quebras de linha e formatação correta
if calcImc < 18.5:
    print(f"Sua altura é {altura} cm\nSeu peso é {peso} kg\nSeu IMC é {calcImc:.2f}\nSeu IMC é classificado como: Magreza")
elif 18.5 <= calcImc <= 24.9:
    print(f"Sua altura é {altura} cm\nSeu peso é {peso} kg\nSeu IMC é {calcImc:.2f}\nSeu IMC é classificado como: Normal")
elif 25 <= calcImc <= 29.9:
    print(f"Sua altura é {altura} cm\nSeu peso é {peso} kg\nSeu IMC é {calcImc:.2f}\nSeu IMC é classificado como: Sobrepeso")
elif 30 <= calcImc <= 34.9:
    print(f"Sua altura é {altura} cm\nSeu peso é {peso} kg\nSeu IMC é {calcImc:.2f}\nSeu IMC é classificado como: Obesidade grau I")
elif 35 <= calcImc <= 39.9:
    print(f"Sua altura é {altura} cm\nSeu peso é {peso} kg\nSeu IMC é {calcImc:.2f}\nSeu IMC é classificado como: Obesidade grau II")
else:
    print(f"Sua altura é {altura} cm\nSeu peso é {peso} kg\nSeu IMC é {calcImc:.2f}\nSeu IMC é classificado como: Obesidade grau III")
