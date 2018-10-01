from dna_brush import Dna_brush as Brush
from dna_point import Dna_point as Point
import tools as Tools
import settings as Settings
import numpy as np

class Dna_polygon:

    def __init__(self):
        self.points =[]
        origin = Point()
        for i in range(Settings.points_min):
            point = self.set_new_point(origin)
            self.points.append(point)

        self.brush = Brush()

    def mutate(self,dna_draw):

        if (Tools.will_mutate(Settings.add_point_mutation_rate)):
            self.add_point()
            dna_draw.set_dirty()

        if (Tools.will_mutate(Settings.remove_point_mutation_rate)):
            self.remove_point()
            dna_draw.set_dirty()

        self.brush = self.brush.mutate(dna_draw)

        for index in range(len(self.points)):
            p = self.points[index]
            self.points[index] = p.mutate(dna_draw)

        return self
    

    def set_new_point(self,origin_point):
            point = Point()
            point.x = min(
                         max(0, origin_point.x + np.random.randint(-Settings.move_point_range_min,Settings.move_point_range_min)),
                         Settings.max_width)
            point.y = min(
                         max(0, origin_point.y + np.random.randint(-Settings.move_point_range_min,Settings.move_point_range_min)),
                         Settings.max_height) 
            return point
    
    def remove_point(self):
        print 'removing point'
        if (len(self.points) <= Settings.points_per_polygon_min):
            return 
        
        index = np.random.randint(0,len(self.points))
        self.points.pop(index)

    def add_point(self):
        print 'adding point'
        if (len(self.points) >= Settings.points_per_polygon_max):
            return 
        
        newPoint = Point()
        index = np.random.randint(1,len(self.points) - 1)

        prev_ = self.points[index - 1]
        next_ = self.points[index]

        newPoint.x = (prev_.x + next_.x)/2
        newPoint.y = (prev_.y + next_.y)/2
        
        self.points.insert(index,newPoint)

    def crossover(polygon_a,polygon_b):
        polygons = [polygon_a,polygon_b]
        new_polygon = Dna_polygon()
        index = np.random.randint(0,2)
        new_polygon.brush = polygons[index].brush
        index = np.random.randint(0,2)
        new_polygon.points = polygons[index].points
        return new_polygon