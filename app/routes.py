from app import app, db
from flask import render_template, redirect
from app.forms import FlagForm
from app.models import Player
import random
import json

flags = ['589745c9f4bac232119c8778c969d527', '596e16190d9edc057a0ed4f3c32e312d', 'b41dc55ef1a4f1a5f750edcfa50eb709', '86fb0763c84dd58be4541837d5224acf','21c267100d5fa4ebb3ff18ec71eda507','52b7501e767e0f39c65d2a8188b65ed2','9d8551b9e56b3436baf20be1397becf6','49b0462b3eeb50e1fa0c08ce15ff6167','49b0462b3eeb50e1fa0c08ce15ff6167','37101054f536b2dbc0fdc5cc7c348e87','f9df4e01f86330c25c4c54e7e6451e5b','80f813d22b2953b0348596e20942630e','e5b26e2668a5479bdd68b8637af37aca','7f5716e396818028d45c07c69fe4a204']
# 13 flags
# 589745c9f4bac232119c8778c969d527
# 596e16190d9edc057a0ed4f3c32e312d
# b41dc55ef1a4f1a5f750edcfa50eb709
# 86fb0763c84dd58be4541837d5224acf

@app.route('/robots.txt')
def robots():
    return 'b41dc55ef1a4f1a5f750edcfa50eb709'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FlagForm()
    players = Player.query.order_by(Player.score.desc()).all()

    if form.validate_on_submit():
        if form.hash.data in flags:
            player = Player.query.filter_by(alias=form.alias.data).first()
            if player is not None and player.check_hash(form.alias_hash.data):
                players_flags = json.loads(player.flags)
                if form.hash.data in players_flags:
                    msg = 'Du har allerede afleveret dette flag.'
                    return render_template('msg.html', msg=msg)
                else:
                    player.score += 1
                    players_flags.append(form.hash.data)
                    player.flags = json.dumps(players_flags)
                    db.session.commit()
                    msg = 'Endnu et flag, endnu et point.'
                    return render_template('msg.html', msg=msg)
                # do something useful
            elif player is not None and not player.check_hash(form.alias_hash.data):
                msg = 'Forkert alias hash.'
                return render_template('msg.html', msg=msg)
            elif player is None:
                generated_alias_hash = str(random.getrandbits(128))
                players_flags = json.dumps([form.hash.data])
                player = Player(alias=form.alias.data, alias_hash=generated_alias_hash, score=1, flags=players_flags)
                db.session.add(player)
                db.session.commit()
                msg = 'Stærkt, det var første flag! Fremover skal du bruge denne hash til at aflevere flag: {}'.format(generated_alias_hash)
                return render_template('msg.html', msg=msg)
        else:
            msg = 'Ugyldigt flag.'
            return render_template('msg.html', msg=msg)


    return render_template('index.html', form=form, players=players)
