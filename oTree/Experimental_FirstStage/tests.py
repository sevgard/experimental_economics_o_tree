from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Intro)
        yield (pages.UnconditionalContribute, {'contribution': c(76)})
        yield (pages.ConditionalContribute, {'response_0': c(0), 'response_10': c(10), 'response_20': c(20),
                                               'response_30': c(30), 'response_40': c(40),
                                                'response_50': c(50), 'response_60': c(60), 'response_70': c(70), 'response_80': c(80),
                                               'response_90': c(90), 'response_100': c(100), 'response_110': c(110),
                                                'response_120': c(120), 'response_130': c(130), 'response_140': c(140),
                                             'response_150': c(150), 'response_160': c(160), 'response_170': c(170),
                                             'response_180': c(180), 'response_190': c(190), 'response_200': c(200)})
