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
        species = npc_any_species.initiate()
        stats = npc_stats.initiate()
        spellbook = npc_spellbook.initiate()
        print({"mood": mood, "tag": tag, "species": species, "stats": stats, "spellbook": spellbook})


class Stats(Operation):
    def __init__(self):
        super().__init__()

    def initiate(self):
        skill = random.randint(1, 3) + 3
        stamina = random.randint(1, 6) + random.randint(1, 6) + 12
        luck = random.randint(1, 6) + 6
        return {"skill": skill, "stamina": stamina, "luck": luck}
    
class AnySpeciesGenerator(Operation):
    def __init__(self):
        super().__init__()
    
    def initiate(self):
        coin_flip = random.randint(1, 2)
        species = None
        if coin_flip == 1:
            species = npc_animal_species.initiate()
        else:
            species = npc_fantasy_species.initiate()
        return species

#class InitiativeTracker(Operation):
    #def __init__(self):
    
    #def initiate(self):
        #print()


# Lists of outcomes:
pc_background_outcomes = []
npc_color_outcomes = []
npc_animal_species_outcomes = []
npc_fantasy_species_outcomes = []


# Fill outcome lists from files
def fill_outcome_list(outcome_list, file_path):
    with open(file_path, 'r') as file:
        for line in file:
            outcome = line.strip()
            if outcome:
                outcome_list.append(outcome)

fill_outcome_list(pc_background_outcomes, 'backgrounds.txt')
fill_outcome_list(npc_color_outcomes, 'colors.txt')
fill_outcome_list(npc_animal_species_outcomes, 'animal_species.txt')
fill_outcome_list(npc_fantasy_species_outcomes, 'fantasy_species.txt')


# List of generators and operations:
pc_complete = PCComplete()
pc_background = Generator(pc_background_outcomes)
pc_stats = Stats()

npc_complete = NPCComplete()
npc_mood = Generator([])
npc_tag = Generator([])
npc_any_species = AnySpeciesGenerator()
npc_animal_species = Generator(npc_animal_species_outcomes)
npc_fantasy_species = Generator(npc_fantasy_species_outcomes)
npc_stats = Stats()
npc_spellbook = Generator([])
npc_color = Generator(npc_color_outcomes)

initiative_start = None  # Placeholder for initiative start operation

loot_any = Generator([])
loot_common = Generator([])
loot_uncommon = Generator([])
loot_rare = Generator([])
loot_legendary = Generator([])

world_biome = Generator([])
world_building = Generator([])
world_location = Generator([])
