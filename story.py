import time


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
        self.enter_branch(1)

    def enter_branch(self, id):
        available_choices = []
        working_branch = self.get_branch_by_id(id)
        # print(working_branch.id)
        print('')
        print(working_branch.trunk)
        time.sleep(0.25)
        print(working_branch.text)
        if not working_branch.end:
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
                    print(choice, working_branch.id)
                    self.enter_branch(int(choice))
                else:
                    print('The choice is invalid, please try again.')
        elif working_branch.end:
            self.end()

    def get_branch_by_id(self, id):
        for x in self.branch_list:
            if x.check_id(id):
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


class Branch(object):

    def __init__(self, id, trunk, text, choice_list = [], end=False):
        self.id = id
        self.trunk = trunk
        self.text = text
        self.choice_list = choice_list
        self.end = end

    def get_choice(self, x):
        return self.choice_list[x]
        # print()

    def get_trunk(self):
        return self.trunk

    def check_id(self, id):
        if id == self.id:
            return True
        else:
            return False


branch_ = Branch(1678, '', '', [(971, ''), (118, '')])#template for branches
branch_1 = Branch(1, 'hi', 'What will you say?', [(2, 'bye'), (3, 'hello')])
branch_2 = Branch(2, 'bye', 'What will you eat', [(4, 'ice cream'), (5, 'sandwich')])
branch_3 = Branch(3, 'what', 'ABCD', [(6, 'good night'), (7, 'morning!')])
branch_4 = Branch(4, 'I like ice cream', 'pick a number', [(8, 'eight'), (9, 'nine')])
branch_8 = Branch(8, 'It\'s time for the end', 'THE END', [(),()], True)

list = [branch_1, branch_2, branch_3, branch_4, branch_8]
taco = Story('Test story', list, 'bob')
taco = Story('Test story', list)

print(taco.start())
