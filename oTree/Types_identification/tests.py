from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        #yield (pages.FirstPage, {'id_number': self.participant.id_in_session})
        yield (pages.Introduction)
        yield (pages.Instructions)


