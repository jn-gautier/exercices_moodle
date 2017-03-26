#! /usr/bin/python3
# -*- coding: utf-8 -*- 
import random





class Exercice():
    def __init__(self):
         self.symbole=''
         self.ion=0
         self.numero_atomique=0
         self.liste_masses_isotopes=[]
         
    def creer_enonce(self):
        self.masse_atomique=random.choice(self.liste_masses_isotopes)
        self.neutrons=int(self.masse_atomique)-self.numero_atomique
        self.electrons=self.numero_atomique+self.ion
        self.symbole_tex=self.symbole
        charge=abs(self.ion)
        if charge==1:charge=''
        
        if self.ion<0:
            self.symbole_tex+='^{%s+}'%charge
        elif self.ion>0:
            self.symbole_tex+='^{%s-}'%charge
         
        
        choix=random.randint(1,2)
        if choix==1:
             #je donne A et je demande n0
             self.enonce='<p>Complète le tableau suivant :</p> \n'
             self.enonce+='<table border="2" style="border-collapse: collapse;">\n'
             self.enonce+='<tr><td style="padding: 5px">Symbole</td><td style="padding: 5px">\(p^+\)</td><td style="padding: 5px">\(n^0\)</td><td style="padding: 5px">\(e^-\)</td><td style="padding: 5px">A</td></tr>\n'
             self.enonce+='<tr><td style="padding: 5px">\(%s\)</td><td style="padding: 5px">{1:NUMERICAL:=%s}</td><td style="padding: 5px">{1:NUMERICAL:=%s}</td><td style="padding: 5px">{1:NUMERICAL:=%s}</td><td style="padding: 5px">%s</td></tr>\n'%(self.symbole_tex,self.numero_atomique,self.neutrons,self.electrons,self.masse_atomique)
             self.enonce+="</table><br/>"
             #{1:NUMERICAL:=2}
        
        if choix==2:
             #je donne n0 et je demande A 
             self.enonce='<p>Complète le tableau suivant :</p> \n'
             self.enonce+='<table border="2" style="border-collapse: collapse;">\n'
             self.enonce+='<tr><td style="padding: 5px">Symbole</td><td style="padding: 5px">\(p^+\)</td><td style="padding: 5px">\(n^0\)</td><td style="padding: 5px">\(e^-\)</td><td style="padding: 5px">A</td></tr>\n'
             self.enonce+='<tr><td style="padding: 5px">\(%s\)</td><td style="padding: 5px">{1:NUMERICAL:=%s}</td><td style="padding: 5px">%s</td><td style="padding: 5px">{1:NUMERICAL:=%s}</td><td style="padding: 5px">{1:NUMERICAL:=%s}</td></tr>\n'%(self.symbole_tex,self.numero_atomique,self.neutrons,self.electrons,self.masse_atomique)
             self.enonce+="</table><br/>"
       








if __name__=="__main__":
     questionnaire=[]
     
     myfile=open('./isotopes', "r")
     
     for ligne in myfile:
         exercice=Exercice()
         liste_masses=''
         ligne=ligne.rstrip('\n\r').split('\t')
         exercice.symbole=ligne[0]
         exercice.ion=int(ligne[1])
         exercice.numero_atomique=int(ligne[2])
         liste_masses=ligne[3]
         exercice.liste_masses_isotopes=liste_masses.split(';')
         for masse in exercice.liste_masses_isotopes:
             masse=int(masse)
         exercice.creer_enonce()
         questionnaire.append(exercice)
         
         
     
     f = open('./exe_isotopes_moodle.xml','w')
     f.write('<?xml version="1.0" encoding="UTF-8"?> \n')
     f.write("<quiz> \n")
     f.write('<question type="category"> \n')
     f.write("<category> \n")
     f.write("<text>$course$/Chimie/Isotopes</text> \n")
     f.write("</category> \n")
     f.write("</question> \n")
     for question in questionnaire:
     
         f.write('<question type="cloze"> \n')
         f.write("<name> \n")
         f.write("<text>Isotopes</text> \n")
         f.write("</name> \n")
         f.write('<questiontext format="html"> \n')
         f.write("<text><![CDATA[ %s ]]></text>  \n" %question.enonce)
         f.write("</questiontext>  \n")
         f.write('<generalfeedback format="html">  \n')
         f.write("<text></text>  \n")
         f.write("</generalfeedback>  \n")
         f.write("<penalty>0.3333333</penalty>  \n")
         f.write("<hidden>0</hidden>  \n")
         f.write("</question>  \n")
     f.write('</quiz> \n')
     f.close()
     