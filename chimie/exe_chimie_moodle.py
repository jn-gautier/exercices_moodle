#! /usr/bin/python3
# -*- coding: utf-8 -*- 
import random
import subprocess
from copy import deepcopy,copy

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
        while self.non_metal.symbole=="N":
            self.non_metal=copy(dico_non_metaux[random.choice(liste_non_metaux)])
    
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
        self.latex+=self.metal.symbole
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
        self.latex+=self.metal.symbole
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
        self.formule=self.metal.symbole+str(self.metal.indice)+"(OH)"+str(self.indice_hydroxyle)
        self.formule=self.formule.replace("1","")
        self.latex=""
        self.latex+=self.metal.symbole
        if self.metal.indice!=1:
            self.latex+="_{"+str(self.metal.indice)+"}"    
        if self.indice_hydroxyle!=1:
            self.latex+="(OH)_{"+str(self.indice_hydroxyle)+"}"
        else:
            self.latex+="OH"
        
        #print (self.formule,self.nom)

class Oxyde_non_met():
    def __init__(self):
        self.atomes()
        self.molecule()
        self.famille="Oxyde non-métallique"
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
        self.latex+=self.metal.symbole
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
class Reaction():
    def __init__(self):
        pass
    
    def schema_obtention(self):
        if self.choix==1:
            corps_1=self.liste_corps[0]
            corps_2=self.liste_corps[1]
            corps_3=self.liste_corps[2]
            corps_4=self.liste_corps[3]
            self.reponse="$$ %s \\  %s + %s \\ %s \\rightarrow  %s \\ %s + \\  %s \\ %s $$" %(corps_1.coef,corps_1.latex,corps_2.coef,corps_2.latex,corps_3.coef,corps_3.latex,corps_4.coef,corps_4.latex)
            
            self.enonce="<p>Dans l'équation suivante :</p>"
            self.enonce+="$$ %s \\  %s + %s \\ %s \\rightarrow  %s \\ X + \\  %s \\ Y $$" %(corps_1.coef,corps_1.latex,corps_2.coef,corps_2.latex,corps_3.coef,corps_4.coef)
            self.enonce+="<p>La formule de X est : {1:SHORTANSWER_C:=%s}</p>" %corps_3.formule
            self.enonce+="<p>La formule de Y est : {1:SHORTANSWER_C:=%s}</p>"%corps_4.formule
            
        if self.choix==2:
            corps_1=self.liste_corps[0]
            corps_2=self.liste_corps[1]
            corps_3=self.liste_corps[2]
            corps_4=self.liste_corps[3]
            
            self.reponse="$$ %s \\  %s + %s \\ %s \\rightarrow  %s \\ %s + \\  %s \\ %s $$" %(corps_1.coef,corps_1.latex,corps_2.coef,corps_2.latex,corps_3.coef,corps_3.latex,corps_4.coef,corps_4.latex)
            self.enonce="<p>Dans l'équation suivante : </p>"
            self.enonce+="$$ %s \\  X + %s \\ %s \\rightarrow  %s \\ %s + \\  %s \\ Y $$" %(corps_1.coef,corps_2.coef,corps_2.latex,corps_3.coef,corps_3.latex,corps_4.coef)
            self.enonce+="<p>La formule de X est : {1:SHORTANSWER_C:=%s}</p>" %corps_1.formule
            self.enonce+="<p>La formule de Y est : {1:SHORTANSWER_C:=%s}</p>"%corps_4.formule
        
        if self.choix==3:
            corps_1=self.liste_corps[0]
            corps_2=self.liste_corps[1]
            corps_3=self.liste_corps[2]
            corps_4=self.liste_corps[3]
            self.reponse="$$ %s \\  %s + %s \\ %s \\rightarrow  %s \\ %s + \\  %s \\ %s $$" %(corps_1.coef,corps_1.latex,corps_2.coef,corps_2.latex,corps_3.coef,corps_3.latex,corps_4.coef,corps_4.latex)
            self.enonce="<p>Dans l'équation suivante : </p>"
            self.enonce+="$$ %s \\  X + %s \\ Y \\rightarrow  %s \\ %s + \\  %s \\ %s $$" %(corps_1.coef,corps_2.coef,corps_3.coef,corps_3.latex,corps_4.coef,corps_4.latex)
            self.enonce+="<p>La formule de X est : {1:SHORTANSWER_C:=%s}</p>" %corps_1.formule
            self.enonce+="<p>La formule de Y est : {1:SHORTANSWER_C:=%s}</p>"%corps_2.formule
            
        if self.choix==4:
            corps_1=self.liste_corps[0]
            corps_2=self.liste_corps[1]
            corps_3=self.liste_corps[2]
            self.reponse="$$ %s \\  %s + %s \\ %s \\rightarrow  %s \\ %s $$" %(corps_1.coef,corps_1.latex,corps_2.coef,corps_2.latex,corps_3.coef,corps_3.latex)
            self.enonce="<p>Dans l'équation suivante : </p>"
            self.enonce+="$$ %s \\  %s + %s \\ %s \\rightarrow  %s \\ X $$" %(corps_1.coef,corps_1.latex,corps_2.coef,corps_2.latex,corps_3.coef)
            self.enonce+="<p>La formule de X est : {1:SHORTANSWER_C:=%s}</p>" %corps_3.formule
        
        if self.choix==5:
            corps_1=self.liste_corps[0]
            corps_2=self.liste_corps[1]
            corps_3=self.liste_corps[2]
            self.reponse="$$ %s \\  %s + %s \\ %s \\rightarrow  %s \\ %s $$" %(corps_1.coef,corps_1.latex,corps_2.coef,corps_2.latex,corps_3.coef,corps_3.latex)
            self.enonce="<p>Dans l'équation suivante : </p>"
            self.enonce+="$$ %s \\  X + %s \\ Y \\rightarrow  %s \\ %s $$" %(corps_1.coef,corps_2.coef,corps_3.coef,corps_3.latex)
            self.enonce+="<p>La formule de X est : {1:SHORTANSWER_C:=%s}</p>" %corps_1.formule
            self.enonce+="<p>La formule de Y est : {1:SHORTANSWER_C:=%s}</p>" %corps_2.formule
    
    def schema_ponderation(self):
        if self.choix==1:
            corps_1=self.liste_corps[0]
            corps_2=self.liste_corps[1]
            corps_3=self.liste_corps[2]
            corps_4=self.liste_corps[3]
            self.reponse="$$ %s \\  %s + %s \\ %s \\rightarrow  %s \\ %s + \\  %s \\ %s $$" %(corps_1.coef,corps_1.latex,corps_2.coef,corps_2.latex,corps_3.coef,corps_3.latex,corps_4.coef,corps_4.latex)
            
            self.enonce="<p>Dans l'équation suivante :</p>"
            self.enonce+="$$ a \\  %s + b \\ %s \\rightarrow  c \\ %s + \\  d \\ %s $$" %(corps_1.latex,corps_2.latex,corps_3.latex,corps_4.latex)
            self.enonce+="<p>La valeur du coefficient a est : {1:NUMERICAL:=%s}</p>" %corps_1.coef
            self.enonce+="<p>La valeur du coefficient b est : {1:NUMERICAL:=%s}</p>" %corps_2.coef
            self.enonce+="<p>La valeur du coefficient c est : {1:NUMERICAL:=%s}</p>" %corps_3.coef
            self.enonce+="<p>La valeur du coefficient d est : {1:NUMERICAL:=%s}</p>" %corps_4.coef
        #
        if self.choix==2:
            corps_1=self.liste_corps[0]
            corps_2=self.liste_corps[1]
            corps_3=self.liste_corps[2]
            self.reponse="$$ %s \\  %s + %s \\ %s \\rightarrow  %s \\ %s $$" %(corps_1.coef,corps_1.latex,corps_2.coef,corps_2.latex,corps_3.coef,corps_3.latex)
            
            self.enonce="<p>Dans l'équation suivante :</p>"
            self.enonce+="$$ a \\  %s + b \\ %s \\rightarrow  c \\ %s $$" %(corps_1.latex,corps_2.latex,corps_3.latex)
            self.enonce+="<p>La valeur du coefficient a est : {1:NUMERICAL:=%s}</p>" %corps_1.coef
            self.enonce+="<p>La valeur du coefficient b est : {1:NUMERICAL:=%s}</p>" %corps_2.coef
            self.enonce+="<p>La valeur du coefficient c est : {1:NUMERICAL:=%s}</p>" %corps_3.coef
            
    
