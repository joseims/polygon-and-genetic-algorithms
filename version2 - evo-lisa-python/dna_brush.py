import tools as Tools
import settings as Settings
import numpy as np

class Dna_brush:
    
    def __init__(self):
        self.red = Tools.get_random_color()
        self.green = Tools.get_random_color()
        self.blue = Tools.get_random_color()
        self.alpha = Tools.get_random_alpha()

    def mutate(self,dna_draw):


        if (Tools.will_mutate(Settings.red_mutation_rate)):
            self.red = Tools.get_random_color()
            dna_draw.set_dirty()
            print "color mutation"

        if (Tools.will_mutate(Settings.green_mutation_rate)):
            self.green = Tools.get_random_color()
            dna_draw.set_dirty()
            print "color mutation"

        if (Tools.will_mutate(Settings.blue_mutation_rate)):
            self.blue = Tools.get_random_color()
            dna_draw.set_dirty()
            print "color mutation"

        if (Tools.will_mutate(Settings.alpha_mutation_rate)):
            self.alpha = Tools.get_random_alpha()
            dna_draw.set_dirty()
            print "color mutation"
        
        return self