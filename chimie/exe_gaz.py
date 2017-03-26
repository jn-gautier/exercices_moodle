#! /usr/bin/python3
# -*- coding: utf-8 -*- 
import random
import re
import copy

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
        self.formule=""
        self.latex=""
        self.nom=""
        self.solubilite=""
        self.masse_molaire=0
        
        
    
    
    def gene_valeurs(self):
        self.solubilite,self.solubilite_latex=convert_sci(self.solubilite)
        
        facteur=random.choice([0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
        
        self.cc_massique=facteur*self.solubilite
        self.cc_massique,self.cc_massique_latex=convert_sci(self.cc_massique)
        
        self.cc_molaire=self.cc_massique/self.masse_molaire
        self.cc_molaire,self.cc_molaire_latex=convert_sci(self.cc_molaire)
        
        self.volume_sol_litre=float(random.randint(100,1500))/100
        if self.volume_sol_litre<0.5:
            self.volume_sol=self.volume_sol_litre*1000
            self.unites_volume="[ml]"
        else :
            self.volume_sol=self.volume_sol_litre
            self.unites_volume="[L]"
        self.volume_sol,self.volume_sol_latex=convert_sci(self.volume_sol)
        self.volume_sol_litre,self.volume_sol_litre_latex=convert_sci(self.volume_sol_litre)
        
        self.masse=self.cc_massique*self.volume_sol_litre
        self.masse,self.masse_latex=convert_sci(self.masse)
        
        self.mole=self.cc_massique*self.volume_sol_litre/self.masse_molaire
        self.mole,self.mole_latex=convert_sci(self.mole)
        
        self.volume_gaz_litre=self.mole*22.4
        self.volume_gaz_litre,self.volume_gaz_litre_latex=convert_sci(self.volume_gaz_litre)
        
        choix=random.randint(1,5)
        if choix==1 : self.exe_1()
        if choix==2 : self.exe_2()
        if choix==3 : self.exe_3()
        if choix==4 : self.exe_4()
        if choix==5 : self.exe_5()
    #
    def exe_1(self):
        
        self.enonce="<p>On dissous complètement \(%s\) [L] de %s (CNTP) dans \(%s\) %s d'eau.<br/>"%(self.volume_gaz_litre_latex,self.nom,self.volume_sol_latex,self.unites_volume)
        self.enonce+="Quelle sera la concentration massique de la solution obtenue?</p>"
        self.enonce+="<p>\(\gamma \)={2:NUMERICAL:=%s:%s}"%(self.cc_massique,self.cc_massique*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~[g]~[L]~=[g/L]~[mol/L]}</p>"
        
        self.feedback="<p><b>Données</b><br/>"
        self.feedback+="Formule : \( %s \)<br/>"%self.latex
        self.feedback+="\(M=%s[g \cdot mol^{-1}]\)<br/>"%(self.masse_molaire)
        self.feedback+="\(V_{gaz}=%s[L]\) <br/>"%self.volume_gaz_litre_latex
        self.feedback+="\(V_{sol}=%s[L]\) </p>"%self.volume_sol_litre_latex
        self.feedback+="<br/>"
        
        self.feedback+="<p><b>Inconnue</b><br/>"
        self.feedback+="\(\gamma\)=?</p>"
        self.feedback+="<br/>"
        
        self.feedback+="<p><b>Équations</b>s<br/>"
        self.feedback+="\(n=\\frac{V_{gaz}}{22,4}\)<br/>"
        self.feedback+="\(n=\\frac{m}{M} \\ \\rightarrow \\ m=n \cdot M\)<br/>"
        self.feedback+="\(\gamma=\\frac{m}{V_{sol}} \)"
        self.feedback+="</p>"
        self.feedback+="<br/>"
        
        self.feedback+="<p><b>Résolution</b><br/>"
        self.feedback+="\(n=\\frac{V_{gaz}}{22,4} \\ \\rightarrow \\ n=\\frac{%s}{22,4} \\ \\rightarrow \\ n=%s[mol]\)<br/>"%(self.volume_gaz_litre_latex,self.mole_latex)
        self.feedback+="\(m=n \cdot M \\ \\rightarrow \\ m=%s \cdot %s \\ \\rightarrow \\ m=%s [g]\)<br/>"%(self.mole_latex,self.masse_molaire,self.masse_latex)
        self.feedback+="\(\gamma=\\frac{m}{V_{sol}} \\ \\rightarrow \\ \gamma=\\frac{%s}{%s} \\ \\rightarrow \\ \gamma=%s[g/L]\)"%(self.masse_latex,self.volume_sol_latex,self.cc_massique_latex)
        self.feedback+="</p>"
        self.feedback+="<br/>"
        
        self.feedback+="<p><b>Réponse</b><br/>"
        self.feedback+="La concentration massique vaut : \( \gamma=%s[g \cdot L^{-1}]\).</p>"%self.cc_massique_latex
    #
    def exe_2(self):
        
        self.enonce="<p>Quel est le volume occupé par \(%s\) [mol] de %s (CNTP)?</p>"%(self.mole_latex,self.nom)
        self.enonce+="<p>V={2:NUMERICAL:=%s:%s}"%(self.volume_gaz_litre,self.volume_gaz_litre*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~[g]~=[L]~[g/L]~[mol/L]}</p>"
        
        self.feedback="<p><b>Données</b><br/>"
        self.feedback+="Formule : \( %s \)<br/>"%self.latex
        self.feedback+="\(n=%s[mol] \)"%self.mole_latex
        self.feedback+="</p>"
        self.feedback+="<br/>"
        
        self.feedback+="<p><b>Inconnue</b><br/>"
        self.feedback+="\(V_{gaz}\)=?</p>"
        self.feedback+="<br/>"
        
        self.feedback+="<p><b>Équation</b><br/>"
        self.feedback+="\(n=\\frac{V_{gaz}}{22,4} \\ \\rightarrow \\ V=n \cdot 22,4\)"
        self.feedback+="</p>"
        self.feedback+="<br/>"
        
        self.feedback+="<p><b>Résolution</b><br/>"
        self.feedback+="\(V=n \cdot 22,4 \\ \\rightarrow \\ V=%s \cdot 22,4 \\ \\rightarrow \\ V=%s [L]\)"%(self.mole_latex,self.volume_gaz_litre_latex)
        self.feedback+="</p>"
        self.feedback+="<br/>"
        
        self.feedback+="<p><b>Réponse</b><br/>"
        self.feedback+="La volume est de  : \( V_{gaz}=%s[L]\).</p>"%self.volume_gaz_litre_latex
    
    def exe_3(self):
        
        self.enonce="<p>Combien de moles y'a-t-il dans \(%s\) [L] de %s (CNTP)?</p>"%(self.volume_gaz_litre_latex,self.nom)
        self.enonce+="<p>n={2:NUMERICAL:=%s:%s}"%(self.mole,self.mole*3/100)
        self.enonce+="{1:MC:[g/mol]~=[mol]~[g]~[L]~[g/L]~[mol/L]}</p>"
        
        self.feedback="<p><b>Données</b><br/>"
        self.feedback+="Formule : \( %s \)<br/>"%self.latex
        self.feedback+="\(V_{gaz}\)=%s[L] "%self.volume_gaz_litre_latex
        self.feedback+="</p>"
        self.feedback+="<br/>"
        
        self.feedback+="<p><b>Inconnue</b><br/>"
        self.feedback+="n=?</p>"
        self.feedback+="<br/>"
        
        self.feedback+="<p><b>Équation</b><br/>"
        self.feedback+="\(n=\\frac{V_{gaz}}{22,4}\)"
        self.feedback+="</p>"
        self.feedback+="<br/>"
        
        self.feedback+="<p><b>Résolution</b><br/>"
        self.feedback+="\(n=\\frac{V}{22,4}\\ \\rightarrow \\ n=\\frac{%s}{22,4} \\ \\rightarrow \\ n=%s[mol]\)"%(self.volume_gaz_litre_latex,self.mole_latex)
        self.feedback+="</p>"
        self.feedback+="<br/>"
        
        self.feedback+="<p><b>Réponse</b><br/>"
        self.feedback+="Le nombre de moles est de  : \( n=%s[mol]\).</p>"%self.mole_latex
        
    def exe_4(self):
        
        self.enonce="<p>Quelle est la masse de \(%s\) [L] (CNTP) de %s?</p>"%(self.volume_gaz_litre_latex,self.nom)
        self.enonce+="<p>m={2:NUMERICAL:=%s:%s}"%(self.masse,self.masse*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~=[g]~[L]~[g/L]~[mol/L]}</p>"
        
        self.feedback="<p><b>Données</b><br/>"
        self.feedback+="Formule : \( %s \)<br/>"%self.latex
        self.feedback+="\(M=%s[g \cdot mol^{-1}]\)<br/>"%(self.masse_molaire)
        self.feedback+="\(V_{gaz}=%s[L]\) </p>"%self.volume_gaz_litre_latex
        self.feedback+="<br/>"
        
        self.feedback+="<p><b>Inconnue</b><br/>"
        self.feedback+="m=?</p>"
        self.feedback+="<br/>"
        
        self.feedback+="<p><b>Équations</b>s<br/>"
        self.feedback+="\(n=\\frac{V_{gaz}}{22,4}\)<br/>"
        self.feedback+="\(n=\\frac{m}{M} \\ \\rightarrow \\ m=n \cdot M\)</p>"
        self.feedback+="<br/>"
        
        self.feedback+="<p><b>Résolution</b><br/>"
        self.feedback+="\(n=\\frac{V_{gaz}}{22,4} \\ \\rightarrow \\ n=\\frac{%s}{22,4} \\ \\rightarrow \\ n=%s[mol]\)<br/>"%(self.volume_gaz_litre_latex,self.mole_latex)
        self.feedback+="\(m=n \cdot M \\ \\rightarrow \\ m=%s \cdot %s \\ \\rightarrow \\ m=%s [g]\)</p>"%(self.mole_latex,self.masse_molaire,self.masse_latex)
        self.feedback+="<br/>"
        
        self.feedback+="<p><b>Réponse</b><br/>"
        self.feedback+="La masse vaut : \(m=%s[g]\).</p>"%self.masse_latex
        
    def exe_5(self):
        
        self.enonce="<p>Quel est le volume (CNTP) occupé par \(%s\) [g] de %s?</p>"%(self.masse_latex,self.nom)
        self.enonce+="<p>V={2:NUMERICAL:=%s:%s}"%(self.volume_gaz_litre,self.volume_gaz_litre*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~[g]~=[L]~[g/L]~[mol/L]}</p>"
        
        self.feedback="<p><b>Données</b><br/>"
        self.feedback+="Formule : \( %s \)<br/>"%self.latex
        self.feedback+="\(M=%s[g \cdot mol^{-1}]\)<br/>"%(self.masse_molaire)
        self.feedback+="\(m=%s[g] \)</p>"%self.masse_latex
        self.feedback+="<br/>"
        
        self.feedback+="<p><b>Inconnue</b><br/>"
        self.feedback+="\(V_{gaz}\)=?</p>"
        self.feedback+="<br/>"
        
        self.feedback+="<p><b>Équations</b>s<br/>"
        self.feedback+="\(n=\\frac{m}{M}\)<br/>"
        self.feedback+="\(n=\\frac{V_{gaz}}{22,4}  \\ \\rightarrow \\ V_{gaz}=n \cdot 22,4\)</p>"
        self.feedback+="<br/>"
        
        
        self.feedback+="<p><b>Résolution</b><br/>"
        self.feedback+="\(n=\\frac{m}{M} \\ \\rightarrow \\ n=\\frac{%s}{%s} \\ \\rightarrow \\ n=%s[mol]\)<br/>"%(self.masse_latex,self.masse_molaire,self.mole_latex)
        self.feedback+="\(V_{gaz}=n \cdot 22,4 \\ \\rightarrow \\ V_{gaz}=%s \cdot 22,4 \\ \\rightarrow \\ V_{gaz}=%s [L]\)</p>"%(self.mole_latex,self.volume_gaz_litre_latex)
        self.feedback+="<br/>"
        
        self.feedback+="<p><b>Réponse</b><br/>"
        self.feedback+="Le volume vaut : \(V_{gaz}\)=%s[L].</p>"%self.volume_gaz_litre_latex
    #
    
    
    
    

if __name__=="__main__":
     questionnaire=[]
     liste_molec=[]
     
     myfile=open('./liste_gaz.csv', "r")
     for ligne in myfile:
         liste_infos=ligne.rstrip('\n\r').split('\t')
         #print(liste_infos)
         molecule=Molecule()
         
         molecule.formule=liste_infos[0]
         molecule.latex=liste_infos[1]
         molecule.nom=liste_infos[2]
         #print(liste_infos[3])
         molecule.solubilite=float(liste_infos[3])
         molecule.masse_molaire=int(liste_infos[4])
         liste_molec.append(molecule)
     
     pattern=re.compile(r'(de )([aeiouh])')#on remplace les "de a","de h",... par un d avec une apostrophe
     for i in range(50):
         molecule=copy.deepcopy(random.choice(liste_molec))
         molecule.gene_valeurs()
         match=pattern.search(molecule.enonce)
         if match:
            sub="d'"+match.group(2)
            molecule.enonce=re.sub(pattern,sub,molecule.enonce)
         questionnaire.append(molecule)
     
     
         
     
     f = open('./exe_gaz.xml','w')
    
     f.write('<?xml version="1.0" encoding="UTF-8"?> \n')
     f.write("<quiz> \n")
     f.write('<question type="category"> \n')
     f.write("<category> \n")
     f.write("<text>$course$/Chimie/Volume molaire gazeux</text> \n")
     f.write("</category> \n")
     f.write("</question> \n")
     for question in questionnaire:
        f.write('<question type="cloze"> \n')
        f.write("<name> \n")
        f.write("<text>Volume molaire gazeux</text> \n")
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
        f.write('\n')
     f.write('</quiz>')
     f.close()
     