from flask import Flask, render_template
from model_with_sqlalchemy import db
from model_with_sqlalchemy import Staff
from model_with_sqlalchemy import app

# app = Flask(__name__, static_url_path='/static', static_folder='./static')

@app.route('/show_staff')
def hello_google():
    staff_data = [[d.ID, d.Name, d.DeptId, str(d.Age), d.Gender, d.Salary] for d in db.session.query(Staff)]
    print(staff_data)
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                                              column=column)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
