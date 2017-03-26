#! /usr/bin/python3
# -*- coding: utf-8 -*- 
import random
from copy import copy
import re

class Atome():
    """Un atome est défini par un nom, un symbole et une valence"""
    def __init__(self):
        self.nom=""
        self.symbole=""
        self.valence=0
        self.indice=0
        self.etage_ox=[]
        self.latex=" latex "
        self.formule=" formule "
class Groupement():
    """Un groupement est défini par un nom, un symbole et une valence"""
    def __init__(self):
        self.nom=""
        self.symbole=""
        self.valence=0
        self.acide=""
        self.indice=0
        self.latex=""

class Eau():
    def __init__(self):
        #self.famille="Métal"
        #self.fonction="M"
        self.latex=" H_{2}O "
        self.formule="H20"

class Hydrogene():
    def __init__(self):
        #self.famille="Métal"
        #self.fonction="M"
        self.latex=" H_{2} "
        self.formule="H2"

class Oxygene():
    def __init__(self):
        #self.famille="Métal"
        #self.fonction="M"
        self.latex=" O_{2} "
        self.formule="02"

class Metal():
    def __init__(self):
        self.famille="Métal"
        self.fonction="M"
        self.metal=dico_metaux[random.choice(liste_metaux)]
        self.latex=self.metal.symbole
        self.formule=self.metal.symbole

class Sel2():
    def __init__(self):
        self.famille="Sel binaire"
        self.fonction="MX"
        self.atomes()
        self.molecule()
        
    def atomes(self):    
        self.metal=copy(dico_metaux[random.choice(liste_metaux)])
        self.non_metal=copy(dico_non_metaux[random.choice(liste_non_metaux)])
        #while self.non_metal.symbole=="N":
        #    self.non_metal=copy(dico_non_metaux[random.choice(liste_non_metaux)])
    
    def molecule(self):
        self.metal.indice=self.non_metal.valence
        self.non_metal.indice=self.metal.valence
        if self.metal.valence==self.non_metal.valence:
            self.metal.indice=1
            self.non_metal.indice=1
        self.masse_molaire=self.non_metal.masse*self.non_metal.indice+self.metal.masse*self.metal.indice
        self.nom="%sure de %s" %(self.non_metal.racine,self.metal.racine)
        self.nom=self.nom.replace('de a',"d'a")
        self.nom=self.nom.replace("de i","d'i")
        
        self.formule=self.metal.symbole+str(self.metal.indice)+self.non_metal.symbole+str(self.non_metal.indice)
        self.formule=self.formule.replace("1","")
        self.latex=""
        self.latex+=self.metal.latex
        if self.metal.indice!=1:
            self.latex+="_{"+str(self.metal.indice)+"}"    
        self.latex+=self.non_metal.symbole
        if self.non_metal.indice!=1:
            self.latex+="_{"+str(self.non_metal.indice)+"}"
        
        #print (self.formule,self.nom,self.latex)

class Acide2():
    def __init__(self):
        self.atomes()
        self.molecule()
        self.famille="Acide binaire"
        self.fonction="HX"
    
    def atomes(self):
        self.non_metal=copy(dico_non_metaux[random.choice(liste_non_metaux)])
        while self.non_metal.symbole=="N":
             self.non_metal=copy(dico_non_metaux[random.choice(liste_non_metaux)])
    
    def molecule(self):
        self.non_metal.indice=1
        self.indice_hydrogene=self.non_metal.valence
        self.masse_molaire=self.non_metal.masse*self.non_metal.indice+1*self.indice_hydrogene
        self.nom="acide %shydrique" %(self.non_metal.racine)
        self.nom=self.nom.replace('hh','h')
        self.formule="H"+str(self.indice_hydrogene)+self.non_metal.symbole
        self.formule=self.formule.replace("1","")
        self.latex=""
        self.latex+="H"
        if self.indice_hydrogene!=1:
            self.latex+="_{"+str(self.indice_hydrogene)+"}"    
        self.latex+=self.non_metal.symbole
        #print (self.formule,self.nom)
        
