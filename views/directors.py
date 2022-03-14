from flask import request
from flask_restx import Resource, Namespace

from HW19.dao.model.director import DirectorSchema
from HW19.implemented import director_service
from HW19.service.auth import auth_required, admin_required

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        all_directors = director_service.get_all()
        return DirectorSchema(many=True).dump(all_directors), 200

    @admin_required
    def post(self):
        req_json = request.json
        new_director = director_service.create(req_json)
        return f"Created id: {new_director.id}", 201


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_required
    def get(self, rid=int):
        director = director_service.get_one(rid)
        if director:
            return DirectorSchema().dump(director), 200
        return "", 404

    @admin_required
    def put(self, rid=int):
        req_json = request.json
        if not req_json.get('id'):
            req_json['id'] = rid
        if director_service.update(req_json):
            return f"Update id: {rid}", 201
        return "not found", 404

    @admin_required
    def delete(self, rid=int):
        if director_service.delete(rid):
            return "", 204
        return "not found", 404
