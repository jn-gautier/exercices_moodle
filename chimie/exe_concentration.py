#! /usr/bin/python3
# -*- coding: utf-8 -*- 
import random
from copy import deepcopy,copy
import re

def convert_sci(nombre):
     nombre_sci='%.4E' %(nombre)
     nombre_sci=nombre_sci.split('E')
     base=nombre_sci[0]
     exposant=nombre_sci[1]
     
     nombre=float(base)*(10**int(exposant)) #on reformate le nombre pour ne conserver que 4 chifres signicatifs
     
     if (nombre>9999) or (nombre<0.1):
         base=base.replace('.',',')
         
         decimales=base.split(',')[1]
         arrondi=1
         for chiffre in decimales:
             if chiffre!='0':
                 arrondi=0
         if arrondi==1: #s'il n'y a pas de décimales on ne prend que la partie entière afin d'éviter les expressions du type 1,0000
             base=base.split(',')[0]
         #
         nombre_latex=('%s \\times 10^{%s}')%(base,exposant)
         
         
     else:
         nombre=round(nombre,5) #pour éviter le péril des virgules flottantes
         nombre_latex=str(nombre)
         nombre_latex=nombre_latex.replace('.',',')
         
     return (nombre,nombre_latex)




class Molecule():
    def __init__(self):
        self.famille=""
        self.fonction=""
        self.formule=""
        self.latex=""
        self.nom=""
        self.masse_molaire=0
        self.solubilite=0
        self.simple=0
        
    
    
    def gene_valeurs(self):
        self.solubilite,self.solubilite_latex=convert_sci(self.solubilite)
        
        self.cc_massique=0.8*self.solubilite
        self.cc_massique,self.cc_massique_latex=convert_sci(self.cc_massique)
        
        self.cc_molaire=self.cc_massique/self.masse_molaire
        self.cc_molaire,self.cc_molaire_latex=convert_sci(self.cc_molaire)
        
        self.volume_litre=float(random.randint(100,1500))/1000
        if self.volume_litre<0.5:
            self.volume=self.volume_litre*1000
            self.unites_volume="[ml]"
        else :
            self.volume=self.volume_litre
            self.unites_volume="[L]"
        self.volume,self.volume_latex=convert_sci(self.volume)
        self.volume_litre,self.volume_litre_latex=convert_sci(self.volume_litre)
        
        self.masse=self.cc_massique*self.volume_litre
        self.masse,self.masse_latex=convert_sci(self.masse)
        
        self.mole=self.cc_massique*self.volume_litre/self.masse_molaire
        self.mole,self.mole_latex=convert_sci(self.mole)
        
        choix=random.randint(1,10)
        if choix==1 : self.exe_1()
        if choix==2 : self.exe_2()
        if choix==3 : self.exe_3()
        if choix==4 : self.exe_4()
        if choix==5 : self.exe_5()
        if choix==6 : self.exe_6()
        if choix==7 : self.exe_7()
        if choix==8 : self.exe_8()
        if choix==9 : self.exe_9()
        if choix==10 : self.exe_10()
        
        #
    
    def exe_1(self):
        self.type_exe='cloze'
        self.num_exe=1
        if self.simple==0:
            self.text_sup=', \(%s\),'%self.latex
        else:
            self.text_sup=''
        
        self.enonce="<p>Quelle serait la concentration massique et la concentration molaire d'une solution obtenue en dissolvant une masse de \(%s [g]\) de %s%s dans un volume de \(%s %s\) d'eau?</p>"%(self.masse_latex,self.nom,self.text_sup,self.volume_latex,self.unites_volume)
        self.enonce+="<p> \( C_{M}= \) {2:NUMERICAL:=%s:%s} "%(self.cc_molaire,self.cc_molaire*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~[g]~[L]~[g/L]~=[mol/L]}</p>"
        self.enonce+="<p> \( \gamma= \) {2:NUMERICAL:=%s:%s} "%(self.cc_massique,self.cc_massique*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~[g]~[L]~=[g/L]~[mol/L]}</p>"
        
        self.feedback="<p>Données<br/>"
        self.feedback+="Formule : \( %s \)<br/>"%self.latex
        self.feedback+="\(M=%s[g \cdot mol^{-1}] \)<br/>"%self.masse_molaire
        self.feedback+="\(m=%s[g]\) <br/>"%self.masse_latex
        self.feedback+="\(V_{eau}=%s[L]\)</p>"%self.volume_litre_latex
        self.feedback+="\n"
        
        self.feedback+="<p>Inconnues<br/>"
        self.feedback+="\(C_{M} \\ et \\ \gamma \)"
        self.feedback+="</p> \n"
        
        self.feedback+="<p>Équations<br/>"
        self.feedback+="\(n=\\frac{m}{M}\)<br/>"
        self.feedback+="\(C_{M}=\\frac{n}{V_{eau}} \\ et \\ \gamma=\\frac{m}{V}\)</p>"
        self.feedback+="\n"
        
        self.feedback+="<p>Résolution<br/>"
        self.feedback+="\(n=\\frac{m}{M} \\ \\rightarrow \\ n=%s[mol] \)<br/>"%self.mole_latex
        self.feedback+="\(C_{M}=\\frac{n}{V} \\ \\rightarrow \\ C_{M}=%s[mol \cdot L^{-1}] \)<br/>"%self.cc_molaire_latex
        self.feedback+="\(\gamma=\\frac{m}{V} \\ \\rightarrow \\ \gamma=%s[g \cdot L^{-1}] \)</p>"%self.cc_massique_latex
        
        
    
    def exe_2(self):
        """
        Quelle serait la concentration massique et la concentration molaire d'une solution obtenue en dissolvant une quantité de #### [mol] de #### dans un volume de #### [L] d'eau?
        """
        self.type_exe='cloze'
        self.num_exe=2
        if self.simple==0:
            self.text_sup=', \(%s\),'%self.latex
        else:
            self.text_sup=''
        
        self.enonce="<p>Quelle serait la concentration massique et la concentration molaire d'une solution obtenue en dissolvant une quantité de \(%s [mol]\) de %s%s dans un volume de \(%s %s\) d'eau?</p>"%(self.mole_latex,self.nom,self.text_sup,self.volume_latex,self.unites_volume)
        self.enonce+="<p> \( C_{M}= \) {2:NUMERICAL:=%s:%s} "%(self.cc_molaire,self.cc_molaire*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~[g]~[L]~[g/L]~=[mol/L]}</p>"
        self.enonce+="<p> \( \gamma= \) {2:NUMERICAL:=%s:%s} "%(self.cc_massique,self.cc_massique*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~[g]~[L]~=[g/L]~[mol/L]}</p>"
        
        self.feedback="<p>Données<br/>"
        self.feedback+="Formule : \( %s \)<br/>"%self.latex
        self.feedback+="M=%s[\(g \cdot mol^{-1}\)] <br/>"%self.masse_molaire
        self.feedback+="\(n=%s[mol] \)<br/>"%self.mole_latex
        self.feedback+="\(V_{eau}=%s[L]\)</p>"%self.volume_litre_latex
        self.feedback+="\n"
        
        self.feedback+="<p>Inconnues<br/>"
        self.feedback+="\(C_{M} \\ et \\ \gamma \)"
        self.feedback+="</p> \n"
        
        self.feedback+="<p>Équations<br/>"
        self.feedback+="\(n=\\frac{m}{M} \\ \\rightarrow \\ m=n \cdot M \)<br/>"
        self.feedback+="\(C_{M}=\\frac{n}{V_{eau}} \\ et \\ \gamma=\\frac{m}{V}\)</p>"
        self.feedback+="\n"
        
        self.feedback+="<p>Résolution<br/>"
        self.feedback+="\(m=n \cdot M \\ \\rightarrow \\ m=%s[g] \)<br/>"%self.masse_latex
        self.feedback+="\(C_{M}=\\frac{n}{V} \\ \\rightarrow \\ C_{M}=%s[mol \cdot L^{-1}] \)<br/>"%self.cc_molaire_latex
        self.feedback+="\(\gamma=\\frac{m}{V} \\ \\rightarrow \\ \gamma=%s[g \cdot L^{-1}] \)</p>"%self.cc_massique_latex
        
        
    def exe_3(self):
        """
        Dans quel volume d'eau faut-il dissoudre une masse de #### [g] pour préparer une solution dont la concentration molaire est de #### \([mol.L^{-1}]\)?
        """
        self.num_exe=3
        self.type_exe='cloze'
        if self.simple==0:
            self.text_sup=', \(%s\),'%self.latex
        else:
            self.text_sup=''
        
        self.enonce="<p>Dans quel volume d'eau faut-il dissoudre une masse de \(%s [g]\) de %s%s pour préparer une solution dont la concentration molaire est de \(%s [mol.L^{-1}]\)?</p>"%(self.masse_latex,self.nom,self.text_sup,self.cc_molaire_latex)
        self.enonce+="<p>V= {2:NUMERICAL:=%s:%s}  "%(self.volume_litre,self.volume_litre*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~[g]~=[L]~[g/L]~[mol/L]}</p>"
        
        #self.reponse=self.volume_litre
        
        self.feedback="<p>Données<br/>"
        self.feedback+="Formule : \( %s \)<br/>"%self.latex
        self.feedback+="M=%s[\(g \cdot mol^{-1}\)] <br/>"%self.masse_molaire
        self.feedback+="m=%s[g] <br/>"%self.masse_latex
        self.feedback+="\(C_{M}=%s[mol \cdot L^{-1}]\)</p>"%self.cc_molaire_latex
        self.feedback+="\n"
        
        self.feedback+="<p>Inconnue<br/>"
        self.feedback+="\(V_{eau} \)"
        self.feedback+="</p> \n"
        
        self.feedback+="<p>Équations<br/>"
        self.feedback+="\(n=\\frac{m}{M} \)<br/>"
        self.feedback+="\(C_{M}=\\frac{n}{V_{eau}} \\ \\rightarrow \\ V_{eau}=\\frac{n}{C_{M}}\)</p>"
        self.feedback+="\n"
        
        self.feedback+="<p>Résolution<br/>"
        self.feedback+="\(n=\\frac{m}{M} \\ \\rightarrow \\ n=%s[mol] \)<br/>"%self.mole_latex
        self.feedback+="\(V_{eau}=\\frac{n}{C_{M}} \\ \\rightarrow \\ V_{eau}=%s[L]\)</p>"%self.volume_litre_latex 
        
    def exe_4(self):
        """
        Dans quel volume d'eau faut-il dissoudre une masse de #### [g] pour préparer une solution dont la concentration massique est de #### \([g.L^{-1}]\)?
        """
        self.num_exe=4
        self.type_exe='cloze'
        if self.simple==0:
            self.text_sup=', \(%s\),'%self.latex
        else:
            self.text_sup=''
        
        self.enonce="<p>Dans quel volume d'eau faut-il dissoudre une masse de \(%s [g]\) de %s%s pour préparer une solution dont la concentration massique est de \(%s [g.L^{-1}]\)?</p>"%(self.masse_latex,self.nom,self.text_sup,self.cc_massique_latex)
        self.enonce+="<p>V= {2:NUMERICAL:=%s:%s}  "%(self.volume_litre,self.volume_litre*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~[g]~=[L]~[g/L]~[mol/L]}</p>"
        
        self.reponse=self.volume_litre
        
        self.feedback="<p>Données<br/>"
        self.feedback+="Formule : \( %s \)<br/>"%self.latex
        self.feedback+="m=%s[g] <br/>"%self.masse_latex
        self.feedback+="\( \gamma =%s[g \cdot L^{-1}]\)</p>"%self.cc_massique_latex
        self.feedback+="\n"
        
        self.feedback+="<p>Inconnue<br/>"
        self.feedback+="\(V_{eau} \)"
        self.feedback+="</p> \n"
        
        self.feedback+="<p>Équation<br/>"
        self.feedback+="\( \gamma =\\frac{m}{V_{eau}} \\ \\rightarrow \\ V_{eau}=\\frac{m}{ \gamma}\)</p>"
        self.feedback+="\n"
        
        self.feedback+="<p>Résolution<br/>"
        self.feedback+="\(V_{eau}=\\frac{m}{ \gamma} \\ \\rightarrow \\ V_{eau}=%s[L]\)</p>"%self.volume_litre_latex
        
    def exe_5(self):
        """
        Dans quel volume d'eau faut-il dissoudre une quantité de #### [mol] pour préparer une solution dont la concentration molaire est de #### \([mol.L^{-1}]\)?
        """
        self.num_exe=5
        self.type_exe='cloze'
        if self.simple==0:
            self.text_sup=', \(%s\),'%self.latex
        else:
            self.text_sup=''
        
        self.enonce="<p>Dans quel volume d'eau faut-il dissoudre une quantité de \(%s [mol]\) de %s%s pour préparer une solution dont la concentration molaire est de \(%s [mol.L^{-1}]\)?</p>"%(self.mole_latex,self.nom,self.text_sup,self.cc_molaire_latex)
        self.enonce+="<p>V= {2:NUMERICAL:=%s:%s}  "%(self.volume_litre,self.volume_litre*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~[g]~=[L]~[g/L]~[mol/L]}</p>"
        
        self.reponse=self.volume_litre
        
        self.feedback="<p>Données<br/>"
        self.feedback+="Formule : \( %s \)<br/>"%self.latex
        self.feedback+="\(n=%s[mol] \)<br/>"%self.mole_latex
        self.feedback+="\(C_{M}=%s[mol \cdot L^{-1}]\)</p>"%self.cc_molaire_latex
        self.feedback+="\n"
        
        self.feedback+="<p>Inconnue<br/>"
        self.feedback+="\(V_{eau} \)"
        self.feedback+="</p> \n"
        
        self.feedback+="<p>Équation<br/>"
        self.feedback+="\(C_{M}=\\frac{n}{V_{eau}} \\ \\rightarrow \\ V_{eau}=\\frac{n}{C_{M}}\)</p>" 
        self.feedback+="\n"
        
        self.feedback+="<p>Résolution<br/>"
        self.feedback+="\(V_{eau}=\\frac{n}{C_{M}} \\ \\rightarrow \\ V_{eau}=%s[L]\)</p>"%self.volume_litre_latex 
        
    def exe_6(self):
        """
        Dans quel volume d'eau faut-il dissoudre une quantité de #### [mol] pour préparer une solution dont la concentration massique est de #### \([g.L^{-1}]\)?
        """
        self.num_exe=6
        self.type_exe='cloze'
        if self.simple==0:
            self.text_sup=', \(%s\),'%self.latex
        else:
            self.text_sup=''
        
        self.enonce="<p>Dans quel volume d'eau faut-il dissoudre une quantité de \(%s [mol]\) de %s%s pour préparer une solution dont la concentration massique est de \(%s [g.L^{-1}]\)?</p>"%(self.mole_latex,self.nom,self.text_sup,self.cc_massique_latex)
        self.enonce+="<p>V= {2:NUMERICAL:=%s:%s}  "%(self.volume_litre,self.volume_litre*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~[g]~=[L]~[g/L]~[mol/L]}</p>"
        
        self.reponse=self.volume_litre
        
        self.feedback="<p>Données<br/>"
        self.feedback+="Formule : \( %s \)<br/>"%self.latex
        self.feedback+="M=%s[\(g \cdot mol^{-1}\)] <br/>"%self.masse_molaire
        self.feedback+="\(n=%s[mol] \)<br/>"%self.mole_latex
        self.feedback+="\(\gamma=%s[g \cdot L^{-1}]\)</p>"%self.cc_massique_latex
        self.feedback+="\n"
        
        self.feedback+="<p>Équations<br/>"
        self.feedback+="\(n=\\frac{m}{M} \\ \\rightarrow \\ m=n \cdot M\)<br/>"
        self.feedback+="\(\gamma=\\frac{m}{V_{eau}} \\ \\rightarrow \\ V_{eau}=\\frac{m}{\gamma}\)</p>" 
        self.feedback+="\n"
        
        
        self.feedback+="<p>Inconnue<br/>"
        self.feedback+="\(V_{eau} \)"
        self.feedback+="</p> \n"
        
        self.feedback+="<p>Résolution<br/>"
        self.feedback+="\(m=n \cdot M \\ \\rightarrow \\ m=%s[g]\)<br/>"%self.masse_latex
        self.feedback+="\(V_{eau}=\\frac{m}{\gamma} \\ \\rightarrow \\ V_{eau}=%s[L]\)</p>"%self.volume_litre_latex 
    
    def exe_7(self):
        """
        Quelle masse de #### faut-il dissoudre dans un volume de ### [L] d'eau pour préparer une solution dont la concentration massique est de #### \([g.L^{-1}]\)?
        """
        self.num_exe=7
        self.type_exe='cloze'
        if self.simple==0:
            self.text_sup=', \(%s\),'%self.latex
        else:
            self.text_sup=''
        
        self.enonce="<p>Quelle masse de %s%s faut-il utiliser pour préparer \(%s%s\) d'une solution dont la concentration massique est de \(%s [g.L^{-1}]\)?</p>"%(self.nom,self.text_sup,self.volume_latex,self.unites_volume,self.cc_massique_latex)
        self.enonce+="<p>m= {2:NUMERICAL:=%s:%s}  "%(self.masse,self.masse*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~=[g]~[L]~[g/L]~[mol/L]}</p>"
        
        self.reponse=self.masse
        
        self.feedback="<p>Données<br/>"
        self.feedback+="Formule : \( %s \)<br/>"%self.latex
        self.feedback+="\(V_{sol.} =%s[L] \)<br/>"%self.volume_litre_latex
        self.feedback+="\(\gamma=%s[g \cdot L^{-1}]\)</p>"%self.cc_massique_latex
        self.feedback+="\n"
        
        self.feedback+="<p>Inconnue<br/>"
        self.feedback+="\(m_{soluté} \)"
        self.feedback+="</p> \n"
        
        self.feedback+="<p>Équation<br/>"
        self.feedback+="\(\gamma=\\frac{m}{V_{sol.}} \\ \\rightarrow \\ m=\gamma \cdot V_{sol.}\)</p>" 
        self.feedback+="\n"
        
        self.feedback+="<p>Résolution<br/>"
        self.feedback+="\(m=\gamma \cdot V_{sol.} \\ \\rightarrow \\ m=%s[g]\)</p>"%self.masse_latex 
    
    def exe_8(self):
        """
        Quelle masse de #### faut-il dissoudre dans un volume de ### [L] d'eau pour préparer une solution dont la concentration molaire est de #### \([mol.L^{-1}]\)?
        """
        self.num_exe=8
        self.type_exe='cloze'
        if self.simple==0:
            self.text_sup=', \(%s\),'%self.latex
        else:
            self.text_sup=''
        
        self.enonce="<p>Quelle masse de %s%s faut-il utiliser pour préparer \(%s%s\) d'une solution dont la concentration molaire est de \(%s [mol.L^{-1}]\)?</p>"%(self.nom,self.text_sup,self.volume_latex,self.unites_volume,self.cc_molaire_latex)
        self.enonce+="<p>m= {2:NUMERICAL:=%s:%s}  "%(self.masse,self.masse*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~=[g]~[L]~[g/L]~[mol/L]}</p>"
        
        self.reponse=self.masse
        
        self.feedback="<p>Données<br/>"
        self.feedback+="Formule : \( %s \)<br/>"%self.latex
        self.feedback+="M=%s[\(g \cdot mol^{-1}\)] <br/>"%self.masse_molaire
        self.feedback+="\(V_{sol.} =%s[L] \)<br/>"%self.volume_litre_latex
        self.feedback+="\(C_{M} =%s[mol \cdot L^{-1}]\)</p>"%self.cc_molaire_latex
        self.feedback+="\n"
        
        self.feedback+="<p>Inconnue<br/>"
        self.feedback+="\(m_{soluté} \)"
        self.feedback+="</p> \n"
        
        self.feedback+="<p>Équations<br/>"
        self.feedback+="\(n=C_{M} \cdot V_{sol.}\)<br/>"
        self.feedback+="\(n=\\frac{m}{M} \\ \\rightarrow \\ m=n \cdot M\)</p>" 
        self.feedback+="\n"
        
        self.feedback+="<p>Résolution<br/>"
        self.feedback+="\(n=C_{M} \cdot V_{sol.} \\ \\rightarrow \\ n=%s[mol]\)<br/>"%self.mole_latex
        self.feedback+="\(m=n \cdot M \\ \\rightarrow \\ m=%s[g]\)</p>"%self.masse_latex
    
    
    def exe_9(self):
        """
        Combien de moles de #### sont contenues dans un volume de ### [L] d'une solution dont la concentration massique est de #### \([g.L^{-1}]\)?
        """
        self.num_exe=9
        self.type_exe='cloze'
        if self.simple==0:
            self.text_sup=', \(%s\),'%self.latex
        else:
            self.text_sup=''
        
        self.enonce="<p>Combien de moles de %s%s sont contenues dans un volume de \(%s%s\) d'une solution dont la concentration massique est de \(%s [g.L^{-1}]\)?</p>"%(self.nom,self.text_sup,self.volume_latex,self.unites_volume,self.cc_massique_latex)
        self.enonce+="<p>n= {2:NUMERICAL:=%s:%s}  "%(self.mole,self.mole*3/100)
        self.enonce+="{1:MC:[g/mol]~=[mol]~[g]~[L]~[g/L]~[mol/L]}</p>"
        
        self.reponse=self.mole
        
        self.feedback="<p>Données<br/>"
        self.feedback+="Formule : \( %s \)<br/>"%self.latex
        self.feedback+="M=%s[\(g \cdot mol^{-1}\)] <br/>"%self.masse_molaire
        self.feedback+="\(V_{sol.} =%s[L] \)<br/>"%self.volume_litre_latex
        self.feedback+="\(\gamma=%s[g \cdot L^{-1}]\)</p>"%self.cc_massique_latex
        self.feedback+="\n"
        
        self.feedback+="<p>Inconnue<br/>"
        self.feedback+="\(n_{soluté} \)"
        self.feedback+="</p> \n"
        
        self.feedback+="<p>Équation<br/>"
        self.feedback+="\(\gamma=\\frac{m}{V_{sol.}} \\ \\rightarrow \\ m=\gamma \cdot V_{sol.}\)<br/>"
        self.feedback+="\(n=\\frac{m}{M} \)</p>" 
        self.feedback+="\n"
        
        self.feedback+="<p>Résolution<br/>"
        self.feedback+="\(m=\gamma \cdot V_{sol.} \\ \\rightarrow \\ m=%s[g] \)<br/>"%self.masse_latex
        self.feedback+="\(n=\\frac{m}{M}  \\ \\rightarrow \\ n=%s[mol]\)</p>"%self.mole_latex
        
        
    def exe_10(self):
        """
        Combien de moles de #### sont contenues dans un volume de ### [L] d'une solution dont la concentration molaire est de #### \([mol.L^{-1}]\)?
        """
        self.num_exe=10
        self.type_exe='cloze'
        if self.simple==0:
            self.text_sup=', \(%s\),'%self.latex
        else:
            self.text_sup=''
        
        self.enonce="<p>Combien de moles de %s%s sont contenues dans un volume de \(%s%s\) d'une solution dont la concentration molaire est de \(%s [mol.L^{-1}]\)?</p>"%(self.nom,self.text_sup,self.volume_latex,self.unites_volume,self.cc_molaire_latex)
        self.enonce+="<p>n= {2:NUMERICAL:=%s:%s}  "%(self.mole,self.mole*3/100)
        self.enonce+="{1:MC:[g/mol]~=[mol]~[g]~[L]~[g/L]~[mol/L]}</p>"
        
        self.reponse=self.mole
        
        self.feedback="<p>Données<br/>"
        self.feedback+="Formule : \( %s \)<br/>"%self.latex
        self.feedback+="\(V_{sol.} =%s[L] \)<br/>"%self.volume_litre_latex
        self.feedback+="\(C_{M}=%s[mol \cdot L^{-1}]\)</p>"%self.cc_molaire_latex
        self.feedback+="\n"
        
        self.feedback+="<p>Inconnue<br/>"
        self.feedback+="\(n_{soluté} \)"
        self.feedback+="</p> \n"
        
        self.feedback+="<p>Équation<br/>"
        self.feedback+="\(C_{M}=\\frac{n}{V_{sol.}} \\ \\rightarrow \\ n=C_{M} \cdot V_{sol.}\)</p>"
        self.feedback+="\n"
        
        self.feedback+="<p>Résolution<br/>"
        self.feedback+="\(n=C_{M} \cdot V_{sol.} \\ \\rightarrow \\ n=%s[g] \)</p>"%self.mole_latex
        



