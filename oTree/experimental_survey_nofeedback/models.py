from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'experimental_survey_nofeedback'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    question_types = models.PositiveIntegerField(
        label='''
        Suppose your own type is Type B and you have been assigned to the group with two other players of Type B.
        How many players of Type A are in your group? (Write down the number)
        ''',
        min=1, max=1
    )

    question_rounds = models.PositiveIntegerField(
        label='''
        How many rounds are in the game? (Write down the number)
        ''',
        min=20, max=20
    )

    question_contribution = models.PositiveIntegerField(
        label='''
        Suppose you decided to press "No" button in some round of the game. What will happen then?
        Option 1: I will proceed to the next round.
        Option 2: I will exit the game but have the possibility to return to the game.
        Option 3: All my investments to the joint project will automatically become zero.
        Option 4: I will exit the game and wait till all other players end the game. My investment will stay at the level of the last round.
        (Write down the number of the option)
        ''',
        min=4, max=4
    )

    question_feedback = models.PositiveIntegerField(
        label='''
        Which information can you see during each round?
        Option 1: How many players are still in the game.
        Option 2: Who left the game.
        Option 3: Current level of other players' investments.
        Option 4: None of mentioned above
        (Write down the number of the option)
        ''',
        min=4, max=4
    )

