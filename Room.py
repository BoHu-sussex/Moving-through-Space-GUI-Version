class Room:
    """
    This class is to create a room.
    """

    def __init__(self, name, description, monster, image_path):
        """
        initialize a room.
        :param name: the name of this room.
        :param description: the text based description of this room.
        :param monster: the corresponding monster in this room.
        :param image_path: the image file path of this room.
        """
        self.name = name
        self.description = description
        self.monster = monster
        self.rewards = []  # the rewards list in the room.
        self.next_rooms = {}  # the dictionary of all the next rooms of this room and their directions.
        self.is_win = False  # label if player has won this room already.
        self.image_path = image_path

    def set_next_room(self, direction, next_room):
        """
        Set next rooms for this room. The next room is a dictionary, the `key` is the direction and the `value` is
        the corresponding next room.
        :param direction: the direction of the next room.
        :param next_room: one next
        room of this room.
        :return: None
        """
        self.next_rooms[direction] = next_room

    def show_next_rooms(self):
        """
        return all the next rooms.
        :return: str
        """
        text = []
        room_id = 1

        for direction, room in self.next_rooms.items():
            if room.is_win:
                message = "(You have already won this room.)"
            else:
                message = "(You have not won this room yet.)"

            print(f"* id-{room_id}:\n    Direction: `{direction}`\n    Next room: `{room.name}`\n    {message} ")
            text.append([direction,
                         f'* id-{room_id}:\n    Direction: {direction}\n    Next room: {room.name}\n    {message}\n-----------------------------------'])
            room_id += 1

        return text

    def add_rewards(self, reward):
        """
        Add rewards to a room.
        :param reward: an item to be added.
        :return: None
        """
        self.rewards.append(reward)

    def show_rewards(self):
        """
        show all the rewards in the room.
        :return: str
        """
        text = []

        for reward_id, reward in enumerate(self.rewards):  # show the items in a room.
            text.append(
                f'* id-{reward_id + 1}: \nName: {reward.name}\nDescription: {reward.description}\nWeight: {reward.weight}\nKind: {reward.kind}\nLevel: {reward.level}\n---------------------------------------------------------------------')

        return text

    def show_description(self):
        """
        return the description.
        :return: str
        """
        return self.description