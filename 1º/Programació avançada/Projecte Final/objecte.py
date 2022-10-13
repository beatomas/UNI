# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 01:12:35 2020

@author:
"""
import matplotlib.image as image
from abc import ABC, abstractmethod
from feature_extractor import FeatureExtractor
import re

class Object(ABC):

    def __init__(self,content,features,label):
        self._content = content
        self._features = features
        self._label = label 
   
    def extract_features(self):  
        self._features = FeatureExtractor.extract(self._content)
   
    def get_features(self):
        return self._features
   
    def get_label(self):
        return self._label
   
    @abstractmethod
    def load(self,file):
        pass
   

class Text(Object):
    def __init__(self,content,features,label):
        super().__init__(content,features,label)

    def load(self,file,train_path):
        self._content = []
        with open(train_path+'/'+file,"r",errors="ignore") as file:
            for line in file:
                words = (re.sub("[^a-zA-Z0-9]", " ",line.lower()).split())
                for word in words:
                    self._content.append(word)
        return self._content
   
   
class Image(Object):
    def __init__(self,content,features,label):
        super().__init__(content,features,label)
       
    def load(self,file,train_path):
        img = image.imread(train_path+'/'+file)
        self._content = img.copy()
        media = self._content.mean()
        self._content[self._content >= media] = 255
        self._content[self._content <= media] = 0
           
        return self._content
