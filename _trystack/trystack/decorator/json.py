from functools import wraps
from flask import request
from trystack.util import jsonify

def json_required(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		if request.content_type != "application/json" :
			return jsonify(
				metadata = {
					"message": "Content type is not OK!"
				},
				status = 415,
			)
		else:
			return f(*args, **kwargs)
	return wrapper;
