import random

from Reward import Reward
from Role import *
from Room import Room


class Game:
    """
    This class is to create the game model.
    """

    def __init__(self):
        """
        Initialize the game.
        1. create all the rewards and monsters.
        2. create all the rooms and each room has its monster and rewards.
        3. `current_room` is the room where player is located now.
        4. create the knight and princess.
        """
        self.create_monsters()
        self.create_rewards()
        self.create_rooms()
        self.visited_rooms = [self.room1]  # record the rooms which have been visited already.
        self.current_room = self.visited_rooms[-1]
        self.knight = Knight("", "You are a knight on an adventure to save the princess.", 10, 3, 3)
        self.princess = Role("Lolly", "You are a princess trapped in a castle, waiting to be rescued by a knight")

    def create_monsters(self):
        """
        Create ten monsters for each room.
        :return: None
        """
        self.monster1 = Monster("Witch",
                                "Witches wear black robes and are good at using evil spells to launch attacks.", 4, 1,
                                "Fehfehfehfeh! Interesting young man. Are you ready for dying under my spell?", 1,
                                'images/monster1.jpg')
        self.monster2 = Monster("Ogre", "The ogre has a large body and sharp claws, and it moves quickly.", 6, 2,
                                "Shahahahaha! I'll tear you to pieces!", 2, 'images/monster2.jpg')
        self.monster3 = Monster("Vampire", "Vampires can fly very fast, and their high-pitched calls are fascinating.",
                                9, 3, "Gegyagyagyagya! I can't wait to taste your blood!", 3, 'images/monster3.jpg')
        self.monster4 = Monster("Night Demon",
                                "A night demon is an evil demon that can ingest your soul if you're not careful.", 12,
                                4, "Gabababababa! I will eat your soul for my snack！", 4, 'images/monster4.jpg')
        self.monster5 = Monster("Dark elf",
                                "Dark elf live underground and have black skin. Although it is small in size, do not underestimate its tricks.",
                                15, 5, "Wiihahahahaha! Self-righteous human beings!", 5, 'images/monster5.jpg')
        self.monster6 = Monster("Werewolf",
                                "A half-human, half-wolf creature usually depicted as taking on the form of a Wolf when the moon is full. \nThey possess great strength and agility, as well as ferocious aggression.",
                                18, 6, "Murufufufufufufu！ I could eat you in one bite!", 6, 'images/monster6.jpg')
        self.monster7 = Monster("Zombie", "A dead body, possessed by evil forces, a slave to the unconscious.", 21, 7,
                                "Wiiwiwiwiwiwi! Come to hell with me!", 7, 'images/monster7.jpg')
        self.monster8 = Monster("Warlock",
                                "Male humans who master dark magic gain power and the ability to control other creatures by learning dark magic and rituals.",
                                24, 8, "Kishishishishishi! I'll cut your eyes out and drink them!", 8,
                                'images/monster8.jpg')
        self.monster9 = Monster("Ghost",
                                "They usually appear at night or in dark places and are accompanied by a cold and eerie atmosphere.",
                                27, 9, "How can you beat me if you can't even see me?", 9, 'images/monster9.jpg')
        self.monster10 = Monster("Dark Dragon",
                                 "The Dark Dragon is a very powerful evil creature with dark scales and sharp claws. \nDark Dragons are usually powerful in attack and magic, capable of spitting fire and creating dark magic.",
                                 30, 10, "Gurararararara！Stupid human!", 10, 'images/monster10.jpg')

    def create_rooms(self):
        """
        1. Create rooms
        2. Add rewards for each room.
        3. Set next rooms for each room.
        :return: None
        """
        # create rooms.
        self.room1 = Room("Castle Kitchen",
                          "It's the kitchen and pantry inside the castle, \nwhere the cooks and servants worked.",
                          self.monster1, 'images/room1.jpg')
        self.room2 = Room("Banquet Hall",
                          "The banqueting Hall in the castle is used for banquets and large dinners, \nwith long tables and ornate decorations.",
                          self.monster2, 'images/room2.jpg')
        self.room3 = Room("Stable",
                          "The stables in the castle are used to keep horses and other livestock, \nusually with mangers, feed cabinets, saddles and other horse gear.",
                          self.monster3, 'images/room3.jpg')
        self.room4 = Room("Castle Hall",
                          "The main meeting place of the castle,\nlocated on the first floor of the main castle, \nwas a place for nobles to meet, dine and perform ceremonies. \nThe hall has high ceilings, ornate frescoes and luxurious furniture.",
                          self.monster4, 'images/room4.jpg')
        self.room5 = Room("Central Stairs",
                          "The central staircase of the castle, \none of the main passageways of the castle, \nleads to the various floors of the castle. \nThe central staircase is located in the center of the main building and can easily connect the various floors.",
                          self.monster5, 'images/room5.jpg')
        self.room6 = Room("Castle Chapel",
                          "Located near the main castle or in the tower, \nit was used as a place for nobles to perform religious ceremonies and prayers. \nThere are altars, ICONS, candlesticks and other religious articles in the church.",
                          self.monster6, 'images/room6.jpg')
        self.room7 = Room("Guard Room",
                          "A place used for guarding soldiers, \nusually at the entrance to a castle or near a fortification. \nThe guard room usually contains beds, weapons and equipment for soldiers.",
                          self.monster7, 'images/room7.jpg')
        self.room8 = Room("Castle Library",
                          "Located in a quiet corner of the main castle, \nit is used for the collection of books, documents and works of art. \nThere are bookshelves, reading tables, chairs and lighting equipment in the study.",
                          self.monster8, 'images/room8.jpg')
        self.room9 = Room("Castle Wall",
                          "The exterior defensive structure of the castle, \nmade of thick stone or brick, nvaries in height and thickness according to the size and importance of the castle. \nThe walls were usually topped with battlements and archeries to provide the convenience of defense and attack.",
                          self.monster9, 'images/room9.jpg')
        self.room10 = Room("State Apartments",
                           "A residence for guests of honour, located on the top floor of the main building. \nThe apartment is richly decorated, with a high level of etiquette and reception atmosphere.",
                           self.monster10, 'images/room10.jpg')

        # add rewards to each room.
        self.room1.add_rewards(self.weapon1)
        self.room1.add_rewards(self.weapon2)
        self.room2.add_rewards(self.potion1)
        self.room2.add_rewards(self.weapon3)
        self.room3.add_rewards(self.weapon4)
        self.room3.add_rewards(self.potion2)
        self.room4.add_rewards(self.weapon5)
        self.room4.add_rewards(self.weapon6)
        self.room5.add_rewards(self.potion3)
        self.room5.add_rewards(self.weapon7)
        self.room6.add_rewards(self.weapon8)
        self.room6.add_rewards(self.potion4)
        self.room7.add_rewards(self.weapon9)
        self.room7.add_rewards(self.weapon10)
        self.room8.add_rewards(self.potion5)
        self.room8.add_rewards(self.weapon11)
        self.room8.add_rewards(self.potion6)
        self.room9.add_rewards(self.weapon12)
        self.room9.add_rewards(self.weapon13)
        self.room9.add_rewards(self.weapon14)

        # set next rooms for each room.
        self.room1.set_next_room("Behind the door", self.room2)
        self.room1.set_next_room("Outside the window", self.room3)
        self.room2.set_next_room("Outside the left door", self.room3)
        self.room2.set_next_room("Outside the main door", self.room4)
        self.room2.set_next_room("Outside the right door", self.room5)
        self.room3.set_next_room("Over the fence", self.room2)
        self.room3.set_next_room("Outside the window", self.room6)
        self.room4.set_next_room("Outside the left door", self.room7)
        self.room4.set_next_room("Outside the main door", self.room5)
        self.room5.set_next_room("Go up the stair", self.room4)
        self.room5.set_next_room("Go down the stair", self.room6)
        self.room6.set_next_room("Outside the left door", self.room5)
        self.room6.set_next_room("Outside the main door", self.room8)
        self.room7.set_next_room("Outside the left door", self.room9)
        self.room7.set_next_room("Outside the main door", self.room8)
        self.room8.set_next_room("Outside the right door", self.room7)
        self.room8.set_next_room("Outside the main door", self.room9)
        self.room9.set_next_room("Outside the main door", self.room10)

    def create_rewards(self):
        """
        Create rewards for each room.
        :return: None
        """
        # rewards of room1
        self.weapon1 = Reward("British Hunting Knife", "A weapon commonly used by English hunters and adventurers.", 1,
                              "weapon", 1)
        self.potion1 = Reward("Apple flavored potion", "Can restore some of your HP.", 1, "potion", 1)
        # rewards of room2
        self.weapon2 = Reward("Hatchet", "A small axe, usually used for easy carrying.", 2, "weapon", 2)
        self.weapon3 = Reward("Stiletto sword", "A short sword used in Italy with a very thin and sharp blade.", 2,
                              "weapon", 2)
        # rewards of room3
        self.weapon4 = Reward("Tang Sword", "Weapons used during the Tang Dynasty", 3, "weapon", 3)
        self.potion2 = Reward("Tablet", "Can restore some of your HP.", 3, "potion", 3)
        # rewards of room4
        self.weapon5 = Reward("Roman Short sword", "A short sword used in ancient Rome.", 4, "weapon", 4)
        self.weapon6 = Reward("Battle Axe",
                              "A large axe used specifically for combat.",
                              4, "weapon", 4)
        # rewards of room5
        self.potion3 = Reward("Elixir", "Can restore some of your HP.", 5, "potion", 5)
        self.weapon7 = Reward("Long sword",
                              "A sword used in medieval Europe with a longer blade and a guard between the tip and the handle. ",
                              5, "weapon", 5)
        # rewards of room6
        self.weapon8 = Reward("Longbow",
                              "A traditional English bow and arrow known for its long bow and high shooting power. ",
                              6, "weapon", 6)
        self.potion4 = Reward("stimulant",
                              "Can restore some of your HP.", 6,
                              "potion", 6)
        # rewards of room7
        self.weapon9 = Reward("Composite Bow",
                              "A compound bow is a bow made using a number of different materials",
                              7, "weapon", 7)
        self.weapon10 = Reward("Recurve Bow",
                               "The recurve bow is a bow with a special shape.",
                               7, "weapon", 7)
        # rewards of room8
        self.potion5 = Reward("Pill", "Can restore some of your HP.", 8, "potion", 8)
        self.weapon11 = Reward("Crossbow",
                               "A crossbow is a bow and arrow that uses a mechanical device to draw the strings.",
                               8, "weapon", 8)
        self.potion6 = Reward("Ointment", "Can restore some of your HP", 8, "potion", 9)
        # rewards of room9
        self.weapon12 = Reward("War Hammer",
                               "A war hammer is a common European mace, usually made of iron or steel.",
                               9, "weapon", 9)
        self.weapon13 = Reward("Berken hatchet",
                               "The Berken hatchet is a French mace with a wide axe and a longer grip. ",
                               9, "weapon", 10)
        self.weapon14 = Reward("Bomb",
                               "It's powerful enough to do a lot of damage at once.",
                               9, "weapon", 10)

    def fight_with_item(self, choose_id):
        """
        implement the fight with item.
        item is a weapon or a potion can be used in a fight.
        :param choose_id: the id of item knight want to use in this fight round.
        :return: str
        """
        text = '\n====================================\n'
        item = self.knight.backpack[choose_id]

        if item.kind == 'potion':  # the item makes effect and the effect depends on the kind of each item.
            hp_before_knight = self.knight.hp  # record the HP before using the potion.
            self.knight.hp = min(self.knight.hp_limit,
                                 self.knight.hp + random.randint(item.level, item.level * 2))
            hp_before_monster = self.current_room.monster.hp
            self.current_room.monster.hp -= random.randint(1, self.knight.attack)
            text += f'{self.knight.name} use the potion {item.name}. HP of {self.knight.name}: {hp_before_knight} ---> {self.knight.hp}\n'
            text += f'Without weapon {self.knight.name} causes some damage on {self.current_room.monster.name}. HP of {self.current_room.monster.name}: {hp_before_monster} ---> {max(0, self.current_room.monster.hp)}\n'
        else:
            # cause the hp of monster decreased.
            attack = random.randint(item.level, item.level + self.knight.attack)
            hp_before = self.current_room.monster.hp
            self.current_room.monster.hp -= attack
            text += f'{self.knight.name} use the weapon {item.name}. HP of {self.current_room.monster.name}: {hp_before} ---> {max(0, self.current_room.monster.hp)}\n'

        if self.current_room.monster.hp > 0:
            # knight suffers damage caused by monster.
            hp_before = self.knight.hp
            self.knight.hp -= self.current_room.monster.attack
            text += f'{self.current_room.monster.name} causes {self.current_room.monster.attack} damage on {self.knight.name}. HP of {self.knight.name}: {hp_before} ---> {max(0, self.knight.hp)}'

        return text

    def fight_no_item(self):
        """
        implement a fight without weapon.
        :return: str
        """
        text = '\n====================================\n'
        hp_before = self.current_room.monster.hp
        self.current_room.monster.hp -= self.knight.attack
        text += f"{self.knight.name} causes {self.knight.attack} damage on {self.current_room.monster.name}. HP of {self.current_room.monster.name}: {hp_before} ---> {max(0, self.current_room.monster.hp)}\n"

        if self.current_room.monster.hp > 0:
            hp_before = self.knight.hp
            self.knight.hp -= self.current_room.monster.attack
            text += f"{self.current_room.monster.name} causes {self.current_room.monster.attack} damage on {self.knight.name}. HP of {self.knight.name}: {hp_before} ---> {max(0, self.knight.hp)}"

        return text

    def welcome(self):
        """
        show the welcome message at the beginning of game.
        :return: str
        """
        text = f'''
        Once upon a time there was a princess named {self.princess.name}.
        She was so beautiful and kind that all people in the country loved her.
        However...
        One day an evil and strong monster, {self.monster10.name}, together with other nine monsters, attacked the country.
        They occupied the royal castle and rubbed the princess.
        
        Now {self.knight.description}
        The survivors from the castle told you that the castle has ten rooms, and each room was occupied by a monster.
        So your task is to dive into the castle and find a way to rescue the princess.
        You have to go through some rooms in the castle, and fight against the monster there.
        Go ahead brave Knight! Your princess is waiting for you!
        '''

        return text