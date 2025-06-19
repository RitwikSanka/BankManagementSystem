from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Account(db.Model):
    accNo = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    balance = db.Column(db.Float, nullable=False)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        accNo = request.form['accNo']
        name = request.form['name']
        balance = request.form['balance']
        acc = Account(accNo=accNo, name=name, balance=balance)
        db.session.add(acc)
        db.session.commit()
        return redirect(url_for('list_accounts'))  # Go to account list after creation
    return render_template('create.html')

@app.route('/get-account/<int:accNo>', methods=['GET'])
def get_account(accNo):
    acc = Account.query.get(accNo)
    if acc:
        return jsonify({
            "accNo": acc.accNo,
            "name": acc.name,
            "balance": acc.balance
        })
    return jsonify({"error": "Account not found"}), 404

@app.route('/deposit/<int:accNo>', methods=['GET', 'POST'])
def deposit(accNo):
    acc = Account.query.get(accNo)
    if not acc:
        return "Account not found", 404

    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            if amount <= 0:
                return render_template('deposit.html', acc=acc, error="Amount must be positive.")
            acc.balance += amount
            db.session.commit()
            return redirect(url_for('list_accounts'))
        except ValueError:
            return render_template('deposit.html', acc=acc, error="Invalid input.")
    
    return render_template('deposit.html', acc=acc)


@app.route('/withdraw/<int:accNo>', methods=['GET', 'POST'])
def withdraw(accNo):
    acc = Account.query.get(accNo)
    if not acc:
        return "Account not found", 404

    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            if amount <= 0:
                return render_template('withdraw.html', acc=acc, error="Amount must be positive.")
            if amount > acc.balance:
                return render_template('withdraw.html', acc=acc, error="Insufficient balance.")
            acc.balance -= amount
            db.session.commit()
            return redirect(url_for('list_accounts'))
        except ValueError:
            return render_template('withdraw.html', acc=acc, error="Invalid input.")
    
    return render_template('withdraw.html', acc=acc)




@app.route('/delete/<int:accNo>', methods=['POST'])
def delete_account(accNo):
    acc = Account.query.get(accNo)
    if acc:
        db.session.delete(acc)
        db.session.commit()
    return redirect(url_for('list_accounts'))


@app.route('/list')
def list_accounts():
    accounts = Account.query.all()
    return render_template('list.html', accounts=accounts)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
