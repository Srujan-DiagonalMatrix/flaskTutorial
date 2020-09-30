from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/student1')
def student():
    return render_template('formData_to_student.html')

@app.route('/student_result', methods=['POST','GET'])
def result():
    if request.method=='POST':
        std_result = request.form
        return render_template('formData_to_result.html', result=std_result)

if __name__=='__main__':
    app.run(debug=True)
