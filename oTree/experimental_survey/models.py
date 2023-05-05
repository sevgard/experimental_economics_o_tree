from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'experimental_survey'
    players_per_group = None
    num_rounds = 1

    instructions_template = 'experimental_survey/InstructionsShort.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.PositiveIntegerField(
        label='What is your age?',
        min=13, max=125)

    gender = models.StringField(
        choices=['Male', 'Female'],
        label='What is your gender?',
        widget=widgets.RadioSelect)

    question_experiment = models.PositiveIntegerField(
        label='''
        Write down the number of the correct option. Option 1: Regardless of your behavior, you will participate
         in both stages of the experiment. Option 2: It depends on your behavior in this first stage whether you 
         will participate in the second stage of the experiment next week. (Write down the number of the option) 
        ''',
        min=2, max=2
    )


    question_role = models.PositiveIntegerField(
        label='''
        Suppose your role in the game is determined as "unconditional". Which investment decision is taken for 
        the payout decision?
        Option 1: Unconditional investment that you made regardless of the investment of the rest of the group.
        Option 2: Conditional investment that you made depending on the average investment of the rest of the group.
        (Write down the number of the option)''',
        min=1, max=1
    )

    question_payout = models.PositiveIntegerField(
        label='''
        Suppose your role in the game is determined as "unconditional". The rest of the team invested in total 300
        points. You contributed 100 points. The endowment is 200 points and the social multiplier is 0.5. What is your
        payout? (Write down the payoff as an integer) 
        ''',
        min=300, max=300
    )

    question_con = models.PositiveIntegerField(
        label='''
        Suppose your role in the game is determined as "conditional". The rest of the team invested in total 300 points,
        so 100 points on average. Your conditional investment decision was as follows:
        
        "..., 0 points for an average investment of 90, 20 points for an average investment of 100, 30 points for
        an average investment of 110,...".
        
        What is your investment for this game? (Write down the investment as number of points)
        
        ''',
        min=20, max=20
    )

    question_payout_con = models.PositiveIntegerField(
        label='''
        Suppose your role in the game is determined as "conditional". The rest of the team invested in total 300 points,
        so 100 points on average. Your conditional investment for an average investment from the rest of the team of
        100 points was 20 points. The endowment is 200 points, the social multiplier is 0.5. 
        What is your payoff in this game? (Write down the payoff as number of points) 
        ''',
        min=340, max=340
    )

