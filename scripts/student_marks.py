from flask import Flask, render_template
app = Flask(__name__)

@app.route('/std')
def stdMarks():
    dict={'Srujan':100, 'Swetha':200, 'Parthiv':300, 'Jay':400}
    return render_template('student_marks.html', marks=dict)

if __name__=='__main__':
    app.run(debug=True)
