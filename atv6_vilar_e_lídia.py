perguntas= ["gosta de ir à praia?",
            "gosta de ir no shopping?",
            "gosta de sair de casa?",
            "gosta de viajar?",
            "gosta de abóbora?",
            "gosta de azeitona?",
            "gosta de picles?",
            "gosta de beber água?",
            "gosta de verduras?",
            "gosta de barulho?"]

respostas= ["sim",
            "sim",
            "sim",
            "sim",
            "não",
            "sim",
            "não",
            "sim",
            "não",
            "não"]

resultado=0

for i in range(10):
    x= input(perguntas[i])
    if x==respostas[i]:
        print("acertou")
        resultado+=1
    else: 
        print("errou")

if resultado>0:
    print(f"sua pontuação foi {resultado}, parabéns!")
else:
    print(f"sua pontuação foi {resultado}")
        
        