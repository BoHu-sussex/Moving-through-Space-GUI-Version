import time
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

from PIL import ImageTk, Image

from Game import Game


class GameGUI:
    """
    This class is to implement the GUI version of the game.
    """

    def __init__(self, root):
        """
        initialize the GUI.
        :param root: the root window.
        """
        self.root = root
        self.game = Game()
        self.create_menubar()
        self.create_frame_welcome()
        self.logfile = open('log-file.txt', 'a')  # create a log file recording user's input.
        self.logfile.write('A new game begin.\n\n')

    def create_frame_room(self):
        """
        create the frame when entering a room.
        :return: none
        """
        if not self.game.current_room.is_win:
            self.frame_room = tk.Frame(self.root, width=600, height=400)
            self.frame_room.pack()

            # loading the image of room
            self.img_room = ImageTk.PhotoImage(Image.open(self.game.current_room.image_path))
            tk.Label(self.frame_room, image=self.img_room).grid(row=0, column=0)

            # add the description of room
            tk.Label(self.frame_room, text=f'Location: {self.game.current_room.name}').grid(row=1, column=0)
            tk.Label(self.frame_room, text=self.game.current_room.description).grid(row=2, column=0)

            # continue the game
            tk.Label(self.frame_room).grid(row=3)
            tk.Button(self.frame_room, text='Continue', command=self.meet_monster).grid(row=4, column=0)
        else:
            self.logfile.write(
                f'\n{time.ctime()}    Knight {self.game.knight.name} returns back the room {self.game.current_room.name} again.')
            self.choose_room()

    def meet_monster(self):
        """
        create the frame when meeting a monster
        :return: none
        """
        self.logfile.write(
            f'\n{time.ctime()}    Knight {self.game.knight.name} meets the monster {self.game.current_room.monster.name}.')
        # clear the window
        self.frame_room.destroy()

        # reset the fight
        self.game.knight.hp = self.game.knight.hp_limit
        self.game.current_room.monster.hp = self.game.current_room.monster.hp_limit
        self.game.knight.alive = True
        self.round_message = ''

        # create a frame to show monster
        self.frame_monster = tk.Frame(self.root, width=600, height=500)
        self.frame_monster.pack()
        self.img_monster = ImageTk.PhotoImage(Image.open(self.game.current_room.monster.image_path))
        tk.Label(self.frame_monster, image=self.img_monster).grid(row=0, column=0)
        tk.Label(self.frame_monster, text=f'Location: {self.game.current_room.name}').grid(row=1, column=0)
        tk.Label(self.frame_monster, text=f'Monster: {self.game.current_room.monster.name}').grid(row=2, column=0)
        tk.Label(self.frame_monster, text=self.game.current_room.monster.show_description()).grid(row=3, column=0)
        tk.Label(self.frame_monster).grid(row=4)

        # monster makes growl
        tk.Button(self.frame_monster, text='Continue', command=self.start_fight).grid(row=5, column=0)

        if self.game.current_room == self.game.room10:
            messagebox.showinfo('Final Boss!',
                                f'Now you encounter the final BOSS!!!\n\n{self.game.current_room.monster.name}: {self.game.current_room.monster.growl}\n\n(Ready to fight!)')
        else:
            messagebox.showinfo('Monster is coming!',
                                f'{self.game.current_room.monster.name}: "{self.game.current_room.monster.growl}"\n\n(Ready to fight!)')

    def start_fight(self):
        """
        create the frame when fight start.
        :return: none.
        """

        # clear the window
        self.frame_monster.destroy()

        # create a frame to perform fight
        self.frame_fight = tk.Frame(self.root, width=600, height=500)
        self.frame_fight.pack()

        # load the image of fighters
        tk.Label(self.frame_fight, image=self.img_knight).grid(row=0, column=0)
        tk.Label(self.frame_fight, text='VS').grid(row=0, column=1)
        tk.Label(self.frame_fight, image=self.img_monster).grid(row=0, column=2)

        # load the info of fighters
        tk.Label(self.frame_fight, text=f'Basic attack: {self.game.knight.attack}').grid(row=1, column=0)
        self.knight_hp_label = tk.Label(self.frame_fight, text=f'Hp: {self.game.knight.hp}')
        self.knight_hp_label.grid(row=2, column=0)
        tk.Label(self.frame_fight, text=f'attack: {self.game.current_room.monster.attack}').grid(row=1, column=2)
        self.monster_hp_label = tk.Label(self.frame_fight, text=f'Hp: {self.game.current_room.monster.hp}')
        self.monster_hp_label.grid(row=2, column=2)

        # add a text area to record the fight round
        tk.Label(self.frame_fight).grid(row=3)
        tk.Label(self.frame_fight).grid(row=4)
        tk.Label(self.frame_fight, text='-----Fight round record-----').grid(row=5, column=0, columnspan=2)

        # create a entry to get the user's input
        self.round_text = ScrolledText(self.frame_fight, height=8, width=40)
        self.round_text.grid(row=6, column=0, columnspan=2)

        # add an entry to choose a weapon or potion
        if not self.game.knight.backpack:
            tk.Label(self.frame_fight, text='(Empty backpack! Fight without weapon!)').grid(row=5, column=2)
        else:
            tk.Label(self.frame_fight, text='Choose an item!(Enter the item id)').grid(row=4, column=2)
            self.item_entry = tk.Entry(self.frame_fight)
            self.item_entry.grid(row=5, column=2)

        # add a button to perform a fight round
        tk.Button(self.frame_fight, text='Attack', command=self.update_round_text).grid(row=6, column=2)

    def update_round_text(self):
        """
        update the fight information into the entry text box.
        :return: none
        """
        if not self.game.knight.backpack:
            text_no_item = self.game.fight_no_item()
            self.round_text.insert('1.0', text_no_item)
            self.logfile.write(f'\n{time.ctime()}    fighting...{text_no_item}')

            # upgrade the info of fighters
            self.knight_hp_label.config(text=f'Hp: {max(0, self.game.knight.hp)}')
            self.monster_hp_label.config(text=f'Hp: {max(0, self.game.current_room.monster.hp)}')

            if self.game.current_room.monster.hp <= 0:
                self.game.current_room.is_win = True
                self.game.current_room.monster.alive = False
                # knight level up
                self.game.knight.increase_attack()
                self.game.knight.increase_capacity()
                self.game.knight.increase_hp_limit()
                messagebox.showinfo('You Win!',
                                    f'You defeat {self.game.current_room.monster.name}!\n\nNow your HP increase to {self.game.knight.hp_limit}\nNow your basic attack increase to {self.game.knight.attack}\nNow your capacity increase to {self.game.knight.capacity}')
                self.choose_reward()

            # lose the fight
            if self.game.knight.hp <= 0:
                self.game.visited_rooms.pop()
                messagebox.showinfo('You Lose...',
                                    f'{self.game.current_room.monster.name} in {self.game.current_room.name} is too hard to defeat...\nYou have to return back to {self.game.visited_rooms[-1].name}')
                self.game.current_room = self.game.visited_rooms[-1]

                # enter the next room
                self.frame_fight.destroy()
                self.create_frame_room()

        # fight with weapon or potion
        else:
            flag = False  # to mark whether the item is chosen
            # prevent error
            try:
                item_id = int(self.item_entry.get()) - 1
                text = self.game.fight_with_item(item_id)
                flag = True
                self.item_entry.delete(0)
            except IndexError:
                self.item_entry.delete(0)
                messagebox.showerror('Oops...', 'Your backpack has no such item.\nPlease enter again.')
                self.frame_fight.destroy()
                self.start_fight()
                self.round_text.insert('1.0', self.round_message)
            except ValueError:
                self.item_entry.delete(0)
                messagebox.showerror('Oops...', 'You must enter an int number!\nPlease enter again.')
                self.frame_fight.destroy()
                self.start_fight()
                self.round_text.insert('1.0', self.round_message)

            if flag:
                self.logfile.write(f'\n{time.ctime()}    fighting...{text}')
                # upgrade the info of fighters
                self.knight_hp_label.config(text=f'Hp: {max(0, self.game.knight.hp)}')
                self.monster_hp_label.config(text=f'Hp: {max(0, self.game.current_room.monster.hp)}')
                self.round_text.insert('1.0', text)
                self.round_message = '{}{}'.format(text, self.round_message)

                if self.game.current_room.monster.hp <= 0:
                    self.game.current_room.is_win = True
                    self.game.current_room.monster.alive = False

                    # whether win the game
                    if not self.game.monster10.alive:
                        self.game_win()
                    else:
                        # knight level up
                        self.game.knight.increase_attack()
                        self.game.knight.increase_capacity()
                        self.game.knight.increase_hp_limit()
                        messagebox.showinfo('You Win!',
                                            f'You defeat {self.game.current_room.monster.name}!\n\nNow your HP increase to {self.game.knight.hp_limit}\nNow your basic attack increase to {self.game.knight.attack}\nNow your capacity increase to {self.game.knight.capacity}')
                        # go to next part of the game
                        self.choose_reward()

                # lose the fight
                if self.game.knight.hp <= 0:
                    self.game.visited_rooms.pop()
                    self.logfile.write(
                        f'\n{time.ctime()}    Knight {self.game.knight.name} loses the fight and returns back the last room.')
                    messagebox.showinfo('You Lose...',
                                        f'{self.game.current_room.monster.name} in {self.game.current_room.name} is too hard to defeat...\nYou have to return back to {self.game.visited_rooms[-1].name}')
                    self.game.current_room = self.game.visited_rooms[-1]
                    # return back to last room.
                    self.frame_fight.destroy()
                    self.create_frame_room()

    def game_win(self):
        """
        create a frame while the final boss was defeated.
        :return: none
        """
        messagebox.showinfo('Game WIN!', 'The final boss is defeated!!!\n The princess is safe now!!!')
        self.frame_fight.destroy()
        # create the frame
        self.frame_win = tk.Frame(self.root, width=600, height=600)
        self.frame_win.pack()
        # load the image of princess
        self.img_princess = ImageTk.PhotoImage(Image.open('images/princess.jpg'))
        tk.Label(self.frame_win, image=self.img_princess).grid(row=0, column=0)

        text = f'{self.game.princess.name}: \n"{self.game.knight.name} you save me! What a brave Knight!"'
        tk.Label(self.frame_win, text=text).grid(row=1, column=0)
        tk.Label(self.frame_win).grid(row=2)
        self.logfile.write(f'\n{time.ctime()}    The final boss is dead. Princess is safe now. You win the game.')
        tk.Button(self.frame_win, text='Finish the game', command=self.root.destroy).grid(row=3, column=0)

    def choose_reward(self):
        """
        create a frame while choosing a reward after beating the monster.
        :return: none
        """
        # clear the window
        self.frame_fight.destroy()

        # create a frame to show a reward box
        self.frame_reward1 = tk.Frame(self.root, width=600, height=300)
        self.frame_reward1.pack()
        self.img_reward = ImageTk.PhotoImage(Image.open('images/reward.jpg'))
        tk.Label(self.frame_reward1, image=self.img_reward).grid(row=0, column=0)
        tk.Label(self.frame_reward1, text=f'{self.game.knight.name} you can choose a reward now!').grid(row=1, column=0)

        # show the reward information.
        texts = self.game.current_room.show_rewards()
        for i, text in enumerate(texts):
            tk.Label(self.frame_reward1, text=text, anchor='w', justify='left').grid(row=i + 2, column=0, sticky='w')

        # create a frame to provide a choose
        self.frame_reward2 = tk.Frame(self.root, width=600, height=300)
        self.frame_reward2.pack()
        tk.Label(self.frame_reward2, text='Enter the reward id: ').grid(row=0, column=0)
        self.reward_entry = tk.Entry(self.frame_reward2)
        self.reward_entry.grid(row=0, column=1)
        tk.Label(self.frame_reward2).grid(row=1)
        tk.Button(self.frame_reward2, text='Continue', command=self.get_reward).grid(row=2, column=0, columnspan=2)

    def get_reward(self):
        """
        add reward to backpack.
        :return: none
        """
        flag = False  # mark whether the reward was correctly chosen.

        # add reward to backpack
        try:
            reward_id = int(self.reward_entry.get()) - 1
            reward = self.game.current_room.rewards[reward_id]
            self.game.knight.backpack.append(reward)
            flag = True
        except ValueError:
            messagebox.showerror('Oops...', 'You must enter an int number!\nPlease entere again.')
            self.frame_reward1.destroy()
            self.frame_reward2.destroy()
            self.choose_reward()
        except IndexError:
            messagebox.showerror('Oops...', 'There is no such item in your backpack.\nPlease enter again.')
            self.frame_reward1.destroy()
            self.frame_reward2.destroy()
            self.choose_reward()

        if flag:
            self.logfile.write(
                f'\n{time.ctime()}    Knight {self.game.knight.name} wins the fight and chooses the reward {reward.name}')
            # overweight
            if self.game.knight.current_weight() > self.game.knight.capacity:
                messagebox.showinfo('Too weight...',
                                    'Now your backpack is too weight...\nYou have to drop something to satisfy your capacity.')
                self.frame_reward1.destroy()
                self.frame_reward2.destroy()
                # perform the drop of items.
                self.drop_items()
            else:
                self.frame_reward1.destroy()
                self.frame_reward2.destroy()
                # choosing the next room
                self.choose_room()

    def drop_items(self):
        """
        create a frame to perform the drop of items.
        :return: none
        """
        self.frame_drop1 = tk.Frame(self.root, width=600, height=300)
        self.frame_drop1.pack()
        # load the image.
        self.img_backpack = ImageTk.PhotoImage(Image.open('images/backpack.jpg'))
        tk.Label(self.frame_drop1, image=self.img_backpack).grid(row=0, column=0)
        tk.Label(self.frame_drop1, text='Choose one to drop...').grid(row=1, column=0)
        # show the weight and capacity.
        self.weight_label = tk.Label(self.frame_drop1, text=f'Total weight: {self.game.knight.current_weight()}')
        self.weight_label.grid(row=2, column=0)
        self.capacity_label = tk.Label(self.frame_drop1, text=f'Capacity: {self.game.knight.capacity}')
        self.capacity_label.grid(row=3, column=0)

        # create a frame to make player input.
        self.frame_drop2 = tk.Frame(self.root, width=600, height=300)
        self.frame_drop2.pack()
        # add a label
        tk.Label(self.frame_drop2).grid(row=0)
        tk.Label(self.frame_drop2, text='Enter the id you want to drop: ').grid(row=1, column=0)
        # add an entry box
        self.drop_entry = tk.Entry(self.frame_drop2)
        self.drop_entry.grid(row=1, column=1)
        # add a button to perform the drop
        tk.Label(self.frame_drop2).grid(row=2)
        tk.Button(self.frame_drop2, text='Continue', command=self.drop_one_item).grid(row=3, column=0, columnspan=2)

    def drop_one_item(self):
        """
        perform the drop
        :return: none
        """
        flag = False  # to mark whether the item was correctly dropped

        try:
            drop_id = int(self.drop_entry.get()) - 1
            self.game.knight.drop(self.game.knight.backpack[drop_id])
            self.weight_label.config(text=f'Total weight: {self.game.knight.current_weight()}')
            self.capacity_label.config(text=f'Capacity: {self.game.knight.capacity}')
            flag = True
        except IndexError:
            messagebox.showerror('Oops...', 'There is no such item in your backpack.\nPlease enter again.')
            self.frame_drop1.destroy()
            self.frame_drop2.destroy()
            self.drop_items()
        except ValueError:
            messagebox.showerror('Oops', 'You must enter an int number!\nPlease enter again.')
            self.frame_drop1.destroy()
            self.frame_drop2.destroy()
            self.drop_items()

        if flag:
            self.logfile.write(f'\n{time.ctime()}    Knight {self.game.knight.name} drops an item.')
            if self.game.knight.current_weight() > self.game.knight.capacity:
                messagebox.showinfo('Still too weight...', 'You have to drop items again.')
                self.drop_entry.delete(0)
            else:
                messagebox.showinfo('Drop finished!', 'Now you can continue your adventure!')
                self.frame_drop1.destroy()
                self.frame_drop2.destroy()
                self.choose_room()

    def choose_room(self):
        """
        create a frame to choose the next room
        :return:
        """
        self.frame_direction1 = tk.Frame(self.root, width=600, height=200)
        self.frame_direction1.pack()
        # load the image
        self.img_next_room = ImageTk.PhotoImage(Image.open('images/next_room.jpg'))
        tk.Label(self.frame_direction1, image=self.img_next_room).grid(row=0, column=0)
        # add a label
        tk.Label(self.frame_direction1, text='Here are the next rooms...').grid(row=1, column=0)

        # create a frame to show the details.
        self.frame_direction2 = tk.Frame(self.root, width=600, height=400)
        self.frame_direction2.pack()
        # get the details of next rooms.
        texts = self.game.current_room.show_next_rooms()
        for i, text in enumerate(texts):
            tk.Label(self.frame_direction2, text=text[1], anchor='w', justify='left').grid(row=i, column=0, sticky='w')
            tk.Label(self.frame_direction2).grid(row=i, column=1)
            tk.Button(self.frame_direction2, text='Choose this direction',
                      command=lambda direction_=text[0]: self.go_next_room(direction_)).grid(row=i, column=2,
                                                                                             columnspan=2)

    def go_next_room(self, direction):
        """
        change the location to next room
        :param direction: the direction of next room, a key in a dictionary.
        :return: none
        """
        # change the current room
        self.game.current_room = self.game.current_room.next_rooms[direction]
        self.game.visited_rooms.append(self.game.current_room)
        self.logfile.write(
            f'\n{time.ctime()}    Knight {self.game.knight.name} goes to the room {self.game.current_room.name}')

        self.frame_direction1.destroy()
        self.frame_direction2.destroy()

        # go to the next room
        self.create_frame_room()

    def create_menubar(self):
        """
        create the menubar of the window
        :return: none
        """
        self.menubar = tk.Menu()
        self.menubar.add_command(label='Quit', command=self.root.destroy)
        self.menubar.add_command(label='About', command=self.show_about)
        self.menubar.add_command(label='Backpack', command=self.show_backpack)
        self.root.config(menu=self.menubar)

    def show_backpack(self):
        """
        show the detail of items in backpack
        :return: none
        """
        messagebox.showinfo('Backpack', self.game.knight.inventory())

    def show_about(self):
        """
        show the game information
        :return: none
        """
        messagebox.showinfo('About',
                            'This game is about a knight going on an adventure to save a princess trapped in a castle, where has been occupied by ten evil monsters.\n\nYour goal is going to rooms in the castle and beating monster here.\n\nIf you beat the final BOSS, the princess will be safe!')

    def create_frame_welcome(self):
        """
        create a frame when game begin.
        :return: none
        """
        self.frame_welcome = tk.Frame(self.root, width=600, height=400)
        self.frame_welcome.pack()

        # loading an image of knight
        self.img_knight = ImageTk.PhotoImage(Image.open('images/knight.jpg'))
        tk.Label(self.frame_welcome, image=self.img_knight).grid(row=0, column=0)

        # add texts on frame_welcome
        text = self.game.welcome()
        tk.Label(self.frame_welcome, text=text).grid(row=1, column=0)

        # add an entry for player to input name
        self.frame_entry_name = tk.Frame(self.root, width=600, height=200)
        self.frame_entry_name.pack()
        # add a entry box
        tk.Label(self.frame_entry_name, text='Enter your name please: ').grid(row=0, column=0)
        self.name_entry = tk.Entry(self.frame_entry_name)
        self.name_entry.grid(row=0, column=1)

        # add a button to begin the game
        tk.Label(self.frame_entry_name).grid(row=1)
        tk.Button(self.frame_entry_name, text='Start the game!', command=self.start_game).grid(row=2, column=0,
                                                                                               columnspan=2)

    def start_game(self):
        """
        get the name of knight inputted by player and go to the next part.
        :return: none
        """
        # get the name
        self.game.knight.name = self.name_entry.get()

        # make sure name cannot be none
        if not self.game.knight.name:
            messagebox.showerror('Oops...', 'You must give knight a name.\nPlease enter again.')
            self.frame_welcome.destroy()
            self.frame_entry_name.destroy()
            self.create_frame_welcome()
        else:
            self.logfile.write(
                f'{time.ctime()}    The player give knight the name: {self.game.knight.name}\n{time.ctime()}    Knight {self.game.knight.name} goes to the room {self.game.current_room.name}')
            messagebox.showinfo('Game Start!',
                                f'Now the game BEGIN!\n\n{self.game.knight.name} now you are entering the first room...')

            # clear the window
            self.frame_welcome.destroy()
            self.frame_entry_name.destroy()

            # go to the first room
            self.create_frame_room()


def main():
    """
    run the GUI
    :return: none
    """
    win = tk.Tk()
    win.title('Moving Through Spaces')
    win.geometry('700x750')
    win.resizable(False, False)
    my_app = GameGUI(win)
    win.mainloop()
    my_app.logfile.write(f'\n{time.ctime()}    The game finished.\n\n\n\n\n\n\n')
    my_app.logfile.close()


if __name__ == '__main__':
    main()
