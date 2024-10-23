from flask import Flask, render_template, redirect, url_for, session, request, flash
import os
from survey import satisfaction_survey  # Adjust this import as necessary

app = Flask(__name__)

# Set secret key from environment variable
app.secret_key = os.environ.get("SECRET_KEY", "a_default_secret_key")  # Default for development

@app.route('/')
def start():
    return render_template('start.html', survey=satisfaction_survey)

@app.route('/start', methods=["POST"])
def start_survey():
    session["responses"] = []
    return redirect(url_for('question', question_id=0))

@app.route('/questions/<int:question_id>')
def question(question_id):
    responses = session.get("responses")
    if responses is None or question_id != len(responses):
        flash("You are trying to access an invalid question.")
        return redirect(url_for('start'))
    
    if question_id >= len(satisfaction_survey.questions):
        return redirect(url_for('thank_you'))

    question = satisfaction_survey.questions[question_id]
    return render_template('question.html', question=question, question_id=question_id)

@app.route('/answer', methods=["POST"])
def handle_answer():
    answer = request.form['answer']
    responses = session['responses']
    responses.append(answer)
    session['responses'] = responses

    if len(responses) == len(satisfaction_survey.questions):
        return redirect(url_for('thank_you'))
    
    return redirect(url_for('question', question_id=len(responses)))

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == "__main__":
    app.run(debug=True)