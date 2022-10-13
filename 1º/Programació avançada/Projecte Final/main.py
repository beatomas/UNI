#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 19:22:08 2020

@author:
"""
from feature_extractor import BOW, Text_HOG, descriptor_HOG, ByN
import re
from classifier import Classifier
import pickle
import os
import errno


         
    
def IMATGE(train_path,test_path,k,opcio,trainig_model):
    if (opcio==1):
        x= classifier.train(train_path)
        return x
        
    if (opcio==2):
        accuracy,testeo,llista_labels= classifier.classify(test_path,k,training_model)
        return accuracy,testeo,llista_labels
    



def TEXTO(train_path, test_path, fitxer_vocabulari, k,opcio,trainig_model):
    if (opcio==1):
        x= classifier.train(train_path)
        return x
        
    if (opcio==2):
        accuracy,testeo,llista_labels= classifier.classify(test_path,k,training_model)
        return accuracy,testeo,llista_labels




nomfitxer= input("Introdueix el nom de fitxer que vols comprovar: ")

comandes=[]
FDE = []

with open (nomfitxer, 'r') as arxiu:
    
    for line in arxiu:
        paraules= line[0:-1]
        
        FDE.append(paraules)



for parametre in range(len(FDE)):
    
    if FDE[0]== "Classificacio":
    
        if (parametre==0) or (parametre==1) or (parametre==4) or (parametre==5):
            comandes.append(FDE[parametre])
            
        if (parametre==2) or (parametre==3) or (parametre==6):
            par= "./"
            for lletra in FDE[parametre]:
                if lletra in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .":
                    par=par+lletra
                else:
                    if par!=par[-1]:
                        par=par+"/"
                        
            comandes.append(par)
            
    
    if FDE[0]== "Entrenament":
        if (parametre==0) or (parametre==1) or (parametre==3) or (parametre==4):
            comandes.append(FDE[parametre])
        
        if (parametre==2) or (parametre==5):
            par= "./"
            for lletra in FDE[parametre]:
                if lletra in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .":
                    par=par+lletra
                else:
                    if par!=par[-1]:
                        par=par+"/"
                        
            comandes.append(par)
        
 
            
        
def document(posicio,comandes):
    llista=[]
    llista2=[]
    
    r = comandes[posicio]

    for x in r:
        llista.append(x)
    
    llista.reverse()
    
    y= True
    for x in llista:
        if x!="/" and y==True:
            
            llista2.append(x)
        
        if x=="/":
            y=False
            
    llista2.reverse()
    
    nom= "".join(llista2)
    
    return nom
    
    
nom= document(-1,comandes)

nom1=document(-4,comandes)



dire = comandes[-1]
llista2=[]
llista3=[]



dire1= dire[2:]

for w in dire1:
    llista2.append(w)



y= True
for lletra in llista2:
    if lletra!="/" and y==True:
        
        llista3.append(lletra)
    
    if lletra=="/":
        y=False
        

directo= "".join(llista3)
directori="./"+directo




try:
    os.mkdir(directori)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
        
        
     
def creacio_output(accuracy,testeo,llista_labels,directori):    
    
    
    llista_output=[]
    contador= 0
    for x in testeo:
                
        suma= testeo[contador]+" "+llista_labels[contador]
        llista_output.append(suma)
        contador+=1
            
    acc = "accuracy = "+str(accuracy)
            
        
    llista_output.append(acc)
    
   
    dir_actual= os.getcwd()
    dir_final= os.path.join(dir_actual,directori)
    fname= os.path.join(dir_final,nom)
        
    with open(fname,"w") as output:
            
        for linea in llista_output:
               output.write(linea+"\n")
               

        
        
        
if comandes[1]=="NEWSGROUPS" or comandes[1]=="newsgroups" or comandes[1]=="spam" or comandes[1]=="SPAM": #TEXTO
    fitxer_vocabulari=[]
    with open ("vocabulary.txt", 'r') as fitxer:
        for line in fitxer:
            paraules = (re.sub("[^a-zA-Z0-9]", " ", line.lower()).split())
            for i in paraules:
                fitxer_vocabulari.append(i)
                
                
    
    if comandes[0] == "Entrenament": #KNN ENTRENAMENT TEXT

        if comandes[-2][0:3] == "KNN":
            feature_extractor = BOW(fitxer_vocabulari)
            
            if comandes[1]== "spam" or comandes[1]=="SPAM":
                labels = ['spam', 'no_spam']
                classifier = Classifier(0, feature_extractor, labels)
                
            elif comandes[1]=="NEWSGROUPS" or comandes[1]=="newsgroups":
                labels = ["ms-windows","crypt","religion-christian","graphics","hardware-mac", "atheism", "hockey", "electronics","politics-guns", "med","hardware-pc","space", "windows-x", "forsale","politics-mideast","religion-misc","autos","baseball", "motorcycles", "politics-misc"]
                classifier = Classifier(6, feature_extractor, labels)
            
            
            
            train_path = comandes[2]
            
            x = TEXTO(train_path, None, fitxer_vocabulari, 0,1,None)
            
            
            with open (nom,"wb") as fit:
               pickle.dump(x,fit)
        
        
        if comandes[-2] == "SVM":
            
            feature_extractor = Text_HOG(fitxer_vocabulari)
            
            if comandes[1]== "spam" or comandes[1]=="SPAM":
                labels = ['spam', 'no_spam']
                classifier = Classifier(5, feature_extractor, labels)
                
            elif comandes[1]=="NEWSGROUPS" or comandes[1]=="newsgroups":
                labels = ["ms-windows","crypt","religion-christian","graphics","hardware-mac", "atheism", "hockey", "electronics","politics-guns", "med","hardware-pc","space", "windows-x", "forsale","politics-mideast","religion-misc","autos","baseball", "motorcycles", "politics-misc"]
                classifier = Classifier(3, feature_extractor, labels)
           
            
            train_path = comandes[2]
            x = TEXTO(train_path, None, fitxer_vocabulari, 0,1,None)
            
            
            with open (nom,"wb") as fit:
               pickle.dump(x,fit)
        
    
    if comandes[0] == "Classificacio": #KNN ENTRENAMENT TEXT
        
        
        # no sabemos si podemos utilizar el HOG para SVM de texto
        
        if comandes[-2][0:3] == "KNN":
            
            feature_extractor = BOW(fitxer_vocabulari)
            
            if comandes[1]== "spam" or comandes[1]=="SPAM":
                labels = ['spam', 'no_spam']
                classifier = Classifier(0, feature_extractor, labels)
                
            elif comandes[1]=="NEWSGROUPS" or comandes[1]=="newsgroups":
                labels = ["ms-windows","crypt","religion-christian","graphics","hardware-mac", "atheism", "hockey", "electronics","politics-guns", "med","hardware-pc","space", "windows-x", "forsale","politics-mideast","religion-misc","autos","baseball", "motorcycles", "politics-misc"]
                classifier = Classifier(6, feature_extractor, labels)
            
            
            train_path = comandes[3] #serializar objeto
            test_path= comandes[2]
            
            k = int(comandes[-2][-1])
            
            with open (nom1,"rb") as fitclass:
                training_model = pickle.load(fitclass)
        
            accuracy,testeo,llista_labels = TEXTO(train_path, test_path, fitxer_vocabulari, k,2,training_model)
            
            creacio_output(accuracy,testeo,llista_labels,directori)
            
        
            
            
        if comandes[-2] == "SVM":
            
            feature_extractor = Text_HOG(fitxer_vocabulari)
            
            if comandes[1]== "spam" or comandes[1]=="SPAM":
                labels = ['spam', 'no_spam']
                classifier = Classifier(5, feature_extractor, labels)
                
            elif comandes[1]=="NEWSGROUPS" or comandes[1]=="newsgroups":
                labels = ["ms-windows","crypt","religion-christian","graphics","hardware-mac", "atheism", "hockey", "electronics","politics-guns", "med","hardware-pc","space", "windows-x", "forsale","politics-mideast","religion-misc","autos","baseball", "motorcycles", "politics-misc"]
                classifier = Classifier(3, feature_extractor, labels)
                
            
            train_path = comandes[3] #serializar objeto
            test_path= comandes[2]
            
            k = None
            
            with open (nom1,"rb") as fitclass:
                training_model = pickle.load(fitclass)
            
            accuracy,testeo,llista_labels = TEXTO(train_path, test_path, fitxer_vocabulari, k,2,training_model)
            creacio_output(accuracy,testeo,llista_labels,directori)
            




if comandes[1]=="MNIST" or comandes[1]=="cifar" or comandes[1]=="CIFAR" or comandes[1]=="mnist": #IMATGE
    
    if comandes[0] == "Entrenament": #ENTRENAMENT IMATGE
        
        
        if comandes[-2][0:3] == "KNN":
            
            feature_extractor = ByN()
            
            labels = ['0','1','2','3','4','5','6','7','8','9']
            classifier = Classifier(1, feature_extractor, labels)


            train_path = comandes[2]
            x = IMATGE(train_path, None, 0,1,None)
            
            
            with open (nom,"wb") as fit:
                pickle.dump(x,fit)
                

        if comandes[-2] == "SVM":
            feature_extractor = descriptor_HOG()
            
            if comandes[1]=="cifar" or comandes[1]=="CIFAR":
                labels = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]
                classifier = Classifier(2, feature_extractor, labels)
            
            elif comandes[1]=="MNIST" or comandes[1]=="mnist":
                labels = ['0','1','2','3','4','5','6','7','8','9']
                classifier = Classifier(4, feature_extractor, labels)
                
            train_path = comandes[2]
            x = IMATGE(train_path, None, 0,1,None)
            
            
            with open (nom,"wb") as fit:
                pickle.dump(x,fit)
        

        
    if comandes[0] == "Classificacio": 
        
        if comandes[-2][0:3] == "KNN":
            feature_extractor = ByN()
            
            labels = ['0','1','2','3','4','5','6','7','8','9']
            classifier = Classifier(1, feature_extractor, labels)
                
                
            train_path = comandes[3] #serializar objeto
            test_path= comandes[2]
            
            k = int(comandes[-2][-1])
            
            
            with open (nom1,"rb") as fitclass:
                training_model = pickle.load(fitclass)
            
            
            accuracy,testeo,llista_labels = IMATGE(train_path, test_path, k,2,training_model)
            
        
            creacio_output(accuracy,testeo,llista_labels,directori)
                
            
            
        if comandes[-2] == "SVM":
            
            feature_extractor = descriptor_HOG()
            
            if comandes[1]=="cifar" or comandes[1]=="CIFAR":
                
                labels = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]
                classifier = Classifier(2, feature_extractor, labels)
            
            elif comandes[1]=="MNIST" or comandes[1]=="mnist":
                labels = ['0','1','2','3','4','5','6','7','8','9']
                classifier = Classifier(4, feature_extractor, labels)
            
            
            
            train_path = comandes[3] 
            test_path= comandes[2]
            
    
            k = None
            
            with open (nom1,"rb") as fitclass:
                training_model = pickle.load(fitclass)
            
            accuracy,testeo,llista_labels= IMATGE(train_path, test_path, k,2,training_model)
            
            creacio_output(accuracy,testeo,llista_labels,directori)
                
            
            

        
            
            
        
        
        
        
        
        