from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emails.db'
db = SQLAlchemy(app)

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

def create_tables():
    with app.app_context():
        db.create_all()

@app.route('/')
def index():
    social_links = {
        'instagram': 'https://www.instagram.com/valorant/',
        'discord': 'https://discord.com/invite/valorant',
        'vk': 'https://vk.com/valorant'
    }
    return render_template('index.html', social_links=social_links)


@app.route('/skins')
def skins():
    return render_template('skins.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')

@app.route('/support', methods=['GET', 'POST'])
def support():
    if request.method == 'POST':
        user_email = request.form['email']
        existing_email = Email.query.filter_by(email=user_email).first()

        if existing_email:
            return "Email already exists!"

        new_email = Email(email=user_email)
        db.session.add(new_email)
        db.session.commit()
        return "Email submitted successfully!"

    return render_template('support.html')


if __name__ == '__main__':
    create_tables()
    app.run(debug=True)