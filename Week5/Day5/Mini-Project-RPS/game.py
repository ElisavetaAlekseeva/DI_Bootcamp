from platform import win32_edition
import random


class Game:
    def get_user_item(self):
        while True:
            users_item = input('Select: (r)ock, (p)aper, (s)cissors: ')
            if users_item == 'r' or users_item == 'p' or users_item == 's':
                return users_item
            else:
                continue


    def get_computer_item(self):
        computer_item = random.choice(['r', 's', 'p'])
        return computer_item


    def get_game_result(self, user_item, computer_item, results):
        self.result = ''
        if (user_item == 'r' and computer_item == 's') or (user_item == 's' and computer_item == 'p') or (user_item == 'p' and computer_item == 'r'):
            self.result = 'won'
            results['won'] += 1
            return self.result

        elif (computer_item == 'r' and user_item == 's') or (computer_item == 's' and user_item == 'p') or (computer_item == 'p' and user_item == 'r'):
            self.result = 'lose'
            results['lose'] += 1
            return self.result
            

        elif computer_item == user_item:
            self.result = 'drew'
            results['drew'] += 1
            return self.result


    def play(self, results):
        users_item = self.get_user_item()
        computer_item = self.get_computer_item()
        self.get_game_result(users_item,computer_item, results)
        print(f'You chose: {users_item}. The computer choise: {computer_item} Result: {self.result}')
        return self.result