class Acide2_base(Reaction):
    def __init__(self):
        self.acide=Acide2()
        self.base=Base()
        self.sel=Sel2()
        self.sel.metal=copy(dico_metaux[self.base.metal.nom])
        self.sel.non_metal=copy(dico_non_metaux[self.acide.non_metal.nom])
        self.sel.molecule()
        
        self.acide.coef=1
        self.base.coef=1
        self.sel.coef=1
        self.eau=Eau()
        self.eau.coef=1
        nb_metal_reac=self.base.metal.indice
        nb_metal_prod=self.sel.metal.indice
        nb_non_metal_reac=self.acide.non_metal.indice
        nb_non_metal_prod=self.sel.non_metal.indice
        #
        
        self.acide.coef=self.sel.non_metal.indice
        self.sel.coef=self.acide.non_metal.indice
        nb_non_metal_reac=self.acide.coef*self.acide.non_metal.indice
        nb_non_metal_prod=self.sel.coef*self.sel.non_metal.indice
        nb_metal_prod=self.sel.coef*self.sel.metal.indice
        nb_metal_reac=self.base.metal.indice
        
        self.sel.coef*=nb_metal_reac
        self.acide.coef*=nb_metal_reac
        self.base.coef*=nb_metal_prod
        nb_hydroxyle=self.base.indice_hydroxyle*self.base.coef
        
        self.eau.coef=nb_hydroxyle
        
        min_coef=min(self.acide.coef,self.base.coef,self.sel.coef,self.eau.coef)
        pgcd=1
        for i in range(min_coef):
            diviseur_valide=True
            diviseur=i+1
            if self.acide.coef/diviseur!=round(self.acide.coef/diviseur):diviseur_valide=False 
            if self.base.coef/diviseur!=round(self.base.coef/diviseur):diviseur_valide=False
            if self.sel.coef/diviseur!=round(self.sel.coef/diviseur):diviseur_valide=False
            if self.eau.coef/diviseur!=round(self.eau.coef/diviseur):diviseur_valide=False
            if diviseur_valide==True:pgcd=diviseur
        self.acide.coef=int(self.acide.coef/pgcd)
        self.base.coef=int(self.base.coef/pgcd)
        self.sel.coef=int(self.sel.coef/pgcd)
        self.eau.coef=int(self.eau.coef/pgcd)
        
        
        self.reaction=str(self.acide.coef)+self.acide.formule+" + "+str(self.base.coef)+self.base.formule+"=>"+str(self.sel.coef)+self.sel.formule+" + "+str(self.eau.coef)+"H20"
    
    def ponderation(self):
        self.choix=1
        self.liste_corps=[self.acide,self.base,self.sel,self.eau]
        self.schema_ponderation()
        
        
    
    def obtention_lect_mol(self):
        self.choix=random.choice([1,2])
        self.liste_corps=[self.acide,self.base,self.sel,self.eau]
        self.schema_obtention()
            
     
    def stoechiometrie(self):
        self.base.volume=float(random.randint(20,100))/100
        if self.base.volume<0.5:
            self.base.volume_litre=self.base.volume
            self.base.unites_volume="[ml]"
            self.base.volume=self.base.volume_litre*1000
        else :
            self.base.volume_litre=self.base.volume
            self.base.unites_volume="[L]"
        
        self.acide.volume=float(random.randint(20,100))/100
        if self.acide.volume<0.5:
            self.acide.volume_litre=self.acide.volume
            self.acide.unites_volume="[ml]"
            self.acide.volume=self.acide.volume_litre*1000
        else :
            self.acide.volume_litre=self.acide.volume
            self.acide.unites_volume="[L]"
        self.volume_total=self.base.volume_litre+self.acide.volume_litre
        self.unites_volume="[L]"
        #
        self.sel.moles=float(random.randint(10,200))/100
        self.acide.moles=round(self.sel.moles/self.sel.coef*self.acide.coef,4)
        self.base.moles=round(self.sel.moles/self.sel.coef*self.base.coef,4)
        #
        self.sel.masse=round(self.sel.moles*self.sel.masse_molaire,4)
        self.acide.masse=round(self.acide.moles*self.acide.masse_molaire,4)
        self.base.masse=round(self.base.moles*self.base.masse_molaire,4)
        #
        self.sel.cmol=round(self.sel.moles/self.volume_total,4)
        self.acide.cmol=round(self.acide.moles/self.acide.volume_litre,4)
        self.base.cmol=round(self.base.moles/self.base.volume_litre,4)
        #
        choix=random.choice([1,2])
        if choix==1:
            self.enonce="<p>On fait réagir complètement %s %s d'une solution de %s dont la concentration vaut %s [M] avec de l'%s.</p>"%(self.acide.volume,self.acide.unites_volume,self.acide.nom,self.acide.cmol,self.base.nom)
            self.enonce+="<p>Quelle masse de %s faut-il prévoir?</p>"%(self.base.nom)
            self.enonce+="<p>Quelle est la masse de sel obtenue?</p>"
            self.enonce+="<p> \( m_{%s}= \) {1:NUMERICAL:=%s:%s} [g] </p>"%(self.base.latex,self.base.masse,self.base.masse*3/100)
            self.enonce+="<p> \( m_{%s}= \) {1:NUMERICAL:=%s:%s} [g] </p>"%(self.sel.latex,self.sel.masse,self.sel.masse*3/100)
            
            #
            self.feedback="<p><ul> "
            self.feedback+="<li> \("+str(self.acide.coef)+" \\  "+self.acide.latex+" + "+str(self.base.coef)+" \\  "+self.base.latex+"  \\rightarrow  "+str(self.sel.coef)+" \\  "+self.sel.latex+" + "+" \\  "+str(self.eau.coef)+" \\ H_{2}O \)</li>"
            self.feedback+="<li> \( n_{%s}=%s[mol] \\ ; \\ M_{%s}=%s[g.mol^{-1}] \\ ; \\ m_{%s}=%s[g] \)</li>"%(self.base.latex,self.base.moles,self.base.latex,self.base.masse_molaire,self.base.latex,self.base.masse)
            self.feedback+="<li> \( n_{%s}=%s[mol] \\ ; \\ M_{%s}=%s[g.mol^{-1}] \\ ; \\ m_{%s}=%s[g] \)</li>"%(self.sel.latex,self.sel.moles,self.sel.latex,self.sel.masse_molaire,self.sel.latex,self.sel.masse)
            self.feedback+="</ul></p> "
        #
        if choix==2:
            self.enonce="<p>On fait réagir complètement %s %s d'une solution de %s dont la concentration vaut %s [M].</p>"%(self.acide.volume,self.acide.unites_volume,self.acide.nom,self.acide.cmol)
            self.enonce+="<p>Quel volume d'une solution %s [M] de %s faut-il prévoir pour réaliser cette réaction?</p>"%(self.base.cmol,self.base.nom)
            self.enonce+="<p>Quelle est la masse de sel obtenue?</p>"
            self.enonce+="<p> \( V_{%s}= \) {1:NUMERICAL:=%s:%s} [L] </p>"%(self.base.latex,self.base.volume_litre,self.base.volume_litre*3/100)
            self.enonce+="<p> \( m_{%s}= \) {1:NUMERICAL:=%s:%s} [g] </p>"%(self.sel.latex,self.sel.masse,self.sel.masse*3/100)
            #
            self.feedback="<p><ul>"
            self.feedback+="<li> \("+str(self.acide.coef)+" \\  "+self.acide.latex+" + "+str(self.base.coef)+" \\  "+self.base.latex+"  \\rightarrow  "+str(self.sel.coef)+" \\  "+self.sel.latex+" + "+" \\  "+str(self.eau.coef)+" \\ H_{2}O \)</li>"
            #    
            self.feedback+="<li> \( n_{%s}=%s[mol] \\ ; \\ V_{%s}=%s[L] \) </li>"%(self.base.latex,self.base.moles,self.base.latex,self.base.volume_litre)
            #    
            self.feedback+="<li> \( n_{%s}=%s[mol] \\ ; \\ M_{%s}=%s[g.mol^{-1}] \\ ; \\ m_{%s}=%s[g] \) </li>"%(self.sel.latex,self.sel.moles,self.sel.latex,self.sel.masse_molaire,self.sel.latex,self.sel.masse)
            self.feedback+="</ul></p>"
        
        
        self.enonce=self.enonce.replace(" de i"," d'i")
        self.enonce=self.enonce.replace(" de a"," d'a")
        self.enonce=self.enonce.replace(" de o"," d'o")
        self.enonce=self.enonce.replace(" de h"," d'h")
        
