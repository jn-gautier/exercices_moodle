#! /usr/bin/python3
# -*- coding: utf-8 -*- 

import random
import math

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
         self.x_a=random.randint(-20,-11)
         self.y_a=self.x_a*self.m+self.p
         
         self.x_b=random.randint(-10,-1)
         self.y_b=self.x_b*self.m+self.p
         
         self.x_c=random.randint(1,10)
         self.y_c=self.x_c*self.m+self.p
         
         self.x_d=random.randint(11,20)
         self.y_d=self.x_d*self.m+self.p
         
         #choix=random.randint(1,6)
         choix=1
         
         if choix==1:
             self.enonce="<p>Complète le tableau suivant : </p>"
             self.enonce+='<table border=1 style="border-collapse:collapse"> <tr> <td colspan="2" style="height: 50px">\(F \\equiv y=%s x+( %s)\)</td></tr>'%(self.m,self.p)
             self.enonce+='<tr><td style="height: 50px;width:150px"> \(X\) </td><td style="height: 50px;width:150px">\(Y\)</td></tr>'
             self.enonce+='<tr><td style="height: 50px"> %s </td><td>{1:NUMERICAL:=%s}</td></tr>'%(self.x_a,self.y_a)
             self.enonce+='<tr><td style="height: 50px"> %s </td><td>{1:NUMERICAL:=%s}</td></tr>'%(self.x_b,self.y_b)
             self.enonce+='<tr><td style="height: 50px"> %s </td><td>{1:NUMERICAL:=%s}</td></tr>'%(self.x_c,self.y_c)
             self.enonce+='<tr><td style="height: 50px"> %s </td><td>{1:NUMERICAL:=%s}</td></tr>'%(self.x_d,self.y_d)
             self.enonce+="</table>"
             
             self.feedback_g=""
             self.feedback_g+='<table border=1 style="border-collapse:collapse"> <tr> <td colspan="2" style="height: 50px">\(F \\equiv y=%s x+( %s)\)</td></tr>'%(self.m,self.p)
             self.feedback_g+='<tr><td style="height: 50px;width:150px"> \(X\) </td><td style="width:300px">\(Y\)</td></tr>'
             self.feedback_g+='<tr><td style="height: 50px"> %s </td><td>\(y=%s \cdot %s + (%s) \ \\rightarrow \ y=%s\)</td></tr>'%(self.x_a,self.m,self.x_a,self.p,self.y_a)
             self.feedback_g+='<tr><td style="height: 50px"> %s </td><td>\(y=%s \cdot %s + (%s) \ \\rightarrow \ y=%s\)</td></tr>'%(self.x_b,self.m,self.x_b,self.p,self.y_b)
             self.feedback_g+='<tr><td style="height: 50px"> %s </td><td>\(y=%s \cdot %s + (%s) \ \\rightarrow \ y=%s\)</td></tr>'%(self.x_c,self.m,self.x_c,self.p,self.y_c)
             self.feedback_g+='<tr><td style="height: 50px"> %s </td><td>\(y=%s \cdot %s + (%s) \ \\rightarrow \ y=%s\)</td></tr>'%(self.x_d,self.m,self.x_d,self.p,self.y_d)
             self.feedback_g+='</table>'
             
        
     #


if __name__=="__main__":
     questionnaire=[]
     for i in range(50):
         question=Fonction()
         #print (question.enonce,question.reponse)
         questionnaire.append(question)
         
     
     
     f = open('./exe_tableau_fct.xml','w')
     
     f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
     f.write('<quiz>\n')
     f.write('<question type="category">\n')
     f.write('<category>\n')
     f.write('<text>$course$/Tableau de valeurs</text>\n')
     f.write('</category>\n')
     f.write('</question>\n')
     for question in questionnaire:
        #f.write('<!-- question: %s  -->\n'%i)
        f.write('<question type="cloze"> \n')
        f.write('<name>\n')
        f.write("<text>Compléter un tableau de valeurs.</text>\n")
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
        f.write('</question>\n')
     f.write('</quiz>\n')
     
     f.close()
     
    
