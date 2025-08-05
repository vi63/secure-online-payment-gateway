from flask import Flask, render_template, request, redirect, session, flash, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/send_otp', methods=['POST'])
def send_otp():
    email = request.form['email']
    otp = str(random.randint(100000, 999999))
    session['otp'] = otp
    session['email'] = email
    print("Generated OTP (simulate email):", otp)  # Simulation only
    return render_template('otp.html')

@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    user_otp = request.form['otp']
    if user_otp == session.get('otp'):
        return redirect('/payment')
    else:
        flash("Invalid OTP. Try again.")
        return render_template('otp.html')

@app.route('/payment')
def payment():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    card_number = request.form['card_number']
    cvv = request.form['cvv']
    expiry = request.form['expiry']
    name = request.form['name']
    amount = request.form['amount']

    if len(cvv) != 3 or not cvv.isdigit():
        flash("Invalid CVV. Please enter a 3-digit CVV.")
        return redirect('/payment')

    # Simulate basic card validation
    if card_number != "1234567812345678" or cvv != "123":
        flash("Transaction failed: Incorrect card details.")
        return redirect('/payment')

    flash("Payment successful!")
    return render_template('success.html', name=name, amount=amount)

if __name__ == '__main__':
    app.run(debug=True)

