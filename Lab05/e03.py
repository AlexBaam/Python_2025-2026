class Question:
    def __init__(self, text, points):
        self.text = text
        self.points = points

    def check(self, answer):
        return f'{answer}'

class SingleChoiceQuestion(Question):
    def __init__(self, text, points, options, correct):
        super().__init__(text, points)
        self.options = options
        self.correct = correct

    def check(self, answer):
        if answer == self.correct:
            return True
        else:
            return False

class MultiChoiceQuestion(Question):
    def __init__(self, text, points, options, corrects):
        super().__init__(text, points)
        self.options = options
        self.corrects = corrects

    def check(self, answers):
        count = 0

        for answer in answers:
            if answer in self.corrects:
                count += 1

        if count == len(self.corrects):
            return True
        else:
            return False

class OpenQuestion(Question):
    def __init__(self, text, points, answer):
        super().__init__(text, points)
        self.answer = answer

    def check(self, answer):
        if answer == self.answer:
            return True
        else:
            return False

class Quiz:
    def __init__(self, title, questions):
        self.questions = questions
        self.title = title

    def add_question(self, question):
        self.questions.append(question)

    def evaluate_quiz(self, answers):
        total = 0

        for answer in answers:
            if self.questions[answers.index(answer)].check(answer):
                total += self.questions[answers.index(answer)].points

        print(f'{total} points')


FirstQuestion = SingleChoiceQuestion('Cate degete am?', 10, [5,10,15,20], 20)
SecondQuestion = MultiChoiceQuestion('De ce sunt aici?', 10, ['A', 'B', 'C'], ['C', 'B'])
ThirdQuestion = OpenQuestion('Cati ani am?', 30, '22 de ani')

New_Quiz = Quiz("My quiz", [FirstQuestion, SecondQuestion])
New_Quiz.add_question(ThirdQuestion)

New_Quiz.evaluate_quiz([20, ['C', 'B'], '22 de ani'])