class Oxyde_met():
    def __init__(self):
        self.atomes()
        self.molecule()
        self.famille="Oxyde métallique"
        self.fonction="MO"
    
    def atomes(self):
        self.metal=copy(dico_metaux[ random.choice(liste_metaux)])
    
    def molecule(self):
        self.metal.indice=2
        self.nom="oxyde de %s" %(self.metal.racine)
        self.nom=self.nom.replace("de a","d'a")
        self.indice_oxygene=self.metal.valence
        if self.metal.valence==2:
            self.metal.indice=1
            self.indice_oxygene=1
        self.masse_molaire=self.metal.masse*self.metal.indice+self.indice_oxygene*16
        self.formule=self.metal.symbole+str(self.metal.indice)+"O"+str(self.indice_oxygene)
        self.formule=self.formule.replace("1","")
        self.latex=""
        self.latex+=self.metal.latex
        if self.metal.indice!=1:
            self.latex+="_{"+str(self.metal.indice)+"}"    
        self.latex+="O"
        if self.indice_oxygene!=1:
            self.latex+="_{"+str(self.indice_oxygene)+"}"
        
        #print (self.formule,self.nom)

class Base():
    def __init__(self):
        self.atomes()
        self.molecule()
        self.famille="Base"
        self.fonction="MOH"
        
    def atomes(self):
        self.metal=copy(dico_metaux[random.choice(liste_metaux)])
       
    def molecule(self):   
        self.metal.indice=1
        self.nom="hydroxyde de %s" %(self.metal.racine)
        self.nom=self.nom.replace("de a","d'a")
        self.indice_hydroxyle=self.metal.valence
        self.masse_molaire=self.metal.masse*self.metal.indice+17*self.indice_hydroxyle
        
        self.formule=''
        self.formule+=self.metal.symbole+str(self.metal.indice)
        if self.indice_hydroxyle!=1:
            self.formule+="(OH)"+str(self.indice_hydroxyle)
        else:
            self.formule+="OH"
        
        #self.formule=self.metal.symbole+str(self.metal.indice)+"(OH)"+str(self.indice_hydroxyle)
        self.formule=self.formule.replace("1","")
        
        self.latex=""
        self.latex+=self.metal.latex
        if self.metal.indice!=1:
            self.latex+="_{"+str(self.metal.indice)+"}"    
        if self.indice_hydroxyle!=1:
            self.latex+="(OH)_{"+str(self.indice_hydroxyle)+"}"
        else:
            self.latex+="OH"

class Oxyde_non_met():
    def __init__(self):
        self.atomes()
        self.molecule()
        self.famille="Oxyde non-métalique"
        self.fonction="XO"
        
    def atomes(self):    
        self.non_metal=copy(dico_non_metaux[random.choice(liste_non_metaux)])
    def molecule(self):    
        self.non_metal.indice=2
        self.indice_oxygene=random.choice(self.non_metal.etage_ox)
        if self.indice_oxygene==1:
            prefixe="hémi"
        if self.indice_oxygene==2:
            prefixe="mon"
            self.indice_oxygene=1
            self.non_metal.indice=1
        if self.indice_oxygene==3:
            prefixe="hémitri"
        if self.indice_oxygene==4:
            prefixe="di"
            self.indice_oxygene=2
            self.non_metal.indice=1
        if self.indice_oxygene==5:
            prefixe="hémipent"
        if self.indice_oxygene==6:
            prefixe="tri"
            self.indice_oxygene=3
            self.non_metal.indice=1
        if self.indice_oxygene==7:
            prefixe="hémihept"
        self.masse_molaire=self.non_metal.masse*self.non_metal.indice+16*self.indice_oxygene
        self.nom="%soxyde de %s" %(prefixe,self.non_metal.nom)
        self.nom=self.nom.replace("de i","d'i")
        self.nom=self.nom.replace("de a","d'a")
        self.formule=self.non_metal.symbole+str(self.non_metal.indice)+"O"+str(self.indice_oxygene)
        self.formule=self.formule.replace("1","")
        self.latex=""
        self.latex+=self.non_metal.symbole
        if self.non_metal.indice!=1:
            self.latex+="_{"+str(self.non_metal.indice)+"}"    
        self.latex+="O"
        if self.indice_oxygene!=1:
            self.latex+="_{"+str(self.indice_oxygene)+"}"
        
        #print (self.formule,self.nom)

