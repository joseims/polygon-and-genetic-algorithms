import numpy as np
import settings as Settings
from PIL import Image
from PIL import ImageDraw

def will_mutate(mutation_rate):
    if (np.random.randint(0,mutation_rate) == 1):
        return True
    return False

def get_random_color():
    return np.random.randint(0,256)

def get_random_alpha():
    return np.random.randint(Settings.alpha_range_min,Settings.alpha_range_max)

def img2color_matrix(img):
    matrix = []
    for x in range(Settings.max_height):
        matrix.append([])
        for y in range(Settings.max_width):
            matrix[x].append([])
            matrix[x][y]= img.load()[x,y]
    return matrix


def save(img,error,gen):
    label = 'example/#gen' + str(gen) + '-' + str(error) + '.png'
    img.save(label)



