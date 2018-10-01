from dna_draw import Dna_draw as Draw
import settings as Settings
import tools as Tools
from PIL import Image
from PIL import ImageDraw
from population import Population
import fitness as Fitness
import copy
import time



target = Image.open("house.jpg")
target_matrix = Tools.img2color_matrix(target)
pop = Population(50,target_matrix)
pop.start()
while(1):
    print "geracao ",pop.gen
    pop = Population.crossover(pop)