from hash import Hash
from logo import generate_logo
from dbController import ObjectController
import config
import logging


def startup():
    operation = input('What you want to do? \n 1 - Generate password \n 2 - Read passwords \n 3 - Add password\n 4 - '
                      'Exit \n')
    try:
        result = int(operation)
    except Exception as e:
        logging.info(e)
        print('Wrong character! \n')
        return startup()
    if result == int(1) or result == int(2) or result == int(3) or result == int(4):
        if result == int(3):
            name = input('Type name of password\n')
            generated_password = input('Type password\n')
            password = ObjectController(config.check_dbtype(), name, generated_password)
            if password.add_object():
                startup()
        if result == int(1):
            strength = input('Choose strength of password? '
                             '\n 0 -  Only letters (low)'
                             '\n 1 - Letters mixed with numbers(medium) '
                             '\n 2 - Letters mixed with numbers and special characters(high) \n')
            try:
                strength = int(strength)
            except Exception as e:
                logging.info(e)
                print('Wrong character! \n')
                return startup()
            if strength != 1 and strength != 0 and strength != 2:
                print('Typed number is not 0/1/2')
                return startup()
            length = input('Type wanted length of password \n')
            try:
                length = int(length)
            except Exception as e:
                logging.info(e)
                print('Wrong character! \n')
                return startup()
            generate = Hash(strength, length)
            generated_password = generate()
            print('Your generated password is:', generated_password)
            __result = input('Do you want to save your password? y/n\n')
            if __result == "yes" or __result == "y":
                name = input('How do you want to call it? \n')
                password = ObjectController(config.check_dbtype(), name, generated_password)
                if password.add_object():
                    startup()
                else:
                    print(password.add_object())
            else:
                startup()
        elif result == int(2):
            password = ObjectController(config.check_dbtype(), None, None)
            password.show_objects()
            __action = input('\nType exit to back to the menu \nType remove to remove any password '
                             '\nType update to update password\n')
            print(__action)
            if __action == 'exit':
                startup()
            if __action == 'update':
                i = 1
                while i == 1:
                    print(i)
                    __ID = input('Type ID of password\n')
                    try:
                        __ID = int(__ID)
                    except Exception as e:
                        logging.info(e)
                        print('Wrong character! \n')
                        return startup()
                    passwd = input('Type new password \n')
                    if password.update_objects(passwd, __ID):
                        print('Updated successfully')
                        __do = input('Do you want to update something else? y/n \n')
                        if __do == 'yes' or 'Yes':
                            pass
                        if __do == 'no' or 'No':
                            i = 0
                            startup()
                        else:
                            i = 0
                            startup()
                    else:
                        print(password.update_objects(passwd, __ID))
                        return startup()
            if __action == 'remove':
                i = 1
                while i == 1:
                    print(i)
                    __ID = input('Type ID of password\n')
                    try:
                        __ID = int(__ID)
                    except Exception as e:
                        logging.info(e)
                        print('Wrong character! \n')
                        return startup()
                    if password.remove_objects(__ID):
                        print('Deleted successfully')
                        __do = input('Do you want to delete something else? y/n \n')
                        if __do == 'yes' or 'Yes':
                            pass
                        if __do == 'no' or 'No':
                            i = 0
                            startup()
                        else:
                            i = 0
                            startup()
                    else:
                        print(password.remove_objects(__ID))
                        return startup()
        else:
            pass

    else:
        print('Wrong operation! \n')
        return startup()


generate_logo()
config.startup_check()
startup()
