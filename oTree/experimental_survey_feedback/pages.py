from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class ControlQuestions(Page):
    form_model = 'player'
    form_fields = ['question_types',
                   'question_rounds',
                   'question_contribution',
                   'question_feedback']


page_sequence = [
    ControlQuestions
]
