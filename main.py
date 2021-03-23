from hash import Hash
from logo import generate_logo
from dbController import ObjectController
import config
import logging


def startup():
    operation = input('What you want to do? \n 1 - Generate password \n 2 - Read passwords \n')
    try:
        result = int(operation)
    except Exception as e:
        logging.info(e)
        print('Wrong character! \n')
        return startup()
    if result == int(1) or result == int(2):
        if result == int(1):
            generate = Hash(0, 16)
            generated_password = generate()
            print('Your generated password is:', generated_password)
            __result = input('Do you want to save your password? y/n')
            if __result == "yes" or __result == "y":
                name = input('How do you want to call it? \n')
                password = ObjectController(config.check_dbtype(), name, generated_password)
                if password.add_object():
                    pass
                else:
                    print(password.add_object())
            else:
                pass
        else:
            password = ObjectController(config.check_dbtype(), None, None)
            password.show_objects()
    else:
        print('Wrong operation! \n')
        return startup()


generate_logo()
config.startup_check()
startup()
