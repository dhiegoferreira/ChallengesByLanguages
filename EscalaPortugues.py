Mat = float(input("Nota de Matemática: "));  #Recebe a nota de Matemática.
Lig = float(input("Nota de Lingugagens: ")); #Recebe a nota de Linguagens.
Red = float(input("Nota da Redação: ")) #Recebe a nota de Redação.


Mat = Mat*0.8 # 80% da nota de matemática 
Lig = Lig*0.1 # 10% da nota de linguagens
Red = Red*0.1 # 10% da nota de redação

SomaNota = float(Mat + Lig + Red) #Soma as notas das três áreas.

CalculaNota = (SomaNota*20)/1000 #Formula da escala portuguesa.

print("=========================");
print(CalculaNota); #Saida do resultado.
