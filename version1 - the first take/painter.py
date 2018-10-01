import cv2
import numpy as np
import time
import datetime
from PIL import Image
import os
import sys
from PIL import ImageDraw
import random

def get_rand_color() :
    return np.random.randint(0,high=256,size=4)

def mutate() :
    mutate = np.random.rand(1)
    return mutate <= mutation_rate

def mutation(i):
    for n in range(50):
        if (mutate()):
            n_mutation = np.random.randint(0,high=8)
            indexes = np.random.randint(0,high=8,size=(n_mutation))
            for index in indexes:
                i[n][index] = np.random.randint(0,high=256)
        if (mutate()) :
            i[n][8:12] = get_rand_color()
        
    if (mutate()):
        random.shuffle(i)
        
    return i
        

#Maior similaridade possivel e 0
def similarity(color1,color2):
    b = (color1[0]-color2[0])
    g = (color1[1]-color2[1])
    r = (color1[2]-color2[2])
    return b*b+g*g+r*r

def fitness(img,target):
    fit = 0
    for w in range(200):
        for h in range(200):
            cor_img = img.load()[w,h]
            cor_target = target.load()[w,h]
            fit = fit + similarity(cor_img,cor_target)
    return fit

def crossover(pop):
    pop = recombination(pop)    
    for i in range(50):
        pop[i][0] = mutation(pop[i][0])
 
    return pop


def recombination(pop):
    new_pop = []
    for i in range(len(pop)):
        i1 = tournament(pop,tournament_k)
        i2 = tournament(pop,tournament_k)
        parent = [i1[0],i2[0]]
        new_i = int_crossover(parent)
        new_pop.append([new_i,0])
    return new_pop

def int_crossover(parent):
    ni = []
    for poly in range(50):
        start_point = 0
        n_poly = []
        for i in range(0,8):
            parent_i = np.random.randint(0,2)
            n_poly = n_poly + parent[parent_i][poly][i:i+1]
        parent_i = np.random.randint(0,2)
        n_poly = n_poly + parent[parent_i][poly][8:12]
        ni.append(n_poly)
    return ni

def point_crossover(parent):
    ni = []
    for poly in range(50):
        start_point = 0
        n_poly = []
        parent_i = 0
        for i in range(0,8,2):
            n_poly = n_poly + parent[parent_i][poly][i:i+2]
            parent_i = parent_i ^ 1
        n_poly = n_poly + parent[parent_i][poly][8:12]
        ni.append(n_poly)
    return ni

#k-way tournmant 
def tournament(pop,k):
    mini = ((255**2)*3)*200*200
    selected = []
    selecteds = []
    for i in range(k):
        index = np.random.randint(0,len(pop))
        while(index in selecteds):
            index = np.random.randint(0,len(pop))
        selecteds.append(index)
        if (pop[index][1] < mini):
            mini = pop[index][1]
            selected = pop[index]
    return selected



#gene
#cada gene corresponde a um poligono
#Os 8 primeiros pontos sao os vertices, e os 4 ultimos sao BGRA
def create_gene():
    return np.random.randint(0,high=256,size=(12))

def draw_polygon(gene):
    pts = []
    for i in range(0,8):
        pts.append(gene[i])
    color = (gene[8],gene[9],gene[10],gene[11])
    return [pts,color]

#Individuo
#Cada individuo e um array de n genes
def process_ind(gene):
    img = blank
    imgDraw = ImageDraw.Draw(img,'RGBA')
    n = len(gene)
    for i in range(n):
        pts,color = draw_polygon(gene[i])
        imgDraw.polygon(pts,fill=color)
    return img


def create_cromo(n):
    cromo = []
    for i in range(n):
        gene = create_gene()
        cromo.append(gene.tolist())
    return cromo

def process_pop(pop):
    max_fit = sys.maxsize
    max_img = 0
    for i in range(len(pop)):
        img = process_ind(pop[i][0])
        target = Image.open("house.jpg")
        fit = fitness(img,target)
        if (fit <= max_fit):
            max_fit = fit
            max_img = img
        pop[i][1]= fit
    save(max_img,max_fit,pop)
    return pop

    
#populacao
#a populacao e um array de arrays de ordem 2(gene,fit_points)
def create_pop(n_pop,n_polygon):
    pop = []
    for i in range(n_pop):
        pop.append([0,0])
        pop[i][0] = create_cromo(n_polygon)
    return pop


def save(img,fit,pop):
    pop = sorted(pop,key=lambda i: i[1])
    for i in range(10):
        print pop[i][1],
    print ''
    label = 'example/#gen'+ str(generation) + "-" +  str(fit) + '.png'
    img.save(label)


tournament_k = 4
blank = Image.new('RGB',(200,200),(0,0,0))
mutation_rate = 0.02
pop_size = 50
n_polygon = 50
generation = 0
pop = create_pop(pop_size,n_polygon)
while(1):
    print "geracao",generation,'-',
    pop = process_pop(pop)
    pop = crossover(pop)
    generation = generation + 1
