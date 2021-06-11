from flask import Flask

application = Flask(__name__)

@application.route('/',methods=['GET','POST'])
def index():
    return "Flask application is running and created by Avnish Yadav"



if __name__=="__main__":
    application.run()



