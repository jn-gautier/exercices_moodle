#! /usr/bin/python3
# -*- coding: utf-8 -*- 

import random
import math

     
     #
class Fonction:
     """Une fonction est déterminée par son équation. Cette équation est celle d'une droite"""
     def __init__(self):
         self.m=0
         while self.m==0:
             self.m=random.randint(-7,7)
         
         self.p=0
         while self.p==0:
             self.p=random.randint(-15,15)
         #
         self.x_a=0
         while self.x_a==0:
             self.x_a=random.randint(-20,20)
         self.y_a=self.x_a*self.m+self.p
         
         self.x_b=0
         while (self.x_b==0) or (self.x_b==self.x_a):
             self.x_b=random.randint(-20,20)
         self.y_b=self.x_b*self.m+self.p
         
         self.x_c=0
         while (self.x_c==0) or (self.x_c==self.x_a) or (self.x_c==self.x_b):
             self.x_c=random.randint(-20,20)
         self.y_c=self.x_c*self.m+self.p
         
         choix=random.randint(1,6)
         #choix=4
         
         if choix==1:
             self.enonce="<p>Une droite passe par le point \(A\) de coordonnées \( (%s \,;\, %s) \)" %(self.x_a,self.y_a)
             self.enonce+=" et le point \(B\) de coordonnées \( (%s \,;\, %s) \).</p>"%(self.x_b,self.y_b)
             self.enonce+="<p>Si le point \(C\) appartient à cette droite," 
             self.enonce+=" et que \(y_C\) vaut %s, quelle est l'abscisse de \(C\)? </p>"%(self.y_c)
             
             self.reponse=str(self.x_c)
             
             self.feedback_g=""
             self.feedback_g+="<p>Puisqu'on connait les coordonnées de deux points, on peut calculer la pente.</p>"
             self.feedback_g+="<p>\(m=\\frac{y_a - y_b}{x_a - x_b}  \ \\rightarrow \ m=\\frac{%s - (%s)}{%s - (%s)} \ \\rightarrow \ m=%s \)</p>"%(self.y_a,self.y_b,self.x_a,self.x_b,self.m)
             self.feedback_g+="<p>Puisqu'on connait maintenant la valeur de la pente et les coordonnées d'un point, on peut écrire : </p>"
             self.feedback_g+="<p>\(y=m \cdot x + p \ \\rightarrow \ y_a=m \cdot x_a + p \ \\rightarrow \ p=y_a-m \cdot x_a \ \\rightarrow \ p=%s \ - \ %s \cdot %s \ \\rightarrow \ p=%s\)</p>"%(self.y_a,self.m,self.x_a,self.p)  
             self.feedback_g+="<p>L'équation de la droite est donc : \( y=%sx+(%s) \).</p>"%(self.m,self.p)
             self.feedback_g+="<p>Donc : \(y_c=%s \cdot x_c + %s \ \\rightarrow \ x_c=\\frac{y_c - %s}{%s} \ \\rightarrow \ "
             #self.feedback_g+="<p>Donc : \( %s=%s \cdot x_c +(%s) \ \\rightarrow \ "%(self.y_c,self.m,self.p)
             self.feedback_g+="x_c =\\frac{%s -(%s)}{%s} \ \\rightarrow \ x_c=%s\)</p>"%(self.y_c,self.p,self.m,self.x_c)
             self.feedback_g+="<p>Et : \( C : (%s \,;\, %s) \) </p>"%(self.x_c,self.y_c)
             
             self.feedback_q="\( C : (%s \,;\, %s) \)"%(self.x_c,self.y_c)
        #
         if choix==2:
             self.enonce="<p>Une droite passe par le point \(A\) de coordonnées \( (%s \,;\, %s) \)" %(self.x_a,self.y_a)
             self.enonce+=" et le point \(B\) de coordonnées \( (%s \,;\, %s) \).</p>"%(self.x_b,self.y_b)
             self.enonce+="<p>Si le point \(C\) appartient à cette droite," 
             self.enonce+=" et que \(x_C\) vaut %s, quelle est l'ordonnée de \(C\)? </p>"%(self.x_c)
             
             self.reponse=str(self.y_c)
             
             self.feedback_g=""
             self.feedback_g+="<p>Puisqu'on connait les coordonnées de deux points, on peut calculer la pente.</p>"
             self.feedback_g+="<p>\(m=\\frac{y_a - y_b}{x_a - x_b}  \ \\rightarrow \ m=\\frac{%s - (%s)}{%s - (%s)} \ \\rightarrow \ m=%s \)</p>"%(self.y_a,self.y_b,self.x_a,self.x_b,self.m)
             self.feedback_g+="<p>Puisqu'on connait la valeur de la pente et les coordonnées d'un point, on peut écrire : </p>"
             self.feedback_g+="<p>\(y=m \cdot x + p \ \\rightarrow \ y_a=m \cdot x_a + p \ \\rightarrow \ %s=%s \cdot %s + p \ \\rightarrow \ p=%s \ - \ (%s \cdot %s) \ \\rightarrow \ p=%s\)</p>"%(self.y_a,self.m,self.x_a,self.y_a,self.m,self.x_a,self.p)  
             self.feedback_g+="<p>L'équation de la droite est donc : \( y=%sx+(%s) \).</p>"%(self.m,self.p)
             self.feedback_g+="<p>Donc : \( y_c=%s \cdot %s+(%s) \ \\rightarrow \ y_c=%s \)"%(self.m,self.x_c,self.p,self.y_c)
             self.feedback_g+="<p>Et : \( C : (%s \,;\, %s) \) </p>"%(self.x_c,self.y_c)
             
             self.feedback_q="\( C : (%s \,;\, %s) \)"%(self.x_c,self.y_c)
        #
         if choix==3:
             self.enonce="<p>Une droite passe par le point \(A\) de coordonnées \( (%s \,;\, %s) \). " %(self.x_a,self.y_a)
             self.enonce+="La pente de cette droite vaut : \(m=%s\).</p>"%(self.m)
             self.enonce+="<p>Si le point \(C\) appartient à cette droite," 
             self.enonce+=" et que \(x_C\) vaut %s, quelle est l'ordonnée de \(C\)? </p>"%(self.x_c)
             
             self.reponse=str(self.y_c)
             
             self.feedback_g=""
             self.feedback_g+="<p>Puisqu'on connait la valeur de la pente et les coordonnées d'un point, on peut écrire : </p>"
             self.feedback_g+="<p>\(y=m \cdot x + p \ \\rightarrow \ y_a=m \cdot x_a + p \ \\rightarrow \ %s=%s \cdot %s + p \ \\rightarrow \ p=%s \ - \ (%s \cdot %s) \ \\rightarrow \ p=%s\)</p>"%(self.y_a,self.m,self.x_a,self.y_a,self.m,self.x_a,self.p)  
             self.feedback_g+="<p>L'équation de la droite est donc : \( y=%sx+(%s) \).</p>"%(self.m,self.p)
             self.feedback_g+="<p>Donc : \( y_c=%s \cdot %s+(%s) \ \\rightarrow \ y_c=%s \)"%(self.m,self.x_c,self.p,self.y_c)
             self.feedback_g+="<p>Et : \( C : (%s \,;\, %s) \) </p>"%(self.x_c,self.y_c)
             
             self.feedback_q="\( C : (%s \,;\, %s) \)"%(self.x_c,self.y_c)
        #
         if choix==4:
             self.enonce="<p>Une droite passe par le point \(A\) de coordonnées \( (%s \,;\, %s) \). " %(self.x_a,self.y_a)
             self.enonce+="La pente de cette droite vaut : \(m=%s\).</p>"%(self.m)
             self.enonce+="<p>Si le point \(C\) appartient à cette droite," 
             self.enonce+=" et que \(y_C\) vaut %s, quelle est l'abscisse de \(C\)? </p>"%(self.y_c)
             
             self.reponse=str(self.x_c)
             
             self.feedback_g=""
             self.feedback_g+="<p>Puisqu'on connait la valeur de la pente et les coordonnées d'un point, on peut écrire : </p>"
             self.feedback_g+="<p>\(y=m \cdot x + p \ \\rightarrow \ y_a=m \cdot x_a + p \ \\rightarrow \ %s=%s \cdot %s + p \ \\rightarrow \ p=%s \ - \ (%s \cdot %s) \ \\rightarrow \ p=%s\)</p>"%(self.y_a,self.m,self.x_a,self.y_a,self.m,self.x_a,self.p)  
             self.feedback_g+="<p>L'équation de la droite est donc : \( y=%sx+(%s) \).</p>"%(self.m,self.p)
             self.feedback_g+="<p>Donc : \( %s=%s \cdot x_c+(%s) \) </p>"%(self.y_c,self.m,self.p)
             self.feedback_g+="<p>Donc : \( x_c=\\frac{%s -(%s)}{%s} \ \\rightarrow \ x_c=%s \)</p>"%(self.y_c,self.p,self.m,self.x_c)
             self.feedback_g+="<p>Et : \( C : (%s \,;\, %s) \) </p>"%(self.x_c,self.y_c)
             
             self.feedback_q="\( C : (%s \,;\, %s) \)"%(self.x_c,self.y_c)
        #
         if choix==5:
             self.enonce="<p>Une droite passe par le point \(A\) de coordonnées \( (%s \,;\, %s) \). " %(self.x_a,self.y_a)
             self.enonce+="L'ordonnée à l'origine de cette droite vaut : \(p=%s\).</p>"%(self.p)
             self.enonce+="<p>Si le point \(C\) appartient à cette droite," 
             self.enonce+=" et que \(x_C\) vaut %s, quelle est l'ordonnée de \(C\)? </p>"%(self.x_c)
             
             self.reponse=str(self.y_c)
             
             
             self.feedback_g=""
             self.feedback_g+="<p>Puisqu'on connait la valeur de l'ordonnée à l'origine et les coordonnées d'un point, on peut écrire : </p>"
             self.feedback_g+="<p>\(y=m \cdot x + p \ \\rightarrow \ y_a=m \cdot x_a + p \ \\rightarrow \ %s=m \cdot %s + %s \ \\rightarrow \ m=\\frac{%s - %s}{%s}\ \\rightarrow \ m=%s\)</p>"%(self.y_a,self.x_a,self.p,self.y_a,self.p,self.x_a,self.m)  
             self.feedback_g+="<p>L'équation de la droite est donc : \( y=%sx+(%s) \).</p>"%(self.m,self.p)
             self.feedback_g+="<p>Donc : \( y_c=%s \cdot %s+(%s) \ \\rightarrow \ y_c=%s \)"%(self.m,self.x_c,self.p,self.y_c)
             self.feedback_g+="<p>Et : \( C : (%s \,;\, %s) \) </p>"%(self.x_c,self.y_c)
             
             self.feedback_q="\( C : (%s \,;\, %s) \)"%(self.x_c,self.y_c)
        #
         if choix==6:
             self.enonce="<p>Une droite passe par le point \(A\) de coordonnées \( (%s \,;\, %s) \). " %(self.x_a,self.y_a)
             self.enonce+="L'ordonnée à l'origine de cette droite vaut : \(p=%s\).</p>"%(self.p)
             self.enonce+="<p>Si le point \(C\) appartient à cette droite," 
             self.enonce+=" et que \(y_C\) vaut %s, quelle est l'abscisse de \(C\)? </p>"%(self.y_c)
             
             self.reponse=str(self.x_c)
             
             self.feedback_g=""
             self.feedback_g+="<p>Puisqu'on connait la valeur de l'ordonnée à l'origine et les coordonnées d'un point, on peut écrire : </p>"
             self.feedback_g+="<p>\(y=m \cdot x + p \ \\rightarrow \ y_a=m \cdot x_a + p \ \\rightarrow \ %s=m \cdot %s + %s \ \\rightarrow \ m=\\frac{%s - %s}{%s}\ \\rightarrow \ m=%s\)</p>"%(self.y_a,self.x_a,self.p,self.y_a,self.p,self.x_a,self.m)  
             self.feedback_g+="<p>L'équation de la droite est donc : \( y=%sx+(%s) \).</p>"%(self.m,self.p)
             self.feedback_g+="<p>Donc : \( %s=%s \cdot x_c+(%s) \) </p>"%(self.y_c,self.m,self.p)
             self.feedback_g+="<p>Donc : \( x_c=\\frac{%s -(%s)}{%s} \ \\rightarrow \ x_c=%s \)</p>"%(self.y_c,self.p,self.m,self.x_c)
             self.feedback_g+="<p>Et : \( C : (%s \,;\, %s) \) </p>"%(self.x_c,self.y_c)
             
             self.feedback_q="\( C : (%s \,;\, %s) \)"%(self.x_c,self.y_c)
     #


