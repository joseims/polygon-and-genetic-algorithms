from dna_polygon import Dna_polygon as Polygon
import settings as Settings
import tools as Tools
import numpy as np
import fitness

class Dna_draw :

    def __init__(self) :
        self.fit = Settings.min_fit
        self.polygons = []

        for i in range(Settings.polygons_min):
            self.polygons.append(Polygon())

        self.dirty = False

    def set_dirty(self):
        self.dirty = True

    def is_dirty(self):
        return self.dirty

    def set_fit(self,target):
        fit,img = fitness.fitness(self,target)
        self.fit = fit



    def mutate(self):
        if (Tools.will_mutate(Settings.add_polygon_mutation_rate)):
            self.add_polygon()
            self.set_dirty()
        
        if (Tools.will_mutate(Settings.remove_polygon_mutation_rate)):
            self.remove_polygon()
            self.set_dirty()

        if (Tools.will_mutate(Settings.move_polygon_mutation_rate)):
            self.move_polygon()
            self.set_dirty()

        for index in range(len(self.polygons)):
            self.polygons[index] = self.polygons[index].mutate(self)

        return self
    
    def get_polygon_count(self):
        return len(self.polygons)

    def crossover(draw_a, draw_b):
        polygons_count = min(draw_a.get_polygon_count(),draw_b.get_polygon_count())
        new_draw = Dna_draw()
        new_draw.polygons = [[]] * polygons_count
        for i in range(polygons_count):
            polygon_a = draw_a.polygons[i]
            polygon_b = draw_b.polygons[i]
            child = Polygon.crossover(polygon_a,polygon_b)
            new_draw.polygons[i] = child

        max_polygon_count = max(draw_a.get_polygon_count(),draw_b.get_polygon_count())
        if (max_polygon_count != polygons_count):
            extra_poly = []
            if (draw_a.get_polygon_count == max_polygon_count):
                extra_poly = draw_a.polygons[-1]
            else :
                extra_poly = draw_b.polygons[-1]
            new_draw.polygons.append(extra_poly)
        return new_draw


    def add_polygon(self):
        print 'adding polygon'
        if (len(self.polygons) == Settings.polygons_max):
            return
        new_poly = Polygon()
        index = np.random.randint(0,len(self.polygons))
        self.polygons.insert(index,new_poly)
        
    
    def move_polygon(self):
        print 'moving polygon'
        if (len(self.polygons) <= 1):
            return
        index = np.random.randint(0,len(self.polygons))
        poly = self.polygons[index]
        index = np.random.randint(0,len(self.polygons))
        self.polygons.insert(index,poly)
    
    def remove_polygon(self):
        print 'removing polygon'
        if (len(self.polygons) == Settings.polygons_min):
            return
        index = np.random.randint(0,len(self.polygons))
        poly = self.polygons.pop(index)
    