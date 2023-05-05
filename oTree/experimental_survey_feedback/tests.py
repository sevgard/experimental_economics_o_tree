from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants



class PlayerBot(Bot):

    def play_round(self):

        yield (pages.ControlQuestions, {
            'question_types': 1,
            'question_rounds': 20,
            'question_contribution': 4,
            'question_feedback': 4,
        })

        #for value in [
        #    self.player.crt_bat,
        #    self.player.payoff
        #]:
        #    assert value != None
