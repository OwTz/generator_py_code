#gerador de senha Interativo com o usuário

import random
tamanho=int(input("digite aqui o tamanho da senha que deseja: "))

#aqui está insero todos os tipos de letras/simbolos que quer q a senha contenha!
lower_case = "qwertyuiopasdfghjklçzxcvbnm"
Uper_case = "QWERTYUIOPASDFGHJKLÇZXCVBNM"
numbers_case="1234567890"
symbols_case = "!@#$%&*()"

for_pass = lower_case+Uper_case+symbols_case+numbers_case
#definindo tamanho da senha que agora está com a variável, para o usuário decidir
tamanho_da_senha = tamanho
#
password="".join(random.sample(for_pass, tamanho_da_senha))
print("a senha gerada é: ", password)
