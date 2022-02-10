import typing

class EndGameException(Exception):
    pass

class Outcome(typing.NamedTuple):
    interaction: str
    outcome_value: typing.Any = None
