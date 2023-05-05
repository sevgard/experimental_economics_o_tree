from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from scipy import stats

doc = """
This is a one-period allocation game with 4 players.
"""

class Constants(BaseConstants):
    name_in_url = 'Experimental_FirstStage'
    players_per_group = 4
    num_rounds = 1

    endowment = c(200)
    multiplier = 0.5
    offer_increment = c(10)
    offer_choices = currency_range(0, endowment, offer_increment)

    instructions_template_uncon = 'experimental_FirstStage/InstructionsUnconditional.html'
    instructions_template_con = 'experimental_FirstStage/Instructions.html'

class Subsession(BaseSubsession):
    pass

def question(amount):
    return 'What is your investment if the rest of your group invested on average {}?'.format(c(amount))

class Group(BaseGroup):
    average = models.CurrencyField()

    total_contribution = models.CurrencyField()

    individual_share = models.CurrencyField()

    teamavg = models.CurrencyField()

    conditional = models.CurrencyField()

    def set_payoffs(self):
        p1, p2, p3, p4 = self.get_players()

        self.average = (p2.contribution + p3.contribution + p4.contribution) / 3

        # Get rounded average
        self.teamavg = round(self.average, -1)

        responses = {0: p1.response_0, 10: p1.response_10, 20: p1.response_20, 30: p1.response_30, 40: p1.response_40,
                     50: p1.response_50, 60: p1.response_60, 70: p1.response_70, 80: p1.response_80, 90: p1.response_90,
             100: p1.response_100, 110: p1.response_110, 120: p1.response_120, 130: p1.response_130, 140: p1.response_140,
             150: p1.response_150, 160: p1.response_160, 170: p1.response_170, 180: p1.response_180, 190: p1.response_190,
             200: p1.response_200}

        for i in range(0,200,10):
            if self.teamavg == i:
                self.conditional = responses[i]


        self.total_contribution = self.conditional + p2.contribution + p3.contribution + p4.contribution
        self.individual_share = self.total_contribution * Constants.multiplier / Constants.players_per_group

        p1.private = Constants.endowment - self.conditional
        p2.private = Constants.endowment - p2.contribution
        p3.private = Constants.endowment - p3.contribution
        p4.private = Constants.endowment - p4.contribution

        p1.payoff = p1.private + self.individual_share
        p2.payoff = p2.private + self.individual_share
        p3.payoff = p3.private + self.individual_share
        p4.payoff = p4.private + self.individual_share




class Player(BasePlayer):

    response_0 = models.CurrencyField(min=0, max=Constants.endowment, label=question(0))
    response_10 = models.CurrencyField(min=0, max=Constants.endowment, label=question(10))
    response_20 = models.CurrencyField(min=0, max=Constants.endowment, label=question(20))
    response_30 = models.CurrencyField(min=0, max=Constants.endowment, label=question(30))
    response_40 = models.CurrencyField(min=0, max=Constants.endowment, label=question(40))
    response_50 = models.CurrencyField(min=0, max=Constants.endowment, label=question(50))
    response_60 = models.CurrencyField(min=0, max=Constants.endowment, label=question(60))
    response_70 = models.CurrencyField(min=0, max=Constants.endowment, label=question(70))
    response_80 = models.CurrencyField(min=0, max=Constants.endowment, label=question(80))
    response_90 = models.CurrencyField(min=0, max=Constants.endowment, label=question(90))
    response_100 = models.CurrencyField(min=0, max=Constants.endowment, label=question(100))
    response_110 = models.CurrencyField(min=0, max=Constants.endowment, label=question(110))
    response_120 = models.CurrencyField(min=0, max=Constants.endowment, label=question(120))
    response_130 = models.CurrencyField(min=0, max=Constants.endowment, label=question(130))
    response_140 = models.CurrencyField(min=0, max=Constants.endowment, label=question(140))
    response_150 = models.CurrencyField(min=0, max=Constants.endowment, label=question(150))
    response_160 = models.CurrencyField(min=0, max=Constants.endowment, label=question(160))
    response_170 = models.CurrencyField(min=0, max=Constants.endowment, label=question(170))
    response_180 = models.CurrencyField(min=0, max=Constants.endowment, label=question(180))
    response_190 = models.CurrencyField(min=0, max=Constants.endowment, label=question(190))
    response_200 = models.CurrencyField(min=0, max=Constants.endowment, label=question(200))

    contribution = models.CurrencyField(min=0, max=Constants.endowment)

    type = models.StringField()
    corr = models.FloatField()
    con_average = models.FloatField()
    private = models.CurrencyField()


    def set_type(self):
        x = [self.response_0, self.response_10, self.response_20, self.response_30, self.response_40, self.response_50,
                 self.response_60, self.response_70, self.response_80, self.response_90,
                 self.response_100, self.response_110, self.response_120, self.response_130, self.response_140,
                 self.response_150, self.response_160, self.response_170, self.response_180, self.response_190,
                 self.response_200]

        y = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]


        self.corr = stats.spearmanr(x, y)[0]

        self.con_average = sum(x)/21

        # Type A = FreeRider, Type B = CC (conditional), Type C = UC (unconditional), Type D = other
        if self.corr > 0.4:
            self.type = 'B'
        elif self.con_average > 150:
            self.type = 'C'
        elif self.con_average < 15:
            self.type = 'A'
        else:
            self.type = 'D'


    def role(self):
        if self.id_in_group == 1:
            return 'conditional'
        else:
            return 'unconditional'