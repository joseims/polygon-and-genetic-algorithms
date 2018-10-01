from dna_draw import Dna_draw as Draw
import settings as Settings
import tools as Tools
from PIL import Image
from PIL import ImageDraw
import fitness as Fitness
import copy
import time



target = Image.open("house.jpg")
target_matrix = Tools.img2color_matrix(target)


def start_evolution():
    conta = 0
    generation = 0
    sig = 0
    draw = Draw()
    error = Fitness.fitness(draw,target_matrix)[0]
    while(1):
        conta = conta + 1
        new_draw = copy.deepcopy(draw).mutate()
        if (new_draw.is_dirty()):
            generation = generation + 1
            print conta,generation,sig
            new_error,new_img = Fitness.fitness(new_draw,target_matrix)
            print new_error,"=erro novo /",error,"=erro antigo"
            if (new_error <= error):
                sig = sig  + 1
                draw = new_draw
                draw.dirty = False
                Tools.save(new_img,new_error,generation)
                error = new_error

start_evolution()