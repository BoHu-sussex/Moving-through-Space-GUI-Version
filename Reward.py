class Reward:
    """
    This class is to create a reward.
    A reward is provided while knight winning one room.
    """

    def __init__(self, name, description, weight, kind, level):
        """
        Initialize a reward.
        :param name: the name of a reward.
        :param description: sentences describing the reward item.
        :param weight: the weight of a reward item.
        :param kind: the kind of a reward item, `weapon` or `potion`.
        :param level: the level of a reward item, which is corresponding to its effect.
        """
        self.name = name
        self.description = description
        self.weight = weight
        self.kind = kind
        self.level = level