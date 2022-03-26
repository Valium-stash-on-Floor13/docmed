from flask import Flask, render_template, request
app = Flask(__name__)
from bot import medbot

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')



@app.route('/get')
def get_bot_response():
    userText=request.args.get('msg')
    return str(medbot.chat(userText))
    

@app.route('/about')
def about_page():
    return render_template("about.html")




if __name__ == "__main__":
    # turn debug mode off after production   
    app.run()