import time
import enum
import random


class Story(object):

    def __init__(self, title, branch_list, author = ''):
        self.title = title
        self.branch_list = branch_list
        self.author = author

    def start(self):
        available_choices = []
        print(self.title)
        if len(self.author) > 0:
            print('By ' + self.author)
        print('This is an interactive story. Type the number before the option to select the option.')
        start = self.get_start()
        self.enter_branch(start.id)

    def enter_branch(self, id):
        available_choices = []
        working_branch = self.get_branch_by_id(id)
        # print(working_branch.id)
        print('')
        print(working_branch.trunk)
        time.sleep(0.25)
        print(working_branch.text)
        if working_branch.type != Type.END:
            if working_branch.type == Type.RNG:
                for x in range(len(working_branch.choice_list)):
                    id_list = working_branch.get_choice(x)
                    available_choices.append(str(x))
                    print(id_list[1])
                    time.sleep(0.25)
                done = False
                print(working_branch.id)
                new_list = working_branch.randomize_choices()
                while not done:
                    print(new_list)
                    choice = input('Pick a number from 1 to ' + str(len(new_list)) + '. Your number will give you a random option from this list.')
                    choice = int(choice)
                    choice -= 1
                    choice = str(choice)
                    if choice in available_choices:
                        done = True
                        print(choice)
                        next_branch = new_list[int(choice)][0]
                        print(new_list[int(choice)][1])
                        self.enter_branch(next_branch)
                    else:
                        print('The choice is invalid, please try again.')
            else:
                for x in range(len(working_branch.choice_list)):
                    id_list = working_branch.get_choice(x)
                    available_choices.append(str(id_list[0]))
                    print(str(id_list[0]) + ':', id_list[1])
                    time.sleep(0.25)
                # print(available_choices)
                done = False
                while not done:
                    choice = input('What is your choice? ')
                    choice = str(choice)
                    if choice in available_choices:
                        done = True
                        print(choice)
                        self.enter_branch(int(choice))
                    else:
                        print('The choice is invalid, please try again.')
        elif working_branch.type == Type.END:
            self.end()

    def get_branch_by_id(self, id):
        for x in self.branch_list:
            if x.check_id(id):
                return x

    def get_start(self):
        for x in self.branch_list:
            if x.type == Type.START:
                return x

    def end(self):
        print('Thank you for playing ' + self.title)
        if len(self.author) > 0:
            print('by ' + self.author)
        repeat = input('Would you like to play again? Y/N ')
        if repeat == 'Y':
            print('')
            self.start()
        elif repeat == 'N':
            pass
        else:
            print('Would you like to play again? Type Y for yes and N for no.')


class Type(enum.Enum):
    START = 1
    END = 2
    MIDDLE = 3
    RNG = 4


class Branch(object):

    def __init__(self, id, trunk, text, choice_list, type = Type.MIDDLE):
        self.id = id
        self.trunk = trunk
        self.text = text
        self.choice_list = choice_list
        self.type = type

    def get_choice(self, x):
        return self.choice_list[x]

    def check_id(self, id):
        if id == self.id:
            return True
        else:
            return False

    def get_raw_choices(self):
        choice_list = []
        for x in self.choice_list:
            choice_list.append(x[1])
        return choice_list


class RNGBranch(Branch):

    def __init__(self, id, trunk, text, choice_list, type=Type.RNG):
        self.id = id
        self.trunk = trunk
        self.text = text
        self.choice_list = choice_list
        self.type = type

    def randomize_choices(self):
        choice_list = self.choice_list
        random_list = []
        for x in range(len(choice_list)):
            choice = random.choice(choice_list)
            random_list.append(choice)
            choice_list.remove(choice)
        self.choice_list = random_list
        return random_list

'''Testing/Debugging Code'''
# branch_ = Branch(1678, '', '', [(971, ''), (118, '')])  #template for branches
# branch_1 = Branch(1, 'hi', 'What will you say?', [(2, 'bye'), (3, 'hello'), (8, 'banana')], Type.START)
# branch_2 = Branch(2, 'bye', 'What will you eat', [(4, 'ice cream'), (5, 'sandwich')])
# branch_3 = Branch(3, 'what', 'ABCD', [(6, 'good night'), (7, 'morning!')])
# branch_4 = Branch(4, 'I like ice cream', 'pick a number', [(8, 'eight'), (9, 'nine')])
# branch_8 = Branch(8, 'It\'s time for the end', 'THE END', [], Type.END)
# branch_test = RNGBranch(2, 'woah', 'kapow', [(4, 'abcd'), (8, 'etghg')])
# list = [branch_1, branch_2, branch_3, branch_4, branch_8]
# list2 = [branch_1, branch_test, branch_4, branch_8]
# taco = Story('Test story', list2)
# taco.start()

