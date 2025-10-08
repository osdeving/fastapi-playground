questions = [
    {
        'question' : 'Quanto é 2+2?',
        'options' : ['2', 'não sei', '4', 'pi', 'e'],
        'answer' : '4'
    },
    {
        'question' : 'Quanto é 10 / 2?',
        'options' : ['5', 'não sei', '4', 'pi', 'e'],
        'answer' : '5'
    },
    {
        'question' : 'Qual  hipotenusa de um triângulo cujo catetos valem 3 e 2?',
        'options' : ['2', 'não sei', '4', 'pi', '5'],
        'answer' : '5'
    },
    {
        'question' : 'Qual a melhor linguagem de programação do mundo?',
        'options' : ['C', 'Python', 'Java', 'Depende', 'HTML'],
        'answer' : 'Depende'
    },
]

number_of_questions = len(questions)
correct_answers = 0
actual_question = 0

while True:
    question = questions[actual_question]

    print('\n', question['question'], '\n')

    [print(f"{chr(65+i)}) {opt}") for i, opt in enumerate(question["options"])]

    answer = input('\nEscolha uma opção e aperte enter: ').lower()

    if answer == 'q':
        break

    chosen = question['options'][ord(answer) - ord('a')]

    if chosen == question['answer']:
        correct_answers += 1
        print("✅ Correto!")
    else:
        print("❌ Errado!")

    actual_question = (actual_question + 1) % number_of_questions

print(f'\nVocê acertou {correct_answers} perguntas de {number_of_questions}!')




