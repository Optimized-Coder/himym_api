from flask import Blueprint, jsonify, request, redirect, url_for, render_template
from ..models import Character, Episode
from ..extensions import db

import datetime

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
    
# add characters
@api.route('/characters/add', methods=['GET', 'POST'])
def add_character():
    if request.method == 'POST':
        name = request.form.get('name')
        full_name = request.form.get('full_name')
        portrayed_by = request.form.get('portrayed_by')
        home_town = request.form.get('home_town')
        form_dob = request.form.get('dob')
        occupation = request.form.get('occupation')
        
        dob = datetime.datetime.strptime(
           form_dob,
            "%Y-%m-%d"
        )

        c = Character(
            name = name,
            full_name = full_name,
            portrayed_by = portrayed_by,
            home_town = home_town,
            date_of_birth = dob,
            occupation = occupation
        )
        db.session.add(c)
        db.session.commit()

        return redirect(url_for('api.get_characters'))

    return render_template(
        'add_character.html'
    )
# DELETE CHARACTERS
@api.route('characters/<int:id>/delete/')
def delete_character(id):
    character = Character.query\
    .filter_by(id=id).first()
    character_exists = bool(character)
    if not character_exists:
        return redirect(url_for('not_found'))
    else:
        db.session.delete(character)
        db.session.commit()

        return redirect(url_for('api.get_characters'))

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

# ADD EPISODES
@api.route('/episodes/add/', methods=['GET', 'POST'])
def add_episode():
    if request.method == 'POST':
        season_number = request.form.get('season_number')
        episode_number = request.form.get('episode_number')
        form_first_aired = request.form.get('first_aired')
        director = request.form.get('director')
        episode_name = request.form.get('episode_name')

        first_aired = datetime.datetime.strptime(
           form_first_aired,
            "%Y-%m-%d"
        )

        ep = Episode(
            season_number = season_number,
            episode_number = episode_number,
            first_aired = first_aired,
            director = director,
            episode_name = episode_name
        )

        db.session.add(ep)
        db.session.commit()

        return redirect(url_for('api.get_episodes'))

    return render_template(
        'add_episode.html'
    )

# DELETE EPISODE
@api.route('/episodes/<int:id>/delete/')
def delete_episode(id):
    episode = Episode.query.filter_by(id=id).first()
    episode_exists = bool(episode)

    if not episode_exists:
        return redirect(url_for('not_found'))
    else:
        db.session.delete(episode)
        db.session.commit()

        return redirect(url_for('api.get_episodes'))