import unittest

from Reward import Reward
from Role import *
from Room import Room


class Test(unittest.TestCase):
    """
    Perform the automatic unit test.
    """
    def setUp(self):
        # set up monsters.
        self.monster1 = Monster("Witch",
                                "Witches wear black robes and are good at using evil spells to launch attacks.", 3, 1,
                                "Fehfehfehfeh! Interesting young man. Are you ready for dying under my spell?", 1,
                                'images/monster1.jpg')
        self.monster2 = Monster("Ogre", "The ogre has a large body and sharp claws, and it moves quickly.", 6, 2,
                                "Shahahahaha! I'll tear you to pieces!", 2, 'images/monster2.jpg')
        self.monster3 = Monster("Vampire", "Vampires can fly very fast, and their high-pitched calls are fascinating.",
                                9, 3, "Gegyagyagyagya! I can't wait to taste your blood!", 3, 'images/monster3.jpg')
        # set up rooms.
        self.room1 = Room("Castle Kitchen",
                          "It's the kitchen and pantry inside the castle, where the cooks and servants worked.",
                          self.monster1, 'images/room1.jpg')
        self.room2 = Room("Banquet Hall",
                          "The banqueting Hall in the castle is used for banquets and large dinners, with long tables and ornate decorations.",
                          self.monster2, 'images/room2.jpg')
        self.room3 = Room("Stable",
                          "The stables in the castle are used to keep horses and other livestock, usually with mangers, feed cabinets, saddles and other horse gear.",
                          self.monster3, 'images/room3.jpg')
        # set up the knight.
        self.knight = Knight("Bobo", "You are a knight on an adventure to save a princess.", 10, 3, 3)
        # set up rewards.
        self.weapon1 = Reward("British Hunting Knife", "A weapon commonly used by English hunters and adventurers.", 1,
                              "weapon", 1)
        self.potion1 = Reward("Apple flavored potion", "Can restore some of your HP.", 1, "potion", 1)
        self.weapon2 = Reward("Hatchet", "A small axe, usually used for easy carrying.", 2, "weapon", 2)
        self.weapon3 = Reward("Stiletto sword", "A short sword used in Italy with a very thin and sharp blade.", 2,
                              "weapon", 2)

    def tearDown(self):
        del self.monster1
        del self.monster2
        del self.monster3
        del self.room1
        del self.room2
        del self.room3
        del self.knight
        del self.weapon1
        del self.weapon2
        del self.weapon3
        del self.potion1

    def test_monster(self):
        # test whether the monster makes the right growl.
        self.assertEqual(self.monster1.make_growl(), self.monster1.growl)
        self.assertEqual(self.monster2.make_growl(), self.monster2.growl)
        self.assertEqual(self.monster3.make_growl(), self.monster3.growl)

    def test_room(self):
        # test whether the room has the right monster.
        self.assertEqual(self.room1.monster, self.monster1)
        self.assertEqual(self.room2.monster, self.monster2)
        self.assertEqual(self.room3.monster, self.monster3)

        # add rewards to room.
        self.room1.add_rewards(self.weapon1)
        self.room1.add_rewards(self.weapon2)
        self.room2.add_rewards(self.potion1)
        self.room2.add_rewards(self.weapon3)

        # test whether the room has the right reward list.
        self.assertEqual(self.room1.rewards, [self.weapon1, self.weapon2])
        self.assertEqual(self.room2.rewards, [self.potion1, self.weapon3])

        # set the neighbor relationship between rooms.
        self.room1.set_next_room("Behind the door", self.room2)
        self.room1.set_next_room("Outside the window", self.room3)
        self.room2.set_next_room("Outside the left door", self.room3)

        # test whether the room has the right directions for corresponding next rooms.
        self.assertEqual(self.room1.next_rooms["Behind the door"], self.room2)
        self.assertEqual(self.room1.next_rooms["Outside the window"], self.room3)
        self.assertEqual(self.room2.next_rooms["Outside the left door"], self.room3)

    def test_knight(self):
        # test whether knight has the right initial total weight of backpack.
        self.assertEqual(self.knight.current_weight(), 0)

        # add item to knight's backpack
        self.knight.backpack.append(self.weapon1)

        # test whether the backpack has the right weight.
        self.assertEqual(self.knight.current_weight(), 1)

        # test whether the knight can afford the total weight of backpack.
        self.assertTrue(self.knight.capacity > self.knight.current_weight())


if __name__ == '__main__':
    unittest.main()