if __name__=="__main__":
     questionnaire=[]
     for i in range(120):
         question=Fonction()
         #print (question.enonce,question.reponse)
         questionnaire.append(question)
         
     
     
     f = open('./exe_trouv_eqn_droite.xml','w')
     
     f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
     f.write('<quiz>\n')
     f.write('<!-- question: 0  -->\n')
     f.write('<question type="category">\n')
     f.write('<category>\n')
     f.write('<text>$course$/Rechercher équation droite</text>\n')
     f.write('</category>\n')
     f.write('</question>\n')
     for question in questionnaire:
        #f.write('<!-- question: %s  -->\n'%i)
        f.write('<question type="numerical">\n')
        f.write('<name>\n')
        f.write("<text>Trouver l'équation d'une droite puis les coordonnées d'un point.</text>\n")
        f.write('</name>\n')
        f.write('<questiontext format="html">\n')
        f.write('<text><![CDATA[ ')
        f.write(question.enonce)
        f.write(']]></text>\n')
        f.write('</questiontext>\n')
        f.write('<generalfeedback format="html">\n')
        f.write('<text><![CDATA[ ')
        f.write(question.feedback_g)
        f.write(']]></text>\n')
        f.write('</generalfeedback>\n')
        f.write('<defaultgrade>1.0000000</defaultgrade>\n')
        f.write('<penalty>0.3333333</penalty>\n')
        f.write('<hidden>0</hidden>\n')
        f.write('<answer fraction="100" format="moodle_auto_format">\n')
        f.write('<text>')
        f.write(question.reponse)
        f.write('</text>\n')
        f.write('<feedback format="html">\n')
        f.write('<text><![CDATA[ ')
        f.write(question.feedback_q)    
        f.write(']]></text>\n')
        f.write('</feedback>\n')
        f.write('<tolerance>0</tolerance>\n')
        f.write('</answer>\n')
        f.write('<unitgradingtype>0</unitgradingtype>\n')
        f.write('<unitpenalty>0.1000000</unitpenalty>\n')
        f.write('<showunits>3</showunits>\n')
        f.write('<unitsleft>0</unitsleft>\n')
        f.write('</question>\n')
     f.write('</quiz>\n')
     
     f.close()
     
    
