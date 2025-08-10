import random

from menus import *


class Operation:
    def __init__(self):
        pass
    def initiate(self):
        pass


class Generator(Operation):
    def __init__(self, outcomes):
        super().__init__()
        self.outcomes = outcomes
    
    def initiate(self):
        result_index = random.randint(0, (len(self.outcomes) - 1))
        result = self.outcomes[result_index]
        return result


class PCComplete(Operation):
    def __init__(self):
        super().__init__()
    
    def initiate(self):
        background = pc_background.initiate()
        stats = pc_stats.initiate()
        print({"background": background, "stats": stats})


class NPCComplete(Operation):
    def __init__(self):
        super().__init__()

    def initiate(self):
        mood = npc_mood.initiate()
        tag = npc_tag.initiate()
        species = npc_species.initiate()
        stats = npc_stats.initiate()
        spellbook = npc_spellbook.initiate()
        print({"mood": mood, "tag": tag, "species": species, "stats": stats, "spellbook": spellbook})


#class InitiativeTracker(Operation):
    #def __init__(self):
    
    #def initiate(self):
        #print()


# Lists of outcomes:
pc_background_outcomes = []
pc_stats_outcomes = []
npc_background_outcomes = []
npc_stats_outcomes = []


# Fill outcome lists from files
def fill_outcome_list(outcome_list, file_path):
    with open(file_path, 'r') as file:
        for line in file:
            outcome = line.strip()
            if outcome:
                outcome_list.append(outcome)

fill_outcome_list(pc_background_outcomes, 'backgrounds.txt')


# List of generators:
pc_complete = PCComplete()
pc_background = Generator(pc_background_outcomes)
pc_stats = Generator([])

npc_complete = NPCComplete()
npc_mood = Generator([])
npc_tag = Generator([])
npc_species = Generator([])
npc_stats = Generator([])
npc_spellbook = Generator([])

initiative_start = None  # Placeholder for initiative start operation

loot_any = Generator([])
loot_common = Generator([])
loot_uncommon = Generator([])
loot_rare = Generator([])
loot_legendary = Generator([])

world_biome = Generator([])
world_building = Generator([])
world_location = Generator([])
