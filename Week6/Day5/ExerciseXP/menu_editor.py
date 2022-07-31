
def load_manager(name, price):
    return MenuItem(name, price)

def show_user_menu():
    print("""
        MENU
    (a) Add an item
    (d) Delete an item
    (v) View the menu
    (x) Exit
    """)
    user_input = input('Your choice: ')
    if user_input == 'a':
        add_item_to_menu()
    elif user_input == 'd':
        remove_item_from_menu()
    elif user_input == 'v':
        show_restaurant_menu()
    elif user_input == 'x':
        break
    

def add_item_to_menu():
    user_input = (input('enter name and price: ')).split(',')
    name = user_input[0]
    price = int(user_input[1])
    item = load_manager(name, price)
    item.save(name, price)
    print('item was added successfully.')

def remove_item_from_menu():
    name = input('name of the item they want to remove from the restaurants menu: ')
    MenuItem.delete(name)

def show_restaurant_menu():
    MenuItem.all()