from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Types_identification'
    players_per_group = None
    num_rounds = 1
    group_size = 4
    with open('Types_identification/part1.csv') as f:
        candidates = list(csv.DictReader(f))


    endowment = c(200)
    multiplier = 0.5
    increment = 10



class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    player_type = models.StringField()



