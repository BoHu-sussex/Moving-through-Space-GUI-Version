class Role:
    """
    This class is to initialize the roles in the game.
    """

    def __init__(self, name, description):
        """
        Initialize a role.
        :param name: the name of the role.
        :param description: some text based description of this role.
        """
        self.name = name
        self.description = description

    def show_description(self):
        """
        Return the description text.
        :return: text
        """
        return self.description


class Fighter(Role):
    """
    This class is to initialize a fighter.
    This class is a subclass of class Role.
    """

    def __init__(self, name, description, hp, attack):
        """
        Initialize a fighter.
        :param name: the name of this fighter.
        :param description: text based description of this fighter.
        :param hp: the HP of fighter.
        :param attack: the basic attack value of this fighter.
        """
        super().__init__(name, description)
        self.hp = hp
        self.hp_limit = hp  # hp limit is the max value of hp.
        self.attack = attack
        self.alive = True  # to mark whether this fighter is alive.

    def die(self):
        """
        to implement the death of a fighter.
        :return: bool
        """
        self.alive = False  # update the mark.

        return True


class Knight(Fighter):
    def __init__(self, name, description, hp, attack, capacity):
        """
        Initialize a knight.
        This class is a subclass of class Fighter.
        :param name: the name of a knight.
        :param description: sentences describing a knight.
        :param hp: the blood volume of a knight, a knight will die if hp <= 0.
        :param attack: the attack value of a knight, which causes corresponding damage to monster.
        :param capacity: the max weight of total items in the backpack the knight can afford.
        """
        super().__init__(name, description, hp, attack)
        self.capacity = capacity
        self.backpack = []  # initialize the backpack.

    def drop(self, item):
        """
        drop sth in the backpack when the total weight of items exceed the capacity.
        :param item: a weapon or a potion.
        :return: bool
        """
        self.backpack.remove(item)  # implement the drop.

        return True

    def inventory(self):
        """
        Check all the items in the backpack.
        :return: str
        """
        if not self.backpack:
            return 'Your backpack is empty!'

        text = 'Here are all the items in your backpack:\n '

        for item_id, item in enumerate(self.backpack):
            text += f"* id-{item_id + 1}:\n    Name: {item.name}\n    Description: {item.description}\n    Weight: {item.weight}\n    Kind: {item.kind}\n    Level: {item.level}\n--------------------\n"

        return text

    def increase_attack(self):
        """
        Increase the basic attack value of the knight while winning a fight.
        :return: bool
        """
        self.attack += 2
        print(f"    * `attack`: {self.attack - 2} ---> {self.attack}")

        return True

    def increase_hp_limit(self):
        """
        Increase the HP limit of the knight while winning a fight.
        :return: bool
        """
        self.hp_limit += 2
        print(f"    * `HP`: {self.hp_limit - 2} ---> {self.hp_limit}\n")

        return True

    def increase_capacity(self):
        """
        Increase the capacity of the knight while winning a fight.
        :return: bool
        """
        self.capacity += 2
        print(f"You get stronger!\n    * `capacity`: {self.capacity - 2} ---> {self.capacity}")

        return True

    def current_weight(self):
        """
        Return the total weight of all the items in backpack.
        :return: int
        """
        s = 0

        for item in self.backpack:
            s += item.weight

        return s


class Monster(Fighter):
    """
    Initialize a monster.
    This class is a subclass of class Fighter.
    """

    def __init__(self, name, description, hp, attack, growl, level, image_path):
        """
        initialize a monster.
        :param name: the name of this monster.
        :param description: text based description of this monster.
        :param hp: HP of this monster.
        :param attack: basic attack value of this monster.
        :param growl: before fight begin, monster will make a growl.
        :param level: the level of this monster.
        :param image_path:
        """
        super().__init__(name, description, hp, attack)
        self.growl = growl
        self.level = level
        self.image_path = image_path

    def make_growl(self):
        """
        Return the growl.
        :return: str
        """
        return self.growl