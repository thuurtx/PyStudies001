import random

#MENU
def menu():
   print("\n==== TESTE DE COVID ====")
   print("Digite [1] Para ENTRAR ou [2] para SAIR")
   menu_choice = int(input())
   while menu_choice != 1 and menu_choice != 2:
      print("\nESCOLHA INVÁLIDA")
      print("\nDigite [1] Para ENTRAR ou [2] para SAIR")
      menu_choice = int(input())
   if menu_choice == 2:
      print("\n\n ==== PROGRAMA FINALIZADO ====\n\n")
      exit()

#SAUDAÇÕES
def saudacoes():
   saud1 = "\nOlá, seja bem vindo ao teste de covid online!"
   saud2 = "\nBem vindo ao teste de covid online, esperamos suprir sua demanda da melhor forma possível!"
   saud3 = "\nEsse é o teste de covid online, seja bem vindo!"
   x = random.randint(1,3)
   if x == 1:
      print(saud1)
   if x == 2:
      print(saud2)
   if x == 3:
      print(saud3)
   
#USUÁRIOS
def users():
   var_entrevistados = int(input("Quantas pessoas realizarão o teste?"))
   return var_entrevistados

#COLETA DE DADOS
def coleta_dados(var_entrevistados):
   cont_principal_quant = var_entrevistados
   cont_principal = 0
   cont_febre = 0
   cont_tosse = 0
   cont_paladar = 0
   cont_olfato = 0
   cont_palolf = 0
   while cont_principal < cont_principal_quant:
      print("\nResponda as seguintes perguntas com 'SIM' OU 'NÃO'.\n\nTem sintomas febris? [1] SIM ou [2] NÃO")
      resp1=int(input())
      print("\n Está com tosse? [1] SIM ou [2] NÃO\n")
      resp2=int(input())
      print("\n Apresenta falta de paladar? [1] SIM ou [2] NÃO\n")
      resp3=int(input())
      print("\n Apresenta Falta de Olfato? [1] SIM ou [2] NÃO")
      resp4=int(input())
      if resp3 == 1 or resp4 == 1:
         diag1 = "\nVocê deve ir ao médico urgentemente!"
         print(diag1)
      else:
         if resp3 == 2 or resp4 == 2:
            diag2 = "\nVocê deve aguardar em casa."
            print(diag2)
      cont_febre, cont_tosse, cont_paladar, cont_olfato, cont_palolf = calculo(resp1, resp2, resp3, resp4, cont_febre, cont_tosse, cont_paladar, cont_olfato, cont_palolf)
      cont_principal = cont_principal + 1

#CÁLCULO
def calculo(resp1, resp2, resp3, resp4, cont_febre, cont_tosse, cont_paladar, cont_olfato, cont_palolf):
   if resp1 == 1:
      cont_febre = cont_febre + 1
   if resp2 == 1:
      cont_tosse = cont_tosse + 1
   if resp3 == 1:
      cont_paladar = cont_paladar + 1
   if resp4 == 1:
      cont_olfato = cont_olfato + 1
   if resp3 == 1 and resp4 == 1:
      cont_palolf = cont_palolf + 1
   print("\nNúmero de pessoas que apresentaram febre:", cont_febre)
   print("\nNúmero de pessoas que apresentaram tosse:", cont_tosse)
   print("\nNúmero de pessoas que apresentaram paladar:", cont_paladar)
   print("\nNúmero de pessoas que apresentaram olfato:", cont_olfato)
   print("\nNúmero de pessoas que apresentaram perda de olfato e paladar:", cont_palolf)
   return cont_febre, cont_tosse, cont_paladar, cont_olfato, cont_palolf

#FIM
def fim():
   print("\n==== FIM DO TESTE DE COVID ====")
