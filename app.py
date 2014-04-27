import os
from urlparse import urlparse
from flask import Flask
from flask import render_template
from flask import request
# from flask.ext.mongoengine import MongoEngine
from pymongo import MongoClient
from pymongo import Connection

app = Flask(__name__)
# app.config['MONGODB_SETTINGS'] = {'db':'critical_make'}
# app.config['SECRET_KEY'] = "critical1"

MONGO_URL = os.environ.get('MONGOHQ_URL')

if MONGO_URL:
	connection = Connection(MONGO_URL)
	db = connection[urlparse(MONGO_URL).path[1:]]
else:
	client = MongoClient('localhost',27017)
	db = client.critical_make
	collection = db.people
	print "made connection!"



# def register_blueprints(app):
#     # Prevents circular imports
#     from views import user
#     app.register_blueprint(user)

# register_blueprints(app)

@app.route('/',methods=['GET','POST'])
def index():
	return render_template('index.html')

@app.route('/data', methods=['GET','POST'])
def data():
	error = None
	if request.method == 'GET':
		person = request.args.get('personId')
		receiver = request.args.get('receiverId')
		myData = {person:receiver}
		collection.insert(myData)
		return "Thanks!"

# @app.route('/me/<my_id>',methods=['GET','POST'])
# def view_me():
# 	return render_template()




# @app.route('/user/<username>', methods=['GET','POST'])
# def user_profile(username):
# 	user = mongo.db.users.find_one_or_404({'_id':username})
# 	return render_template('user.html', user=user)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
