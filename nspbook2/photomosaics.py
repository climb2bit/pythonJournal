import os, random, argparse
from PIL import Image
import numpy as np 
from scipy.spatial import KDTree
import timeit

def getAverageRGBOld(image):
    npixels = image.size[0]*image.size[1]
    cols = image.getcolors(npixels)
    sumRGB = [(x[0]*x[1][0], x[0]*x[1][1], x[0]*x[1][2])for x in cols]
    avg =  tuple([int(sum(x)/npixels)for x in zip(*sumRGB)])
    return avg

def getAverageRGB(image):
    im = np.array(image)
    w, h, d = im.shape
    return tuple(np.average(im.reshape(w*h, d), axis=0))

def splitImage(image, size):
    W, H = image.size[0], image.size[1]
    m,n  = size
    w, h =  int(W/n), int(H/m)
    imgs = []
    for j in range(m):
        for i in range(n):
            imgs.append(image.crop((i*w, j*h,(i+1)*w, (j+1)*h)))
    return imgs

def getImages(imageDir):
    files = os.listdir(imageDir)
    images = []
    for file in files:
        filepath = os.path.abspath(os.path.join(imageDir, file))
        try:
            fp = open(filepath, "rb")
            im = Image.open(fp)
            images.append(im)
            im.load()
            fp.close()
        except:
            print('Invalid image: %s' % (filepath,))
    return images

def getBestMatchIndex(input_avg, avgs):
    avg = input_avg
    index = 0
    min_index = 0
    min_dist = float("inf")
    for val in avgs:
        dist = ((val[0] - avg[0])*(val[0] - avg[0])+
                (val[1] - avg[1])*(val[1] - avg[1])+
                (val[2] - avg[2])*(val[2] - avg[2]))
        if dist < min_dist:
            min_dist = dist
            min_index = index
        index += 1
    return min_index

def getBestMatchIndicesKDT(qavgs, kdtree):
    res = list(kdtree.query(qavgs, k=1))
    min_indices = res[1]
    return min_indices

def createImageGrid(images, dims):
    m, n = dims
    assert m*n == len(images)

    width = max([img.size[0]for img in images])
    height = max([img.size[1]for img in images])    
    grid_img = Image.new('RGB', (n*width, m*height))
    for index in range(len(images)):
        row =  int(index/n)
        col = index - n*row
        grid_img.paste(images[index], (col*width, row*height))
    return grid_img

def createPhotomosaic(target_Image, input_images, grid_size, reuse_images, use_kdt):
    pass

def main():
    pass