altura= float(input("digite sua altura(em metros)..."))
peso= float(input("digite seu peso(em quilogramas)..."))
result= peso/(altura**2)

if result<18.5:
    print(f"seu imc foi {result}. Seu peso está abaixo da média")
elif result>=18.5 and result<=24.9:
    print(f"seu imc foi {result}. Seu peso está na média")
elif result>=25 and result<=29.9:
    print(f"seu imc foi {result}. Seu peso está acima da média")
elif result>=30 and result<=34.9:
    print(f"seu imc foi {result}. Seu peso está em obesidade grau 1")
elif result>=35 and result<=39.9:
    print(f"seu imc foi {result}. Seu peso está em obesidade grau 2")
else:
    print(f"seu imc foi {result}. Seu peso está em obesidade grau 3")
