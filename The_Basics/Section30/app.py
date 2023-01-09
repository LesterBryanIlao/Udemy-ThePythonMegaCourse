from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:superuser@localhost/height_collector'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = round(float(request.form["height_name"]),1)
        
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()

            avg_height = db.session.query(func.avg(Data.height_)).scalar()
            avg_height = round(avg_height, 1)

            count = db.session.query(Data.height_).count()
            send_email(email, height, avg_height, count)
            return render_template('success.html')

    return render_template('index.html', text="Email already provided a response.")


# @app.route('/success', methods=['POST'])
# def success():
#     global file
#     if request.method == 'POST':
#         file = request.files["file"]
#         file.save(secure_filename("uploaded"+file.filename))
#         with open("uploaded"+file.filename, "a") as f:
#             f.write("I added this.")
#         return render_template('index.html')

#     return render_template('index.html', btn="download.html")

# @app.route('/download')
# def download():
#     return send_file("uploaded"+file.filename, attachment_filename="yourfile.csv", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
