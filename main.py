from modules import Question_class

question_list = Question_class.question_list

with open('modules/test.txt', encoding='utf-8') as quest_list:
    for line in quest_list:
        line = line.replace('\n', '')
        sep_list = line.split('/')

        for val in sep_list:
            if '(True)' in val:
                correct = val.replace('(True)', '')

        quest = sep_list[0]
        answer1 = sep_list[1].replace('(True)', '')
        answer2 = sep_list[2].replace('(True)', '')
        answer3 = sep_list[3].replace('(True)', '')

        question = Question_class.Question(quest=quest, answer1=answer1, answer2=answer2,
                                           answer3=answer3, correct=correct)
        question_list.append(question)

if __name__ == '__main__':
    print('Это тест по информатике из 10 вопросов.')
    print()
    for i, items in enumerate(question_list):
        items.start(i)

points = 0
for elem in question_list:
    points += elem.point
avg_points = points / len(question_list)
grade = ''
if avg_points < 0.6:
    grade = 'Неудовлетворительно'
elif 0.6 <= avg_points < 0.8:
    grade = 'Удовлетворительно'
elif 0.8 <= avg_points < 0.95:
    grade = 'Хорошо'
else:
    grade = 'Отлично'

print()
print()
print(f'Набрано {points} правильных ответов \nОценка: {grade}')
