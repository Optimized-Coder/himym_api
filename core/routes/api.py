from flask import Blueprint, jsonify, request, redirect, url_for
from ..models import Character, Episode

api = Blueprint('api', __name__)

'''
******
CHARACTER ROUTES
******
'''
# GET CHARACTERS
@api.route('/characters/', methods=['GET'])
def get_characters():
    characters = Character.query.all()
    return jsonify([character.to_dict()\
                     for character in characters])

@api.route('/characters/<int:id>', methods=['GET'])
def get_character(id):
    character = Character.query.\
        filter_by(id=id).first()
    character_exists = bool(character)
    if not character_exists:
        return redirect(url_for('not_found'))
    else:
        return jsonify(character.to_dict())

'''
******
EPISODE ROUTES
******
'''
# GET EPISODES
@api.route('/episodes/', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict()\
                    for episode in episodes])

@api.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.\
     filter_by(id=id).first()
    episode_exists = bool(episode)
    if not episode_exists:
        return redirect(url_for('not_found'))
    else:
        return jsonify(episode.to_dict())
