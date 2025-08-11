import sys

from operations import *


# define Menu class:

class Menu:
    def __init__(self, text, commands):
        # text prompt (string), possible inputs (list of strings)
        self.text = text
        self.commands = commands
        self.input = None
    
    def print_text(self):
        print(self.text)

    def prompt_input(self):
        user_input = input("Enter a command: ")
        self.input = user_input
    
    def execute_input(self):
        input_object = self.commands.get(self.input)
        if input_object and isinstance(input_object, Menu):
            return input_object
        elif input_object == sys.exit:
            input_object()  # Call sys.exit() to exit the program
        elif input_object:
            print(input_object.initiate())
        else:
            print("Invalid command.")
        return self


# menu objects:

home = Menu(
    "Welcome to Troikabot! Please enter one of the following commands to navigate to the desired menu: 'initiative','pc', 'npc', 'loot', 'world', 'quit'",
    {}
)

npc = Menu(
    "Welcome to the NPC generator! Please enter one of the following commands: 'complete', 'spellbook', 'background', 'stats', 'color', 'back'.",
    {}
)

pc = Menu(
    "Welcome to the PC generator! Please enter one of the following commands: 'complete', 'stats', 'spell', 'background', 'back'",
    {}
)

npc_species = Menu(
    "Welcome to the species generator! Please enter one of the following commands: 'any', 'animal', 'fantasy'",
    {}
)

initiative = Menu(
    "Welcome to the initiative tracker! please enter one of the following commands: 'start', 'back'.",
    {}
)

loot = Menu(
    "Welcome to the loot generator! Please enter one of the following commands: 'any', 'common', 'uncommon', 'rare', 'legendary', 'back'.",
    {}
)

world = Menu(
    "Welcome to the world generator! Please enter one of the following commands: 'complete', 'biome', 'tag', 'aesthetic', 'species', 'building', 'location', 'back'.",
    {}
)


# command lists:

home_commands = {
    "initiative": initiative,
    "pc": pc,
    "npc": npc,
    "loot": loot,
    "world": world,
    "quit": sys.exit
}

pc_commands = {
    "complete": pc_complete,
    "background": pc_background,
    "stats": pc_stats,
    "spell": pc_spell,
    "back": home
}

npc_commands = {
    "complete": npc_complete,
    "mood": npc_mood,
    "tag": npc_tag,
    "species": npc_species,
    "stats": npc_stats,
    "spellbook": npc_spellbook,
    "color": npc_color,
    "back": home
}

species_commands = {
    "any": npc_any_species,
    "animal": npc_animal_species,
    "fantasy": npc_fantasy_species,
    "back": home
}

initiative_commands = {
    "start": initiative_start,
    "back": home
}

loot_commands = {
    "any": loot_any,
    "common": loot_common,
    "uncommon": loot_uncommon,
    "rare": loot_rare,
    "legendary": loot_legendary,
    "back": home
}
    
world_commands = {
    "biome": world_biome,
    "building": world_building,
    "complete": world_complete,
    "aesthetic": world_aesthetic,
    "location": world_location,
    "species": npc_any_species,
    "tag": npc_tag,
    "back": home
}
# linking menus to their command lists:

home.commands = home_commands
npc.commands = npc_commands
pc.commands = pc_commands
npc_species.commands = species_commands
initiative.commands = initiative_commands
loot.commands = loot_commands
world.commands = world_commands
