questions = [
    {
        'question' : 'Quanto é 2+2?',
        'options' : ['2', 'não sei', '4', 'pi', 'e'],
        'answer' : '4'
    },
    {
        'question' : 'Quanto é 10 / 2',
        'options' : ['5', 'não sei', '4', 'pi', 'e'],
        'answer' : '5'
    },
    {
        'question' : 'Qual  hipotenusa de um triângulo cujo catetos valem 3 e 2',
        'options' : ['2', 'não sei', '4', 'pi', '5'],
        'answer' : '5'
    },
    {
        'question' : 'Qual a melhor linguagem de programação do mundo?',
        'options' : ['C', 'Python', 'Java', 'Depende', 'HTML'],
        'answer' : 'Depende'
    },
]

num_of_questions = len(questions)
correct = 0

while True:
    n = 0
    question = questions[n]

    answer = input('Escolha uma opção e aperte enter: ')

    if answer.lower() == 'q':
        break

    n = num_of_questions % n + 1

print(f'Você acertou {correct} perguntas de {num_of_questions}!')




