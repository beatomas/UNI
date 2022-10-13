# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:55:14 2020

@author:
"""

from objecte import Text,Image
import os
import numpy as np
from sklearn import svm
from abc import ABC, abstractmethod

class Train(ABC):
    def __init__(self,tipus,feature_extractor):
        self._tipus = tipus                     #int
        self._feature_extractor = feature_extractor  
        self._training_set = []      #list
        self._training_model = []  #list7

    def load(self,train_path):
        list_files_train = os.listdir(train_path)
        for file in list_files_train:
            self._training_set.append(file)
        return self._training_set

    @abstractmethod
    def create_model(self,train_path):  
        pass
        
        
class TrainSVM(Train):
    def create_model(self, train_path):
        llista_arrays = []
        llista_etiquetes=[]
        content = []
        features = []
        
        if self._tipus == 2:
    
            for file in self._training_set:
                if "airplane" in file:
                    llista_etiquetes.append("airplane")
                    label = "airplane"
                if "automobile" in file:
                    llista_etiquetes.append("automobile")
                    label = "automobile"
                if "bird" in file:
                    llista_etiquetes.append("bird")
                    label = "bird"
                if "cat" in file:
                    llista_etiquetes.append("cat")
                    label = "cat"
                if "deer" in file:
                    llista_etiquetes.append("deer")
                    label = "deer"
                if "dog" in file:
                    llista_etiquetes.append("dog")
                    label = "dog"
                if "frog" in file:
                    llista_etiquetes.append("frog")
                    label = "frog"
                if "horse" in file:
                    llista_etiquetes.append("horse")
                    label = "horse"
                if "ship" in file:
                    llista_etiquetes.append("ship")
                    label = "ship"
                if "truck" in file:
                    llista_etiquetes.append("truck")
                    label = "truck"
                    
                
                a = Image(content,features,label)
                file_content = a.load(file,train_path)
                file_features = self._feature_extractor.extract(file_content)
                llista_arrays.append(file_features)
            
                    
                    
            matriu_x = np.array(llista_arrays)
            matriu_y = np.array(llista_etiquetes)
                                
            self._training_model = svm.SVC()
            self._training_model.fit(matriu_x, matriu_y)

        if self._tipus ==3:
            
            for file in self._training_set:
                if "ms-windows" in file:
                    llista_etiquetes.append("ms-windows")
                    label = "ms-windows"
                
                if "crypt" in file:
                    llista_etiquetes.append("crypt")
                    label = "crypt"
                
                if "religion-christian" in file:
                    llista_etiquetes.append("religion-christian")
                    label = "religion-christian"
                
                if "graphics" in file:
                    llista_etiquetes.append("graphics")
                    label = "graphics"
                    
                if "hardware-mac" in file:
                    llista_etiquetes.append("hardware-mac")
                    label = "hardware-mac"
                    
                if "atheism" in file:
                    llista_etiquetes.append("atheism")
                    label = "atheism"
                    
                if "hockey" in file:
                    llista_etiquetes.append("hockey")
                    label = "hockey"
                
                if "electronics" in file:
                    llista_etiquetes.append("electronics")
                    label = "electronics"
                    
                if "politics-guns" in file:
                    llista_etiquetes.append("politics-guns")
                    label = "politics-guns"
                    
                if "med" in file:
                    llista_etiquetes.append("med")
                    label = "med"
                   
                if "hardware-pc" in file:
                    llista_etiquetes.append("hardware-pc")
                    label = "hardware-pc"
                    
                if "space" in file:
                    llista_etiquetes.append("space")
                    label = "space"
                
                if "windows_x" in file:
                    llista_etiquetes.append("windows_x")
                    label = "windows_x"
                
                if "forsale" in file:
                    llista_etiquetes.append("forsale")
                    label = "forsale"
                    
                if "politics-mideast" in file:
                    llista_etiquetes.append("politics-mideast")
                    label = "politics-mideast"
                    
                if "religion-misc" in file:
                    llista_etiquetes.append("religion-misc")
                    label = "religion-misc"
                
                if "autos" in file:
                    llista_etiquetes.append("autos")
                    label = "autos"
                    
                if "baseball" in file:
                    llista_etiquetes.append("baseball")
                    label = "baseball"
                    
                if "motorcycles" in file:
                    llista_etiquetes.append("motorcycles")
                    label = "motorcycles"
                    
                if "politics-misc" in file:
                    llista_etiquetes.append("politics-misc")
                    label = "politics-misc"
                
            
                a = Text(content,features,label)
                file_content = a.load(file,train_path)
                file_features = self._feature_extractor.extract(file_content)
                llista_arrays.append(file_features)
            
            matriu_x = np.array(llista_arrays)
            matriu_y = np.array(llista_etiquetes)
                                
            
            
            self._training_model = svm.SVC()
            self._training_model.fit(matriu_x, matriu_y)
            
            
        if self._tipus ==4:
             for file in self._training_set:
                 if 'class_0' in file:
                     llista_etiquetes.append("0")
                     label = "0"
                    
                 elif 'class_1' in file:
                     llista_etiquetes.append("1")
                     label = "1"
                
                 elif 'class_2' in file:
                     llista_etiquetes.append("2")
                     label = "2"
                    
                 elif 'class_3' in file:
                     llista_etiquetes.append("3")
                     label = "3"
                    
                 elif 'class_4' in file:
                     llista_etiquetes.append("4")
                     label = "4"
                    
                 elif 'class_5' in file:
                     llista_etiquetes.append("5")
                     label = "5"
                 
                 elif 'class_6' in file:
                     llista_etiquetes.append("6")
                     label = "6"
                    
                 elif 'class_7' in file:
                     llista_etiquetes.append("7")
                     label = "7"
                     
                 elif 'class_8' in file:
                     llista_etiquetes.append("8")
                     label = "8"
                    
                 elif 'class_9' in file:
                     llista_etiquetes.append("9")
                     label = "9"
        
        
                 a = Image(content,features,label)
                 file_content = a.load(file,train_path)
                 file_features = self._feature_extractor.extract(file_content)
                 llista_arrays.append(file_features)
            
                    
                    
             matriu_x = np.array(llista_arrays)
             matriu_y = np.array(llista_etiquetes)
                                
             self._training_model = svm.SVC()
             self._training_model.fit(matriu_x, matriu_y)
        
        if self._tipus ==5:
            for file in self._training_set:
                if 'spmsg' in file:
                    llista_etiquetes.append("spam")
                    label = "spam"
                
                else:
                    llista_etiquetes.append("no_spam")
                    label = "no_spam"
                    
                a = Text(content,features,label)
                file_content = a.load(file,train_path)
                file_features = self._feature_extractor.extract(file_content)
                llista_arrays.append(file_features)
            
            matriu_x = np.array(llista_arrays)
            matriu_y = np.array(llista_etiquetes)
                                
            
            
            self._training_model = svm.SVC()
            self._training_model.fit(matriu_x, matriu_y)
            
        return self._training_model

        
class Train_KNN(Train):
    def create_model(self, train_path):
        
        
        if self._tipus == 1:
            for file in self._training_set:
                content = []
                features = []
                
                if 'class_0' in file:
                    label = 0
                    a = Image(content,features,label)
                    
                elif 'class_1' in file:
                    label = 1
                    a = Image(content,features,label)
                
                elif 'class_2' in file:
                    label = 2
                    a = Image(content,features,label)
                    
                elif 'class_3' in file:
                    label = 3
                    a = Image(content,features,label)
                    
                elif 'class_4' in file:
                    label = 4
                    a = Image(content,features,label)
                    
                elif 'class_5' in file:
                    label = 5
                    a = Image(content,features,label)
                 
                elif 'class_6' in file:
                    label = 6
                    a = Image(content,features,label)
                    
                elif 'class_7' in file:
                    label = 7
                    a = Image(content,features,label)
                    
                elif 'class_8' in file:
                    label = 8
                    a = Image(content,features,label)
                    
                elif 'class_9' in file:
                    label = 9
                    a = Image(content,features,label)
                    
                
                file_content = a.load(file,train_path)
                file_features = self._feature_extractor.extract(file_content)
                self._training_model.append((file_features,label))
                
            
        
        elif self._tipus == 0:
            for file in self._training_set:
                content = []
                features = dict()
                if 'spmsg' in file:
                    label = 'spam'
                    x = True                  
                    a = Text(content,features,label)
                    file_content = a.load(file,train_path)
                    file_features = self._feature_extractor.extract(file_content)
                else:
                    label = 'no_spam'
                    x = False
                    a = Text(content,features,label)
                    file_content = a.load(file,train_path)
                    file_features = self._feature_extractor.extract(file_content)
                self._training_model.append((file_features,x))
        
        elif self._tipus == 6:
            for file in self._training_set:
                content = []
                features = dict()
                if "ms-windows" in file:
                    label = "ms-windows"
                if "crypt" in file:
                    label = "crypt"                
                if "religion-christian" in file:           
                    label = "religion-christian"                
                if "graphics" in file:      
                    label = "graphics"                    
                if "hardware-mac" in file:                 
                    label = "hardware-mac"                    
                if "atheism" in file:                 
                    label = "atheism"                    
                if "hockey" in file:                   
                    label = "hockey"                
                if "electronics" in file:                  
                    label = "electronics"                    
                if "politics-guns" in file:                    
                    label = "politics-guns"                    
                if "med" in file:                   
                    label = "med"                   
                if "hardware-pc" in file:                    
                    label = "hardware-pc"                    
                if "space" in file:                    
                    label = "space"                
                if "windows_x" in file:                    
                    label = "windows_x"                
                if "forsale" in file:                    
                    label = "forsale"                    
                if "politics-mideast" in file:                   
                    label = "politics-mideast"                    
                if "religion-misc" in file:                    
                    label = "religion-misc"                
                if "autos" in file:                    
                    label = "autos"                    
                if "baseball" in file:                    
                    label = "baseball"                    
                if "motorcycles" in file:                    
                    label = "motorcycles" 
                if "politics-misc" in file:            
                    label = "politics-misc"
                    
                a = Text(content,features,label)
                file_content = a.load(file,train_path)
                file_features = self._feature_extractor.extract(file_content)
                self._training_model.append((file_features,label))
                
                
        return self._training_model
    