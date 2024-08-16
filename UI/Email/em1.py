
from distutils import config
from email import message
from sre_constants import SUCCESS
from flask import Flask,render_template,request
from flask_mail import  Mail,Message



app = Flask(__name__)
# list1=["pavan@hexaware.com","shrunga@hexaware.com","chitra@hexaware.com","krishnendu@hexaware.com","sagar@hexaware.com","sandeep@hexaware.com","guruprasad@hexaware.com"]
app.config['MAIL_SERVER'] ='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "guruprasadsuvarna58@gmail.com"
app.config['MAIL_PASSWORD'] = "hcqpppucltwlotqz"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


mail=Mail(app)


@app.route('/')
def home():
    # return render_template("index.html")
    return render_template("index.html")
# if __name__ == '__main__':
#    app.run(debug=True,port=8000)


@app.route('/email', methods=['GET','POST'])
def email():
    #    To = request.form['To']

    #    if To in list1:
    #        return "<script>alert('Email sent successfully!')</script>"
    #    else:
    #       return "<script>alert('Invalid email address!')</script>"
    if request.method=="POST":
      To = request.form['To']
      Subject=request.form['Subject']
      msg=request.form['msg']

      message=Message(Subject,sender="guruprasadsuvarna58@gmail.com",recipients=[To])
      message.body=msg
      mail.send(message)
      success="message snt"
    return render_template("result.html",success=success)


      

@app.route('/components', methods=['GET'])
def components():
    return render_template("components.html")

if __name__ == '__main__':
    app.run(debug=True,port=8000)
