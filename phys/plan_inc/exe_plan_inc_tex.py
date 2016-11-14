#! /usr/bin/python
# -*- coding: utf-8 -*- 

"""Attention, ce script ne génère pas encore d'exercice pour moodle;
Il s'git d'un script utilisé pour créer des exercices dans un fichier tex 
et qui pourrait être modifié pour créer des exercices au format moodle xml.
Le gros du travail consite à créer les images en svg pour la correction.
Il faut aussi prévoir d'otimiser le code, le rendre plus lisible, ..."""

import random
import math
import subprocess

def convert_sci(nombre):
     nombre_sciE='%.4E' %(nombre)
     nombre_sciE=nombre_sciE.split('E')
     #
     base=nombre_sciE[0]
     base=base.replace('.',',')
     exposant=nombre_sciE[1]
     #
     decimales=base.split(',')[1]
     arrondi=1
     for chiffre in decimales:
         if chiffre!='0':
             arrondi=0
     if arrondi==1:
         base=base.split(',')[0]
     #
     if exposant[1:]=='00':
         nombre_sci=base
     #
     elif exposant[1:]=='01':
         nombre=round(nombre,4)
         nombre_sci=str(nombre)
         nombre_sci=nombre_sci.replace('.',',')
     else:
         nombre_sci=base+'\\times 10^{'+exposant+'}'
     #
     return nombre_sci


class Question1:
     def __init__(self):
         self.masse=random.randint(1,90)
         self.unites_masse=random.choice(['[g]','[kg]','[To]'])
         if self.unites_masse=='[g]':
             self.masse_si=self.masse/1000.0
         elif self.unites_masse=='[To]':
             self.masse_si=self.masse*1000
         else:
             self.masse_si=self.masse
         self.masse_si=float(self.masse_si)
         if (self.masse_si > 9999) or (self.masse_si < 0.1):
             self.masse_si_str=convert_sci(self.masse_si)
         else:
             self.masse_si_str=str(self.masse_si).replace('.',',')
         #
         self.alpha=random.randint(5,60)
         #
         self.fgx=self.masse_si*10*(math.sin(math.radians(self.alpha)))
         self.fgx=round(self.fgx,3)
         if (self.fgx > 9999) or (self.fgx < 0.1):
             self.fgx_str=convert_sci(self.fgx)
         else:
             self.fgx_str=str(self.fgx).replace('.',',')
         #
         self.fgy=self.masse_si*10*(math.cos(math.radians(self.alpha)))
         self.fgy=round(self.fgy,3)
         if (self.fgy > 9999) or (self.fgy < 0.1):
             self.fgy_str=convert_sci(self.fgy)
         else:
             self.fgy_str=str(self.fgy).replace('.',',')
         #
     ###
     def type1_0(self):
         self.enonce="\mbox{(a)} D\\'etermine l'intensit\\'e de la composante normale et de la composante tangantielle du poids pour un objet de ${%s %s}$ se trouvant sur un plan incliné formant un angle de ${%s\degres}$ vers le haut." %(self.masse_si_str,self.unites_masse,self.alpha)
         self.reponse='${F_{gX} =%s [N]  ;  F_{gY}=%s [N]}$' %(self.fgx_str,self.fgy_str)
     ###
     def type1_1(self):
         self.enonce="\mbox{(b)} D\\'etermine la masse d'un objet se trouvant sur un plan incliné formant un angle de ${%s\degres}$ vers le haut s'il faut une force de ${%s [N]}$ dirigée vers le haut de la pente pour le maintenir au repos sur celle-ci." %(self.alpha,self.fgx_str)
         self.reponse='${m=%s [kg]}$' %self.masse_si_str
     ###
     def type1_2(self):
         self.enonce="\mbox{(c)} D\\'etermine la masse d'un objet se trouvant sur un plan incliné formant un angle de ${%s\degres}$ vers le haut si la composante tangantielle de son poids vaut ${%s [N]}$." %(self.alpha,self.fgx_str)
         self.reponse='${m=%s [kg]}$' %self.masse_si_str
     ###
     def type1_3(self):
         self.enonce="\mbox{(d)} D\\'etermine la masse d'un objet se trouvant sur un plan incliné formant un angle de ${%s\degres}$ vers le haut si la composante normale de son poids vaut ${%s [N]}$." %(self.alpha,self.fgy_str)
         self.reponse='${m=%s [kg]}$' %self.masse_si_str
     ###
     def type1_4(self):
         self.enonce="\mbox{(e)} D\\'etermine l'angle de la pente sur laquelle se trouve un objet dont la masse vaut ${%s %s}$ s'il faut une force de ${%s [N]}$ dirigée vers le haut de la pente pour le maintenir au repos." %(self.masse,self.unites_masse,self.fgx_str)
         self.reponse='${\\alpha=%s\degres}$' %self.alpha
     ###
     def type1_5(self):
         self.enonce="\mbox{(f)} D\\'etermine l'angle de la pente sur laquelle se trouve un objet dont la masse vaut ${%s %s}$ si l'intensité de la composante tangantielle de son poids est de ${%s [N]}$." %(self.masse,self.unites_masse,self.fgx_str)
         self.reponse='${\\alpha=%s\degres}$' %self.alpha
     ###
     def type1_6(self):
         self.enonce="\mbox{(g)} D\\'etermine l'angle de la pente sur laquelle se trouve un objet dont la masse vaut ${%s %s}$ si l'intensité de la composante normale de son poids est de ${%s [N]}$." %(self.masse,self.unites_masse,self.fgy_str)
         self.reponse='${\\alpha=%s \degres}$' %self.alpha
