from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    author = "Me"
    name = "You"
    return render_template('index.html', title = 'HOME')


@app.route('/Setting')
def setting():
    return render_template('Setting.html',title = 'ABOUT')



@app.route('/about')
def about():
    return render_template('about.html',title = 'ABOUT')

@app.route('/Aggregate')
def aggregate():
    return render_template('Aggregate.html',title = 'AGGREGATE')

@app.route('/Assessment')
def assessment():
    return render_template('Assessment.html',title = 'ASSESSMENT')

@app.route('/AssessmentPlan')
def assessmentPlan():
    return render_template('AssessmentPlan.html',title = 'ASSESSMENT_PLAN')


if __name__ == '__main__':
    app.run()
