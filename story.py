class Story(object):

    def __init__(self, branch_list):
        self.branch_list = branch_list

    def start(self):
        available_choices = []
        print('This is an interactive story. Type the number before the option to select the option.')
        starting_branch = self.branch_list[0]
        print(starting_branch.trunk)
        print(starting_branch.text)
        choice_dict = starting_branch.choice_list
        # print(choice_dict)
        for x in range(len(choice_dict)):
            id_list = choice_dict[x]
            available_choices.append(str(id_list[0]))
            print(str(id_list[0]) + ':', id_list[1])
        print(available_choices)
        choice = input('What is your choice? ')
        # if choice in available_choices:
        #     print('yes')
        # else:
        #     print('no')
        choice = str(choice)
        if choice in available_choices:
            self.enter_branch(choice)
            print(choice)
        else:
            print(choice, 3)

    def enter_branch(self, id):
        working_branch = self.get_branch_by_id(id)

    def get_branch_by_id(self, id):
        for x in self.branch_list:
            if x.check_id(id):
                return x
        print('tacooo')


class Branch(object):

    def __init__(self, id,  trunk, text, choice_list):
        self.id = id
        self.trunk = trunk
        self.text = text
        self.choice_list = choice_list

    def get_choice(self, x):
        print(self.choice_list[x])
        # print()

    def get_trunk(self):
        return self.trunk

    def check_id(self, id):
        if id == self.id:
            return True
        else:
            return False


branch1 = Branch(1, 'hi', 'What will you say?', [ (2,'bye'), (3,'hello')])
branch2 = Branch(2, 'bye', 'What will you eat', [(4,'ice cream'), (5,'sandwich')])
list = [branch1, branch2]
taco = Story(list)
print(taco.start())