class Sel3():
    def __init__(self):
        self.atomes()
        self.molecule()
        self.famille="Sel ternaire"
        self.fonction="MXO"
        
    def atomes(self):
        self.metal=copy(dico_metaux[ random.choice(liste_metaux)])
        self.groupement=copy(dico_groupement[ random.choice(liste_groupement)])
        
    def molecule(self):    
        self.metal.indice=self.groupement.valence
        self.groupement.indice=self.metal.valence
        if self.metal.valence==self.groupement.valence:
            self.metal.indice=1
            self.groupement.indice=1
        self.masse_molaire=self.metal.masse*self.metal.indice+self.groupement.masse*self.groupement.indice
        self.nom="%s de %s" %(self.groupement.nom,self.metal.racine)
        self.nom=self.nom.replace('de a',"d'a")
        self.nom=self.nom.replace("de i","d'i")
        if self.groupement.indice>1:
            self.formule=self.metal.symbole+str(self.metal.indice)+"("+self.groupement.symbole+")"+str(self.groupement.indice)
        else :
            self.formule=self.metal.symbole+str(self.metal.indice)+self.groupement.symbole+str(self.groupement.indice)
        self.formule=self.formule.replace("1","")
        self.latex=""
        self.latex+=self.metal.latex
        if self.metal.indice!=1:
            self.latex+="_{"+str(self.metal.indice)+"}"    
        #self.latex+=self.non_metal.symbole
        if self.groupement.indice!=1:
            self.latex+="("+self.groupement.latex+")"
            self.latex+="_{"+str(self.groupement.indice)+"}"
        else:
            self.latex+=self.groupement.latex
        
        #print (self.formule,self.nom)

class Acide3():
    def __init__(self):
        self.atomes()
        self.molecule()
        self.famille="Acide ternaire"
        self.fonction="HXO"
        
    def atomes(self):    
        self.groupement=copy(dico_groupement[ random.choice(liste_groupement)])
        
    def molecule(self):    
        self.groupement.indice=1
        self.indice_hydrogene=self.groupement.valence
        self.masse_molaire=self.groupement.masse*self.groupement.indice+1*self.indice_hydrogene
        self.nom="acide %s" %self.groupement.acide
        #self.nom=self.nom.replace('hh','h')
        
        self.formule="H"+str(self.indice_hydrogene)+self.groupement.symbole
        self.formule=self.formule.replace("1","")
        self.latex=""
        self.latex+="H"
        if self.indice_hydrogene!=1:
            self.latex+="_{"+str(self.indice_hydrogene)+"}"    
        if self.groupement.indice!=1:
            self.latex+="("+self.groupement.latex+")"
            self.latex+="_{"+str(self.groupement.indice)+"}"
        else:
            self.latex+=self.groupement.latex

    


