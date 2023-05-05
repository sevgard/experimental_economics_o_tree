from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
from otree.api import Submission

class PlayerBot(Bot):
    def play_round(self):
        yield(pages.Introduction)
        yield Submission(pages.Announcement, check_html=False)
        yield (pages.Contribute, {'choice': 1})
        yield (pages.Total_payoff)
