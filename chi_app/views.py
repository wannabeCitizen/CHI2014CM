from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from slugify import slugify

from flask.ext.mongoengine.wtf import model_form
from chi_app.models import *

user = Blueprint('chi_folk', __name__, template_folder='templates')

class Search(MethodView):

	def get(self):
		name = request.args.get('name', '')

class Home(MethodView):

	def get(self):
		return render_template('chi_folk/home.html')

user.add_url_rule('/', view_func=Home.as_view('home'))