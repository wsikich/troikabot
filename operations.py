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
        return f"Background: {background} | Stats: {stats}"


class NPCComplete(Operation):
    def __init__(self):
        super().__init__()

    def initiate(self):
        mood = npc_mood.initiate()
        tag = npc_tag.initiate()
        species = npc_any_species.initiate()
        stats = npc_stats.initiate()
        has_spells = random.randint(1, 3)
        if has_spells == 1:
            spellbook = npc_spellbook.initiate()
        else: 
            spellbook = None
        return f"Mood: {mood} | Tag: {tag} | Species: {species} | Stats: {stats} | Spellbook: {spellbook}"


class Stats(Operation):
    def __init__(self):
        super().__init__()

    def initiate(self):
        skill = random.randint(1, 3) + 3
        stamina = random.randint(1, 6) + random.randint(1, 6) + 12
        luck = random.randint(1, 6) + 6
        return f"skill: {skill} stamina: {stamina} luck: {luck}"
    

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
    

class SpellbookGenerator(Operation):
    def __init__(self, outcomes):
        super().__init__()
        self.outcomes = outcomes
    
    def initiate(self):
        spell_list = []
        spell_count = random.randint(1, 6)
        while spell_count > 0:
            result_index = random.randint(0, (len(self.outcomes) - 1))
            result = self.outcomes[result_index]
            if result not in spell_list:
                spell_list.append(result)
                spell_count -= 1
        return spell_list


class CompleteWorldGenerator(Operation):
    def __init__(self):
        super().__init__()

    def initiate(self):
        biome_count = random.randint(1, 3)
        biome_list = []
        while biome_count > 0:
             new_biome = world_biome.initiate()
             if new_biome not in biome_list:
                 biome_list.append(new_biome)
                 biome_count -= 1
        government = world_government.initiate()
        species_count = random.randint(1, 3)
        species_list = []
        while species_count > 0:
            new_species = npc_any_species.initiate()
            if new_species not in species_list:
                species_list.append(new_species)
                species_count -= 1
        aesthetic_count = random.randint(1, 2)
        aesthetic_list = []
        while aesthetic_count > 0:
            new_aesthetic = world_aesthetic.initiate()
            if new_aesthetic not in aesthetic_list:
                aesthetic_list.append(new_aesthetic)
                aesthetic_count -= 1

        return f"Biomes: {biome_list} | Government: {government} | Dominant Species: {species_list} | Aesthetic: {aesthetic_list}"

#class InitiativeTracker(Operation):
    #def __init__(self):
    
    #def initiate(self):
        #print()


# Lists of outcomes:
pc_background_outcomes = []

npc_color_outcomes = []
npc_animal_species_outcomes = []
npc_fantasy_species_outcomes = []
npc_mood_outcomes = []
npc_tag_outcomes = []
npc_spellbook_outcomes = []

world_biome_outcomes = []
world_government_outcomes = []
world_aesthetic_outcomes = []
world_building_outcomes = []
world_location_outcomes = []


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
fill_outcome_list(npc_mood_outcomes, 'moods.txt')
fill_outcome_list(npc_tag_outcomes, 'tags.txt')
fill_outcome_list(npc_spellbook_outcomes, 'spells.txt')

fill_outcome_list(world_biome_outcomes, 'biomes.txt')
fill_outcome_list(world_government_outcomes, 'governments.txt')
fill_outcome_list(world_aesthetic_outcomes, 'aesthetics.txt')
fill_outcome_list(world_building_outcomes, 'buildings.txt')
fill_outcome_list(world_location_outcomes, 'locations.txt')

# List of generators and operations:
pc_complete = PCComplete()
pc_background = Generator(pc_background_outcomes)
pc_stats = Stats()
pc_spell = Generator(npc_spellbook_outcomes)

npc_complete = NPCComplete()
npc_mood = Generator(npc_mood_outcomes)
npc_tag = Generator(npc_tag_outcomes)
npc_any_species = AnySpeciesGenerator()
npc_animal_species = Generator(npc_animal_species_outcomes)
npc_fantasy_species = Generator(npc_fantasy_species_outcomes)
npc_stats = Stats()
npc_spellbook = SpellbookGenerator(npc_spellbook_outcomes)
npc_color = Generator(npc_color_outcomes)

initiative_start = None  # Placeholder for initiative start operation

loot_any = Generator([])
loot_common = Generator([])
loot_uncommon = Generator([])
loot_rare = Generator([])
loot_legendary = Generator([])

world_complete = CompleteWorldGenerator()
world_biome = Generator(world_biome_outcomes)
world_government = Generator(world_government_outcomes)
world_building = Generator(world_building_outcomes)
world_location = Generator(world_location_outcomes)
world_aesthetic = Generator(world_aesthetic_outcomes)
