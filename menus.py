from operations import *


class Menu:
    def __init__(self, text, commands):
        # text prompt (string), possible inputs (list of strings)
        self.text = text
        self.commands = commands
    
    def print_text(self):
        print(self.text)

    
    def prompt_input(self):
        user_input = input("Enter a command: ")
        for command in self.commands:
            if user_input == command:
                return command
        raise Exception("Unknown command")


main_menu = Menu(
    "Welcome to Troikabot! Please enter one of the following commands to navigate to the desired menu: 'initiative','pc', 'npc', 'loot', 'world', 'quit'",
    ["initiative", "pc", "npc", "loot", "world", "quit"]
)

npc_generator = Menu(
    "Welcome to the NPC generator! Please enter one of the following commands: 'complete', 'background', 'stats', 'back'.", 
    ["complete", "background", "stats", "back"]
)

pc_generator = Menu(
    "Welcome to the PC generator! Please enter one of the following commands: 'complete', 'mood', 'tag', 'species', 'stats', 'spellbook', 'back'.",
    ["complete", "mood", "tag", "species", "stats", "spellbook", "back"]
)

initiative_tracker = Menu(
    "Welcome to the initiative tracker! please enter one of the following commands: 'start', 'back'.",
    ["start", "back"]
)

loot_generator = Menu(
    "Welcome to the loot generator! Please enter one of the following commands: 'any', 'common', 'uncommon', 'rare', 'legendary', 'back'.",
    ["any", "common", "uncommon", "rare", "back"]
)