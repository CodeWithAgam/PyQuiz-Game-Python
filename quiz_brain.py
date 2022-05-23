class QuizBrain:
    def __init__(self, question_list):
        """Function to initialize the QuizBrain class"""
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_question(self):
        """Function to check if there are still questions left"""
        return self.question_number < len(self.question_list)

    def new_question(self):
        """Function to return a new question"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        question = current_question.question
        user_answer = input(f"Q{self.question_number}: {question} - True/False: ").lower()
        self.check_answer(user_answer, current_question.answer) 
    
    def check_answer(self, user_answer, correct_answer):
        """Function to check if the answer is correct"""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect!")
        print(f"Correct Answer is: {correct_answer}")
        print(f"Your Current Score is {self.score}/{self.question_number}\n")