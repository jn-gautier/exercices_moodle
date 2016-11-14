#! /usr/bin/python
# -*- coding: utf-8 -*- 

import random
import math
import subprocess

def convert_sci(nombre):
     if (nombre>1000) or (nombre<0.1):
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
         if arrondi==1: #s'il n'y a pas de décimales
             base=base.split(',')[0]
         #
         nombre_sci=base+'\\times 10^{'+exposant+'}'
         
     else:
         nombre_str=str(nombre)
         nombre_str=nombre_str.replace('.',',')
         partie_entiere=nombre_str.split(',')[0]
         entiers_significatifs=len(partie_entiere)
         if partie_entiere=='0':
             entiers_significatifs=0
         #decimaux_significatifs=0
         partie_decimale=''
         if (len(nombre_str.split(','))>1):#s'il y a une partie decimale
             partie_decimale=nombre_str.split(',')[1]
             #decimaux_significatifs=len(partie_decimale)
         
         decimaux_a_prendre=4-entiers_significatifs
         decimaux_pris=partie_decimale[0:decimaux_a_prendre]
         
         if decimaux_pris!='':
             nombre_sci=partie_entiere+','+decimaux_pris
         else:
             nombre_sci=partie_entiere
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
         #
         self.unites_vitesse=random.choice(['[m/s]','[km/h]'])
         if self.unites_vitesse=='[km/h]':
             self.vitesse_si=random.randint(1,15)
             self.vitesse=self.vitesse_si*3.6
             
         if self.unites_vitesse=='[m/s]':
             self.vitesse=random.randint(1,25)
             self.vitesse_si=self.vitesse
             self.unites_vitesse='[m.s^{-1}]'
         #
         self.hauteur=random.randint(1,90)
         #self.unites_hauteur=random.choice(['[cm]','[m]','[km]'])
         if self.unites_masse=='[To]':
             self.unites_hauteur='[km]'  
         if self.unites_masse=='[g]':
             self.unites_hauteur='[cm]'
         else : self.unites_hauteur='[m]'
        
         #
         if self.unites_hauteur=='[cm]':
             self.hauteur_si=self.hauteur/100.0
         elif self.unites_hauteur=='[km]':
             self.hauteur_si=self.hauteur*1000
         else:
             self.hauteur_si=self.hauteur
         #
         self.energie_cin=convert_sci(0.5*self.masse_si*self.vitesse_si**2)
         self.energie_pot=convert_sci(self.masse_si*10*self.hauteur_si)
         self.energie_meca=convert_sci((0.5*self.masse_si*self.vitesse_si**2)+(self.masse_si*10*self.hauteur_si))
         self.hauteur=str(self.hauteur).replace('.',',')
         self.vitesse=str(self.vitesse).replace('.',',')
         #
         choix=random.randint(1,9)
         ponderateur=random.choice([[0.4,0.5,0.7,0.8],[0.5,0.7,0.8,1.1],[0.7,0.8,1.1,1.2],[0.8,1.1,1.2,1.4],[1.1,1.2,1.4,1.6]])
         #
         if choix==1:
             self.enonce="Détermine l'énergie cinétique d'un objet de \(%s %s\) se déplaçant à une vitesse de \(%s %s\)." %(self.masse,self.unites_masse,self.vitesse,self.unites_vitesse)
             self.feedback='$$E_c =%s [J]$$' %self.energie_cin
             self.reponse='$$E_c =%s [J]$$' %self.energie_cin
             self.reponses_fausses=[]
             for facteur in ponderateur:
                 self.reponses_fausses.append("$$E_c ="+convert_sci(facteur*0.5*self.masse_si*self.vitesse_si**2)+" [J]$$")
                 
         ###
         if choix==2:
             self.enonce="Détermine la masse d'un objet se déplaçant à une vitesse de \(%s %s\) et dont l'énergie cinétique est de \(%s[J]\)." %(self.vitesse,self.unites_vitesse,self.energie_cin)
             self.reponse='$$m=%s [kg]$$' %self.masse_si
             self.feedback='$$m=%s [kg]}$$' %self.masse_si
             self.reponses_fausses=[]
             for facteur in ponderateur:
                 self.reponses_fausses.append("$$m="+str(self.masse_si*facteur)+" [kg]$$")
         ###
         if choix==3:
             self.enonce="Détermine la vitesse d'un objet de \(%s %s\) possédant une énergie cinétique de \(%s [J]\)." %(self.masse,self.unites_masse,self.energie_cin)
             
             self.reponses_fausses=[]
             for facteur in ponderateur:
                 self.reponses_fausses.append("$$v="+convert_sci(self.vitesse_si*facteur)+" [m.s^{-1}]$$")
             
             self.vitesse_si=convert_sci(self.vitesse_si)
             self.feedback='$$v=%s [m.s^{-1}]$$' %self.vitesse_si
             self.reponse='$$v=%s [m.s^{-1}]$$' %self.vitesse_si
             
         ###
         if choix==4:
             self.enonce="Détermine l'énergie potentielle d'un objet dont la masse vaut \(m=%s %s\) et qui se trouve à une hauteur de \(%s %s\)." %(self.masse,self.unites_masse,self.hauteur,self.unites_hauteur)
             self.feedback='$$E_p =%s [J]$$' %self.energie_pot
             self.reponse='$$E_p =%s [J]$$' %self.energie_pot
             self.reponses_fausses=[]
             for facteur in ponderateur:
                 self.reponses_fausses.append("$$E_p ="+convert_sci(self.masse_si*10*self.hauteur_si*facteur)+" [J]$$")
             
         ###
         if choix==5:
             self.enonce="Détermine la hauteur à laquelle se trouve un objet dont la masse vaut \(%s %s\) et qui possède une énergie potentielle de \( %s [J]\)." %(self.masse,self.unites_masse,self.energie_pot)
             self.feedback='$$h=%s [m]$$' %self.hauteur_si
             self.reponse='$$h=%s [m]$$' %self.hauteur_si
             self.reponses_fausses=[]
             for facteur in ponderateur:
                 self.reponses_fausses.append("$$h="+str(self.hauteur_si*facteur)+" [m]$$")
         ###
         if choix==6:
             self.enonce="Détermine la masse d'un objet se trouvant à une hauteur de \(%s %s\) et possédant une énergie potentielle de \(%s [J]\)." %(self.hauteur,self.unites_hauteur,self.energie_pot)
             self.reponse='$$m=%s [kg]$$' %self.masse_si
             self.feedback='$$m=%s [kg]}$$' %self.masse_si
             self.reponses_fausses=[]
             for facteur in ponderateur:
                 self.reponses_fausses.append("$$m="+str(self.masse_si*facteur)+" [kg]$$")
         ###
         if choix==7:
             self.enonce="Détermine la masse d'un corps possédant une énergie mécanique de \(%s [J]\) lorsqu'il se déplace à une vitesse constante de \(%s %s\) à une hauteur de \(%s %s\)." %(self.energie_meca,self.vitesse,self.unites_vitesse,self.hauteur,self.unites_hauteur)
             self.reponse='$$m=%s [kg]$$' %self.masse_si
             self.feedback='$$m=%s [kg]}$$' %self.masse_si
             self.reponses_fausses=[]
             for facteur in ponderateur:
                 self.reponses_fausses.append("$$m="+str(self.masse_si*facteur)+" [kg]$$")
         ###
         if choix==8:
             self.enonce="Un corps dont la masse vaut : \(m=%s %s\) possède une énergie mécanique de \(%s [J]\) lorsqu'il se déplace à une vitesse constante de \(%s %s\). Détermine la hauteur à laquelle il se trouve." %(self.masse,self.unites_masse,self.energie_meca,self.vitesse,self.unites_vitesse)
             self.feedback='$$h=%s [m]$$' %self.hauteur_si
             self.reponse='$$h=%s [m]$$' %self.hauteur_si
             self.reponses_fausses=[]
             for facteur in ponderateur:
                 self.reponses_fausses.append("$$h="+str(self.hauteur_si*facteur)+" [m]$$")
         ###
         if choix==9:
             self.enonce="À quelle vitesse se déplace un objet de \(%s %s\) possédant une énergie mécanique de \(%s [J]\) lorsqu'il se déplace à une hauteur de \(%s %s\)?" %(self.masse,self.unites_masse,self.energie_meca,self.hauteur,self.unites_hauteur)
             
             self.reponses_fausses=[]
             for facteur in ponderateur:
                 self.reponses_fausses.append("$$v="+convert_sci(self.vitesse_si*facteur)+" [m.s^{-1}]$$")
             
             self.vitesse_si=convert_sci(self.vitesse_si)
             self.feedback='$$v=%s [m.s^{-1}]$$' %self.vitesse_si
             self.reponse='$$v=%s [m.s^{-1}]$$' %self.vitesse_si