class Acide3_base(Reaction):
    def __init__(self):
        self.acide=Acide3()
        self.base=Base()
        self.sel=Sel3()
        self.sel.metal=copy(dico_metaux[self.base.metal.nom])
        self.sel.groupement=copy(dico_groupement[self.acide.groupement.nom])
        self.sel.molecule()
        self.acide.coef=self.base.metal.valence
        self.base.coef=self.acide.groupement.valence
        self.sel.coef=1
        self.eau=Eau()
        self.eau.coef=self.base.metal.valence
        
        
        self.acide.coef=1
        self.base.coef=1
        self.sel.coef=1
        self.eau.coef=1
        nb_metal_reac=self.base.metal.indice
        nb_metal_prod=self.sel.metal.indice
        nb_groupement_reac=self.acide.groupement.indice
        nb_groupement_prod=self.sel.groupement.indice
        #
        
        self.acide.coef=self.sel.groupement.indice
        self.sel.coef=self.acide.groupement.indice
        nb_non_metal_reac=self.acide.coef*self.acide.groupement.indice
        nb_non_metal_prod=self.sel.coef*self.sel.groupement.indice
        nb_metal_prod=self.sel.coef*self.sel.metal.indice
        nb_metal_reac=self.base.metal.indice
        
        self.sel.coef*=nb_metal_reac
        self.acide.coef*=nb_metal_reac
        self.base.coef*=nb_metal_prod
        nb_hydroxyle=self.base.indice_hydroxyle*self.base.coef
        
        self.eau.coef=nb_hydroxyle
        
        min_coef=min(self.acide.coef,self.base.coef,self.sel.coef,self.eau.coef)
        pgcd=1
        for i in range(min_coef):
            diviseur_valide=True
            diviseur=i+1
            if self.acide.coef/diviseur!=round(self.acide.coef/diviseur):diviseur_valide=False 
            if self.base.coef/diviseur!=round(self.base.coef/diviseur):diviseur_valide=False
            if self.sel.coef/diviseur!=round(self.sel.coef/diviseur):diviseur_valide=False
            if self.eau.coef/diviseur!=round(self.eau.coef/diviseur):diviseur_valide=False
            if diviseur_valide==True:pgcd=diviseur
        self.acide.coef=int(self.acide.coef/pgcd)
        self.base.coef=int(self.base.coef/pgcd)
        self.sel.coef=int(self.sel.coef/pgcd)
        self.eau.coef=int(self.eau.coef/pgcd)
        
        
        self.reaction=str(self.acide.coef)+self.acide.formule+" + "+str(self.base.coef)+self.base.formule+"=>"+str(self.sel.coef)+self.sel.formule+" + "+str(self.eau.coef)+"H20"
        
    def ponderation(self):
        self.choix=1
        self.liste_corps=[self.acide,self.base,self.sel,self.eau]
        self.schema_ponderation()
        
    def obtention_lect_mol(self):
        self.choix=random.choice([1,2])
        self.liste_corps=[self.acide,self.base,self.sel,self.eau]
        self.schema_obtention()
    
    def stoechiometrie(self):
        self.base.volume=float(random.randint(20,100))/100
        if self.base.volume<0.5:
            self.base.volume_litre=self.base.volume
            self.base.unites_volume="[ml]"
            self.base.volume=self.base.volume_litre*1000
        else :
            self.base.volume_litre=self.base.volume
            self.base.unites_volume="[L]"
        
        self.acide.volume=float(random.randint(20,100))/100
        if self.acide.volume<0.5:
            self.acide.volume_litre=self.acide.volume
            self.acide.unites_volume="[ml]"
            self.acide.volume=self.acide.volume_litre*1000
        else :
            self.acide.volume_litre=self.acide.volume
            self.acide.unites_volume="[L]"
        self.volume_total=self.base.volume_litre+self.acide.volume_litre
        self.unites_volume="[L]"
        #
        self.sel.moles=float(random.randint(10,200))/100
        self.acide.moles=round(self.sel.moles/self.sel.coef*self.acide.coef,4)
        self.base.moles=round(self.sel.moles/self.sel.coef*self.base.coef,4)
        #
        self.sel.masse=round(self.sel.moles*self.sel.masse_molaire,4)
        self.acide.masse=round(self.acide.moles*self.acide.masse_molaire,4)
        self.base.masse=round(self.base.moles*self.base.masse_molaire,4)
        #
        self.sel.cmol=round(self.sel.moles/self.volume_total,4)
        self.acide.cmol=round(self.acide.moles/self.acide.volume_litre,4)
        self.base.cmol=round(self.base.moles/self.base.volume_litre,4)
        #
        choix=random.choice([1,2])
        if choix==1:
            self.enonce="<p>On fait réagir complètement %s %s d'une solution de %s dont la concentration vaut %s [M] avec de l'%s.</p>"%(self.acide.volume,self.acide.unites_volume,self.acide.nom,self.acide.cmol,self.base.nom)
            self.enonce+="<p>Quelle masse de %s faut-il prévoir?</p>"%(self.base.nom)
            self.enonce+="<p>Quelle est la masse de sel obtenue?</p>"
            self.enonce+="<p> \( m_{%s}= \) {1:NUMERICAL:=%s:%s} [g] </p>"%(self.base.latex,self.base.masse,self.base.masse*3/100)
            self.enonce+="<p> \( m_{%s}= \) {1:NUMERICAL:=%s:%s} [g] </p>"%(self.sel.latex,self.sel.masse,self.sel.masse*3/100)
            
            #
            self.feedback="<p><ul> "
            self.feedback+="<li> \("+str(self.acide.coef)+" \\  "+self.acide.latex+" + "+str(self.base.coef)+" \\  "+self.base.latex+"  \\rightarrow  "+str(self.sel.coef)+" \\  "+self.sel.latex+" + "+" \\  "+str(self.eau.coef)+" \\ H_{2}O \)</li>"
            self.feedback+="<li> \( n_{%s}=%s[mol] \\ ; \\ M_{%s}=%s[g.mol^{-1}] \\ ; \\ m_{%s}=%s[g] \)</li>"%(self.base.latex,self.base.moles,self.base.latex,self.base.masse_molaire,self.base.latex,self.base.masse)
            self.feedback+="<li> \( n_{%s}=%s[mol] \\ ; \\ M_{%s}=%s[g.mol^{-1}] \\ ; \\ m_{%s}=%s[g] \)</li>"%(self.sel.latex,self.sel.moles,self.sel.latex,self.sel.masse_molaire,self.sel.latex,self.sel.masse)
            self.feedback+="</ul></p> "
        #
        if choix==2:
            self.enonce="<p>On fait réagir complètement %s %s d'une solution de %s dont la concentration vaut %s [M].</p>"%(self.acide.volume,self.acide.unites_volume,self.acide.nom,self.acide.cmol)
            self.enonce+="<p>Quel volume d'une solution %s [M] de %s faut-il prévoir pour réaliser cette réaction?</p>"%(self.base.cmol,self.base.nom)
            self.enonce+="<p>Quelle est la masse de sel obtenue?</p>"
            self.enonce+="<p> \( V_{%s}= \) {1:NUMERICAL:=%s:%s} [L] </p>"%(self.base.latex,self.base.volume_litre,self.base.volume_litre*3/100)
            self.enonce+="<p> \( m_{%s}= \) {1:NUMERICAL:=%s:%s} [g] </p>"%(self.sel.latex,self.sel.masse,self.sel.masse*3/100)
            #
            self.feedback="<p><ul>"
            self.feedback+="<li> \("+str(self.acide.coef)+" \\  "+self.acide.latex+" + "+str(self.base.coef)+" \\  "+self.base.latex+"  \\rightarrow  "+str(self.sel.coef)+" \\  "+self.sel.latex+" + "+" \\  "+str(self.eau.coef)+" \\ H_{2}O \)</li>"
            #    
            self.feedback+="<li> \( n_{%s}=%s[mol] \\ ; \\ V_{%s}=%s[L] \) </li>"%(self.base.latex,self.base.moles,self.base.latex,self.base.volume_litre)
            #    
            self.feedback+="<li> \( n_{%s}=%s[mol] \\ ; \\ M_{%s}=%s[g.mol^{-1}] \\ ; \\ m_{%s}=%s[g] \) </li>"%(self.sel.latex,self.sel.moles,self.sel.latex,self.sel.masse_molaire,self.sel.latex,self.sel.masse)
            self.feedback+="</ul></p>"
        
        
        self.enonce=self.enonce.replace(" de i"," d'i")
        self.enonce=self.enonce.replace(" de a"," d'a")
        self.enonce=self.enonce.replace(" de o"," d'o")
        self.enonce=self.enonce.replace(" de h"," d'h")

class Acide2_oxyde_met(Reaction):
    def __init__(self):
        self.acide=Acide2()
        self.oxyde=Oxyde_met()
        self.sel=Sel2()
        self.sel.metal=copy(dico_metaux[self.oxyde.metal.nom])
        self.sel.non_metal=copy(dico_non_metaux[self.acide.non_metal.nom])
        self.sel.molecule()
        
        self.acide.coef=1
        self.oxyde.coef=1
        self.sel.coef=1
        self.eau=Eau()
        self.eau.coef=1
        nb_metal_reac=self.oxyde.metal.indice
        nb_metal_prod=self.sel.metal.indice
        nb_non_metal_reac=self.acide.non_metal.indice
        nb_non_metal_prod=self.sel.non_metal.indice
        #
        if nb_metal_reac!=nb_metal_prod:
            self.sel.coef=self.sel.coef*nb_metal_reac
            self.oxyde.coef=self.oxyde.coef*nb_metal_prod
            nb_metal_reac=nb_metal_reac*self.oxyde.coef
            nb_metal_prod=nb_metal_prod*self.sel.coef
            nb_non_metal_prod=nb_non_metal_prod*self.sel.coef
        #   
        if nb_non_metal_reac!=nb_non_metal_prod:
            self.sel.coef=self.sel.coef*nb_non_metal_reac
            self.acide.coef=self.acide.coef*nb_non_metal_prod
            self.oxyde.coef=self.oxyde.coef*nb_non_metal_reac
            
            nb_non_metal_reac=self.acide.non_metal.indice*self.acide.coef
            nb_non_metal_prod=self.sel.non_metal.indice*self.sel.coef
            nb_metal_prod=self.sel.metal.indice*self.sel.coef
            nb_metal_reac=self.oxyde.metal.indice*self.oxyde.coef
        nb_oxygene_reac=self.oxyde.indice_oxygene*self.oxyde.coef
        self.eau.coef=nb_oxygene_reac
        #
        
        min_coef=min(self.acide.coef,self.oxyde.coef,self.sel.coef,self.eau.coef)
        pgcd=1
        for i in range(min_coef):
            diviseur_valide=True
            diviseur=i+1
            if self.acide.coef/diviseur!=round(self.acide.coef/diviseur):diviseur_valide=False 
            if self.oxyde.coef/diviseur!=round(self.oxyde.coef/diviseur):diviseur_valide=False
            if self.sel.coef/diviseur!=round(self.sel.coef/diviseur):diviseur_valide=False
            if self.eau.coef/diviseur!=round(self.eau.coef/diviseur):diviseur_valide=False
            if diviseur_valide==True:pgcd=diviseur
        self.acide.coef=int(self.acide.coef/pgcd)
        self.oxyde.coef=int(self.oxyde.coef/pgcd)
        self.sel.coef=int(self.sel.coef/pgcd)
        self.eau.coef=int(self.eau.coef/pgcd)
        self.reaction=str(self.acide.coef)+self.acide.formule+" + "+str(self.oxyde.coef)+self.oxyde.formule+" => "+str(self.sel.coef)+self.sel.formule+" + "+str(self.eau.coef)+"H20"
        print (self.reaction)
    
    def ponderation(self):
        self.choix=1
        self.liste_corps=[self.acide,self.oxyde,self.sel,self.eau]
        self.schema_ponderation()
     
    def obtention_lect_mol(self):
        self.choix=random.choice([1,2])
        self.liste_corps=[self.acide,self.oxyde,self.sel,self.eau]
        self.schema_obtention()
            
            