class Gene_molecule():
    def __init__(self):
        dico_solub={}
        questionnaire=[]
        liste_nom=[]
        liste_formules=[]
        liste_latex=[]
        tentatives=0
        
        myfile=open('./tableau_solubilite.csv', "r")
        for ligne in myfile:
             liste_infos=ligne.rstrip('\n\r').split('\t')
             formule=liste_infos[1]
             formule=formule.replace(' ','')
             dico_solub[formule]=liste_infos[2]
        myfile.close()
        
        #print(dico_solub)
        
        while tentatives<5000:
            choix=random.choice([1,2,3,4,5,6,7])
            if choix==1 : exercice=Sel2()
            if choix==2 : exercice=Acide2()
            if choix==3 : exercice=Oxyde_met()
            if choix==4 : exercice=Base()
            if choix==5 : exercice=Oxyde_non_met()
            if choix==6 : exercice=Sel3()
            if choix==7 : exercice=Acide3()
            
            if exercice.nom not in liste_nom:
                 #print(exercice.nom)
                 questionnaire.append(exercice)
                 liste_nom.append(exercice.nom)
                 liste_formules.append(exercice.formule)
                 liste_latex.append(exercice.latex)
                 tentatives=0
            else:
                 tentatives+=1
        
        
        f = open('./liste_molecules_simples.csv','w')
        for question in questionnaire:
            try:
                 dico_solub[question.formule]
                 f.write(question.famille)
                 f.write('\t')
                 f.write(question.fonction )
                 f.write('\t' )
                 f.write(question.formule )
                 f.write('\t' )
                 f.write(question.latex )
                 f.write('\t')
                 f.write(question.nom )
                 f.write('\t' )
                 f.write(str(question.masse_molaire))
                 f.write('\t' )
                 f.write(dico_solub[question.formule])
                 f.write('\n')
            
            
            except:
                 try:
                     dico_solub[question.latex]
                     f.write(question.famille)
                     f.write('\t')
                     f.write(question.fonction )
                     f.write('\t' )
                     f.write(question.formule )
                     f.write('\t' )
                     f.write(question.latex )
                     f.write('\t')
                     f.write(question.nom )
                     f.write('\t' )
                     f.write(str(question.masse_molaire))
                     f.write('\t' )
                     f.write(dico_solub[question.latex])
                     f.write('\n')
                     
            
                 except:
                     pass





if __name__=="__main__":
     liste_metaux=[]
     liste_non_metaux=[]
     liste_groupement=[]
     dico_metaux={}
     dico_non_metaux={}
     dico_groupement={}
     
     myfile=open('./metaux_simples.txt', "r")
     for ligne in myfile:
         liste_infos=ligne.rstrip('\n\r').split('\t')
         atome=Atome()
         atome.nom=liste_infos[0]
         atome.symbole=liste_infos[1]
         atome.formule=liste_infos[1]
         atome.latex=liste_infos[5]
         atome.masse=int(liste_infos[2])
         atome.valence=int(liste_infos[3])
         atome.racine=liste_infos[4]
         #atome.latex=liste_infos[4]
         liste_metaux.append(atome.nom)
         dico_metaux[atome.nom]=atome
     
     myfile=open('./non_metaux.txt', "r")
     for ligne in myfile:
         liste_infos=ligne.rstrip('\n\r').split('\t')
         atome=Atome()
         atome.nom=liste_infos[0]
         atome.symbole=liste_infos[1]
         atome.formule=liste_infos[1]
         atome.latex=liste_infos[1]
         atome.masse=int(liste_infos[2])
         atome.valence=int(liste_infos[3])
         atome.racine=liste_infos[4]
         etage_ox=liste_infos[5:]
         for etage in etage_ox:
             atome.etage_ox.append(int(etage))
         liste_non_metaux.append(atome.nom)
         dico_non_metaux[atome.nom]=atome
     
     myfile=open('./groupements_simples.txt', "r")
     for ligne in myfile:
         liste_infos=ligne.rstrip('\n\r').split('\t')
         groupement=Groupement()
         groupement.nom=liste_infos[0]
         groupement.symbole=liste_infos[1]
         groupement.masse=int(liste_infos[2])
         groupement.valence=int(liste_infos[3])
         groupement.acide=liste_infos[4]
         groupement.latex=liste_infos[5]
         liste_groupement.append(groupement.nom)
         dico_groupement[groupement.nom]=groupement
     
     Gene_molecule()
#pondérer les eqn
#pondérer et faire lect_mol
#compléter les eqn, les pondérer et faire lect_mol