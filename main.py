from flask import Flask, render_template, url_for, flash, redirect, request
from flask_mail import Mail, Message
# from firebase import firebase
# firebase1 = firebase.FirebaseApplication(f'https://srideviconstructions-f8cea-default-rtdb.asia-southeast1.firebasedatabase.app/', None)
app = Flask(__name__)
# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = firebase1.get('server_email', None)
# app.config['MAIL_PASSWORD'] = firebase1.get('server_pass', None)
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True

# mail = Mail(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/services")
def servicess():
    return render_template('services.html')



@app.route("/contact", methods=['GET', 'POST'])
def contactus():
    # if request.method == 'POST':
    #     name = request.form.get('name')
    #     email = request.form.get('email')
    #     phone = request.form.get('phone')
    #     req = request.form.get('requirments')
    #     msgBody = f"Name: {name} \nEmail: {email} \nPhone: {phone} \nRequirement: {req}"
    #     msg = Message(subject=f"Service request from {name}", body=msgBody, sender='info.builtintech', recipients=['akshithmysa.physics@gmail.com', firebase1.get('server_email', None)])
    #     mail.send(msg)
    #     return render_template('contactus.html', msgSent=True)
    #     # return 'sent'
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)