from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
This is a one-period public goods game with 4 players.
"""


class Constants(BaseConstants):
    name_in_url = 'clock_mechanism_nofeedback'
    players_per_group = 4
    num_rounds = 20

    endowment = c(200)
    multiplier = 0.5
    increment = 10

    instructions_template = 'clock_mechanism_nofeedback/Instructions.html'


class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    total_earnings = models.CurrencyField()
    individual_share = models.CurrencyField()

    def set_payoffs(self):
        for player in self.get_players():
            if player.role() == 'active':
                if player.choice == 1:
                    player.instant_contribution = Constants.increment
                else:
                    player.instant_contribution = 0
            else:
                player.instant_contribution = 0

        for player in self.get_players():
            if self.round_number ==1:
                player.contribution = player.instant_contribution
            else:
                player.contribution = player.instant_contribution + player.in_round(self.round_number-1).contribution

        players = self.get_players()
        contributions = [p.contribution for p in players]
        self.total_contribution = sum(contributions)
        self.total_earnings = self.total_contribution * Constants.multiplier * Constants.players_per_group
        self.individual_share = self.total_contribution * Constants.multiplier
        for p in self.get_players():
            if self.round_number == Constants.num_rounds:
                p.payoff = Constants.endowment - p.contribution + self.individual_share
            else:
                p.payoff = 0

class Player(BasePlayer):
    choice = models.IntegerField()
    instant_contribution = models.CurrencyField()
    contribution = models.CurrencyField()
    #for group seleciton:
    #type_a_number = models.IntegerField()
    #group_type = models.StringField()

    def role(self):
        if self.round_number == 1:
            return 'active'
        elif self.in_round(self.round_number - 1).choice == 1:
            return 'active'
        else:
            return 'passive'

    def left(self):
        if self.round_number == 1:
            return 'Still in the game'
        elif self.in_round(self.round_number-1).choice == 1:
            return 'Still in the game'
        elif self.in_round(self.round_number-1).choice == 0:
            return self.round_number-1
        else:
            return self.in_round(self.round_number-1).left()

    def investments(self):
        if self.round_number == 1:
            return 0
        else:
            return self.in_round(self.round_number - 1).contribution