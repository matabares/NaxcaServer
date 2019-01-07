from flask import Flask

app = Flask(__name__)



from mod_rts.controller import mod_rts as mod_rts

app.register_blueprint(mod_rts)



if __name__ == '__main__':
    app.run(debug=True)