class Acide3_oxyde_met(Reaction):
    def __init__(self):
        self.acide=Acide3()
        self.oxyde=Oxyde_met()
        self.sel=Sel3()
        self.eau=Eau()
        self.sel.metal=copy(dico_metaux[self.oxyde.metal.nom])
        self.sel.groupement=copy(dico_groupement[self.acide.groupement.nom])
        self.sel.molecule()
        
        self.acide.coef=1
        self.oxyde.coef=1
        self.sel.coef=1
        
        self.eau.coef=1
        nb_metal_reac=self.oxyde.metal.indice
        nb_metal_prod=self.sel.metal.indice
        nb_gpmt_reac=self.acide.groupement.indice
        nb_gpmt_prod=self.sel.groupement.indice
        
        if nb_metal_reac!=nb_metal_prod:
            self.sel.coef=self.sel.coef*nb_metal_reac
            self.oxyde.coef=self.oxyde.coef*nb_metal_prod
            nb_metal_reac=nb_metal_reac*self.oxyde.coef
            nb_metal_prod=nb_metal_prod*self.sel.coef
            nb_gpmt_prod=nb_gpmt_prod*self.sel.coef
        #   
        if nb_gpmt_reac!=nb_gpmt_prod:
            self.sel.coef=self.sel.coef*nb_gpmt_reac
            self.acide.coef=self.acide.coef*nb_gpmt_prod
            self.oxyde.coef=self.oxyde.coef*nb_gpmt_reac
            
            nb_gpmt_reac=self.acide.groupement.indice*self.acide.coef
            nb_gpmt_prod=self.sel.groupement.indice*self.sel.coef
            nb_metal_prod=self.sel.metal.indice*self.sel.coef
            nb_metal_reac=self.oxyde.metal.indice*self.oxyde.coef
        nb_oxygene_reac=self.oxyde.indice_oxygene*self.oxyde.coef
        self.eau.coef=nb_oxygene_reac
        #
        
        min_coef=min(self.acide.coef,self.oxyde.coef,self.sel.coef,self.eau.coef)
        pgcd=1
        for i in range(min_coef):
            diviseur_valide=True
            diviseur=i+1
            if self.acide.coef/diviseur!=round(self.acide.coef/diviseur):diviseur_valide=False 
            if self.oxyde.coef/diviseur!=round(self.oxyde.coef/diviseur):diviseur_valide=False
            if self.sel.coef/diviseur!=round(self.sel.coef/diviseur):diviseur_valide=False
            if self.eau.coef/diviseur!=round(self.eau.coef/diviseur):diviseur_valide=False
            if diviseur_valide==True:pgcd=diviseur
        self.acide.coef=int(self.acide.coef/pgcd)
        self.oxyde.coef=int(self.oxyde.coef/pgcd)
        self.sel.coef=int(self.sel.coef/pgcd)
        self.eau.coef=int(self.eau.coef/pgcd)
        
        self.reaction=str(self.acide.coef)+self.acide.formule+" + "+str(self.oxyde.coef)+self.oxyde.formule+" => "+str(self.sel.coef)+self.sel.formule+" + "+str(self.eau.coef)+"H20"
        print (self.reaction)
        
    def ponderation(self):
        self.choix=1
        self.liste_corps=[self.acide,self.oxyde,self.sel,self.eau]
        self.schema_ponderation()
        
    def obtention_lect_mol(self):
        self.choix=random.choice([1,2])
        self.liste_corps=[self.acide,self.oxyde,self.sel,self.eau]
        self.schema_obtention()

class Acide2_metal(Reaction):
    def __init__(self):
        self.acide=Acide2()
        self.metal=dico_metaux[random.choice(liste_metaux)]
        self.sel=Sel2()
        self.hydrogene=Hydrogene()
        self.sel.metal=copy(dico_metaux[self.metal.nom])
        self.sel.non_metal=copy(dico_non_metaux[self.acide.non_metal.nom])
        self.sel.molecule()
        
        self.acide.coef=1
        self.metal.coef=1
        self.sel.coef=1
        self.hydrogene.coef=1
        nb_metal_reac=1
        nb_metal_prod=self.sel.metal.indice
        nb_non_metal_reac=self.acide.non_metal.indice
        nb_non_metal_prod=self.sel.non_metal.indice
        
        if nb_metal_reac!=nb_metal_prod:
            self.metal.coef=self.metal.coef*nb_metal_prod
            nb_metal_reac=nb_metal_reac*self.metal.coef
            #nb_non_metal_prod=nb_non_metal_prod*self.sel.coef
        #
        if nb_non_metal_reac!=nb_non_metal_prod:
            self.sel.coef=self.sel.coef*nb_non_metal_reac
            self.acide.coef=self.acide.coef*nb_non_metal_prod
            self.metal.coef=self.metal.coef*nb_non_metal_reac
            
            nb_non_metal_reac=self.acide.non_metal.indice*self.acide.coef
            nb_non_metal_prod=self.sel.non_metal.indice*self.sel.coef
            nb_metal_prod=self.sel.metal.indice*self.sel.coef
            nb_metal_reac=self.metal.coef
        nb_hydrogene_reac=self.acide.indice_hydrogene*self.acide.coef
        self.hydrogene.coef=nb_hydrogene_reac/2
        #
        if round(self.hydrogene.coef)!=self.hydrogene.coef:
            self.hydrogene.coef=self.hydrogene.coef*2
            self.sel.coef=self.sel.coef*2
            self.acide.coef=self.acide.coef*2
            self.metal.coef=self.metal.coef*2
        
        pgcd=1
        self.acide.coef=int(self.acide.coef/pgcd)
        self.metal.coef=int(self.metal.coef/pgcd)
        self.sel.coef=int(self.sel.coef/pgcd)
        self.hydrogene.coef=int(self.hydrogene.coef/pgcd)
        min_coef=min(self.acide.coef,self.metal.coef,self.sel.coef,self.hydrogene.coef)
        
        for i in range(min_coef):
            diviseur_valide=True
            diviseur=i+1
            if self.acide.coef/diviseur!=round(self.acide.coef/diviseur):diviseur_valide=False 
            if self.metal.coef/diviseur!=round(self.metal.coef/diviseur):diviseur_valide=False
            if self.sel.coef/diviseur!=round(self.sel.coef/diviseur):diviseur_valide=False
            if self.hydrogene.coef/diviseur!=round(self.hydrogene.coef/diviseur):diviseur_valide=False
            if diviseur_valide==True:pgcd=diviseur
        self.acide.coef=int(self.acide.coef/pgcd)
        self.metal.coef=int(self.metal.coef/pgcd)
        self.sel.coef=int(self.sel.coef/pgcd)
        self.hydrogene.coef=int(self.hydrogene.coef/pgcd)
        
        self.reaction=str(self.acide.coef)+self.acide.formule+" + "+str(self.metal.coef)+self.metal.symbole+" => "+str(self.sel.coef)+self.sel.formule+" + "+str(self.hydrogene.coef)+"H2"
        print (self.reaction)
    
    def ponderation(self):
        self.choix=1
        self.liste_corps=[self.acide,self.metal,self.sel,self.hydrogene]
        self.schema_ponderation()
        
    def obtention_lect_mol(self):
        self.choix=random.choice([1,2,3])
        self.liste_corps=[self.acide,self.metal,self.sel,self.hydrogene]
        self.schema_obtention()

class Acide3_metal(Reaction):
    def __init__(self):
        self.acide=Acide3()
        self.metal=dico_metaux[random.choice(liste_metaux)]
        self.sel=Sel3()
        self.hydrogene=Hydrogene()
        self.sel.metal=copy(dico_metaux[self.metal.nom])
        self.sel.groupement=copy(dico_groupement[self.acide.groupement.nom])
        self.sel.molecule()
        
        self.acide.coef=1
        self.metal.coef=1
        self.sel.coef=1
        self.hydrogene.coef=1
        nb_metal_reac=1
        nb_metal_prod=self.sel.metal.indice
        nb_groupement_reac=self.acide.groupement.indice
        nb_groupement_prod=self.sel.groupement.indice
        
        if nb_metal_reac!=nb_metal_prod:
            self.metal.coef=self.metal.coef*nb_metal_prod
            nb_metal_reac=nb_metal_reac*self.metal.coef
            #nb_non_metal_prod=nb_non_metal_prod*self.sel.coef
        #
        if nb_groupement_reac!=nb_groupement_prod:
            self.sel.coef=self.sel.coef*nb_groupement_reac
            self.acide.coef=self.acide.coef*nb_groupement_prod
            self.metal.coef=self.metal.coef*nb_groupement_reac
            
            nb_groupement_reac=self.acide.groupement.indice*self.acide.coef
            nb_groupement_prod=self.sel.groupement.indice*self.sel.coef
            nb_metal_prod=self.sel.metal.indice*self.sel.coef
            nb_metal_reac=self.metal.coef
        nb_hydrogene_reac=self.acide.indice_hydrogene*self.acide.coef
        self.hydrogene.coef=nb_hydrogene_reac/2
        #
        if round(self.hydrogene.coef)!=self.hydrogene.coef:
            self.hydrogene.coef=self.hydrogene.coef*2
            self.sel.coef=self.sel.coef*2
            self.acide.coef=self.acide.coef*2
            self.metal.coef=self.metal.coef*2
        
        pgcd=1
        self.acide.coef=int(self.acide.coef/pgcd)
        self.metal.coef=int(self.metal.coef/pgcd)
        self.sel.coef=int(self.sel.coef/pgcd)
        self.hydrogene.coef=int(self.hydrogene.coef/pgcd)
        min_coef=min(self.acide.coef,self.metal.coef,self.sel.coef,self.hydrogene.coef)
        
        for i in range(min_coef):
            diviseur_valide=True
            diviseur=i+1
            if self.acide.coef/diviseur!=round(self.acide.coef/diviseur):diviseur_valide=False 
            if self.metal.coef/diviseur!=round(self.metal.coef/diviseur):diviseur_valide=False
            if self.sel.coef/diviseur!=round(self.sel.coef/diviseur):diviseur_valide=False
            if self.hydrogene.coef/diviseur!=round(self.hydrogene.coef/diviseur):diviseur_valide=False
            #
            if diviseur_valide==True:pgcd=diviseur
        self.acide.coef=int(self.acide.coef/pgcd)
        self.metal.coef=int(self.metal.coef/pgcd)
        self.sel.coef=int(self.sel.coef/pgcd)
        self.hydrogene.coef=int(self.hydrogene.coef/pgcd)
        
        self.reaction=str(self.acide.coef)+self.acide.formule+" + "+str(self.metal.coef)+self.metal.symbole+" => "+str(self.sel.coef)+self.sel.formule+" + "+str(self.hydrogene.coef)+"H2"
        print (self.reaction)
    
    def ponderation(self):
        self.choix=1
        self.liste_corps=[self.acide,self.metal,self.sel,self.hydrogene]
        self.schema_ponderation()
    
    def obtention_lect_mol(self):
        self.choix=random.choice([1,2,3])
        self.liste_corps=[self.acide,self.metal,self.sel,self.hydrogene]
        self.schema_obtention()
    
