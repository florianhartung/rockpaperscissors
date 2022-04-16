from rps import *
import random

# Define objects
rock = RPSObject("rock")
paper = RPSObject("paper")
scissors = RPSObject("scissors")

# Define rules
rock >> scissors
scissors >> paper
paper >> rock

# Save objects by name
rps_objects = {obj.name.casefold(): obj for obj in [rock, paper, scissors]}


def get_object_by_name(name: str) -> RPSObject:
    return rps_objects.get(name.casefold())


def random_cpu_choice():
    return random.choice(list(rps_objects.values()))


def get_player_choice():
    objects_list_string = str(list(rps_objects.keys()))[1:-1].replace('\'', '')

    player_choice_str = input(f"Please choose one of {objects_list_string}.\nYour choice: ")
    return get_object_by_name(player_choice_str)


def main():
    cpu_choice = random_cpu_choice()
    player_choice = get_player_choice()

    if player_choice is None:
        print("Invalid choice!")
        return

    print(f"I chose {cpu_choice.name}")

    outcome = player_choice > cpu_choice
    if outcome == RPSOutcome.WIN:
        print("You win!")
    elif outcome == RPSOutcome.LOSS:
        print("You lost!")
    elif outcome == RPSOutcome.TIE:
        print("Tie!")


if __name__ == '__main__':
    main()
