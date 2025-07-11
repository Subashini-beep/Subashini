from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Create a database model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    ph=db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return f"Users('{self.name}', '{self.email}','{self.ph}')"

# Create the database
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    users = Users.query.all()  # Get all users from the database
    return render_template('home.html', users=users)

@app.route("/add", methods=["POST"])
def add_user():
    name = request.form.get("name")
    email = request.form.get("Email")
    ph = request.form.get("ph")

    if name and email and ph:
        new_user = Users(name=name, email=email,ph=ph)
        db.session.add(new_user)
        db.session.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)