class Oxyde_met_eau(Reaction):
    def __init__(self):
        self.oxyde=Oxyde_met()
        self.base=Base()
        self.eau=Eau()
        self.base.metal=copy(dico_metaux[self.oxyde.metal.nom])
        self.base.molecule()
        self.oxyde.coef=1
        self.eau.coef=1
        self.base.coef=1
        nb_metal_reac=self.oxyde.metal.indice
        nb_metal_prod=self.base.metal.indice
        nb_oxygene_reac=self.oxyde.indice_oxygene
        nb_oxygene_prod=self.base.indice_hydroxyle
        
        if nb_metal_reac!=nb_metal_prod:
            
            self.base.coef*=nb_metal_reac
            self.oxyde.coef*=nb_metal_prod
            nb_metal_reac=self.oxyde.metal.indice*self.oxyde.coef
            nb_metal_prod=self.base.metal.indice*self.base.coef
            nb_oxygene_reac*=self.oxyde.coef
            nb_oxygene_prod*=self.base.coef
        self.eau.coef=nb_oxygene_prod/2
        
        if round(self.eau.coef)!=self.eau.coef:
            self.oxyde.coef*=2
            self.eau.coef*=2
            self.base.coef*=2
        
        pgcd=1
        self.oxyde.coef=int(self.oxyde.coef)
        self.eau.coef=int(self.eau.coef)
        self.base.coef=int(self.base.coef)
        #self.hydrogene.coef=int(self.hydrogene.coef/pgcd)
        min_coef=min(self.oxyde.coef,self.eau.coef,self.base.coef)
        
        for i in range(min_coef):
            diviseur_valide=True
            diviseur=i+1
            if self.oxyde.coef/diviseur!=round(self.oxyde.coef/diviseur):diviseur_valide=False 
            if self.eau.coef/diviseur!=round(self.eau.coef/diviseur):diviseur_valide=False
            if self.base.coef/diviseur!=round(self.base.coef/diviseur):diviseur_valide=False
            #
            if diviseur_valide==True:pgcd=diviseur
        self.oxyde.coef=int(self.oxyde.coef/pgcd)
        self.eau.coef=int(self.eau.coef/pgcd)
        self.base.coef=int(self.base.coef/pgcd)
        
        self.reaction=str(self.oxyde.coef)+self.oxyde.formule+" + "+str(self.eau.coef)+"H2O"+" => "+str(self.base.coef)+self.base.formule
        print (self.reaction)
    
    def ponderation(self):
        self.choix=2
        self.liste_corps=[self.oxyde,self.eau,self.base]
        self.schema_ponderation()
    
    def obtention_lect_mol(self):
        self.choix=random.choice([4,5])
        self.liste_corps=[self.oxyde,self.eau,self.base]
        self.schema_obtention()
        
        
        
    
class Oxyde_non_met_eau(Reaction):
    def __init__(self):
        self.acide=Acide3()
        self.eau=Eau()
        while self.acide.formule in ["H1NO2","H1NO3","H1ClO2","H1ClO3","H1IO3","H1MnO4"]:
            self.acide=Acide3()
        self.oxyde=Oxyde_non_met()
        if self.acide.groupement.symbole=="ClO4":
            self.oxyde.non_metal.nom="chlore"
            self.oxyde.non_metal.symbole="Cl"
            self.oxyde.non_metal.valence=1
            self.oxyde.non_metal.racine="chlor"
            self.oxyde.non_metal.etage_ox=[7]
        if self.acide.groupement.symbole=="ClO":
            self.oxyde.non_metal.nom="chlore"
            self.oxyde.non_metal.symbole="Cl"
            self.oxyde.non_metal.valence=1
            self.oxyde.non_metal.racine="chlor"
            self.oxyde.non_metal.etage_ox=[1]
        if self.acide.groupement.symbole=="BO3":
            self.oxyde.non_metal.nom="bore"
            self.oxyde.non_metal.symbole="B"
            self.oxyde.non_metal.valence=3
            self.oxyde.non_metal.racine="bor"
            self.oxyde.non_metal.etage_ox=[3]
        if self.acide.groupement.symbole=="SO3":
            self.oxyde.non_metal.nom="soufre"
            self.oxyde.non_metal.symbole="S"
            self.oxyde.non_metal.valence=2
            self.oxyde.non_metal.racine="sulf"
            self.oxyde.non_metal.etage_ox=[4]
        if self.acide.groupement.symbole=="SO4":
            self.oxyde.non_metal.nom="soufre"
            self.oxyde.non_metal.symbole="S"
            self.oxyde.non_metal.valence=2
            self.oxyde.non_metal.racine="sulf"
            self.oxyde.non_metal.etage_ox=[6]
        if self.acide.groupement.symbole=="PO3":
            self.oxyde.non_metal.nom="phosphore"
            self.oxyde.non_metal.symbole="P"
            self.oxyde.non_metal.valence=3
            self.oxyde.non_metal.racine="phosph"
            self.oxyde.non_metal.etage_ox=[3]
        if self.acide.groupement.symbole=="PO4":
            self.oxyde.non_metal.nom="phopshore"
            self.oxyde.non_metal.symbole="P"
            self.oxyde.non_metal.valence=3
            self.oxyde.non_metal.racine="phosp"
            self.oxyde.non_metal.etage_ox=[5]
        if self.acide.groupement.symbole=="CO3":
            self.oxyde.non_metal.nom="carbone"
            self.oxyde.non_metal.symbole="C"
            self.oxyde.non_metal.valence=4
            self.oxyde.non_metal.racine="###"
            self.oxyde.non_metal.etage_ox=[4]
        self.oxyde.molecule()
        
        self.oxyde.coef=1
        self.acide.coef=self.oxyde.non_metal.indice
        nb_hydrogene_prod=self.acide.coef*self.acide.indice_hydrogene
        self.eau.coef=nb_hydrogene_prod/2
        
        if round(self.eau.coef)!=self.eau.coef:
            self.oxyde.coef*=2
            self.eau.coef*=2
            self.acide.coef*=2
        
        self.oxyde.coef=int(self.oxyde.coef)
        self.eau.coef=int(self.eau.coef)
        self.acide.coef=int(self.acide.coef)
        
        pgcd=1
        min_coef=min(self.oxyde.coef,self.eau.coef,self.acide.coef)
        
        for i in range(min_coef):
            diviseur_valide=True
            diviseur=i+1
            if self.oxyde.coef/diviseur!=round(self.oxyde.coef/diviseur):diviseur_valide=False 
            if self.eau.coef/diviseur!=round(self.eau.coef/diviseur):diviseur_valide=False
            if self.acide.coef/diviseur!=round(self.acide.coef/diviseur):diviseur_valide=False
            #
            if diviseur_valide==True:pgcd=diviseur
        self.oxyde.coef=int(self.oxyde.coef/pgcd)
        self.eau.coef=int(self.eau.coef/pgcd)
        self.acide.coef=int(self.acide.coef/pgcd)
        
        self.reaction=str(self.oxyde.coef)+self.oxyde.formule+" + "+str(self.eau.coef)+"H2O"+" => "+str(self.acide.coef)+self.acide.formule
        print (self.reaction)
    
    def ponderation(self):
        self.choix=2
        self.liste_corps=[self.oxyde,self.eau,self.acide]
        self.schema_ponderation()
    
    def obtention_lect_mol(self):
        self.choix=random.choice([4,5])
        self.liste_corps=[self.oxyde,self.eau,self.acide]
        self.schema_obtention()
        
class Metal_oxygene(Reaction):
    def __init__(self):
        self.oxyde=Oxyde_met()
        self.oxygene=Oxygene()
        self.metal=copy(dico_metaux[self.oxyde.metal.nom])
        self.metal.coef=1
        self.oxygene.coef=1
        self.oxyde.coef=1
        nb_oxygene_reac=2
        nb_oxygene_prod=self.oxyde.indice_oxygene
        self.oxygene.coef*=nb_oxygene_prod
        self.oxyde.coef*=2
        #nb_oxygene_reac=2*self.oxygene.coef
        nb_metal_prod=self.oxyde.coef*self.oxyde.metal.indice
        self.metal.coef=nb_metal_prod
        
        pgcd=1
        min_coef=min(self.oxyde.coef,self.oxygene.coef,self.metal.coef)
        
        for i in range(min_coef):
            diviseur_valide=True
            diviseur=i+1
            if self.oxyde.coef/diviseur!=round(self.oxyde.coef/diviseur):diviseur_valide=False 
            if self.oxygene.coef/diviseur!=round(self.oxygene.coef/diviseur):diviseur_valide=False
            if self.metal.coef/diviseur!=round(self.metal.coef/diviseur):diviseur_valide=False
            #
            if diviseur_valide==True:pgcd=diviseur
        self.oxyde.coef=int(self.oxyde.coef/pgcd)
        self.oxygene.coef=int(self.oxygene.coef/pgcd)
        self.metal.coef=int(self.metal.coef/pgcd)
        
        self.reaction=str(self.metal.coef)+self.metal.symbole+" + "+str(self.oxygene.coef)+"O2"+" => "+str(self.oxyde.coef)+self.oxyde.formule
        print (self.reaction)
        
    def ponderation(self):
        self.choix=2
        self.liste_corps=[self.metal,self.oxygene,self.oxyde]
        self.schema_ponderation()
        
    def obtention_lect_mol(self):
        self.choix=random.choice([4,5])
        self.liste_corps=[self.metal,self.oxygene,self.oxyde]
        self.schema_obtention()
        
        

