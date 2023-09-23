def calcular_juros_simples(capital, taxa, período):
    juros= capital*taxa*período
    montante=capital+juros
    return montante

def calcular_juros_compostos(capital, taxa, período):
    montante= capital* (1+taxa) ** período
    juros= montante - capital
    return montante

print("olá, seja bem vindo a calculadora de juros.")
print()
while True:
    escolha= int(input("Para começa, escolha o tipo de juros que deseja calcular.\n1=Juros Simples \n2= Juros Compostos \n3=Sair..."))
    if escolha ==1:
        capital=float(input("digite o capital inicial(em reais)..."))
        taxa=float(input("digite a taxa(em decimal)..."))
        período=int(input("digite o período(em anos)..."))
        resultado=calcular_juros_simples(capital, taxa, período)
        print(f"o montante acumulado ao redor de {período} anos é de R${resultado}")    
    
    elif escolha==2:
       capital=float(input("digite o capital inicial(em reais)..."))
       taxa=float(input("digite a taxa(em decimal)..."))
       período=int(input("digite o período(em anos)..."))
       resultado=calcular_juros_compostos(capital, taxa, período)
       print(f"o montante acumulado ao redor de {período} anos é de R${resultado}")
    
    elif escolha==3:
        break
        
    else:
        print("digite um número de 1 a 3, por favor")
        
        
        
          
           