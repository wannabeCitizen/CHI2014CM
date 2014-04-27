import datetime
from flask import url_for
from chi_app import db
from slugify import slugify

class Participant(db.Document):
	created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
	name = db.StringField(max_length=255, required=True, unique=True)
	slug = db.StringField(max_length=255, required=False)
	data = db.DictField(required=True)
	#Can add an embedded data structure later if necessary
	# comments = db.ListField(db.EmbeddedDocumentField('Extra'))

	def get_absolute_url(self):
	   return url_for('participant', kwargs={'slug': self.slug})

	def __unicode__(self):
	   return self.name

	meta = {
	   'ordering': ['-created_at']
	}


   #Class for extra things like graphs that we may need later
   # class Extra(db.EmbeddedDocument):
   #  created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
   #  body = db.StringField(verbose_name="Comment", required=True)
   #  author = db.StringField(verbose_name="Name", max_length=255, required=True)