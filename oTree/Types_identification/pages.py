from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class FirstPage(Page):
    pass

class ResultsWaitPage(WaitPage):
    pass

class Introduction(Page):
    def vars_for_template(self):

        for candidate in Constants.candidates:
            if candidate['participant.label'] == self.participant.label:
                self.player.player_type = candidate['Experimental_FirstStage.1.player.type']


        return {
            'player_type': self.player.player_type,
        }
class Instructions(Page):
    def vars_for_template(self):
        self.participant.vars['type'] = self.player.player_type

        return {
            'participant_type': self.participant.vars['type']
        }

page_sequence = [
    #FirstPage,
    Introduction,
    Instructions
]