###
###
###
class Question2:
     def __init__(self):
         #liste=['a','b','c','d','e','f','g','h','i','j','k','l']
         #self.type_exe=random.choice(liste)
         #self.choix=self.liste.index(self.type_exe)
         #self.type_exe=''
         self.choix=random.randint(1,12)
         self.ponderateur=random.choice([[0.4,0.5,0.7,0.8],[0.5,0.7,0.8,1.1],[0.7,0.8,1.1,1.2],[0.8,1.1,1.2,1.4],[1.1,1.2,1.4,1.6]])
         
         self.masse=random.randint(1,25)
         #self.unites_masse='[kg]'
         #self.masse_si=self.masse
         #
         
         self.vitesse_0=random.randint(8,50)
         #self.vitesse_si=self.vitesse
         #self.unites_vitesse='[m.s^{-1}]'
         #
         self.hauteur_3=(self.vitesse_0**2)/(2*10.0)
         #self.unites_hauteur='[m]'
         #self.hauteur=self.hauteur_si
         #
         self.hauteur_1=random.randint(1,round(self.hauteur_3-1))
         self.vitesse_1=math.sqrt((self.vitesse_0**2)-(2*10*self.hauteur_1))
         self.energie_cin_1=self.masse*(self.vitesse_1**2)/2
         self.energie_pot_1=self.masse*10*self.hauteur_1
         #
         self.vitesse_2=random.randint(1,round(self.vitesse_0-1))
         self.hauteur_2=(((self.vitesse_0**2)-(self.vitesse_2**2))/(2.0*10))
         self.energie_cin_2=self.masse*(self.vitesse_2**2)/2
         self.energie_pot_2=self.masse*10*self.hauteur_2
         #
         self.vitesse_0_str=convert_sci(self.vitesse_0)
         
         self.hauteur_1_str=convert_sci(self.hauteur_1)
         self.vitesse_1_str=convert_sci(self.vitesse_1)
         self.energie_cin_1_str=convert_sci(self.energie_cin_1)
         self.energie_pot_1_str=convert_sci(self.energie_pot_1)
         
         self.hauteur_2_str=convert_sci(self.hauteur_2)
         self.vitesse_2_str=convert_sci(self.vitesse_2)
         self.energie_cin_2_str=convert_sci(self.energie_cin_2)
         self.energie_pot_2_str=convert_sci(self.energie_pot_2)
         
         self.hauteur_3_str=convert_sci(self.hauteur_3)
         #
         self.energie_meca_str=convert_sci(self.masse*(self.vitesse_0**2)/2)
         #self.choix=random.randint(1,12)
         #choix=4
         
         
         #
     def gene_exe(self):
         
         if self.choix==1:
             self.enonce="(a) Un objet de \(%s [kg]\), initialement au repos, tombe en chute libre depuis une hauteur de \(%s [m]\). Quelle est la vitesse d'impact de cet objet ?" %(self.masse,self.hauteur_3_str)
             #
             self.reponse='\(v_{impact}=%s [m.s^{-1}]\)' %(self.vitesse_0_str)
             self.feedback=""
             self.feedback+="<p>Lorsque l'objet est à \(%s [m]\) de hauteur, toute l'énergie mécanique est sous forme d'énergie potentielle : \(E_m = E_p\).</p>"%(self.hauteur_3_str)
             self.feedback+="<p>Donc: \(E_m =E_p =m \cdot g \cdot h \ \\rightarrow \ E_m =%s \cdot 10 \cdot %s \ \\rightarrow \ E_m =%s [J] \) </p>"%(self.masse,self.hauteur_3_str,self.energie_meca_str)
             self.feedback+="<p>Lorsque l'objet arrive au sol, toute l'énergie mécanique se trouve sous forme d'énergie cinétique : \(E_m = E_c\).</p>"
             self.feedback+="<p>Donc : \(E_m =E_c =\\frac{m \cdot v^2}{2} \ \leftrightarrow \ v =\sqrt{\\frac{2 \cdot E_m}{m}} \ \\rightarrow \ v =\sqrt{\\frac{2 \cdot %s}{%s}} \ \\rightarrow \ v=%s [m.s^{-1}]\) </p>"%(self.energie_meca_str,self.masse,self.vitesse_0_str)
             self.reponses_fausses=[]
             for facteur in self.ponderateur:
                 self.reponses_fausses.append("\(v_{impact}=%s [m.s^{-1}]\)" %(convert_sci(self.vitesse_0*facteur)))
         #
         if self.choix==2:
             self.enonce="(b) Un objet de \(%s [kg]\), initialement au repos, tombe en chute libre depuis une hauteur de \(%s [m]\). Quelle est sa vitesse lorsqu'il se trouve à une hauteur de \(%s [m]\)?" %(self.masse,self.hauteur_3_str,self.hauteur_1_str)
             #
             self.reponse='\(v=%s [m.s^{-1}]\)' %(self.vitesse_1_str)
             #
             self.feedback=''
             self.feedback+="<p>Lorsque l'objet est à \(%s [m]\) de hauteur, toute l'énergie mécanique est sous forme d'énergie potentielle : \(E_m = E_p\).</p>"%(self.hauteur_3_str)
             self.feedback+="<p>Donc: \(E_m =E_p =m \cdot g \cdot h \ \\rightarrow \ E_m =%s \cdot 10 \cdot %s \ \\rightarrow \ E_m =%s [J] \) </p>"%(self.masse,self.hauteur_3_str,self.energie_meca_str)
             self.feedback+="<p>Lorsque l'objet est à \(%s [m]\) de hauteur, son énergie potentielle vaut : \(E_p =%s \cdot 10 \cdot %s \ \\rightarrow \ E_p =%s  [J]\)</p>"%(self.hauteur_1_str,self.masse,self.hauteur_1_str,self.energie_pot_1_str)
             self.feedback+="<p>Dans ce cas, son énergie cinétique vaut : \(E_c =E_m - E_p \ \\rightarrow \  E_c =%s [J]\)</p>" %(self.energie_cin_1_str)
             self.feedback+="<p>Donc : \(v =\sqrt{\\frac{2 \cdot E_c}{m}} \ \\rightarrow \ v =\sqrt{\\frac{2 \cdot %s}{%s}} \ \\rightarrow \ v=%s [m.s^{-1}]\) </p>"%(self.energie_cin_1_str,self.masse,self.vitesse_1_str)
             self.reponses_fausses=[]
             for facteur in self.ponderateur:
                 self.reponses_fausses.append("\(v=%s [m.s^{-1}]\)" %(convert_sci(self.vitesse_1*facteur)))
         #
         if self.choix==3:
             self.enonce="(c) Un objet de \(%s [kg]\), initialement au repos, tombe en chute libre depuis une hauteur de \(%s [m]\). À quelle hauteur se trouve-t-il lorsqu'il possède une vitesse de \(%s [m.s^{-1}]\)?" %(self.masse,self.hauteur_3_str,self.vitesse_2_str)
             #
             self.reponse='\(h=%s [m]\)' %(self.hauteur_2_str)
             self.feedback=''
             self.feedback+="<p>Lorsque l'objet est à \(%s [m]\) de hauteur, toute l'énergie mécanique est sous forme d'énergie potentielle : \(E_m = E_p\).</p>"%(self.hauteur_3_str)
             self.feedback+="<p>Donc: \(E_m =E_p =m \cdot g \cdot h \ \\rightarrow \ E_m =%s \cdot 10 \cdot %s \ \\rightarrow \ E_m =%s [J] \) </p>"%(self.masse,self.hauteur_3_str,self.energie_meca_str)
             self.feedback+="<p>Lorsque l'objet possède une vitesse de \(%s [m.s^{-1}]\), son énergie cinétique vaut : \(E_c =\\frac{%s \cdot (%s)^{2}}{2} \ \\rightarrow \ E_c =%s  [J]\)</p>"%(self.vitesse_2_str,self.masse,self.vitesse_2_str,self.energie_cin_2_str)
             self.feedback+="<p>Dans ce cas, son énergie potentielle vaut : \(E_p =E_m - E_c \ \\rightarrow \  E_p =%s [J]\)</p>" %(self.energie_pot_2_str)
             self.feedback+="<p>Donc : \(h =\\frac{E_p}{m \cdot g} \ \\rightarrow \ h =\\frac{%s}{%s \cdot 10} \ \\rightarrow \ h=%s [m]\) </p>"%(self.energie_pot_2_str,self.masse,self.hauteur_2_str)
             self.reponses_fausses=[]
             for facteur in self.ponderateur:
                 self.reponses_fausses.append("\(h=%s [m]\)" %(convert_sci(self.hauteur_2*facteur)))
         
         if self.choix==4:
             self.enonce="(d) Un objet de \(%s [kg]\) est lancé verticalement vers le haut avec une vitesse initiale de \(%s [m.s^{-1}]\). Quelle sera la hauteur maximale atteinte par cet objet?" %(self.masse,self.vitesse_0_str)
             #
             self.reponse='\(h_{max}=%s [m]\)' %(self.hauteur_3_str)
             self.reponses_fausses=[]
             for facteur in self.ponderateur:
                 self.reponses_fausses.append("\(h_{max}=%s [m]\)" %(convert_sci(self.hauteur_3*facteur)))
             self.feedback=""
             self.feedback+="<p>Lorsque l'objet est au niveau du sol, toute l'énergie mécanique est sous forme d'énergie cinétique : \(E_m = E_c\).</p>"
             self.feedback+="<p>Donc: \(E_m =E_c =\\frac{m \cdot v^2}{2} \ \\rightarrow \ E_m =\\frac{%s \cdot %s^2}{2} \ \\rightarrow \ E_m =%s [J] \) </p>"%(self.masse,self.vitesse_0_str,self.energie_meca_str)
             self.feedback+="<p>Lorsqu'il arrive à sa hauteur maximale, sa vitesse est nulle et toute son énergie mécanique est sous forme d'énergie potentielle : \(E_m = E_p\).</p>"
             self.feedback+="<p>Donc : \(E_m =E_p =m \cdot g \cdot h \ \leftrightarrow \ h =\\frac{E_p}{m \cdot g} \ \\rightarrow \ h =\\frac{%s}{%s \cdot 10}} \ \\rightarrow \ h=%s [m]\) </p>"%(self.energie_meca_str,self.masse,self.hauteur_3_str)
         ###
         if self.choix==5:
             self.enonce="(e) Un objet de \(%s [kg]\) est lancé verticalement vers le haut avec une vitesse initiale de \(%s [m.s^{-1}]\). Quelle sera sa vitesse lorsqu'il se trouve à une hauteur de \(%s [m]\)?" %(self.masse,self.vitesse_0_str,self.hauteur_1_str)
             self.reponse='\(v=%s [m.s^{-1}]\)' %(self.vitesse_1_str)
             self.reponses_fausses=[]
             for facteur in self.ponderateur:
                 self.reponses_fausses.append("\(v=%s [m.s^{-1}]\)" %(convert_sci(self.vitesse_1*facteur)))
             self.feedback=""
             self.feedback+="<p>Lorsque l'objet est au niveau du sol, toute l'énergie mécanique est sous forme d'énergie cinétique : \(E_m = E_c\).</p>"
             self.feedback+="<p>Donc: \(E_m =E_c =\\frac{m \cdot v^2}{2} \ \\rightarrow \ E_m =\\frac{%s \cdot %s^2}{2} \ \\rightarrow \ E_m =%s [J] \) </p>"%(self.masse,self.vitesse_0_str,self.energie_meca_str)
             
             self.feedback+="<p>Lorsque l'objet est à \(%s [m]\) de hauteur, son énergie potentielle vaut : \(E_p =%s \cdot 10 \cdot %s \ \\rightarrow \ E_p =%s  [J]\)</p>"%(self.hauteur_1_str,self.masse,self.hauteur_1_str,self.energie_pot_1_str)
             self.feedback+="<p>Dans ce cas, son énergie cinétique vaut : \(E_c =E_m - E_p \ \\rightarrow \  E_c =%s [J]\)</p>" %(self.energie_cin_1_str)
             self.feedback+="<p>Donc : \(v =\sqrt{\\frac{2 \cdot E_c}{m}} \ \\rightarrow \ v =\sqrt{\\frac{2 \cdot %s}{%s}} \ \\rightarrow \ v=%s [m.s^{-1}]\) </p>"%(self.energie_cin_1_str,self.masse,self.vitesse_1_str)
         
         
         if self.choix==6:
             self.enonce="(f) Un objet de \(%s [kg]\) est lancé verticalement vers le haut avec une vitesse initiale de \(%s [m.s^{-1}]\). À quelle hauteur se trouve se trouve-t-il lorsqu'il possède une vitesse de \(%s [m.s^{-1}]\)?" %(self.masse,self.vitesse_0_str,self.vitesse_2_str)
             self.reponse='\(h=%s [m]\)' %(self.hauteur_2_str)
             self.reponses_fausses=[]
             for facteur in self.ponderateur:
                 self.reponses_fausses.append("\(h=%s [m]\)" %(convert_sci(self.hauteur_2*facteur)))
             self.feedback=''
             self.feedback+="<p>Lorsque l'objet est au niveau du sol, toute l'énergie mécanique est sous forme d'énergie cinétique : \(E_m = E_c\).</p>"
             self.feedback+="<p>Donc: \(E_m =E_c =\\frac{m \cdot v^2}{2} \ \\rightarrow \ E_m =\\frac{%s \cdot %s^2}{2} \ \\rightarrow \ E_m =%s [J] \) </p>"%(self.masse,self.vitesse_0_str,self.energie_meca_str)
             self.feedback+="<p>Lorsque l'objet possède une vitesse de \(%s [m.s^{-1}]\), son énergie cinétique vaut : \(E_c =\\frac{%s \cdot (%s)^{2}}{2} \ \\rightarrow \ E_c =%s  [J]\)</p>"%(self.vitesse_2_str,self.masse,self.vitesse_2_str,self.energie_cin_2_str)
             self.feedback+="<p>Dans ce cas, son énergie potentielle vaut : \(E_p =E_m - E_c \ \\rightarrow \  E_p =%s [J]\)</p>" %(self.energie_pot_2_str)
             self.feedback+="<p>Donc : \(h =\\frac{E_p}{m \cdot g} \ \\rightarrow \ h =\\frac{%s}{%s \cdot 10} \ \\rightarrow \ h=%s [m]\) </p>"%(self.energie_pot_2_str,self.masse,self.hauteur_2_str)
             
         
         
         if self.choix==7:
             self.enonce="(g) Avec quelle vitesse faut-il lancer un objet de \(%s [kg]\) vers le haut pour qu'il atteigne une hauteur de \(%s [m]\)?" %(self.masse,self.hauteur_3_str)
             self.reponse='\(v_{init}=%s [m.s^{-1}]\)' %(self.vitesse_0_str)
             self.reponses_fausses=[]
             for facteur in self.ponderateur:
                 self.reponses_fausses.append("\(v_{init}=%s [m.s^{-1}]\)" %(convert_sci(self.vitesse_0*facteur)))
             self.feedback=""
             self.feedback+="<p>Lorsque l'objet est à \(%s [m]\) de hauteur, toute l'énergie mécanique est sous forme d'énergie potentielle : \(E_m = E_p\).</p>"%(self.hauteur_3_str)
             self.feedback+="<p>Donc: \(E_m =E_p =m \cdot g \cdot h \ \\rightarrow \ E_m =%s \cdot 10 \cdot %s \ \\rightarrow \ E_m =%s [J] \) </p>"%(self.masse,self.hauteur_3_str,self.energie_meca_str)
             self.feedback+="<p>Lorsque l'objet est au niveau du sol, toute l'énergie mécanique se trouve sous forme d'énergie cinétique : \(E_m = E_c\).</p>"
             self.feedback+="<p>Donc : \(E_m =E_c =\\frac{m \cdot v^2}{2} \ \leftrightarrow \ v =\sqrt{\\frac{2 \cdot E_m}{m}} \ \\rightarrow \ v =\sqrt{\\frac{2 \cdot %s}{%s}} \ \\rightarrow \ v=%s [m.s^{-1}]\) </p>"%(self.energie_meca_str,self.masse,self.vitesse_0_str)
             
             
         
         if self.choix==8:
             self.enonce="(h) De quelle hauteur faut-il lâcher un objet de \(%s [kg]\) pour qu'il touche le sol avec une vitesse de \(%s [m.s^{-1}]\)?" %(self.masse,self.vitesse_0_str)
             self.reponse='\(h_{init}=%s [m]\)' %(self.hauteur_3_str)
             self.reponses_fausses=[]
             for facteur in self.ponderateur:
                 self.reponses_fausses.append("\(h_{init}=%s [m]\)" %(convert_sci(self.hauteur_3*facteur)))
             self.feedback=""
             self.feedback+="<p>Lorsque l'objet est au niveau du sol, toute l'énergie mécanique est sous forme d'énergie cinétique : \(E_m = E_c\).</p>"
             self.feedback+="<p>Donc: \(E_m =E_c =\\frac{m \cdot v^2}{2} \ \\rightarrow \ E_m =\\frac{%s \cdot %s^2}{2} \ \\rightarrow \ E_m =%s [J] \) </p>"%(self.masse,self.vitesse_0_str,self.energie_meca_str)
             self.feedback+="<p>Lorsqu'il est à sa hauteur de départ, sa vitesse est nulle et toute son énergie mécanique est sous forme d'énergie potentielle : \(E_m = E_p\).</p>"
             self.feedback+="<p>Donc : \(E_m =E_p =m \cdot g \cdot h \ \leftrightarrow \ h =\\frac{E_p}{m \cdot g} \ \\rightarrow \ h =\\frac{%s}{%s \cdot 10}} \ \\rightarrow \ h=%s [m]\) </p>"%(self.energie_meca_str,self.masse,self.hauteur_3_str)
             
         if self.choix==9:
             #
             self.enonce="(i) Avec quelle vitesse faut-il lancer un objet de \(%s [kg]\) vers le haut pour qu'il atteigne une hauteur de \(%s [m]\) avec une vitesse de \(%s [m.s^{-1}]\)?" %(self.masse,self.hauteur_1_str,self.vitesse_1_str)
             
             self.reponse='\(v_{init}=%s [m.s^{-1}]\)' %(self.vitesse_0_str)
             self.reponses_fausses=[]
             for facteur in self.ponderateur:
                 self.reponses_fausses.append("\(v_{init}=%s [m.s^{-1}]\)" %(convert_sci(self.vitesse_0*facteur)))
             self.feedback=""
             self.feedback="<p>Lorsque l'objet est à \(%s [m]\) de haut avec une vitesse de \(%s [m.s^{-1}]\), il possède une énergie mécanique égale à :</p>"%(self.hauteur_1_str,self.vitesse_1_str)
             self.feedback="<p>\(E_m = E_p + E_c \ \leftrightarrow E_m=m \cdot g \cdot h + \\frac{m \cdot v^2}{2} \ \\rightarrow E_m=%s \cdot 10 \cdot %s + \\frac{%s \cdot %s^2}{2} \ \\rightarrow E_m = %s [J]\)</p>"%(self.masse,self.hauteur_1_str,self.masse,self.vitesse_1_str,self.energie_meca_str)
             self.feedback+="<p>Lorsque l'objet est au niveau du sol, toute l'énergie mécanique se trouve sous forme d'énergie cinétique : \(E_m = E_c\).</p>"
             self.feedback+="<p>Donc : \(E_m =E_c =\\frac{m \cdot v^2}{2} \ \leftrightarrow \ v =\sqrt{\\frac{2 \cdot E_m}{m}} \ \\rightarrow \ v =\sqrt{\\frac{2 \cdot %s}{%s}} \ \\rightarrow \ v=%s [m.s^{-1}]\) </p>"%(self.energie_meca_str,self.masse,self.vitesse_0_str)
             
         ###
         if self.choix==10:
             #
             self.enonce="(j) Quelle sera la vitesse d'impact d'un objet de \(%s [kg]\) en chute libre s'il possède une vitesse de \(%s [m.s^{-1}]\) lorsqu'il se trouve à une hauteur de \(%s [m]\)?" %(self.masse,self.vitesse_1_str,self.hauteur_1_str)
             self.reponse='\(v_{impact} =%s [m.s^{-1}]\)' %(self.vitesse_0_str)
             self.reponses_fausses=[]
             for facteur in self.ponderateur:
                 self.reponses_fausses.append("\(v_{impact}=%s [m.s^{-1}]\)" %(convert_sci(self.vitesse_0*facteur)))
             self.feedback=""
             self.feedback="<p>Lorsque l'objet est à \(%s [m]\) de haut avec une vitesse de \(%s [m.s^{-1}]\), il possède une énergie mécanique égale à :</p>"%(self.hauteur_1_str,self.vitesse_1_str)
             self.feedback="<p>\(E_m = E_p + E_c \ \leftrightarrow E_m=m \cdot g \cdot h + \\frac{m \cdot v^2}{2} \ \\rightarrow E_m=%s \cdot 10 \cdot %s + \\frac{%s \cdot %s^2}{2} \ \\rightarrow E_m = %s [J]\)</p>"%(self.masse,self.hauteur_1_str,self.masse,self.vitesse_1_str,self.energie_meca_str)
             self.feedback+="<p>Lorsque l'objet arrive au sol, toute l'énergie mécanique se trouve sous forme d'énergie cinétique : \(E_m = E_c\).</p>"
             self.feedback+="<p>Donc : \(E_m =E_c =\\frac{m \cdot v^2}{2} \ \leftrightarrow \ v =\sqrt{\\frac{2 \cdot E_m}{m}} \ \\rightarrow \ v =\sqrt{\\frac{2 \cdot %s}{%s}} \ \\rightarrow \ v=%s [m.s^{-1}]\) </p>"%(self.energie_meca_str,self.masse,self.vitesse_0_str)
             
         ###
         if self.choix==11:
             #
             self.enonce="(k) Quelle sera la hauteur atteinte par un objet de \(%s [kg]\) lancé vers le haut s'il possède une vitesse de \(%s [m.s^{-1}]\) lorsqu'il se trouve à une hauteur de \(%s [m]\)?" %(self.masse,self.vitesse_1_str,self.hauteur_1_str)
             
             self.reponse='\(h_{max}=%s [m]\)' %(self.hauteur_3_str)
             self.reponses_fausses=[]
             for facteur in self.ponderateur:
                 self.reponses_fausses.append("\(h_{max}=%s [m]\)" %(convert_sci(self.hauteur_3*facteur)))
             self.feedback=""
             self.feedback="<p>Lorsque l'objet est à \(%s [m]\) de haut avec une vitesse de \(%s [m.s^{-1}]\), il possède une énergie mécanique égale à :</p>"%(self.hauteur_1_str,self.vitesse_1_str)
             self.feedback="<p>\(E_m = E_p + E_c \ \leftrightarrow E_m=m \cdot g \cdot h + \\frac{m \cdot v^2}{2} \ \\rightarrow E_m=%s \cdot 10 \cdot %s + \\frac{%s \cdot %s^2}{2} \ \\rightarrow E_m = %s [J]\)</p>"%(self.masse,self.hauteur_1_str,self.masse,self.vitesse_1_str,self.energie_meca_str)
             self.feedback+="<p>Lorsqu'il arrive à sa hauteur maximale, sa vitesse est nulle et toute son énergie mécanique est sous forme d'énergie potentielle : \(E_m = E_p\).</p>"
             self.feedback+="<p>Donc : \(E_m =E_p =m \cdot g \cdot h \ \leftrightarrow \ h =\\frac{E_p}{m \cdot g} \ \\rightarrow \ h =\\frac{%s}{%s \cdot 10}} \ \\rightarrow \ h=%s [m]\) </p>"%(self.energie_meca_str,self.masse,self.hauteur_3_str)
         ###
         if self.choix==12:
             #
             self.enonce="(l) De quelle hauteur faut-il lâcher un objet de \(%s [kg]\) pour qu'il possède une vitesse de \(%s [m.s^{-1}]\) lorsqu'il se trouve à une hauteur de \(%s [m]\)?" %(self.masse,self.vitesse_1_str,self.hauteur_1_str)
             self.reponse='\(h_{init}=%s [m]\)' %(self.hauteur_3_str)
             self.reponses_fausses=[]
             for facteur in self.ponderateur:
                 self.reponses_fausses.append("\(h_{init}=%s [m]\)" %(convert_sci(self.hauteur_3*facteur)))
             
             self.feedback=""
             self.feedback="<p>Lorsque l'objet est à \(%s [m]\) de haut avec une vitesse de \(%s [m.s^{-1}]\), il possède une énergie mécanique égale à :</p>"%(self.hauteur_1_str,self.vitesse_1_str)
             self.feedback="<p>\(E_m = E_p + E_c \ \leftrightarrow E_m=m \cdot g \cdot h + \\frac{m \cdot v^2}{2} \ \\rightarrow E_m=%s \cdot 10 \cdot %s + \\frac{%s \cdot %s^2}{2} \ \\rightarrow E_m = %s [J]\)</p>"%(self.masse,self.hauteur_1_str,self.masse,self.vitesse_1_str,self.energie_meca_str)
             self.feedback+="<p>Lorsqu'il est à sa hauteur de départ, sa vitesse est nulle et toute son énergie mécanique est sous forme d'énergie potentielle : \(E_m = E_p\).</p>"
             self.feedback+="<p>Donc : \(E_m =E_p =m \cdot g \cdot h \ \leftrightarrow \ h =\\frac{E_p}{m \cdot g} \ \\rightarrow \ h =\\frac{%s}{%s \cdot 10}} \ \\rightarrow \ h=%s [m]\) </p>"%(self.energie_meca_str,self.masse,self.hauteur_3_str)
         
         
