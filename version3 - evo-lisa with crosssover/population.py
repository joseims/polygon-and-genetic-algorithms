import numpy as np
import settings
import tools
from dna_draw import Dna_draw as Draw
class Population :
    
    def __init__(self,size,target):
        self.size = size
        self.population = []
        self.target = target
        self.gen = 0
        for i in range(size):
            self.population.append([])

    def start(self):
        best_fit = settings.min_fit
        best_index = -1
        for i in range(self.size):
            draw =  Draw()
            draw.set_fit(self.target)
            self.population[i] = draw
            if (draw.fit <= best_fit):
                best_index = i
                best_fit = draw.fit
        tools.save(self.population[best_index],best_fit,0)
        
    
    def get_draw(self,index):
        return self.population[index]
    
    def get_fit(self,index):
        return self.get_draw(index).fit

    def get_draw_fit(self,index):
        return [self.get_draw(index),self.get_fit(index)]


    def __select_parent(self,pop):
        return pop.__tournament_selection(pop,6)


    def __tournament_selection(self,pop,k):
        mini = settings.min_fit
        selected = -1
        chosen = []
        for i in range(k):
            index = np.random.randint(0,self.size)
            while(index in chosen):
                index = np.random.randint(0,len(pop.population))
            chosen.append(index)
            fit = pop.get_fit(index)   
            if (fit < mini):
                mini = fit
                selected = index
        return pop.population[selected]

    
    def crossover(pop):
        best_fit = settings.min_fit
        best_index = -1
        new_pop = Population(pop.size,pop.target)
        new_pop.gen = pop.gen + 1
        for i in range(pop.size):
            parent_a = pop.__select_parent(pop)
            parent_b = pop.__select_parent(pop)
            child = Draw.crossover(parent_a,parent_b)
            child.mutate()
            child.set_fit(pop.target)
            if (child.fit <= best_fit):
                best_index = i
                best_fit = child.fit
            new_pop.population[i] = child
        tools.save(new_pop.population[best_index],best_fit,new_pop.gen)
        print best_fit 
        return new_pop



        
        