class Non_metal_oxygene(Reaction):
    def __init__(self):
        self.oxygene=Oxygene()
        self.oxyde=Oxyde_non_met()
        while self.oxyde.formule not in ["S1O2","S1O3","P2O5","P2O3","C1O2","Cl1O2"]:
            self.oxyde=Oxyde_non_met()
        
        self.non_metal=copy(dico_non_metaux[self.oxyde.non_metal.nom])
        if self.non_metal.symbole=="Cl":
            self.indice_non_metal=2
        else:
            self.indice_non_metal=1
        self.non_metal.coef=1
        self.oxygene.coef=1
        self.oxyde.coef=1
        nb_oxygene_reac=2
        nb_oxygene_prod=self.oxyde.indice_oxygene
        self.oxygene.coef*=nb_oxygene_prod
        self.oxyde.coef*=2
        #nb_oxygene_reac=2*self.oxygene.coef
        nb_non_metal_prod=self.oxyde.coef*self.oxyde.non_metal.indice
        
        if self.non_metal.symbole=="Cl":
            self.non_metal.coef=nb_non_metal_prod/2
            self.non_metal.nom_utile="dichlore"
        else:
            self.non_metal.coef=nb_non_metal_prod
            self.non_metal.nom_utile=self.non_metal.nom
        
        
        
        if round(self.non_metal.coef)!=self.non_metal.coef:
            self.non_metal.coef=int(self.non_metal.coef*2)
            self.oxygene.coef=int(self.oxygene.coef*2)
            self.oxyde.coef=int(self.oxyde.coef*2)
        else:
            self.non_metal.coef=int(self.non_metal.coef)
            self.oxygene.coef=int(self.oxygene.coef)
            self.oxyde.coef=int(self.oxyde.coef)
        
        pgcd=1
        min_coef=min(self.oxyde.coef,self.oxygene.coef,self.non_metal.coef)
        
        
        for i in range(min_coef):
            diviseur_valide=True
            diviseur=i+1
            if self.oxyde.coef/diviseur!=round(self.oxyde.coef/diviseur):diviseur_valide=False 
            if self.oxygene.coef/diviseur!=round(self.oxygene.coef/diviseur):diviseur_valide=False
            if self.non_metal.coef/diviseur!=round(self.non_metal.coef/diviseur):diviseur_valide=False
            #
            if diviseur_valide==True:pgcd=diviseur
        self.oxyde.coef=int(self.oxyde.coef/pgcd)
        self.oxygene.coef=int(self.oxygene.coef/pgcd)
        self.non_metal.coef=int(self.non_metal.coef/pgcd)
        
        self.reaction=str(self.non_metal.coef)+self.non_metal.symbole+str(self.indice_non_metal)+" + "+str(self.oxygene.coef)+"O2"+" => "+str(self.oxyde.coef)+self.oxyde.formule
        print (self.reaction)
        
    
    def ponderation(self):
        self.choix=2
        self.liste_corps=[self.non_metal,self.oxygene,self.oxyde]
        self.schema_ponderation()
    
    def obtention_lect_mol(self):
        self.choix=random.choice([5])
        self.liste_corps=[self.non_metal,self.oxygene,self.oxyde]
        self.schema_obtention()
        
        
        
    
    
class Non_metal_hydrogene(Reaction):
    def __init__(self):
        self.acide=Acide2()
        self.hydrogene=Hydrogene()
        #H2S,HCl,HF,HBr,HI
        while self.acide.formule not in ["H2S","H1Cl","H1F","H1Br","H1I"]:
            #print (self.acide.formule)
            self.acide=Acide2()
        self.non_metal=copy(dico_non_metaux[self.acide.non_metal.nom])
        if self.non_metal.symbole in ["Cl","I","Br"]:
            self.indice_non_metal=2
        else:
            self.indice_non_metal=1
        
        self.non_metal.coef=1
        self.hydrogene.coef=1
        self.acide.coef=1
        nb_hydrogene_reac=2
        nb_hydrogene_prod=self.acide.indice_hydrogene
        self.hydrogene.coef*=nb_hydrogene_prod
        self.acide.coef*=2
        #nb_oxygene_reac=2*self.oxygene.coef
        nb_non_metal_prod=self.acide.coef*self.acide.non_metal.indice
        
        if self.non_metal.symbole in ["Cl","I","Br"]:
            self.non_metal.coef=nb_non_metal_prod/2
            self.non_metal.nom_utile="di"+self.non_metal.nom
        else:
            self.non_metal.coef=nb_non_metal_prod
            self.non_metal.nom_utile=self.non_metal.nom
        if round(self.non_metal.coef)!=self.non_metal.coef:
            self.non_metal.coef*=2
            self.hydrogene.coef*=2
            self.acide.coef*=2
        
        pgcd=1
        min_coef=min(self.acide.coef,self.hydrogene.coef,self.non_metal.coef)
        
        for i in range(min_coef):
            diviseur_valide=True
            diviseur=i+1
            if self.acide.coef/diviseur!=round(self.acide.coef/diviseur):diviseur_valide=False 
            if self.hydrogene.coef/diviseur!=round(self.hydrogene.coef/diviseur):diviseur_valide=False
            if self.non_metal.coef/diviseur!=round(self.non_metal.coef/diviseur):diviseur_valide=False
            #
            if diviseur_valide==True:pgcd=diviseur
        self.acide.coef=int(self.acide.coef/pgcd)
        self.hydrogene.coef=int(self.hydrogene.coef/pgcd)
        self.non_metal.coef=int(self.non_metal.coef/pgcd)
        
        self.reaction=str(self.non_metal.coef)+self.non_metal.symbole+str(self.indice_non_metal)+" + "+str(self.hydrogene.coef)+"H2"+" => "+str(self.acide.coef)+self.acide.formule
        print (self.reaction)
        
        
    def ponderation(self):
        self.choix=2
        self.liste_corps=[self.non_metal,self.hydrogene,self.acide]
        self.schema_ponderation()
    
    def obtention_lect_mol(self):
        self.choix=random.choice([4,5])
        self.liste_corps=[self.non_metal,self.hydrogene,self.acide]
        self.schema_obtention()
        
#non_metal+H2

class Fonction_chimique():
    def __init__(self):
        questionnaire=[]
        liste_nom=[]
        liste_fonction=["Métal","Sel binaire","Acide binaire","Oxyde métallique","Base","Oxyde non-métallique","Sel ternaire","Acide ternaire"]
        while len(liste_nom)<100:
            choix=random.choice([1,2,3,4,5,6,7])
            if choix==1 : exercice=Sel2()
            if choix==2 : exercice=Acide2()
            if choix==3 : exercice=Oxyde_met()
            if choix==4 : exercice=Base()
            if choix==5 : exercice=Oxyde_non_met()
            if choix==6 : exercice=Sel3()
            if choix==7 : exercice=Acide3()
            if exercice.nom not in liste_nom:
                questionnaire.append(exercice)
                liste_nom.append(exercice.nom)
        f = open('./exe_groupement.xml','w')
        
        f.write('<?xml version="1.0" encoding="UTF-8"?> \n')
        f.write('<quiz>  \n')
        f.write('<question type="category">  \n')
        f.write('<category>  \n')
        f.write('<text>$course$/Défaut pour sciences 3h - 4GT/Fonctions chimiques</text>  \n')
        f.write('</category>  \n')
        f.write('</question>  \n')
        for question in questionnaire:
            liste_fonction=["Métal","Sel binaire","Acide binaire","Oxyde métallique","Base","Oxyde non-métallique","Sel ternaire","Acide ternaire"]
            f.write('<question type="multichoice">  \n')
            f.write('<name>  \n')
            f.write('<text>Fonction chimique</text>  \n')
            f.write('</name>  \n')
            f.write('<questiontext format="html">  \n')
            f.write('<text><![CDATA[<p>Détermine la fonction chimique du corps suivant : </p><p>$$ %s $$</p>]]></text>  \n'% question.latex)
            f.write('</questiontext>  \n')
            f.write('<generalfeedback format="html">  \n')
            f.write('<text></text>  \n')
            f.write('</generalfeedback>  \n')
            f.write('<defaultgrade>1.0000000</defaultgrade>  \n')
            f.write('<penalty>0.3333333</penalty>  \n')
            f.write('<hidden>0</hidden>  \n')
            f.write('<single>true</single>   \n')
            f.write('<shuffleanswers>true</shuffleanswers>  \n')
            f.write('<answernumbering>abc</answernumbering>  \n')
            f.write('<correctfeedback format="html">  \n')
            f.write('<text>Votre réponse est correcte.</text>  \n')
            f.write('</correctfeedback>  \n')
            f.write('<incorrectfeedback format="html">  \n')
            f.write('<text>Votre réponse est incorrecte.</text>  \n')
            f.write('</incorrectfeedback>  \n')
            f.write('<shownumcorrect/>  \n')
            f.write('<answer fraction="100" format="html">  \n')
            f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.famille)
            liste_fonction.remove(question.famille)
            #if question.famille not in liste_fonction : print (question.famille, 'pas dans liste')
            #print (question.famille)
            f.write('<feedback format="html">  \n')
            f.write('<text></text>  \n')
            f.write('</feedback>  \n')
            f.write('</answer>  \n')
            for fonction in liste_fonction:
                f.write('<answer fraction="0" format="html">  \n')
                f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%fonction)
                f.write('<feedback format="html">  \n')
                f.write('<text></text>  \n')
                f.write('</feedback>  \n')
                f.write('</answer>  \n')
            f.write('</question>  \n')
        f.write('</quiz>\n')
        f.close()

