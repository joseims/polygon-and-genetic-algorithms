import numpy as np
import settings as Settings
import tools as Tools

class Dna_point:

    def __init__(self):
        self.x = np.random.randint(0,Settings.max_width)
        self.y = np.random.randint(0,Settings.max_height)

    def mutate(self,dna_draw):
        
        if (Tools.will_mutate(Settings.move_point_max_mutation_rate)):
            self.x = np.random.randint(0,Settings.max_width)
            self.y = np.random.randint(0,Settings.max_height)
            print "point mutation max"
            dna_draw.set_dirty()
    
        if (Tools.will_mutate(Settings.move_point_mid_mutation_rate)):
            self.x = min(
                         max(0, self.x + np.random.randint(-Settings.move_point_range_mid,Settings.move_point_range_mid)),
                         Settings.max_width)
            self.y = min(
                         max(0, self.y + np.random.randint(-Settings.move_point_range_mid,Settings.move_point_range_mid)),
                         Settings.max_height)  
            print "point mutation mid"          
            dna_draw.set_dirty()

        if (Tools.will_mutate(Settings.move_point_min_mutation_rate)):
            self.x = min(
                         max(0, self.x + np.random.randint(-Settings.move_point_range_min,Settings.move_point_range_min)),
                         Settings.max_width)
            self.y = min(
                         max(0, self.y + np.random.randint(-Settings.move_point_range_min,Settings.move_point_range_min)),
                         Settings.max_height) 
            print "point mutation min"           
            dna_draw.set_dirty()

        return self

