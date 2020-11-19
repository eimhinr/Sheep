class AnswerCard():

    # answers = set_answeers()
    # answers = set_answeers()

    def __init__(self, user_name, score):
        self.user_name = user_name
        self.score = score
        self.answers = answers

    def set_answers(self):
        ans = {}
        for i in range(0,26):
            ans[str(i)] = i+9
        return ans

    def create_new_card(self, list_of_answers):
        self.answers = set_answers(self)

    def update_answers(self):
        pass

test = AnswerCard("eimhin", 0)

print(i for i in test.answers.values)