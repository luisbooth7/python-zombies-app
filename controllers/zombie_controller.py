from flask_restful import Resource, reqparse

from models.infected_model import Infected
from models.healed_model import Healed


class GetZombies(Resource):
    def get(self):
        zombies = Infected.select_infected()
        return {'zombies': zombies}


class FilterZombies(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('param', type=str)
        parser.add_argument('value', type=str)
        args = parser.parse_args()

        _param = args['param']
        _value = args['value']

        zombies = Infected.filter_infected(_param, _value)
        return {'zombies': zombies}


class GetZombieInfo(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        args = parser.parse_args()

        _id = args['id']

        zombies_info = Infected.select_infected_info(_id)
        return {'zombies': zombies_info}


class AddZombie(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('graveyard', type=str)
        parser.add_argument('city', type=str)
        args = parser.parse_args()

        _name = args['name']
        _graveyard = args['graveyard']
        _city = args['city']

        print(_name);

        Infected.insert_infected(_name, _graveyard, _city)


class DeleteZombie(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        parser.add_argument('name', type=str)
        args = parser.parse_args()

        _id = args['id']
        _name = args['name']

        Healed.insert_healed(_name)
        Infected.delete_infected(_id)


class UpdateZombie(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        parser.add_argument('graveyard', type=str)
        parser.add_argument('city', type=str)
        args = parser.parse_args()

        _id = args['id']
        _graveyard = args['graveyard']
        _city = args['city']

        print(_id);

        Infected.update_infected(_id, _graveyard, _city)


class GetHealed(Resource):
    def get(self):
        healed = Healed.select_healed()
        return {'healed': healed}


resources = [
    (GetZombies, '/GetZombies'),
    (FilterZombies, '/FilterZombies'),
    (GetZombieInfo, '/GetZombieInfo'),
    (AddZombie, '/AddZombie'),
    (DeleteZombie, '/DeleteZombie'),
    (UpdateZombie, '/UpdateZombie'),
    (GetHealed, '/GetHealed')
]