class Nomenclature():
    def __init__(self):
        questionnaire=[]
        liste_nom=[]
        while len(liste_nom)<100:
            choix=random.choice([1,2,3,4,5,6,7])
            if choix==1 : exercice=Sel2()
            if choix==2 : exercice=Acide2()
            if choix==3 : exercice=Oxyde_met()
            if choix==4 : exercice=Base()
            if choix==5 : exercice=Oxyde_non_met()
            if choix==6 : exercice=Sel3()
            if choix==7 : exercice=Acide3()
            if exercice.nom not in liste_nom:
                exercice.formule=exercice.formule.replace("1","")
                questionnaire.append(exercice)
                liste_nom.append(exercice.nom)
        f = open('./exe_nomenclature_F_N.xml','w')
        
        f.write('<?xml version="1.0" encoding="UTF-8"?> \n')
        f.write('<quiz>  \n')
        f.write('<question type="category">  \n')
        f.write('<category>  \n')
        f.write('<text>$course$/Défaut pour sciences 3h - 4GT/Nomenclature F=>N </text>  \n')
        f.write('</category>  \n')
        f.write('</question>  \n')
        for question in questionnaire:
             print (question.formule)
             f.write('<question type="shortanswer">  \n')
             f.write('<name>  \n')
             f.write('<text>Nomenclature</text>  \n')
             f.write('</name>  \n')
             f.write('<questiontext format="html">  \n')
             f.write('<text><![CDATA[<p>Donne le nom du corps suivant :</p><p>$$ %s $$</p>]]></text>  \n' %question.latex)
             f.write('</questiontext>  \n')
             f.write('<generalfeedback format="html">  \n')
             f.write('<text></text>  \n')
             f.write('</generalfeedback>  \n')
             f.write('<defaultgrade>1.0000000</defaultgrade>  \n')
             f.write('<penalty>0.3333333</penalty>  \n')
             f.write('<hidden>0</hidden>  \n')
             f.write('<usecase>0</usecase>  \n')
             f.write('<answer fraction="100" format="moodle_auto_format">  \n')
             f.write('<text>%s</text>  \n'%question.nom)
             f.write('<feedback format="html">  \n')
             f.write('<text><![CDATA[<p>Bravo !</p>]]></text>  \n')
             f.write('</feedback>  \n')
             f.write('</answer>  \n')
             f.write('<hint format="html">  \n')
             f.write('<text><![CDATA[<p>Fonction chimique : %s</p>]]></text>  \n'%question.famille)
             f.write('</hint>  \n')
             f.write('</question>  \n')
             
             #f.write('<question type="shortanswer">  \n')
             #f.write('<name>  \n')
             #f.write('<text>Nomenclature</text>  \n')
             #f.write('</name>  \n')
             #f.write('<questiontext format="html">  \n')
             #f.write('<text><![CDATA[<p>Donne la formule du corps suivant :</p><p>%s</p>]]></text>  \n' %question.nom)
             #f.write('</questiontext>  \n')
             #f.write('<generalfeedback format="html">  \n')
             #f.write('<text></text>  \n')
             #f.write('</generalfeedback>  \n')
             #f.write('<defaultgrade>1.0000000</defaultgrade>  \n')
             #f.write('<penalty>0.3333333</penalty>  \n')
             #f.write('<hidden>0</hidden>  \n')
             #f.write('<usecase>1</usecase>  \n')
             #f.write('<answer fraction="100" format="moodle_auto_format">  \n')
             #f.write('<text>%s</text>  \n'%question.formule)
             #f.write('<feedback format="html">  \n')
             #f.write('<text></text>  \n')
             #f.write('</feedback>  \n')
             #f.write('</answer>  \n')
             #f.write('<hint format="html">  \n')
             #f.write('<text><![CDATA[<p>Fonction chimique : %s</p>]]></text>  \n' %question.fonction)
             #f.write('</hint>  \n')
             #f.write('</question>  \n')

        f.write('</quiz>')
        f.close()

class Ponderation():
    def __init__(self):
        questionnaire=[]
        liste_nom=[]
        while len(liste_nom)<100:
            
            choix=random.choice([1,2,3,4,5,6,7,9,10,11])
            if choix==1 : exercice=Acide2_base()
            if choix==2 : exercice=Acide3_base()
            if choix==3 : exercice=Acide2_oxyde_met()
            if choix==4 : exercice=Acide3_oxyde_met()
            if choix==5 : exercice=Acide2_metal()
            if choix==6 : exercice=Acide3_metal()
            if choix==7 : exercice=Oxyde_met_eau()
            if choix==8 : exercice=Oxyde_non_met_eau()
            if choix==9 : exercice=Metal_oxygene()
            if choix==10 : exercice=Non_metal_oxygene()
            if choix==11 : exercice=Non_metal_hydrogene()
            
            if exercice.reaction not in liste_nom:
                exercice.ponderation()
                questionnaire.append(exercice)
                liste_nom.append(exercice.reaction)
        
        f = open('./exe_ponderation.xml','w')
        f.write('<?xml version="1.0" encoding="UTF-8"?> \n')
        f.write("<quiz> \n")
        f.write('<question type="category"> \n')
        f.write("<category> \n")
        f.write("<text>$course$/Défaut pour Sciences 3h - 4GT/Pondération</text> \n")
        f.write("</category> \n")
        f.write("</question> \n")
        for question in questionnaire:
             
            f.write('<question type="cloze"> \n')
            f.write("<name> \n")
            f.write("<text>Pondération</text> \n")
            f.write("</name> \n")
            f.write('<questiontext format="html"> \n')
            f.write("<text><![CDATA[ %s ]]></text>  \n" %question.enonce)
            f.write("</questiontext>  \n")
            f.write('<generalfeedback format="html">  \n')
            f.write("<text> %s </text>  \n" %question.reponse)
            f.write("</generalfeedback>  \n")
            f.write("<penalty>0.3333333</penalty>  \n")
            f.write("<hidden>0</hidden>  \n")
            f.write("</question>  \n")
        f.write('</quiz>')
        f.close()
        
class Obtention():
    def __init__(self):
        questionnaire=[]
        liste_nom=[]
        while len(liste_nom)<100:
            
            choix=random.choice([1,2,3,4,5,6,7,9,10,11])
            if choix==1 : exercice=Acide2_base()
            if choix==2 : exercice=Acide3_base()
            if choix==3 : exercice=Acide2_oxyde_met()
            if choix==4 : exercice=Acide3_oxyde_met()
            if choix==5 : exercice=Acide2_metal()
            if choix==6 : exercice=Acide3_metal()
            if choix==7 : exercice=Oxyde_met_eau()
            if choix==8 : exercice=Oxyde_non_met_eau()
            if choix==9 : exercice=Metal_oxygene()
            if choix==10 : exercice=Non_metal_oxygene()
            if choix==11 : exercice=Non_metal_hydrogene()
            
            if exercice.reaction not in liste_nom:
                exercice.obtention_lect_mol()
                questionnaire.append(exercice)
                liste_nom.append(exercice.reaction)
        
        f = open('./exe_obtention.xml','w')
        f.write('<?xml version="1.0" encoding="UTF-8"?> \n')
        f.write("<quiz> \n")
        f.write('<question type="category"> \n')
        f.write("<category> \n")
        f.write("<text>$course$/Défaut pour Sciences 3h - 4GT/Obtention</text> \n")
        f.write("</category> \n")
        f.write("</question> \n")
        for question in questionnaire:
             
            f.write('<question type="cloze"> \n')
            f.write("<name> \n")
            f.write("<text>Réaction d'obtention</text> \n")
            f.write("</name> \n")
            f.write('<questiontext format="html"> \n')
            f.write("<text><![CDATA[ %s ]]></text>  \n" %question.enonce)
            f.write("</questiontext>  \n")
            f.write('<generalfeedback format="html">  \n')
            f.write("<text> %s </text>  \n" %question.reponse)
            f.write("</generalfeedback>  \n")
            f.write("<penalty>0.3333333</penalty>  \n")
            f.write("<hidden>0</hidden>  \n")
            f.write("</question>  \n")
        f.write('</quiz>')
        f.close()


class Mole_masse_molaire():
    def __init__(self):
        questionnaire=[]
        liste_nom=[]
        while len(liste_nom)<100:
            choix=random.choice([1,2,3,4,5,6,7])
            if choix==1 : exercice=Sel2()
            if choix==2 : exercice=Acide2()
            if choix==3 : exercice=Oxyde_met()
            if choix==4 : exercice=Base()
            if choix==5 : exercice=Oxyde_non_met()
            if choix==6 : exercice=Sel3()
            if choix==7 : exercice=Acide3()
            if exercice.nom not in liste_nom:
                exercice.moles=(float(random.randint(1,50)))/10
                exercice.masse=round(exercice.moles*exercice.masse_molaire,2)
                
                choix=random.choice([1,2])
                if choix==1:
                    exercice.enonce="Quelle est la masse de %s mole(s) de %s ?" %(exercice.moles,exercice.nom)
                    exercice.reponse=exercice.masse
                    exercice.feedback="$$ m_{%s} = %s [g] $$" %(exercice.latex,exercice.masse)
                if choix==2:
                    exercice.enonce="Combien de moles y'a-t-il dans %s [g] de %s ?" %(exercice.masse,exercice.nom)
                    exercice.reponse=exercice.moles
                    exercice.feedback="$$ n_{%s} = %s [mol] $$"%(exercice.latex,exercice.moles)
                
                exercice.enonce=exercice.enonce.replace(" de i"," d'i")
                exercice.enonce=exercice.enonce.replace(" de a"," d'a")
                exercice.enonce=exercice.enonce.replace(" de o"," d'o")
                exercice.enonce=exercice.enonce.replace(" de h"," d'h")
                questionnaire.append(exercice)
                liste_nom.append(exercice.nom)
        
        f = open('./exe_mole_masse_molaire.xml','w')
     
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<quiz>\n')
        #f.write('<!-- question: 0  -->\n')
        f.write('<question type="category">\n')
        f.write('<category>\n')
        f.write('<text>Défaut pour Sciences 3h - 4GT/Masse molaire</text>\n')
        f.write('</category>\n')
        f.write('</question>\n')
        for question in questionnaire:
        #f.write('<!-- question: %s  -->\n'%i)
            f.write('<question type="numerical">\n')
            f.write('<name>\n')
            f.write('<text>Masse molaire</text>\n')
            f.write('</name>\n')
            f.write('<questiontext format="html">\n')
            f.write('<text><![CDATA[<p>%s</p>]]></text>\n' %question.enonce)
            f.write('</questiontext>\n')
            f.write('<generalfeedback format="html">\n')
            f.write('<text>%s</text>\n'%question.feedback)
            f.write('</generalfeedback>\n')
            f.write('<defaultgrade>1.0000000</defaultgrade>\n')
            f.write('<penalty>0.3333333</penalty>\n')
            f.write('<hidden>0</hidden>\n')
            f.write('<answer fraction="100" format="moodle_auto_format">\n')
            f.write('<text>%s</text>\n'%question.reponse)
            f.write('<feedback format="html">\n')
            f.write('<text></text>\n')
            f.write('</feedback>\n')
            f.write('<tolerance>1</tolerance>\n')
            f.write('</answer>\n')
            f.write('<unitgradingtype>0</unitgradingtype>\n')
            f.write('<unitpenalty>0.1000000</unitpenalty>\n')
            f.write('<showunits>3</showunits>\n')
            f.write('<unitsleft>0</unitsleft>\n')
            f.write('</question>\n')
        f.write('</quiz>\n')
        f.close()

