import random
tamanho = int(input("digite o numero de caracteres você quer seu e-mail: "))
mailbox = "@gmail.com"
lower_case = "qwertyuiopasdfghjklçzxcvbnm"
Uper_case = "QWERTYUIOPASDFGHJKLÇZXCVBNM"
numbers_case="1234567890"
symbols_case = "!@#$%&*()"


for_pass = lower_case+Uper_case+numbers_case
mail_pass =for_pass

tamanho_mail=tamanho

mail="".join(random.sample(mail_pass, tamanho_mail))
mail_f=mail+mailbox
print("o E-mail gerado é: ", mail_f)
