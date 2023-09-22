names = ["Jessa", "Eric", "Bob"]
pasta_names= "arquivo_de_nomes.txt"
file= open(pasta_names, "w")
for name in names:
    file.write("%s\n" % name)
file.close()