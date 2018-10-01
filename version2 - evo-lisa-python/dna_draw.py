from dna_polygon import Dna_polygon as Polygon
import settings as Settings
import tools as Tools
import numpy as np

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
        
    def __str__(self):
        print "=========="
        print 'n_polygons =',len(self.polygons)
        # for i in range(len(self.polygons)):
        #     print 'polygon ',i,"=",
        #     polygon = self.polygons[i]
        #     for j in range(len(polygon.points)):
        #         points = self.polygons[i].points
        #         print points[j].x,',', points[j].y,';',
        #     print ''
        #     brush = polygon.brush
        #     print 'r=',brush.red,'g=',brush.green,'b=',brush.blue,'a=',brush.alpha
        print "=========="
        return ''
        

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
    