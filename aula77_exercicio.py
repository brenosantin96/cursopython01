#Exercício - Sistema de perguntas e respostas:

questions = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

QtQuestions = len(questions)
QtAnsweredCorrect = 0
answeredQuestions = 0

while (answeredQuestions < QtQuestions):
    
    for question in questions:
        answer = input(question.get("Pergunta"))
        answeredQuestions = answeredQuestions + 1
        if(answer == question.get('Resposta')):
            print(question.get('Resposta'))
            QtAnsweredCorrect = QtAnsweredCorrect + 1
            

print(f'De {QtQuestions} perguntas, voce acertou {QtAnsweredCorrect} perguntas.')
        
    
    
        
