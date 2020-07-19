from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/TESTDB'
db = SQLAlchemy(app)


class Staff(db.Model):
    __tablename__ = 'Staff'

    ID = db.Column(db.String(10), primary_key=True)
    Name = db.Column(db.String(10), nullable=False)
    DeptId = db.Column(db.String(10), nullable=False)
    Age = db.Column(db.Integer)
    Gender = db.Column(db.String(3))
    Salary = db.Column(db.Integer)
    RecordDt = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return "<User(name='%s', record='%s'>" % (self.Name, self.RecordDt)
