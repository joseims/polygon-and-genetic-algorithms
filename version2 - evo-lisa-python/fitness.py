import settings as Settings
from PIL import Image
from PIL import ImageDraw
import copy

def error(color1,color2):
    r = (color1[0]-color2[0])
    g = (color1[1]-color2[1])
    b = (color1[2]-color2[2])
    return b*b+g*g+r*r

def fitness(dna_draw,target_matrix):
    fit = 0
    img = process_dna_draw(dna_draw)
    for w in range(Settings.max_width):
        for h in range(Settings.max_height):
            cor_img = img.load()[w,h]
            cor_target = target_matrix[w][h]
            fit = fit + error(cor_img,cor_target)
    return [fit,img]


def process_dna_draw(dna_draw):
    img = copy.deepcopy(blank)
    assert img == blank
    imgDraw = ImageDraw.Draw(img,'RGBA')
    n = len(dna_draw.polygons)
    for i in range(n):
        polygon = dna_draw.polygons[i]
        pts,color = draw_polygon(dna_draw.polygons[i])
        imgDraw.polygon(pts,fill=color)
    return img

blank = Image.new('RGB',(200,200),(0,0,0))

def draw_polygon(dna_polygon):
    pts = []
    for i in range(len(dna_polygon.points)):
        dna_point = dna_polygon.points[i]
        pts.append(dna_point.x)
        pts.append(dna_point.y)
    dna_brush = dna_polygon.brush
    color = (dna_brush.red,dna_brush.green,dna_brush.blue,dna_brush.alpha)
    return [pts,color]


    
