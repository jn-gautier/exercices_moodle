#! /usr/bin/python3
# -*- coding: utf-8 -*- 

import random
import math

     
     #
class Equation:
     """Une équation est une égalité entre deux membres"""
     def __init__(self):
         self.x=0
         while self.x==0:
             self.x=random.randint(-50,50)
         
         self.a=0
         while self.a==0:
             self.a=random.randint(-30,30)
         #
         i=random.choice([0,1,2,4])
         if i==0:
             self.b=i
         else:
             self.b=random.randint(-30,30)
         #
         i=random.choice([0,1,2,4])
         if i==0:
             self.c=i
         else:
             self.c=random.randint(-30,30)
         """A ce stade, il y a une valeur de x et de a non nulles et une valeur de b et de c qui sont comprises entre -30 et 30 zéro compris"""
         """l'équation à la forme (a+c) y + b = (a x + b) + cy ou y est le symbole de l'inconnue"""
         self.a_plus_c=self.a+self.c
         self.ax_plus_b=(self.a*self.x)+self.b
         
         self.div_com_acb=self.div_com(self.a_plus_c,self.b) # permet de faire une mise évidence dans le membre de gauche
         self.div_com_axbc=self.div_com(self.ax_plus_b,self.c) # permet de faire une mise évidence dans le membre de droite
         
         if (len(self.div_com_acb)!=0) & (len(self.div_com_axbc)==0):
             i=random.choice([-1,1])
             div_com=random.choice(self.div_com_acb)
             div_com=div_com*i
             
             self.enonce=""
             self.enonce+=str(div_com)+"( "
             self.enonce+="%sx" %str(int(self.a_plus_c/div_com))
             
             if (self.b/div_com)<0:
                 self.enonce+=" - %s" %(str(int(self.b*-1/div_com)))
             else:
                 self.enonce+=" + %s" %(str(int(self.b/div_com)))
             self.enonce+=" )"
             self.enonce+=" = "
             if self.ax_plus_b !=0:
                 self.enonce+=str(self.ax_plus_b)
             if self.c!=0:
                 if self.c<0:
                     self.enonce+=" - %sx" %(str(self.c*-1))
                 else:
                     self.enonce+=" + %sx" %(str(self.c)) 
             if ((self.ax_plus_b==0) & (self.c==0)):
                 self.enonce+="0"
             
         elif (len(self.div_com_acb)==0) & (len(self.div_com_axbc)!=0):
             
             i=random.choice([-1,1])
             div_com=random.choice(self.div_com_axbc)
             div_com=div_com*i
             self.enonce=""
             if self.a_plus_c!=0:
                 self.enonce+="%sx" %str(self.a_plus_c)
             if self.b!=0:
                 if self.b<0:
                     self.enonce+=" - %s" %(str(self.b*-1))
                 else:
                     self.enonce+=" + %s" %(str(self.b))
             if (self.a_plus_c==0) & (self.b==0):
                 self.enonce+="0"
             self.enonce+=" = "
             self.enonce+=str(div_com)
             self.enonce+="( "
             self.enonce+=str(int(self.ax_plus_b/div_com))
             if (self.c/div_com)<0:
                 self.enonce+=" - %sx" %(str(int(self.c*-1/div_com)))
             else:
                 self.enonce+=" + %sx" %(str(int(self.c/div_com)))
             self.enonce+=" )"
             
         elif (len(self.div_com_acb)!=0) & (len(self.div_com_axbc)!=0):
             i=random.choice([-1,1])
             div_com=random.choice(self.div_com_acb)
             div_com=div_com*i
             
             self.enonce=""
             self.enonce+=str(div_com)+"( "
             self.enonce+="%sx" %str(int(self.a_plus_c/div_com))
             
             if (self.b/div_com)<0:
                 self.enonce+=" - %s" %(str(int(self.b*-1/div_com)))
             else:
                 self.enonce+=" + %s" %(str(int(self.b/div_com)))
             self.enonce+=" )"
             self.enonce+=" = "
             
             i=random.choice([-1,1])
             div_com=random.choice(self.div_com_axbc)
             div_com=div_com*i
             
             self.enonce+=str(div_com)
             self.enonce+="( "
             self.enonce+=str(int(self.ax_plus_b/div_com))
             if (self.c/div_com)<0:
                 self.enonce+=" - %sx" %(str(int(self.c*-1/div_com)))
             else:
                 self.enonce+=" + %sx" %(str(int(self.c/div_com)))
             self.enonce+=" )"
         
         else:
             self.enonce=""
             if self.a_plus_c!=0:
                 self.enonce+="%sx" %str(self.a_plus_c)
             if self.b!=0:
                 if self.b<0:
                     self.enonce+=" - %s" %(str(self.b*-1))
                 else:
                     self.enonce+=" + %s" %(str(self.b))
             if (self.a_plus_c==0) & (self.b==0):
                 self.enonce+="0 "
             self.enonce+=" = "
             if self.ax_plus_b !=0:
                 self.enonce+=str(self.ax_plus_b)
             if self.c!=0:
                 if self.c<0:
                     self.enonce+=" - %sx" %(str(self.c*-1))
                 else:
                     self.enonce+=" + %sx" %(str(self.c)) 
             if ((self.ax_plus_b==0) & (self.c==0)):
                 self.enonce+="0"
         #
         self.reponse=str(self.x)
         self.reponse2=str(self.x*-1)
         
     def div_com(self,a,b):
         diviseurs_a=[]
         diviseurs_b=[]
         diviseurs_commun=[]
         a=float(a)
         b=float(b)
         
         for div in range(100):
             if (div !=0) & (div!=1) & (a!=0) & (b!=0):
                 if (a/div==round(a/div)):
                     diviseurs_a.append(div)
                 if (b/div==round(b/div)):
                     diviseurs_b.append(div)
         
         for div in diviseurs_a:
             if div in diviseurs_b:
                 diviseurs_commun.append(div)
         return diviseurs_commun
     #


