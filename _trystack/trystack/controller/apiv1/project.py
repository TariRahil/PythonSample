from flask import request
from trystack.util import jsonify
from trystack.model import Project
from trystack.decorator import json_required
from trystack.schema.apiv1 import ProjectSchema
from trystack.trystack import db

class ProjectController:
	@json_required
	def get_projects():
		try:
			projects = Project.query.all()
		except Exception as e:
			print(e)
			return jsonify(status=500)
		projects_schema = ProjectSchema(many = True)
		return jsonify({"projects":projects_schema.dump(projects)})
		
	@json_required
	def get_project(project_id):
		try:
			project = Project.query.get(project_id)
		except Exception as e:
			print(e)
			return jsonify(status=500)
		if project is None:
			return jsonify(status=404)
		project_schema = ProjectSchema()
		return jsonify(
			{"project": project_schema.dump(project)}
		)
		
	@json_required
	def create_project():
		project_schema = ProjectSchema(only=["name"])
		try:
			request_data = project_schema.load(request.get_json())
		except Exception as e:
			print(e)
			return jsonify(status=400)
		if not request_data["name"]:
			return jsonify(status=400)
		try:
			project = Project.query.filter_by(name= request_data["name"]).first()
		except Exception as e:
			print(e)
			return jsonify(status=500)
		if project is not None:
			return jsonify(status=404)
		project = Project(name=request_data["name"])
		db.session.add(project)
		try:
			db.session.commit()
		except Exception as e:
			print(e)
			db.session.rollback()
		project_schema=ProjectSchema()
		return jsonify(
			state = {"project":project_schema.dump(project)},
			status = 201
		)
		
	@json_required
	def update_project(project_id):
		project_schema = ProjectSchema(only=["status"])
		try:
			request_data = project_schema.load(request.get_json())
		except Exception as e:
			print(e)
			return jsonify(status=400)
		if request_data["status"] < 0 or request_data["status"] > 1:
			return jsonify(status=400)
		try:
			project=Project.query.get(project_id)
		except Exception as e:
			print(e)
			return jsonify(status=500)
		if project is None:
			return jsonify(status=404)
		project.status=request_data["status"]
		try:
			db.session.commit()
		except Exception as e:
			print(e)
			db.session.rollback()
		project_schema=ProjectSchema()
		return jsonify(
			{"project":project_schema.dump(project)}
		)
		
	@json_required
	def delete_project(project_id):
		try:
			project = Project.query.get(project_id)
		except Exception as e:
			print(e)
			return jsonify(status=500)
		if project is None:
			return jsonify(status=404)
		db.session.delete(project)
		try:
			db.session.commit()
		except Exception as e:
			print(e)
			db.session.rollback()
		return jsonify(status=204)