if __name__=="__main__":
     liste_molecules=[]
     liste_molecules_simples=[]
     questionnaire=[]
     
     myfile=open('./liste_molecules_simples.csv', "r")
     for ligne in myfile:
         liste_infos=ligne.rstrip('\n\r').split('\t')
         liste_molecules_simples.append(liste_infos[2])
         
     
     myfile=open('./liste_molecules.csv', "r")
     for ligne in myfile:
         liste_infos=ligne.rstrip('\n\r').split('\t')
         #print(liste_infos)
         molecule=Molecule()
         molecule.famille=liste_infos[0]
         molecule.fonction=liste_infos[1]
         molecule.formule=liste_infos[2]
         molecule.latex=liste_infos[3]
         molecule.nom=liste_infos[4]
         molecule.masse_molaire=int(liste_infos[5])
         solubilite=liste_infos[6]
         solubilite=solubilite.replace(',','.')
         molecule.solubilite=float(solubilite)
         if molecule.formule in liste_molecules_simples:
             molecule.simple=1
         else:
             molecule.simple=0
         
         molecule.gene_valeurs()
         liste_molecules.append(molecule.nom)
         
         pattern=re.compile(r'(de )([aeiouh])')#on remplace les "de a","de h",... par un d avec une apostrophe
         match=pattern.search(molecule.enonce)
         if match:
            sub="d'"+match.group(2)
            molecule.enonce=re.sub(pattern,sub,molecule.enonce)
         
         
         
         pattern=re.compile(r"(NH_\{4\})(\}_\{\d\}[A-Z])")#j'ajoute les parenthèses autour du groupement NH4 lorsqu'il est suivi d'un indice
         match=pattern.search(molecule.enonce)
         if match:
            sub='('+match.group(1)+')'+match.group(2)
            molecule.enonce=re.sub(pattern,sub,molecule.enonce)
         
         questionnaire.append(molecule)
     
     
         
     
     f = open('./exe_concentration_moodle.xml','w')
    
     f.write('<?xml version="1.0" encoding="UTF-8"?> \n')
     f.write("<quiz> \n")
     f.write('<question type="category"> \n')
     f.write("<category> \n")
     f.write("<text>$course$/Chimie/Concentration</text> \n")
     f.write("</category> \n")
     f.write("</question> \n")
     for question in questionnaire:
        f.write('<question type="cloze"> \n')
        f.write("<name> \n")
        f.write("<text>Concentration massique et molaire</text> \n")
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
