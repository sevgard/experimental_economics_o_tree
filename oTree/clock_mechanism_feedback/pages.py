from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
from random import shuffle

class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        #Group matching for three types of groups: With no type A players, with 1 Type A player and with 2 Type A players
        if self.round_number == 1:
            players = self.subsession.get_players()

            A_players = [p for p in players if p.participant.vars['type'] == 'A']
            B_players = [p for p in players if p.participant.vars['type'] == 'B']
            shuffle(A_players)
            shuffle(B_players)

            group_matrix = []

            # pop elements from B_players until it's empty
            while B_players:
                f0 = [
                    B_players.pop(),
                    B_players.pop(),
                    B_players.pop(),
                    B_players.pop(),
                ]
                group_matrix.append(f0)
                f1 = [
                    A_players.pop(),
                    B_players.pop(),
                    B_players.pop(),
                    B_players.pop(),
                ]
                group_matrix.append(f1)
                f2 = [
                    A_players.pop(),
                    A_players.pop(),
                    B_players.pop(),
                    B_players.pop(),
                ]
                group_matrix.append(f2)
            self.subsession.set_group_matrix(group_matrix)
        for subsession in self.subsession.in_rounds(2, Constants.num_rounds):
            subsession.group_like_round(1)

    def is_displayed(self):
        return self.round_number ==1


class Introduction(Page):
    """Announcement of the group composition"""
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        a_members = []
        b_members = []
        for player in self.group.get_players():
            if player.participant.vars['type'] == 'B':
                b_members.append(player)
            else:
                a_members.append(player)
        return {
            'type_A_quantity': len(a_members),
            'type_B_quantity': len(b_members),
            'player_type': self.participant.vars['type'],
        }


class WaitingforGame(WaitPage):
    def is_displayed(self):
        return self.round_number == 1

    def after_all_players_arrive(self):
        self.group.set_payoffs()

class Contribute(Page):
    """Player: Choose whether to contribute and stay in the game or exit"""
    def is_displayed(self):
        return self.player.role() == 'active'

    timeout_seconds = 30

    def before_next_page(self):
        if self.timeout_happened:
            self.player.choice = 1


    form_model = 'player'
    form_fields = ['choice']

    timeout_submission = {'choice': c(Constants.endowment / 2)}

    def vars_for_template(self):
        return {
            'status': self.player.role(),
            'Round_number': self.round_number,
            'player_number': self.player.id_in_group,
            'player_investments': self.player.investments(),
            'player_left': self.player.left(),
            'player_role': self.player.role(),
            'player_type': self.participant.vars['type'],
        }

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

class Announcement(Page):
    def is_displayed(self):
        return self.player.role() == 'active'


    def vars_for_template(self):
        return {
            'status': self.player.role(),
            'Round_number': self.round_number,
            'player_number': self.player.id_in_group,
            'player_investments': self.player.investments(),
            'player_left': self.player.left(),
            'player_role': self.player.role(),
            'player_type': self.player.type(),
        }

class Total_payoff(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds
    def vars_for_template(self):
        return {
            'choice': self.player.in_round(self.round_number-1).choice,
            'private_account': Constants.endowment-self.player.contribution
        }





page_sequence = [
    ShuffleWaitPage,
    Introduction,
    WaitingforGame,
    Announcement,
    Contribute,
    ResultsWaitPage,
    Total_payoff
]
