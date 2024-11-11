class QuizBrain:

    def __init__(self, q_list):

        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        """Return True if there are still questions or False if there are no question"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """If user get correct or worng answer then move to next question"""
        score = 0
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        """check the user answer if correct or not"""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


#*******************************************************************
        """Code below is different method to solve the proble."""
#*******************************************************************

    # def next_question(self):
    #     game_on = True
    #     score = 0
    #     while game_on:
    #
    #         current_question = self.question_list[self.question_number]
    #         self.question_number += 1
    #         answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
    #
    #         if answer == current_question.answer:
    #             score += 1
    #             print("You got it right!")
    #             print(f"The correct answer was: {current_question.answer}")
    #             print(f"Your current score is: {score}/{self.question_number}")
    #             print("\n")
    #             game_on = True
    #         else:
    #             print(f"Your final score is: {score}")
    #             game_on = False


