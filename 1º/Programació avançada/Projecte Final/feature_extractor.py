# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:14:03 2020

@author:
"""
from abc import ABC, abstractmethod
from skimage.feature import hog
import numpy as np

class FeatureExtractor(ABC):
    
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def extract(self,Object):
        pass
    
    @abstractmethod
    def compute_distance(self,Object1,Object2):
        pass


class TextFeatureExtractor(FeatureExtractor):

    def __init__(self,vocabulary):
        self._vocabulary = vocabulary
        
    def extract(self,Object):
        pass
    
    
    def compute_distance(self,Object1,Object2):

        numerador = 0
        denominador = 0
        denominador1 = 0
        denominador2 = 0

        train1 = self.extract(Object1)
        train2 = self.extract(Object2)
        
        for word in train2.keys():
            if word in train1.keys():
                numerador += min(train1[word],train2[word])
            denominador1 += train2[word]
        
        for word in train1.keys():
            denominador2 += train1[word]

        denominador = min(denominador1,denominador2)
        distance = 1 - (numerador/denominador)
        
           
        return distance
    
class BOW(TextFeatureExtractor):
    
    def extract(self,Object):
        dictionary = dict()  
        for word in Object:
            if word in self._vocabulary:
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
        return dictionary

class Text_HOG(TextFeatureExtractor):
    
    def extract(self,Object):
        repeticiones = []
        dictionary = dict()  
        for word in Object:
            if word in self._vocabulary:
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
        
        for paraula in self._vocabulary:
            if paraula in dictionary:
                repeticiones.append(dictionary[paraula])
            else:
                repeticiones.append(0)
        
        llista_repeticions= np.array(repeticiones)
        
        
        return llista_repeticions
        

class ImageFeatureExtractor(FeatureExtractor):

    def __init__(self):
        pass

    def extract(self,Object1):
        pass

    def compute_distance(self,Object1,Object2):
        sum = 0
        for x, y in zip(Object2, Object1):
            sum += (y - x)**2
        distance = sum**(1/2)

        return distance


class ByN(ImageFeatureExtractor):
    
    def extract(self,Object1):
        pixels = []
        
        for line in Object1:
            suma = 0
            for x in line:
                if x == 0:
                    suma += 1
                    
            pixels.append(suma)
        
        long = len(Object1[0])
        for x in range(long):
            suma = 0
            for line in Object1:
                if line[x] == 0:
                    suma += 1
            pixels.append(suma)
            
        return pixels
    
    
class descriptor_HOG(ImageFeatureExtractor):
    
    def extract (self,Object1):
        features = hog(Object1, pixels_per_cell=(5, 5), cells_per_block=(2, 2))  
        return features    
    


    
    