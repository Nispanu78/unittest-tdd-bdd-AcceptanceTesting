from flask import Flask, render_template, request
from bank.bank import Bank
app = Flask(__name__)
BANK = Bank()


@app.route('/')
def hello_world():
    account_number = request.args.get('account_number')
    balance = BANK.get_account_balance(account_number)
    return render_template('index.html', balance=balance)


if __name__ == '__main__':
    app.run(debug=True)