branch_1 = Branch(1, 'The year is -403.', 'The evil king Bob reigns over the land. One brave adventurer heads out to save the world. Where do you go to start your quest?', [(2, 'The Bar'), (3, 'The Farm'), (4, 'The Mines')], Type.START)
branch_2 = Branch(2, ' You go to the bar,', 'Your lack of identification leads to you being kicked out. You go home.', [], Type.END)
branch_3 = Branch(3, 'You go to a nearby farm, seeking adventure.', 'The farmer asks you to deal with a swarm of evil chickens. Do you accept this quest?', [(5, 'Accept'), (6, 'Refuse')])
branch_4 = Branch(4, 'You go to the mines, run by the Evil King Bob.', ' Do you try to start a revolt or investigate', [(7, 'Revolt'), (8, 'Investigate')])
branch_5 = Branch(5, 'You accept the quest.', 'You hunt down the chickens. Do you fight them or negotiate?', [(9, 'Fight'), (10, 'Negotiate')])
branch_6 = Branch(6, 'You refuse.', ' You go around town looking for another quest, but fail. You just go home, and go back to your life.', [], Type.END)
branch_7 = Branch(7, 'No one listens to your revolt, claiming they won’t be led by someone with a fashion sense as bad as yours.', 'Buy new clothes or try to convince them to follow you?', [(11, 'Buy new clothes'), (12, 'Convince them')])
branch_8 = Branch(8, 'You put on a monocle, becoming the ultimate detective.', 'You find a ticket on a ship going straight to Bob. There, you meet Bob. Do you steal his coffee, or challenge him to a duel?', [(13, 'Steal the coffee'), (14, 'Duel Him')])
branch_9 = Branch(9, 'You try to fight the chickens. ', 'However, the local PETA branch doesn’t allow it, and you go to court for attempted animal abuse. Do you plead guilty or innocent?', [(15, 'Guilty'), (16, 'Innocent')])
branch_10 = Branch(10, 'Through the powers of Diplomacy and Negotiation, you and the chickens come to an accord.', ' They end their evil reign of terror, and you get your reward from the farmer', [], Type.END)
branch_11 = Branch(11, 'You spend the rest of your life raising money to get new clothes. ', 'When you buy them, it’s already been 23 years since a younger, cooler hero defeated Bob.', [], Type.END)
branch_12 = Branch(12, 'They don’t listen, and try to throw you out.', 'Do you resist or leave?', [(17, 'Resist'), (18, 'Leave')])
branch_13 = Branch(13, 'You steal his coffee.', 'He isn’t able to function without it. You win. ', [], Type.END)
branch_14 = Branch(14, 'You duel him in an epic grilling contest.', 'Unfortunately, Bob makes better burgers, and you return home as a humbled man.', [], Type.END)
branch_15 = Branch(15, 'You plead guilty.', 'PETA forgives you for seeing the error of your ways, and lets you go. You go home, where the farmer meets you, angry that you haven’t dealt with the chicken. The farmer makes you spend the rest of your life picking cabbages for him.', [], Type.END)
branch_16 = Branch(16, 'You plead innocent.', 'The court is rigged, and you go to jail. In jail you meet Steve Jeff, Bob’s right hand man. Do you break out with him or stay in jail?', [(19, 'Stay'), (20, 'Break Out')])
branch_17 = Branch(17, 'The guards come by, and force you to work in the mine. ', 'You eventually find a precious diamond. Do you sell it or keep it?', [(21, 'Sell it'), (22, 'Keep it')])
branch_18 = Branch(18, 'You leave.', 'You go home, finding a dragon egg in the woods on the way home. 10 years later, you’re riding a dragon into King Bob’s front door.', [], Type.END)
branch_19 = Branch(19, ' You stay in jail until your 3 week sentence is over.', 'You return home, and see that heroics aren’t for you.', [], Type.END)
branch_20 = Branch(20, '', '', [(971, ''), (118, '')])
branch_21 = Branch(21, '', '', [(971, ''), (118, '')])
branch_22 = Branch(22, '', '', [(971, ''), (118, '')])
branch_23 = Branch(23, '', '', [(971, ''), (118, '')])
branch_24 = Branch(24, '', '', [(971, ''), (118, '')])

branch_list =  [branch_1, branch_2, branch_3, branch_4, branch_5, branch_6, branch_7, branch_8,
                branch_9, branch_10, branch_11, branch_12, branch_13, branch_14, branch_15, branch_16,
                branch_17, branch_18, branch_19, branch_20, branch_21, branch_22, branch_23, branch_24]
my_story = Story('THE RISE OF A HERO', branch_list)


