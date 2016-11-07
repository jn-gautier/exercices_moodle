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
        self.y_true=self.a*self.x+self.b
        modif=random.randint(-3,3)
        while modif==0 : modif=random.randint(-3,3)
        self.y_false=self.y_true+modif
        
        if self.a==1:carac_a=""
        elif self.a==-1:carac_a="-"
        else :carac_a=self.a
        
        if self.b<0:signe_b="-"
        else:signe_b="+"
        
        self.latex="y=%sx%s%s"%(carac_a,signe_b,abs(self.b))
        choix=random.choice([1,2])
        
        if choix==1:
            self.enonce="Le couple de coordonnées (%s ; %s) appartient-il au graphique de la fonction dont l'équation est donnée ci-dessous?"%(self.x,self.y_true)
            self.enonce+="$$ %s $$"%self.latex
            self.feedback="$$ %s=%s \cdot %s %s %s$$"%(self.y_true,self.a,self.x,signe_b,abs(self.b))
            self.true=100
            self.false=0
        if choix==2:
            self.enonce="Le couple de coordonnées (%s ; %s) appartient-il au graphique de la fonction dont l'équation est donnée ci-dessous?"%(self.x,self.y_false)
            self.enonce+="$$ %s $$"%self.latex
            self.feedback="$$ %s \\neq %s \cdot %s %s %s $$"%(self.y_false,self.a,self.x,signe_b,abs(self.b))
            self.true=0
            self.false=100
        
        

if __name__=="__main__":
     questionnaire=[]
     for i in range(40):
         question=Equation()
         questionnaire.append(question)
         
     
     
     f = open('./couple_fct.xml','w')
     
     f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
     f.write('<quiz>\n')
     f.write('<!-- question: 0  -->\n')
     f.write('<question type="category">\n')
     f.write('<category>\n')
     f.write("<text>Défaut pour math 4TQ/Couple et graphique d'une fonction</text>\n")
     f.write('</category>\n')
     f.write('</question>\n')
     for question in questionnaire:
        f.write('<question type="truefalse">\n')
        f.write('<name>\n')
        f.write('<text>Couple et graphique</text>\n')
        f.write('</name>\n')
        f.write('<questiontext format="html">\n')
        f.write('<text><![CDATA[<p> ')
        f.write(question.enonce)
        f.write(' </p>]]></text>\n')
        f.write('</questiontext>\n')
        f.write('<generalfeedback format="html">\n')
        f.write('<text>')
        f.write(question.feedback)
        f.write('</text>\n')
        f.write('</generalfeedback>\n')
        f.write('<defaultgrade>1.0000000</defaultgrade>\n')
        f.write('<penalty>0.3333333</penalty>\n')
        f.write('<hidden>0</hidden>\n')
        f.write('<answer fraction="%s" format="moodle_auto_format">\n'%question.true)
        f.write('<text>true</text>\n')
        f.write('<feedback format="html">\n')
        f.write('<text></text>\n')
        f.write('</feedback>\n')
        f.write('</answer>\n')
        f.write('<answer fraction="%s" format="moodle_auto_format">\n'%question.false)
        f.write('<text>false</text>\n')
        f.write('<feedback format="html">\n')
        f.write('<text></text>\n')
        f.write('</feedback>\n')
        f.write('</answer>\n')
        f.write('</question>\n')
     f.write('</quiz>\n')
     
     f.close()
     
    
