# Argument Parsing:
"""
    Example command: python3 manage.py makemigrations
"""
import sys

import time

def makemigrations():
    time.sleep(1)
    print("Create Model:\n  - Profile\n  - Author\n  - Address\n")

def migrate():
    time.sleep(0.2)
    print("Applying db.models.Profile..........")
    time.sleep(0.2)    
    print("Applying db.models.Author..........")
    time.sleep(0.2)
    print("Applying db.models.Book..........")
    time.sleep(0.2)
    print("Applying db.models.Address..........")
    time.sleep(0.2)
    print("Applying db.models.Profile..........")
    time.sleep(0.2)
    print("Applying db.models.Profile..........")
    time.sleep(0.2)
    print("Applying db.models.Profile..........")
    time.sleep(0.2)
    print("Applying db.models.Profile..........")
    time.sleep(0.2)
    print("Applying db.models.Profile..........")


args = {'makemigrations':makemigrations, 'migrate':migrate}

passed_args = sys.argv[1:]

for i in passed_args:
    try:
        args[i]()
    except:
        print(f'Sorry invalid argument: {i}')
