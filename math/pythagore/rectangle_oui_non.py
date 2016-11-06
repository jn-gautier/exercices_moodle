#! /usr/bin/python3
# -*- coding: utf-8 -*- 

import random
import math

     
     #
class Triangle:
     """Un triangle est déterminé par la longueur de ses trois côtés. Le premier sommet se trouve aux coordonnées (0,0). 
     les coordonnées des autres sommets sont déterminées à partir des côtés et du premier sommet."""
     def __init__(self):
         multiplicateur=float(random.randint(1,500))/10
         
         self.coteAC=round(3*multiplicateur,4)
         self.coteAB=round(4*multiplicateur,4)
         self.coteBC=round(5*multiplicateur,4)
         
         
         
         
         choix=random.randint(1,2)
         
         if choix==1 : 
             #on ne change pas les dimensions
             self.rectangle=1
             self.reponse_exacte="<p>Oui, il s'agit d'un triangle rectangle.</p>"
             self.reponse_non_exacte="<p>Non, il ne s'agit pas d'un triangle rectangle.</p>"
             
         if choix==2:
             self.rectangle=0
             self.reponse_exacte="<p>Non, il ne s'agit pas d'un triangle rectangle.</p>"
             self.reponse_non_exacte="<p>Oui, il s'agit d'un triangle rectangle.</p>"
             
             self.coteBC=self.coteBC+1
             
         
         self.xA=0
         self.yA=0
         self.xB=self.coteAB
         self.yB=0
         self.xC=0
         self.yC=self.coteAC
         
         
         self.liste_sommets=[['A','B','C'],['D','E','F'],['I','J','K'],['M','N','O'],['R','S','T'],['X','Y','Z']]
         self.sommets=random.choice(self.liste_sommets)
         self.nom=self.sommets[0]+self.sommets[1]+self.sommets[2]
         self.A=random.choice(self.sommets)
         self.sommets.remove(self.A)
         self.B=random.choice(self.sommets)
         self.sommets.remove(self.B)
         self.C=random.choice(self.sommets)
         
         self.ponderateur=random.choice([[0.4,0.5,0.7,0.8],[0.5,0.7,0.8,1.1],[0.7,0.8,1.1,1.2],[0.8,1.1,1.2,1.4],[1.1,1.2,1.4,1.6]])
        
     
         self.enonce="<p>Dans le triangle %s :<br/>"%(self.nom)
         
         cote_1="%s%s mesure %s cm.<br/>"%(self.A,self.B,self.coteAB)
         cote_2="%s%s mesure %s cm.<br/>"%(self.A,self.C,self.coteAC)
         cote_3="%s%s mesure %s cm. <br/>"%(self.B,self.C,self.coteBC)
         
         liste_cote=[cote_1,cote_2,cote_3]
         
         
         choix_cote=random.choice(liste_cote)
         liste_cote.remove(choix_cote)
         self.enonce+=choix_cote
         
         choix_cote=random.choice(liste_cote)
         liste_cote.remove(choix_cote)
         self.enonce+=choix_cote
         
         choix_cote=random.choice(liste_cote)
         liste_cote.remove(choix_cote)
         self.enonce+=choix_cote
         self.enonce+="</p>"
         self.enonce+="<p>Ce triangle est-il un triangle rectangle?</p>"
         
         self.feedback="<p>D'après le théorème de Pythagore, le triangle %s est rectangle en %s et son hypothénuse est %s%s <b>si</b> :<br/>"%(self.nom,self.A,self.B,self.C)
         self.feedback+="\({%s%s}^2+{%s%s}^2={%s%s}^2\)</p>"%(self.A,self.B,self.A,self.C,self.B,self.C)
         
         self.feedback+="<p>Vérification : <br/>"
         if self.rectangle==1:
             self.feedback+="\({%s}^2+{%s}^2 \overset{?}{=} {%s}^2\)<br/>"%(self.coteAB,self.coteAC,self.coteBC)
             self.feedback+="\({%s}+{%s} \overset{?}{=} {%s}\)<br/>"%(round(self.coteAB**2,4),round(self.coteAC**2,4),round(self.coteBC**2,4))
             self.feedback+="\(%s=%s\)</p>"%(round(self.coteAB**2+self.coteAC**2,4),round(self.coteBC**2,4))
             self.feedback+="<p>Conclusion : <br/>Il s'agit bien d'un triangle rectangle</p>"
         
         if self.rectangle==0:
             self.feedback+="\({%s}^2+{%s}^2 \overset{?}{=} {%s}^2\)<br/>"%(self.coteAB,self.coteAC,self.coteBC)
             self.feedback+="\({%s}+{%s} \overset{?}{=} {%s}\)<br/>"%(round(self.coteAB**2,4),round(self.coteAC**2,4),round(self.coteBC**2,4))
             self.feedback+="\(%s \\neq %s\)</p>"%(round(self.coteAB**2+self.coteAC**2,4),round(self.coteBC**2,4))
             self.feedback+="<p>Conclusion : <br/>Il ne s'agit pas d'un triangle rectangle</p>"
         
         
         
     


if __name__=="__main__":
     questionnaire=[]
     for i in range(50):
         question=Triangle()
         
         questionnaire.append(question)
         
     
     
     f = open('./exe_triangle_rect_vraifaux.xml','w')
     
     f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
     f.write('<quiz>\n')
     f.write('<question type="category">\n')
     f.write('<category>\n')
     f.write('<text>$course$/Théorème de Pythagore/Triangle rectangle - vrai-faux</text>\n')
     f.write('</category>\n')
     f.write('</question>\n')
     for question in questionnaire:
         f.write('<question type="multichoice">  \n')
         f.write('<name>  \n')
         f.write('<text>Le triangle est-il rectangle? V-F</text>  \n')
         f.write('</name>  \n')
         f.write('<questiontext format="html">  \n')
         f.write('<text><![CDATA[%s]]></text>  \n'% question.enonce)
         f.write('</questiontext>  \n')
         f.write('<generalfeedback format="html">  \n')
         f.write('<text><![CDATA[%s]]></text>  \n'%question.feedback)
         f.write('</generalfeedback>  \n')
         f.write('<defaultgrade>1.0000000</defaultgrade>  \n')
         f.write('<penalty>0.3333333</penalty>  \n')
         f.write('<hidden>0</hidden>  \n')
         f.write('<single>true</single>   \n')
         f.write('<shuffleanswers>true</shuffleanswers>  \n')
         
         f.write('<answer fraction="100" format="html">  \n')
         f.write('<text><![CDATA[%s]]></text>  \n'%question.reponse_exacte)
         f.write('<feedback format="html">  \n')
         f.write('<text>Correct!</text>  \n')
         f.write('</feedback>  \n')
         f.write('</answer>  \n')
         
         f.write('<answer fraction="0" format="html">  \n')
         f.write('<text><![CDATA[%s]]></text>  \n'%question.reponse_non_exacte)
         f.write('<feedback format="html">  \n')
         f.write("<text>Désolé, ce n'est pas correct.</text>  \n")
         f.write('</feedback>  \n')
         f.write('</answer>  \n')
         
         f.write('</question>  \n')
     f.write('</quiz>\n')
     
     f.close()
     
