# Dentro desta pasta crie um módulo em python chamado MYTOOLS com as seguintes constantes e funções:
# a.    	PI_INT que é uma string que representa as 100 primeiras casas decimais do número pi. Por exemplo para as 5 primeiras teríamos o inteiro:  14159
# b.	E_INT que é uma string que representa as 100 primeiras casas decimais do número neperiano.  Por exemplo para as 5 primeiras teríamos o inteiro:  71828
# c. 	Uma função chamada pi_real que dado um número natural N maior que 0 e menor que 100 que retorna uma string de uma aproximação pro número pi com N casa decimais: Exemplo pi_real(5) imprime 3,14159
# d.	Uma função chamada e_real que dado um número natural N maior que 0 e menor que 100 que retorna uma string de uma aproximação pro número neperiano com N casa decimais: Exemplo e_real(4) retorna 2,7182

import math

PI_INT = str(str(math.pi)[1:100])
E_INT = str(str(math.e)[1:100])

print("123123"[1:4])

print(PI_INT)
def pi_real(N):
    return int(str(math.pi).split(".")[1][0:N])

def e_real(N):
    return int(str(math.e).split(".")[1][0:N])


