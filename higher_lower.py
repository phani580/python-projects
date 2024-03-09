import random
import game_art
import game_database

print(game_art.game_logo)
def display_info(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name},a {description},frm {country}"
account_1=random.choice(game_database.data)
account_2=random.choice(game_database.data)

print(f"compare 1:{display_info(account_1)}")
print(game_art.vs)
print(f"compare 2:{display_info(account_2)}")







