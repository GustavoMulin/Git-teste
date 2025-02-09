# Descobrindo se e ímpar ou par

num = int(input("Dígite um número inteiro: "))
tipo = "par" if num % 2 == 0 else "ímpar"
print("O número {} é {}".format(num, tipo))
