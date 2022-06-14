from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////SQL/db_water.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////opt/WGBOT/tokens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class DB_water(db.Model):
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False, primary_key=True)
    status = db.Column(db.String(10), nullable=False)
    value = db.Column(db.String(10), nullable=False)


@app.route('/')
def first():
    return "Hello"


@app.route('/street_bath/<status>/<value>', methods=['GET', 'POST'])
def street_bath(status, value):
    print(status)
    print(value)
    if status == "ok":
        try:
            db_add = DB_water(status=status, value=value)
            db.session.add(db_add)
            db.session.commit()


        except:
            db_add = DB_water(status="Error", value="db_add error")
            db.session.add(db_add)
            db.session.commit()

    return str(f"{status} {value}")


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=80)
