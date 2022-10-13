# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:56:00 2020

@author:
"""


from train import Train_KNN, TrainSVM
from classification import Classification_SVM, Classification_KNN


#K
class Classifier:
    def __init__(self,tipus,feature_extractor,labels):
        self._tipus = tipus  
        self._feature_extractor = feature_extractor
        self._labels = labels
        
        
            
        
    def train(self,train_path):
        
        if (self._tipus == 2) or (self._tipus == 3) or (self._tipus==4) or (self._tipus==5):
            self._train = TrainSVM(self._tipus,self._feature_extractor)
        
        if (self._tipus == 1) or (self._tipus == 0)  or (self._tipus==6):
            self._train = Train_KNN(self._tipus,self._feature_extractor)
            
            
        self._train.load(train_path)   #usamos el load Train aunque llamemos a una subclasse suya dando por hecho que lo hereda
        self._training_model =  self._train.create_model(train_path)
        
        return self._training_model
    

      

    def classify(self,test_path,k,training_model):
        
        self._training_model=training_model
        
        if (self._tipus == 2) or (self._tipus == 3) or (self._tipus==4)or (self._tipus==5) :
            self._classification = Classification_SVM(self._feature_extractor,self._training_model,k,self._labels,self._tipus)
        
        if (self._tipus == 1) or (self._tipus == 0) or (self._tipus==6):
            self._classification = Classification_KNN(self._feature_extractor,self._training_model,k,self._labels,self._tipus)
        
            
        self._classification.load(test_path)
        
        accuracy,testeo,llista_labels= self._classification.accuracy(test_path)
       
        
        return accuracy,testeo,llista_labels
    
    
    
    