from py2neo import Graph, Node, Relationship
# from neomodel import (StringProperty, AliasProperty, RelationshipTo, Relationship, ZeroOrOne)
# from neoapi import SerializableStructuredNode, SerializableStructuredRel, DateTimeProperty
from passlib.hash import bcrypt
from datetime import datetime
import os
import uuid
import jsonify

url = os.environ.get('GRAPHENEDB_URL', 'http://localhost:7474')
username = os.environ.get('NEO4J_USERNAME')
password = os.environ.get('NEO4J_PASSWORD')

graph = Graph(url + '/db/data', username=username, password=password)

class User:
    def __init__(self, username):
        self.username = username

    def find(self):
        user = graph.find_one("User", "username", self.username)
        return user

    def register(self, password):
        if not self.find():
            user = Node("User", username = self.username, password=bcrypt.encrypt(password))
            graph.create(user)
            return True
        else:
            return False

    def verify_password(self, password):
        user = self.find()
        if user:
            return bcrypt.verify(password, user['password'])
        else:
            return False

# class Episode(SerializableStructuredNode):
#     __type__ = "episodes"

#     type = StringProperty(default='episodes')
#     id = StringProperty()
#     name = StringProperty()


def get_episodes():
    query = '''
    MATCH(episode:Episode) RETURN episode.name, episode.id
    '''

    results = graph.run(query).data()
    nodes = []

    for result in results:
        nodes.append({"title": result['episode.name']})

    json_nodes = jsonify(nodes)
    print(json_nodes)
    return json_nodes

# def get_episodes():
#     query = '''
#     MATCH(episode:Episode) RETURN episode.name, episode.id
#     '''

#     return graph.run(query)

def get_directors():
    query = '''
    MATCH(director:Director) RETURN director
    '''

    return graph.run(query)