if __name__=="__main__":
     questionnaire=[]
     for i in range(200):
         question=Equation()
         print (question.enonce,question.reponse)
         questionnaire.append(question)
         
     
     
     f = open('./exe_eqn_1deg.xml','w')
     
     f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
     f.write('<quiz>\n')
     f.write('<!-- question: 0  -->\n')
     f.write('<question type="category">\n')
     f.write('<category>\n')
     f.write('<text>Défaut pour math 3TQ/Équations premier degré une inconnue</text>\n')
     f.write('</category>\n')
     f.write('</question>\n')
     for question in questionnaire:
        #f.write('<!-- question: %s  -->\n'%i)
        f.write('<question type="numerical">\n')
        f.write('<name>\n')
        f.write('<text>Équation du premier degré à une inconnue</text>\n')
        f.write('</name>\n')
        f.write('<questiontext format="html">\n')
        f.write('<text><![CDATA[<p>$$ ')
        f.write(question.enonce)
        f.write(' $$</p>]]></text>\n')
        f.write('</questiontext>\n')
        f.write('<generalfeedback format="html">\n')
        f.write('<text></text>\n')
        f.write('</generalfeedback>\n')
        f.write('<defaultgrade>1.0000000</defaultgrade>\n')
        f.write('<penalty>0.3333333</penalty>\n')
        f.write('<hidden>0</hidden>\n')
        f.write('<answer fraction="100" format="moodle_auto_format">\n')
        f.write('<text>')
        f.write(question.reponse)
        f.write('</text>\n')
        f.write('<feedback format="html">\n')
        f.write('<text></text>\n')
        f.write('</feedback>\n')
        f.write('<tolerance>0</tolerance>\n')
        f.write('</answer>\n')
        f.write('<answer fraction="50" format="moodle_auto_format">\n')
        f.write('<text>')
        f.write(question.reponse2)
        f.write('</text>\n')
        f.write('<feedback format="html">\n')
        f.write('<text><![CDATA[<p>Erreur de signe.</p>]]></text>\n')
        f.write('</feedback>\n')
        f.write('<tolerance>0</tolerance>\n')
        f.write('</answer>\n')
        f.write('<unitgradingtype>0</unitgradingtype>\n')
        f.write('<unitpenalty>0.1000000</unitpenalty>\n')
        f.write('<showunits>3</showunits>\n')
        f.write('<unitsleft>0</unitsleft>\n')
        f.write('</question>\n')
        i+=1
     f.write('</quiz>\n')
     
     f.close()
