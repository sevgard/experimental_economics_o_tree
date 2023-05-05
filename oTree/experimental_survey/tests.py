from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants



class PlayerBot(Bot):

    def play_round(self):

        yield (pages.Introduction)

        yield (pages.Demographics, {
            'age': 24,
            'gender': 'Male'})

        yield (pages.Instructions)

        yield (pages.ControlQuestions, {
            'question_experiment': 2,
            'question_role': 1,
            'question_payout': 300,
            'question_con': 20,
            'question_payout_con': 340,
        })