###      
###      
###      

if __name__=="__main__":
     questionnaire=[]
     for i in range(100):
         question=Question1()
         questionnaire.append(question)
             
     f = open('./exe_energie_I.xml','w')
     
     f.write('<?xml version="1.0" encoding="UTF-8"?> \n')
     f.write('<quiz>  \n')
     f.write('<question type="category">  \n')
     f.write('<category>  \n')
     f.write('<text>$course$/Physique/Energie (I)</text>  \n')
     f.write('</category>  \n')
     f.write('</question>  \n')
     for question in questionnaire:
         f.write('<question type="multichoice">  \n')
         f.write('<name>  \n')
         f.write('<text>Energie cinétique et potentielle</text>  \n')
         f.write('</name>  \n')
         f.write('<questiontext format="html">  \n')
         f.write('<text><![CDATA[<p>%s</p>]]></text>  \n'% question.enonce)
         f.write('</questiontext>  \n')
         f.write('<generalfeedback format="html">  \n')
         f.write('<text>%s</text>  \n' %question.feedback)
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
         f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.reponse)
         f.write('<feedback format="html">  \n')
         f.write('<text></text>  \n')
         f.write('</feedback>  \n')
         f.write('</answer>  \n')
         for reponse_fausse in question.reponses_fausses:
             f.write('<answer fraction="0" format="html">  \n')
             f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%reponse_fausse)
             f.write('<feedback format="html">  \n')
             f.write('<text></text>  \n')
             f.write('</feedback>  \n')
             f.write('</answer>  \n')
         f.write('</question>  \n')
     f.write('</quiz>\n')
     f.close()
     
     ###
     
     questionnaire=[]
     liste=['a','b','c','d','e','f','g','h','i','j','k','l']
     for type_exe in liste:
         for j in range(20):
             if type_exe in ['a','d','g','h']:
                 question=Question2()
                 question.choix=liste.index(type_exe)+1
                 #question.type_exe=type_exe
                 #print (question.type_exe,question.choix)
                 question.gene_exe()
                 questionnaire.append(question)
             
     f = open('./exe_energie_II_simple.xml','w')
     
     f.write('<?xml version="1.0" encoding="UTF-8"?> \n')
     f.write('<quiz>  \n')
     f.write('<question type="category">  \n')
     f.write('<category>  \n')
     f.write('<text>$course$/Physique/Energie (II)/simples</text>  \n')
     f.write('</category>  \n')
     f.write('</question>  \n')
     for question in questionnaire:
         f.write('<question type="multichoice">  \n')
         f.write('<name>  \n')
         f.write("<text>Conservation de l'énergie mécanique</text>  \n")
         f.write('</name>  \n')
         f.write('<questiontext format="html">  \n')
         f.write('<text><![CDATA[<p>%s</p>]]></text>  \n'% question.enonce)
         f.write('</questiontext>  \n')
         f.write('<generalfeedback format="html">  \n')
         f.write('<text><![CDATA[%s]]></text>  \n' %question.feedback)
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
         f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.reponse)
         f.write('<feedback format="html">  \n')
         f.write('<text></text>  \n')
         f.write('</feedback>  \n')
         f.write('</answer>  \n')
         for reponse_fausse in question.reponses_fausses:
             f.write('<answer fraction="0" format="html">  \n')
             f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%reponse_fausse)
             f.write('<feedback format="html">  \n')
             f.write('<text></text>  \n')
             f.write('</feedback>  \n')
             f.write('</answer>  \n')
         f.write('</question>  \n')
     f.write('</quiz>\n')
     f.close()