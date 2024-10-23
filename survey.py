class Question:
    def __init__(self, question, choices):
        self.question = question
        self.choices = choices

class Survey:
    def __init__(self, title, instructions, questions):
        self.title = title
        self.instructions = instructions
        self.questions = questions

# Define your satisfaction survey questions
questions = [
    Question("Do you like our service?", ["Yes", "No"]),
    Question("Would you recommend us to others?", ["Definitely", "Maybe", "Not at all"]),
    Question("How would you rate our service?", ["Excellent", "Good", "Average", "Poor"]),
    Question("Any additional comments?", ["None", "Other comments..."])
]

# Create an instance of the Survey
satisfaction_survey = Survey(
    title="Customer Satisfaction Survey",
    instructions="Please answer the following questions:",
    questions=questions
)