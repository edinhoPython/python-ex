from random import randint

aluno1 = str(input('nome do primeiro aluno '))
aluno2 = str(input('nome do segundo aluno '))
aluno3 = str(input('nome do terceiro aluno '))
aluno4 = str(input('nome do quarto aluno '))

alunos = [aluno1, aluno2, aluno3, aluno4]
nome_aluno = randint(0,3)

print(f'o nome do aluno sorteado foi {alunos[nome_aluno]}')