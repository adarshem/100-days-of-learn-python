from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import art

# Create a question bank from the question_data
question_bank = [
    Question(question["text"], question["answer"]) for question in question_data
]

# Create a quiz_brain object from the question_bank
quiz_brain = QuizBrain(question_bank)

# Print the quiz logo
print(f"{art.quiz_logo}\n\n")
# Loop through the questions in the quiz_brain object
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

# Print the final score
quiz_brain.quiz_completed()