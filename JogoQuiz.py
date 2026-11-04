print("Bem-vindo ao meu JogoQuiz \n Jogo Interessante de Jogar")
Player = input ("Você quer jogar o jogo e se sentir menos burro, Fedelho? \n")
if Player.lower() != 'sim':
    print("Good Bye")
    quit()

name_player = input("Coloque seu Nome: ")

print("Vamos Começar o Jogo,",name_player,)

score = 0

answer = input(' Qual é o nome completo da sigla HTML? \n')
if answer.lower() == 'hypertext markup language':
    print("Resposta Certa, Fedelho")
    score += 1
else:
    print('Resposta Errada, seu Trolho!')

answer = input(' Qual é o nome da sigla CPU? \n')
if answer.lower() == 'central processing unit':
    print("Resposta Certa, Fedelho")
    score += 1
else:
    print('Resposta Errada, seu Trolho!')

answer = input(' Qual é o nome da sigla RAM? \n')
if answer.lower() == 'random access memory':
    print("Resposta Certa, Fedelho")
    score += 1
else:
    print('Resposta Errada, seu Trolho!')

print("Você obteve " + str(score)+ " respostas certas")
print("Você obteve " + str((score / 3) *100)+ " de aproveitamento")
