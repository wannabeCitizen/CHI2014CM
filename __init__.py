import os
from flask import Flask
from flask import render_template
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'DB':'critical_make'}
app.config['SECRET_KEY'] = "critical1"

db = MongoEngine(app)


def register_blueprints(app):
    # Prevents circular imports
    from views import user
    app.register_blueprint(user)

register_blueprints(app)

# @app.route('/',methods=['GET','POST'])
# def index():
# 	return render_template('index.html')


# @app.route('/user/<username>', methods=['GET','POST'])
# def user_profile(username):
# 	user = mongo.db.users.find_one_or_404({'_id':username})
# 	return render_template('user.html', user=user)

if __name__ == '__main__':
	#Change this later
	app.debug = True
	app.run(port=5000)