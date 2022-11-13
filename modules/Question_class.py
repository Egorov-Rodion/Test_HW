class Question:
    def __init__(self, quest='', answer1='', answer2='', answer3='', correct='', decision='', point=0):
        self.quest = quest
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.correct = correct
        self.decision = decision
        self.point = point

    def start(self, i):
        print(question_list[i].quest)
        print(question_list[i].answer1)
        print(question_list[i].answer2)
        print(question_list[i].answer3)
        while True:
            choice = input('Выберите вариант ответа: \n'
                           'Введите "1", "2", "3": ')
            if choice not in ['1', '2', '3']:
                print('Пожалуйста, введите цифры "1", "2" или "3".')
            else:
                break

        if choice == '1':
            question_list[i].decision = question_list[i].answer1
        elif choice == '2':
            question_list[i].decision = question_list[i].answer2
        elif choice == '3':
            question_list[i].decision = question_list[i].answer3
            
        if question_list[i].decision == question_list[i].correct:
            self.point = 1


question_list = []
