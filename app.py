from flask import Flask, jsonify, render_template, request, session, url_for, redirect




app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('about.html')

######################################################################################################################
@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

    

@app.route('/send_otp', methods=['POST'])
def send_otp():
    phone_number = request.form['number']
    # Firebase uses reCAPTCHA verification by default for phone auth.
    # To manually send the OTP, you need to disable this in your Firebase console.
    # The following code assumes that you have done so.
    try:
        # phone_auth_data = auth.sign_in_with_phone_number(phone_number)
        session['verification_id'] = phone_auth_data['id']
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    otp = request.form['otp']
    verification_id = session['verification_id']
    try:
        # Verify the OTP
        # auth.sign_in_with_phone_number(otp, verification_id)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})



@app.route('/register', methods=['GET','POST'])
def register():
    return render_template('register.html')

#############################################################################

@app.route('/detail' , methods=['GET', 'POST'])
def detail():
    return render_template('cardetail.html')

@app.route('/booking' , methods=['GET', 'POST'])
def booking():
    return render_template('car_booking.html')

@app.route('/accessories' , methods=['GET', 'POST'])
def accessories():
    return render_template('car_accessories.html')

@app.route('/checkout' , methods=['GET', 'POST'])
def checkout():
    return render_template('car_checkout.html')

@app.route('/success' , methods=['GET', 'POST'])
def success():
    return render_template('car_booking_done.html')

@app.route('/contact' , methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
