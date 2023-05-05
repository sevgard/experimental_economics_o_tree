from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    pass

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age',
                   'gender']

class Instructions(Page):
    pass

class ControlQuestions(Page):
    form_model = 'player'
    form_fields = ['question_experiment',
                   'question_role',
                   'question_payout',
                   'question_con',
                   'question_payout_con']


page_sequence = [
    Introduction,
    Demographics,
    Instructions,
    ControlQuestions
]
