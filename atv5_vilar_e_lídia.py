resultado=0

a=input("gosta de ir à praia?")
if a == "sim":
    print("certa resposta!")
    resultado+=1
else:
    print("resposta errada")

b=input("gosta de ir no shopping?")
if b == "sim":
    print("certa resposta!")
    resultado+=1
else:
    print("resposta errada")

c= input("gosta de sair de casa?")
if c == "sim":
    print("certa resposta!")
    resultado+=1
else:
    print("resposta errada")

d= input("gosta de viajar?")
if d == "não":
    print("certa resposta!")
    resultado+=1
else:
    print("resposta errada")

e= input("gosta de abóbora?")
if e == "não":
    print("certa resposta!")
    resultado+=1
else:
    print("resposta errada")

f= input("gosta de azeitona?")
if f == "sim":
    print("certa resposta!")
    resultado+=1
else:
    print("resposta errada")

g= input("gosta de pícles?")
if g == "não":
    print("certa resposta!")
    resultado+=1
else:
    print("resposta errada")

h= input("gosta de beber água?")
if h == "sim":
    print("certa resposta!")
    resultado+=1
else:
    print("resposta errada")

i= input("gosta de verduras?")
if i == "sim":
    print("certa resposta!")
    resultado+=1
else:
    print("resposta errada")

j= input("gosta de barulho?")
if j == "não":
    print("certa resposta!")
    resultado+=1
else:
    print("resposta errada")

print(f"parabéns, seu resultado foi {resultado}/10")