class Concentrations():
    def __init__(self):
        questionnaire=[]
        liste_nom=[]
        while len(liste_nom)<100:
            choix=random.choice([1,2,3,4,5,6,7])
            if choix==1 : exercice=Sel2()
            if choix==2 : exercice=Acide2()
            if choix==3 : exercice=Oxyde_met()
            if choix==4 : exercice=Base()
            if choix==5 : exercice=Oxyde_non_met()
            if choix==6 : exercice=Sel3()
            if choix==7 : exercice=Acide3()
            if exercice.nom not in liste_nom:
                exercice.moles=(float(random.randint(1,50)))/10
                exercice.masse=round(exercice.moles*exercice.masse_molaire,4)
                exercice.volume=(float(random.randint(2,100)))/10
                if exercice.volume<1:
                    exercice.volume_litre=exercice.volume
                    exercice.unites="[ml]"
                    exercice.volume=exercice.volume_litre*1000
                else :
                    exercice.volume_litre=exercice.volume
                    exercice.unites="[L]"
                    #exercice.volume=exercice.volume_litre*100
                exercice.concentration_massique=round(exercice.masse/exercice.volume_litre,4)
                exercice.concentration_molaire=round(exercice.moles/exercice.volume_litre,4)
                
                choix=random.choice([1,2,3,4,5])
                if choix==1:
                    exercice.enonce="Quelle serait la masse de %s contenue dans %s %s d'une solution %s [M] de %s?" %(exercice.nom,exercice.volume,exercice.unites,exercice.concentration_molaire,exercice.nom)
                    exercice.reponse="%s" %(exercice.masse)
                    exercice.feedback="m_{%s} = %s [g]" %(exercice.latex,exercice.masse)
                    exercice.tolerance=round(0.03*exercice.masse,6)
                if choix==2:
                    exercice.enonce="Quelle masse de %s faudrait-il dissoudre dans %s %s d'eau pour préparer une solution dont la concentration molaire serait de %s [\( mol.L^{-1} \)] ?" %(exercice.nom,exercice.volume,exercice.unites,exercice.concentration_molaire)
                    exercice.reponse="%s"%(exercice.masse)
                    exercice.feedback="m_{%s} = %s [g]"%(exercice.latex,exercice.masse)
                    exercice.tolerance=round(0.03*exercice.masse,6)
                if choix==3:
                    exercice.enonce="Dans quel volume d'eau faudrait-il dissoudre %s [g] de %s pour préparer une solution dont la concentration serait de %s [\( mol.L^{-1} \)]? " %(exercice.masse,exercice.nom,exercice.concentration_molaire)
                    exercice.reponse="%s"%(exercice.volume_litre)
                    exercice.feedback="V_{H_{2}O} = %s [L]"%(exercice.volume_litre)
                    exercice.tolerance=round(0.03*exercice.volume_litre,6)
                if choix==4:
                    exercice.enonce="Quelle serait la concentration molaire d'une solution obtenue en mélangeant %s [g] de %s dans %s %s d'eau?" %(exercice.masse,exercice.nom,exercice.volume,exercice.unites)
                    exercice.reponse="%s"%(exercice.concentration_molaire)
                    exercice.feedback="C_{M}=%s [mol.L^{-1}]"%(exercice.concentration_molaire)
                    exercice.tolerance=round(0.03*exercice.concentration_molaire,6)
                if choix==5:
                    exercice.enonce="Quelle serait la concentration massique d'une solution obtenue en mélangeant %s [mol] de %s dans %s %s d'eau?" %(exercice.moles,exercice.nom,exercice.volume,exercice.unites)
                    exercice.reponse="%s"%(exercice.concentration_massique)
                    exercice.feedback="\\gamma = %s [g.L^{-1}]"%(exercice.concentration_massique)
                    exercice.tolerance=round(0.03*exercice.concentration_massique,6)
                
                exercice.enonce=exercice.enonce.replace(" de i"," d'i")
                exercice.enonce=exercice.enonce.replace(" de a"," d'a")
                exercice.enonce=exercice.enonce.replace(" de o"," d'o")
                exercice.enonce=exercice.enonce.replace(" de h"," d'h")
                if exercice.concentration_molaire < 1.5:
                    questionnaire.append(exercice)
                    liste_nom.append(exercice.nom)
        
        f = open('./exe_concentration.xml','w')
     
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<quiz>\n')
        f.write('<question type="category">\n')
        f.write('<category>\n')
        f.write('<text>Défaut pour Sciences 3h - 4GT/Concentration</text>\n')
        f.write('</category>\n')
        f.write('</question>\n')
        for question in questionnaire:
            f.write('<question type="numerical">\n')
            f.write('<name>\n')
            f.write('<text>Concentration</text>\n')
            f.write('</name>\n')
            f.write('<questiontext format="html">\n')
            f.write('<text><![CDATA[<p>%s</p>]]></text>\n' %question.enonce)
            f.write('</questiontext>\n')
            f.write('<generalfeedback format="html">\n')
            f.write('<text>$$ %s $$</text>\n'%question.feedback)
            f.write('</generalfeedback>\n')
            f.write('<defaultgrade>1.0000000</defaultgrade>\n')
            f.write('<penalty>0.3333333</penalty>\n')
            f.write('<hidden>0</hidden>\n')
            f.write('<answer fraction="100" format="moodle_auto_format">\n')
            f.write('<text>%s</text>\n'%question.reponse)
            f.write('<feedback format="html">\n')
            f.write('<text></text>\n')
            f.write('</feedback>\n')
            f.write('<tolerance>%s</tolerance>\n'%question.tolerance)
            f.write('</answer>\n')
            f.write('<unitgradingtype>0</unitgradingtype>\n')
            f.write('<unitpenalty>0.1000000</unitpenalty>\n')
            f.write('<showunits>3</showunits>\n')
            f.write('<unitsleft>0</unitsleft>\n')
            f.write('</question>\n')
        f.write('</quiz>\n')
        f.close()

class Stoechiometrie():
    def __init__(self):
        questionnaire=[]
        liste_nom=[]
        while len(liste_nom)<100:
            
            choix=random.choice([1,2])
            if choix==1 : exercice=Acide2_base()
            if choix==2 : exercice=Acide3_base()
            if choix==3 : exercice=Acide2_oxyde_met()
            if choix==4 : exercice=Acide3_oxyde_met()
            if choix==5 : exercice=Acide2_metal()
            if choix==6 : exercice=Acide3_metal()
            if choix==7 : exercice=Oxyde_met_eau()
            if choix==8 : exercice=Oxyde_non_met_eau()
            if choix==9 : exercice=Metal_oxygene()
            if choix==10 : exercice=Non_metal_oxygene()
            if choix==11 : exercice=Non_metal_hydrogene()
            
            if exercice.reaction not in liste_nom:
                exercice.stoechiometrie()
                questionnaire.append(exercice)
                liste_nom.append(exercice.reaction)
        
        
        
        
        f = open('./exe_stoechio.xml','w')
        #
        f.write('<?xml version="1.0" encoding="UTF-8"?> \n')
        f.write("<quiz> \n")
        f.write('<question type="category"> \n')
        f.write("<category> \n")
        f.write("<text>$course$/Chimie/Stoechiometrie</text> \n")
        f.write("</category> \n")
        f.write("</question> \n")
        for question in questionnaire:
             
            f.write('<question type="cloze"> \n')
            f.write("<name> \n")
            f.write("<text>Stoechiometrie</text> \n")
            f.write("</name> \n")
            f.write('<questiontext format="html"> \n')
            f.write("<text><![CDATA[ %s ]]></text>  \n" %question.enonce)
            f.write("</questiontext>  \n")
            f.write('<generalfeedback format="html">  \n')
            f.write("<text><![CDATA[ %s ]]></text>  \n" %question.feedback)
            f.write("</generalfeedback>  \n")
            f.write("<penalty>0.3333333</penalty>  \n")
            f.write("<hidden>0</hidden>  \n")
            f.write("</question>  \n")
        f.write('</quiz>')
        f.close()


if __name__=="__main__":
     liste_metaux=[]
     liste_non_metaux=[]
     liste_groupement=[]
     dico_metaux={}
     dico_non_metaux={}
     dico_groupement={}
     
     myfile=open('./metaux.txt', "r")
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
     #Nomenclature()
     #Ponderation()
     #Obtention()
     #Mole_masse_molaire()
     #Concentrations()
     Stoechiometrie()
#pondérer les eqn
#pondérer et faire lect_mol
#compléter les eqn, les pondérer et faire lect_mol