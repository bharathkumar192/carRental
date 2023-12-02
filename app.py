from flask import Flask, jsonify, render_template, request, session, url_for, redirect



user_mail=''
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', show_item='', display=1)


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
        # session['verification_id'] = phone_auth_data['id']
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


import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(otp, recipient_email):
    sender_email = "maadhavi.nirati@gmail.com"
    sender_password = "ovqz pbvb vmmt umgz"

    # Create message
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Your OTP"
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Create the body of the message
    html = '''<html>
        <head>
            <style>
                .otp-style {{
                    font-size: 18px;
                    color: #333333;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <p>Your OTP is: <span class="otp-style">{}</span></p>
        </body>
        </html>'''.format(otp)


    part2 = MIMEText(html, 'html')

    # Attach parts into message container
    msg.attach(part2)

    # Send the message via local SMTP server
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(sender_email, sender_password)
    mail.sendmail(sender_email, recipient_email, msg.as_string())
    mail.quit()


def generate_otp():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])


@app.route('/validate', methods=['GET','POST'])
def validate():
    global user_mail
    data = request.json
    email = data['email']
    user_mail = email
    otp = generate_otp()
    print(otp)
    send_email(otp, email)
    return render_template('login.html')

@app.route('/logged', methods=['POST','GET'])
def logged():
    return render_template('index.html', user_email=user_mail, display='',show_item=1)

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
