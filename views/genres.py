from flask import request
from flask_restx import Resource, Namespace

from HW19.dao.model.genre import GenreSchema
from HW19.implemented import genre_service
from HW19.service.auth import admin_required, auth_required

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        all_genres = genre_service.get_all()
        return GenreSchema(many=True).dump(all_genres), 200

    @admin_required
    def post(self):
        req_json = request.json
        new_genre = genre_service.create(req_json)
        return f"Created id: {new_genre.id}", 201


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_required
    def get(self, rid=int):
        genre = genre_service.get_one(rid)
        if genre:
            return GenreSchema().dump(genre), 200
        return "", 404

    @admin_required
    def put(self, rid=int):
        req_json = request.json
        if not req_json.get('id'):
            req_json['id'] = rid
        if genre_service.update(req_json):
            return f"Update id: {rid}", 201
        return "not found", 404

    @admin_required
    def delete(self, rid=int):
        if genre_service.delete(rid):
            return "", 204
        return "not found", 404





