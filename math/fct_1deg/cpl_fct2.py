#! /usr/bin/python3
# -*- coding: utf-8 -*- 

import random
import math

     
     #
class Equation:
     def __init__(self):
        self.a=random.randint(-10,10)
        while self.a==0 : self.a=random.randint(-10,10)
        self.b=random.randint(-15,15)
        while self.b==0 : self.b=random.randint(-10,10)
        self.x=random.randint(-5,5)
        self.y=self.a*self.x+self.b
        
        
        if self.a==1:carac_a=""
        elif self.a==-1:carac_a="-"
        else :carac_a=self.a
        
        if self.b<0:signe_b="-"
        else:signe_b="+"
        
        self.latex="y=%sx%s%s"%(carac_a,signe_b,abs(self.b))
        choix=random.choice([1,2])
        
        if choix==1:
            self.enonce="<p>Le point A, de coordonnées \((x_A ; y_A)\), appartient au graphique de la fonction \(F \\equiv %s\).</p>"%(self.latex)
            self.enonce+="<p>Qu'elle est l'abscisse de A, \(x_A\), si son ordonnée, \(y_A\), vaut %s?</p>"%self.y
            
            self.reponse=self.x
            
            self.feedback="<p>\(y=m \cdot x +p \\ \\rightarrow \\ x=\\frac{y-p}{m}\)</p>"
            self.feedback+="<p>\(x_A = \\frac{%s-%s}{%s} \\ \\rightarrow \\ x_A =%s\)</p>"%(self.y,self.b,self.a,self.x)
            
        if choix==2:
            self.enonce="<p>Le point A, de coordonnées \((x_A ; y_A)\), appartient au graphique de la fonction \(F \\equiv %s\).</p>"%(self.latex)
            self.enonce+="<p>Qu'elle est l'ordonnée de A, \(y_A\), si son abscisse, \(x_A\), vaut %s?</p>"%self.x
            
            self.reponse=self.y
            
            self.feedback="<p>\(y=m \cdot x +p \)</p>"
            self.feedback+="<p>\(y_A =%s \cdot %s + %s \\ \\rightarrow \\ y_A =%s\)</p>"%(self.a,self.x,self.b,self.y)
        
        

if __name__=="__main__":
     questionnaire=[]
     for i in range(40):
         question=Equation()
         questionnaire.append(question)
         
     
     
     f = open('./couple_fct_2.xml','w')
     
     f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
     f.write('<quiz>\n')
     f.write('<question type="category">\n')
     f.write('<category>\n')
     f.write("<text>Défaut pour math 4TQ/Couple et graphique d'une fonction - 2</text>\n")
     f.write('</category>\n')
     f.write('</question>\n')
     
     for question in questionnaire:
        f.write('<question type="numerical">\n')
        f.write('<name>\n')
        f.write('<text>Calcule la coordonnée manquante</text>\n')
        f.write('</name>\n')
        f.write('<questiontext format="html">\n')
        f.write('<text><![CDATA[')
        f.write(question.enonce)
        f.write(']]></text>\n')
        f.write('</questiontext>\n')
        f.write('<generalfeedback format="html">\n')
        #print (question.feedback)
        f.write('<text><![CDATA[')
        f.write(question.feedback)
        f.write(']]></text>\n')
        f.write('</generalfeedback>\n')
        f.write('<defaultgrade>1.0000000</defaultgrade>\n')
        f.write('<penalty>0.3333333</penalty>\n')
        f.write('<hidden>0</hidden>\n')
        f.write('<answer fraction="100" format="moodle_auto_format">\n')
        f.write('<text>')
        f.write(str(question.reponse))
        f.write('</text>\n')
        f.write('<feedback format="html">\n')
        f.write('<text></text>\n')
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
     
    
