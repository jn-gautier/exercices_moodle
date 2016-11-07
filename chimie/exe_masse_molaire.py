#! /usr/bin/python3
# -*- coding: utf-8 -*- 
import random
from copy import deepcopy,copy

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
        self.simple=0
        
    
    
    def gene_valeurs(self):
        
        self.masse=random.randint(10,999)
        self.masse,self.masse_latex=convert_sci(self.masse)
        
        self.mole=self.masse/self.masse_molaire
        self.mole,self.mole_latex=convert_sci(self.mole)
        
        choix=random.randint(1,4)
        if choix==1 : self.exe_1()
        if choix==2 : self.exe_2()
        if choix==3 : self.exe_3()
        if choix==4 : self.exe_4()
        
        #
    
    
    def exe_1(self):
        
        self.type_exe='numerical'
        if self.simple==0:
            self.text_sup=', \(%s\),'%self.latex
        else:
            self.text_sup=''
        
        self.enonce="<p>Quelle est la masse de %s%s contenue dans \(%s [mol]\) de %s?</p>"%(self.nom,self.text_sup,self.mole_latex,self.nom)
        
        self.reponse=self.masse
        
        self.feedback="<p>Données<br/>"
        self.feedback+="Formule : \( %s \)<br/>"%self.latex
        self.feedback+="M=%s[\(g \cdot mol^{-1}\)] <br/>"%self.masse_molaire
        self.feedback+="\(n=%s[mol]\) </p>"%self.mole_latex
        
        self.feedback+="<p>Équation<br/>"
        self.feedback+="\(n=\\frac{m}{M} \\ \\rightarrow \\ m=n \cdot M \)</p>"
        
        self.feedback+="<p>Résolution<br/>"
        self.feedback+="\(m=n \cdot M \\ \\rightarrow \\ m=%s[g] \)</p>"%self.masse_latex
        
    def exe_2(self):
        self.type_exe='numerical'
        if self.simple==0:
            self.text_sup=', \(%s\),'%self.latex
        else:
            self.text_sup=''
        
        self.enonce="<p>Combien de moles de %s%s y'a-t-il dans \(%s [g]\) de %s?</p>"%(self.nom,self.text_sup,self.masse_latex,self.nom)
        
        self.reponse=self.mole
        
        self.feedback="<p>Données<br/>"
        self.feedback+="Formule : \( %s \)<br/>"%self.latex
        self.feedback+="M=%s[\(g \cdot mol^{-1}\)] <br/>"%self.masse_molaire
        self.feedback+="\(m=%s[g] \)</p>"%self.masse_latex
        
        self.feedback+="<p>Équation<br/>"
        self.feedback+="\(n=\\frac{m}{M} \)</p>"
        
        self.feedback+="<p>Résolution<br/>"
        self.feedback+="\(n=\\frac{m}{M} \\ \\rightarrow \\ n=%s[mol]\)</p>"%self.mole_latex
        
        
    def exe_3(self):
        
        self.type_exe='numerical'
        if self.simple==0:
            self.text_sup=', \(%s\),'%self.latex
        else:
            self.text_sup=''
        
        self.enonce="<p>On possède \(%s [mol]\) de %s%s ; quelle masse cela représente-t-il?</p>"%(self.mole_latex,self.nom,self.text_sup,)
        
        self.reponse=self.masse
        
        self.feedback="<p>Données<br/>"
        self.feedback+="Formule : \( %s \)<br/>"%self.latex
        self.feedback+="M=%s[\(g \cdot mol^{-1}\)] <br/>"%self.masse_molaire
        self.feedback+="\(n=%s[mol]\) </p>"%self.mole_latex
        
        self.feedback+="<p>Équation<br/>"
        self.feedback+="\(n=\\frac{m}{M} \\ \\rightarrow \\ m=n \cdot M \)</p>"
        
        self.feedback+="<p>Résolution<br/>"
        self.feedback+="\(m=n \cdot M \\ \\rightarrow \\ m=%s[g] \)</p>"%self.masse_latex
        
    def exe_4(self):
        self.type_exe='numerical'
        if self.simple==0:
            self.text_sup=', \(%s\),'%self.latex
        else:
            self.text_sup=''
        
        self.enonce="<p>On possède \(%s [g]\) de %s%s ; combien de moles cela représente-t-il?</p>"%(self.masse_latex,self.nom,self.text_sup)
        
        self.reponse=self.mole
        
        self.feedback="<p>Données<br/>"
        self.feedback+="Formule : \( %s \)<br/>"%self.latex
        self.feedback+="M=%s[\(g \cdot mol^{-1}\)] <br/>"%self.masse_molaire
        self.feedback+="\(m=%s[g] \)</p>"%self.masse_latex
        
        self.feedback+="<p>Équation<br/>"
        self.feedback+="\(n=\\frac{m}{M} \)</p>"
        
        self.feedback+="<p>Résolution<br/>"
        self.feedback+="\(n=\\frac{m}{M} \\ \\rightarrow \\ n=%s[mol]\)</p>"%self.mole_latex


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
         molecule.enonce=molecule.enonce.replace(" de i"," d'i")
         molecule.enonce=molecule.enonce.replace(" de a"," d'a")
         molecule.enonce=molecule.enonce.replace(" de o"," d'o")
         molecule.enonce=molecule.enonce.replace(" de h"," d'h")
         questionnaire.append(molecule)
     
     
         
     
     f = open('./exe_masse_molaire_moodle.xml','w')
    
     f.write('<?xml version="1.0" encoding="UTF-8"?> \n')
     f.write("<quiz> \n")
     f.write('<question type="category"> \n')
     f.write("<category> \n")
     f.write("<text>$course$/Chimie/Masse molaire</text> \n")
     f.write("</category> \n")
     f.write("</question> \n")
     for question in questionnaire:
         
         if question.type_exe=='numerical':
             f.write('<question type="numerical">\n')
             f.write('<name>\n')
             f.write('<text>Masse molaire</text>\n')
             f.write('</name>\n')
             f.write('<questiontext format="html">\n')
             f.write('<text><![CDATA[%s]]></text>\n' %question.enonce)
             f.write('</questiontext>\n')
             f.write('<generalfeedback format="html">\n')
             f.write("<text><![CDATA[ %s ]]></text>  \n" %question.feedback)
             f.write('</generalfeedback>\n')
             f.write('<defaultgrade>1.0000000</defaultgrade>\n')
             f.write('<penalty>0.3333333</penalty>\n')
             f.write('<hidden>0</hidden>\n')
             f.write('<answer fraction="100" format="moodle_auto_format">\n')
             f.write('<text>%s</text>\n'%question.reponse)
             f.write('<feedback format="html">\n')
             f.write('<text></text>\n')
             f.write('</feedback>\n')
             f.write('<tolerance>%s</tolerance>\n'%(0.03*question.reponse))
             f.write('</answer>\n')
             f.write('<unitgradingtype>0</unitgradingtype>\n')
             f.write('<unitpenalty>0.1000000</unitpenalty>\n')
             f.write('<showunits>3</showunits>\n')
             f.write('<unitsleft>0</unitsleft>\n')
             f.write('</question>\n')
     f.write('</quiz>')
     f.close()
     