###
def gene_questionnaire(type_question,nb_questions,type_principal,nb_types):
     questionnaire=[]
     x=random.randint(0,nb_types)
     questionnaire=[]
     for i in range(nb_questions):
         if type_question==1:
             question=Question1()
         elif type_question==2:
             question=Question2()
         x=random.randint(0,nb_types)
         choix='type'+str(type_principal)+'_'+str(x)
         getattr(question,choix)()
         questionnaire.append(question)
     return questionnaire

if __name__=="__main__":
     questionnaire1=gene_questionnaire(1,100,1,6)
     
     f = open('./exe_plan_inc.tex','w')
     #
     f.write('\documentclass[12pt, a4paper]{article}\n')
     f.write('\usepackage[margin=2cm]{geometry}\n')
     f.write('\usepackage{setspace}\n')
     f.write('\onehalfspacing \n')
     f.write('\usepackage{fancyhdr}\n')
     f.write('\usepackage{amsfonts}\n')
     f.write('\usepackage{amsmath,amsthm,amssymb}\n')
     f.write('\usepackage{graphicx}\n')
     f.write('\usepackage{hyperref}\n')
     f.write('\usepackage[utf8]{inputenc}\n')
     f.write('\usepackage[T1]{fontenc}\n')
     f.write('\usepackage{lmodern}\n')
     f.write('\usepackage[french]{babel}\n')
     f.write('\usepackage{textcomp}\n')
     f.write('\\begin{document}\n') 
     f.write("\section*{Exercices : décomposition des forces sur un plan inclin\\'e}\n")
     ###
     f.write("\subsection*{\\'Enonc\\'es}\n")
     ###
     f.write("\\begin{enumerate}\n")
     for question in questionnaire1:
         f.write('\item '+'\n')
         f.write(question.enonce+'\n')
     f.write("\\end{enumerate}\n")
     ###
     f.write("\\newpage \n")
     ####
     f.write("\\newpage \n")
     f.write("\subsection*{R\\'eponses}\n")
     ###
     f.write("\\begin{enumerate}\n")
     for question in questionnaire1:
         f.write('\item '+question.reponse+'\n')
     f.write("\\end{enumerate}\n")
     f.write('\\end{document}\n')
     
     f.close()
     proc=subprocess.Popen(['pdflatex','./exe_plan_inc.tex'])
     proc.wait()
