# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:55:47 2020

@author:
"""
from train import TrainSVM, Train_KNN
from objecte import Text,Image
from abc import ABC, abstractmethod


class Classification(ABC):
    def __init__(self,feature_extractor,training_model,k,labels,tipus):
        self._feature_extractor = feature_extractor
        self._training_model = training_model
        self._test_set = []  #list
        self._k = k   #int
        self._labels = labels #list
        self._tipus= tipus
      

    def load(self,test_path):
        if (self._tipus==0) or (self._tipus==1) or self._tipus ==6:
            self._train = Train_KNN(self._tipus,self._feature_extractor)
            
        if (self._tipus==2) or (self._tipus==3) or (self._tipus==4) or (self._tipus ==5):
            self._train = TrainSVM(self._tipus,self._feature_extractor)
            
        testeo = self._train.load(test_path)
        content = []
        features = []
        label = ''
        if self._tipus == 1 or self._tipus == 2 or self._tipus==4 : 
            for file in testeo: 
                a = Image(content,features,label)
                file_content = a.load(file,test_path)
                self._test_set.append(file_content)
                
        elif self._tipus == 0 or self._tipus==3 or self._tipus==5 or self._tipus ==6:
            for file in testeo:
                a = Text(content,features,label)
                file_content = a.load(file,test_path)
                self._test_set.append(file_content)
            
    @abstractmethod
    def classify(self,Object1):
        pass
        
    
    def evaluate(self):            
        nova_llista=[]
        labels=[]
        for x in self._test_set:
            label = self.classify(x)
            nova_llista.append((x,label))
            labels.append(label)
        return labels
   
    
    @abstractmethod
    def accuracy(self,test_path):
        pass
    
    

class Classification_SVM(Classification):
    
    def classify(self,Object1):
        
        if self._tipus == 2 or self._tipus ==3 or self._tipus==4 or self._tipus==5:
            representacion = self._feature_extractor.extract(Object1)
            predicted_label = self._training_model.predict([representacion])
            
            return predicted_label[0]
        
    
    def accuracy(self, test_path):
        
        llista_etiquetes = []
        self._train = TrainSVM(self._tipus,self._feature_extractor)
        testeo = self._train.load(test_path)
        
        if self._tipus==5:
            for file in testeo:
                if 'spmsg' in file:
                    llista_etiquetes.append("spam")
                
                else:
                    llista_etiquetes.append("no_spam")
        
        if self._tipus==4:
            for file in testeo:
                if 'class_0' in file:
                    llista_etiquetes.append("0")
                    
                elif 'class_1' in file:
                    llista_etiquetes.append("1")

                elif 'class_2' in file:
                    llista_etiquetes.append("2")
                    
                elif 'class_3' in file:
                    llista_etiquetes.append("3")
                    
                elif 'class_4' in file:
                    llista_etiquetes.append("4")
                    
                elif 'class_5' in file:
                    llista_etiquetes.append("5")
                 
                elif 'class_6' in file:
                    llista_etiquetes.append("6")
                    
                elif 'class_7' in file:
                    llista_etiquetes.append("7")
                     
                elif 'class_8' in file:
                    llista_etiquetes.append("8")
                    
                elif 'class_9' in file:
                    llista_etiquetes.append("9")
        
        if self._tipus==2: 
            
            for file in testeo:
                
                if "airplane" in file:
                    llista_etiquetes.append("airplane")
                if "automobile" in file:
                    llista_etiquetes.append("automobile")
                if "bird" in file:
                    llista_etiquetes.append("bird")
                if "cat" in file:
                    llista_etiquetes.append("cat")
                if "deer" in file:
                    llista_etiquetes.append("deer")
                if "dog" in file:
                    llista_etiquetes.append("dog")
                if "frog" in file:
                    llista_etiquetes.append("frog")
                if "horse" in file:
                    llista_etiquetes.append("horse")
                if "ship" in file:
                    llista_etiquetes.append("ship")
                if "truck" in file:
                    llista_etiquetes.append("truck")
                    
            
        elif self._tipus==3:
            
            
            for file in testeo:
                if "ms-windows" in file:
                    llista_etiquetes.append("ms-windows") 
                    
                if "crypt" in file:
                    llista_etiquetes.append("crypt")
                
                if "religion-christian" in file:
                    llista_etiquetes.append("religion-christian")
                
                if "graphics" in file:
                    llista_etiquetes.append("graphics")
                    
                if "hardware-mac" in file:
                    llista_etiquetes.append("hardware-mac")

                if "atheism" in file:
                    llista_etiquetes.append("atheism")
                    
                if "hockey" in file:
                    llista_etiquetes.append("hockey")

                if "electronics" in file:
                    llista_etiquetes.append("electronics")

                if "politics-guns" in file:
                    llista_etiquetes.append("politics-guns")

                if "med" in file:
                    llista_etiquetes.append("med")

                if "hardware-pc" in file:
                    llista_etiquetes.append("hardware-pc")

                if "space" in file:
                    llista_etiquetes.append("space")

                if "windows-x" in file: 
                    llista_etiquetes.append("windows-x")

                if "forsale" in file:
                    llista_etiquetes.append("forsale")

                if "politics-mideast" in file:
                    llista_etiquetes.append("politics-mideast")

                if "religion-misc" in file:
                    llista_etiquetes.append("religion-misc")

                if "autos" in file:
                    llista_etiquetes.append("autos")

                if "baseball" in file:
                    llista_etiquetes.append("baseball")

                if "motorcycles" in file:
                    llista_etiquetes.append("motorcycles")

                if "politics-misc" in file:
                    llista_etiquetes.append("politics-misc")

        llista_labels = self.evaluate()
        
   

        llista_boolea = []
       
        for x in range(len(llista_labels)):
            if llista_labels[x] == llista_etiquetes[x]:
                llista_boolea.append(True)
            else:
                llista_boolea.append(False)
               
        
        contador = 0
        for y in llista_boolea:
            if y == True:
                contador += 1
                    
        accuracy = (int(contador)/len(llista_labels))
        
        return accuracy,testeo,llista_labels
            


class Classification_KNN(Classification):
    
    def classify(self,Object1):
        distances_file_train = []
        file_features = self._feature_extractor.extract(Object1)
        
        for i in range (len(self._training_model)):
            distance = self._feature_extractor.compute_distance(self._training_model[i][0],file_features)
            tupla = (distance,self._training_model[i][1])
            distances_file_train.append(tupla)

        distance_with_order = sorted(distances_file_train)
        if self._tipus == 0:
            
            list_boolea = []
            
            for x in range(self._k):
                list_boolea.append(distance_with_order[x][1])
                
            contador_true = 0
            contador_false = 0
                
            for boolea in list_boolea:
                if boolea:
                    contador_true += 1
                else:
                    contador_false += 1
            if contador_true > contador_false:
                return 'spam'
            else:
                return 'no_spam'
       
        if self._tipus == 6:
            lst = []
            for x in range(self._k):
                lst.append(distance_with_order[x][1])
                
            et= max(set(lst), key=lst.count)
            return et
                
    
        if self._tipus == 1:
            llista_num = []
            
            for x in range(self._k):
                llista_num.append(distance_with_order[x][1])
            counter = 0
            num = llista_num[0] 
      
            for i in llista_num: 
                frequency = llista_num.count(i) 
                if(frequency> counter): 
                    counter = frequency 
                    num = i               
            return str(num)
        


    def accuracy(self, test_path):
        
        llista_etiquetes = []
        self._train = Train_KNN(self._tipus,self._feature_extractor)
        testeo = self._train.load(test_path)

        
        if self._tipus==0: 
            
            for file in testeo:
                
                if "spms" in file:
                    llista_etiquetes.append("spam")
                else:
                    llista_etiquetes.append("no_spam")
                    
                    
        if self._tipus==6:
            for file in testeo:
                if "ms-windows" in file:
                        llista_etiquetes.append("ms-windows")
                if "crypt" in file:
                        llista_etiquetes.append("crypt")       
                if "religion-christian" in file:           
                        llista_etiquetes.append("religion-christian")           
                if "graphics" in file:      
                        llista_etiquetes.append("graphics")
                if "hardware-mac" in file:                 
                        llista_etiquetes.append("hardware-mac")     
                if "atheism" in file:                 
                        llista_etiquetes.append("atheism")       
                if "hockey" in file:                   
                        llista_etiquetes.append("hockey")    
                if "electronics" in file:                  
                        llista_etiquetes.append("electronics")           
                if "politics-guns" in file:                    
                        llista_etiquetes.append("politics-guns")                
                if "med" in file:                   
                        llista_etiquetes.append("med")           
                if "hardware-pc" in file:                    
                        llista_etiquetes.append("hardware-pc")                
                if "space" in file:                    
                        llista_etiquetes.append("space")            
                if "windows_x" in file:                    
                        llista_etiquetes.append("windows_x")              
                if "forsale" in file:                    
                        llista_etiquetes.append("forsale")                  
                if "politics-mideast" in file:                   
                        llista_etiquetes.append("politics-mideast")               
                if "religion-misc" in file:                    
                        llista_etiquetes.append("religion-misc")            
                if "autos" in file:                    
                        llista_etiquetes.append("autos")                    
                if "baseball" in file:                    
                        llista_etiquetes.append("baseball")                   
                if "motorcycles" in file:                    
                        llista_etiquetes.append("motorcycles")               
                if "politics-misc" in file:            
                        llista_etiquetes.append("politics-misc")
            

        if self._tipus == 1:
            for file in testeo:
                if 'class_0' in file:
                    llista_etiquetes.append("0")
                    
                elif 'class_1' in file:
                    llista_etiquetes.append("1")
                    
                elif 'class_2' in file:
                    llista_etiquetes.append("2")
                
                elif 'class_3' in file:
                    llista_etiquetes.append("3")
                
                elif 'class_4' in file:
                    llista_etiquetes.append("4")
                
                elif 'class_5' in file:
                    llista_etiquetes.append("5")
                
                elif 'class_6' in file:
                    llista_etiquetes.append("6")
                    
                elif 'class_7' in file:
                    llista_etiquetes.append("7")
                
                elif 'class_8' in file:
                    llista_etiquetes.append("8")
                    
                elif 'class_9' in file:
                    llista_etiquetes.append("9")
        
        llista_labels = self.evaluate()
    
        llista_boolea = []
        for x in range(len(llista_labels)):
            if llista_labels[x] == llista_etiquetes[x]:
                llista_boolea.append(True)
            else:
                llista_boolea.append(False)
       
        contador = 0
        for y in llista_boolea:
            if y == True:
                contador += 1
                    
        accuracy = (int(contador)/len(llista_labels))
            
        return accuracy,testeo,llista_labels
            
            
       
    
    

    