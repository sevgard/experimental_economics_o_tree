from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Transfer(WaitPage):
    def after_all_players_arrive(self):
        pass

class Intro(Page):
    pass

class UnconditionalContribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ConditionalContribute(Page):
    form_model = 'player'
    form_fields = ['response_{}'.format(int(i)) for i in Constants.offer_choices]


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

class TypeWaitPage(WaitPage):
    def is_displayed(self):
        self.player.set_type()

class ResultsConditional(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

class ResultsUnconditional(Page):
    def is_displayed(self):
        return self.player.id_in_group > 1

page_sequence = [
   Transfer,
   Intro,
   UnconditionalContribute,
   ConditionalContribute,
    ResultsWaitPage,
    TypeWaitPage,
    ResultsConditional,
    ResultsUnconditional
]
