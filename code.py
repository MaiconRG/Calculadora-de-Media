print("Calculadora Media de Aprovação")
aluno = str(input("Nome Do Aluno:"))
ra = int(input("Registro do Aluno:"))
n1 = float(input("Qual a Nota do Primeiro Bimestre :"))
n2 = float(input("Qual a Nota do Segundo Bimestre :"))
n3 = float(input("Qual a Nota do Terceiro Bimestre :"))
n4 = float(input("Qual a Nota do Quarto Bimestre :"))
media = n1 + n2 + n3 + n4
mf = media / 4

print("Aluno:",(aluno))
print("RA:",(ra))
print("Nota do 1° Bimestre:",(n1),"Nota do 2° Bimestre:",(n2),"Nota do 3° Bimestre:",(n3),"Nota do 4° Bimestre:",(n4))
print("Media Final:",(mf))

if mf > 7:
    print("Aluno:",(aluno),"Matricula:",(ra),"Estatus: Aprovado, Com Media:",(mf))
elif  mf > 3 :
    print("Aluno:",(aluno),"Matricula:",(ra),"Estatus: Em Recuperação, Com Media:",(mf))
else:
    print("Aluno:",(aluno),"Matricula:",(ra),"Estatus: Reprovado, Com Media:",(mf))