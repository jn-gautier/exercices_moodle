#! /usr/bin/python3
# -*- coding: utf-8 -*- 

import random
from fractions import Fraction

class Exercice:
    def __init__(self):
        self.num=0
        while self.num ==0:
            self.num=random.randint(-10,10)
        
        self.den=1
        while self.den==1:
            self.den=random.randint(2,15)
         
        self.fraction=Fraction(self.num,self.den)
        facteur_1=random.choice([3,4,5,6,7,8,9,11,12,15,16])
        facteur_2=random.choice([-1,1])
        
        self.num=self.num*facteur_1*facteur_2
        self.den=self.den*facteur_1*facteur_2
        
        if self.fraction.denominator==1 : self.__init__()
        
        self.enonce="<p>Simplifie la fraction suivante :</p>"
        self.enonce+="<p>\(\\frac{%s}{%s}\)</p>"%(self.num,self.den)
        
        self.reponse="<p>\(\\frac{%s}{%s}\)</p>"%(self.fraction.numerator,self.fraction.denominator)
        
        self.list_reponses_fausses=[]
        while len(self.list_reponses_fausses)<4:
            if abs(self.fraction.numerator)>3 : 
                modif_num=random.choice([-3,-2,-1,1,2,3])
            else :
                modif_num=self.fraction.numerator*(random.randint(2,5)-1)
            if self.fraction.denominator >3 : 
                modif_den=random.choice([-3,-2,-1,1,2,3])
            else : 
                modif_den=self.fraction.denominator*(random.randint(2,5)-1)
            reponse="<p>\(\\frac{%s}{%s}\)</p>" %(self.fraction.numerator+modif_num,self.fraction.denominator+modif_den)
            if reponse not in self.list_reponses_fausses :
                self.list_reponses_fausses.append(reponse)
                

#class Fraction:
     #def __init__(self):
         #self.num=0
         #while self.num ==0:
             #self.num=random.randint(-100,100)
         #self.den=1
         #while (self.den==self.num) or (self.den in [1,2,4,10,20,40]):
             #self.den=random.randint(2,50)
     
     #def conv_decimal(self):
         #self.decimal=float(self.num)/self.den
         #if self.decimal==round(self.decimal,3):
             #self.limite=1
         #else : self.limite=0
         ##if self.limite==1:
             ##print(self.limite)
     
     #def simplification(self):
         #diviseurs_a=[]
         #diviseurs_b=[]
         #diviseurs_commun=[]
         #a=float(self.num)
         #b=float(self.den)
         
         #max_num_den=max([abs(self.num),abs(self.den)])
         
         #for div in range(max_num_den):
             #if (div !=0) & (div!=1) & (a!=0) & (b!=0):
                 #if (a/div==round(a/div)):
                     #diviseurs_a.append(div)
                 #if (b/div==round(b/div)):
                     #diviseurs_b.append(div)
         
         #for div in diviseurs_a:
             #if div in diviseurs_b:
                 #diviseurs_commun.append(div)
         #if len (diviseurs_commun)!=0:
             #pgdc=max(diviseurs_commun)
             #self.num_s=self.num/pgdc
             #self.den_s=self.den/pgdc
         #else:
             #self.num_s=self.num
             #self.den_s=self.den
         #if (self.num_s>0) & (self.den_s<0):
             #self.num_s=self.num_s*-1
             #self.den_s=self.den_s*-1
         #if (self.num_s<0) & (self.den_s<0):
             #self.num_s=self.num_s*-1
             #self.den_s=self.den_s*-1
         #self.num_s=int(self.num_s)
         #self.den_s=int(self.den_s)



if __name__=="__main__":
     #conv frac_s=>dec
     #conv dec_frac_s
     #simp frac
     questionnaire=[]
     for i in range(100):
         exercice=Exercice()
         print (exercice.num,'/',exercice.den)
         print('####')
         #fraction.simplification()
         #fraction.conv_decimal()
         #while (fraction.limite==0) or (fraction.num==fraction.num_s) or (fraction.den_s==1):
             #fraction=Fraction()
             #fraction.conv_decimal()
             #fraction.simplification()
         
         #fraction.enonce="$$ x= \\frac{%s}{%s} $$"%(fraction.num,fraction.den)
         #fraction.reponse_1="$$ x= \\frac{%s}{%s} $$"%(fraction.num_s,fraction.den_s)
         
         #if abs(fraction.num_s )>3 : modif_num=random.choice([-3,-2,-1,1,2,3])
         #else : modif_num=fraction.num_s
         #if fraction.den_s >3 : modif_den=random.choice([-3,-2,-1,1,2,3])
         #else : modif_den=fraction.den_s
         #fraction.reponse_2="$$ x= \\frac{%s}{%s} $$" %(fraction.num_s+modif_num,fraction.den_s+modif_den)
         
         #if abs(fraction.num_s )>3 : modif_num=random.choice([-3,-2,-1,1,2,3])
         #else : modif_num=fraction.num_s
         #if fraction.den_s >3 : modif_den=random.choice([-3,-2,-1,1,2,3])
         #else : modif_den=fraction.den_s
         #fraction.reponse_3="$$ x= \\frac{%s}{%s} $$" %(fraction.num_s+modif_num,fraction.den_s+modif_den)
         
         #if abs(fraction.num_s )>3 : modif_num=random.choice([-3,-2,-1,1,2,3])
         #else : modif_num=fraction.num_s
         #if fraction.den_s >3 : modif_den=random.choice([-3,-2,-1,1,2,3])
         #else : modif_den=fraction.den_s
         #fraction.reponse_4="$$ x= \\frac{%s}{%s} $$" %(fraction.num_s+modif_num,fraction.den_s+modif_den)
         
         #questionnaire.append(fraction)
         
     #f = open('./exe_simplif_fractions.xml','w')
     
     #f.write('<?xml version="1.0" encoding="UTF-8"?> \n')
     #f.write('<quiz>  \n')
     #f.write('<question type="category">  \n')
     #f.write('<category>  \n')
     #f.write('<text>$course$/Simplification des fractions</text>  \n')
     #f.write('</category>  \n')
     #f.write('</question>  \n')
     #i=1
     #for question in questionnaire:
         #f.write('<question type="multichoice">  \n')
         #f.write('<name>  \n')
         #f.write('<text>Simplification de fraction</text>  \n')
         #f.write('</name>  \n')
         #f.write('<questiontext format="html">  \n')
         #f.write('<text><![CDATA[<p>Simplifie la fraction et choisi la bonne réponse</p><p>%s</p>]]></text>  \n'% question.enonce)
         #f.write('</questiontext>  \n')
         #f.write('<generalfeedback format="html">  \n')
         #f.write('<text></text>  \n')
         #f.write('</generalfeedback>  \n')
         #f.write('<defaultgrade>1.0000000</defaultgrade>  \n')
         #f.write('<penalty>0.3333333</penalty>  \n')
         #f.write('<hidden>0</hidden>  \n')
         #f.write('<single>true</single>   \n')
         #f.write('<shuffleanswers>true</shuffleanswers>  \n')
         #f.write('<answernumbering>abc</answernumbering>  \n')
         #f.write('<correctfeedback format="html">  \n')
         #f.write('<text>Votre réponse est correcte.</text>  \n')
         #f.write('</correctfeedback>  \n')
         #f.write('<incorrectfeedback format="html">  \n')
         #f.write('<text>Votre réponse est incorrecte.</text>  \n')
         #f.write('</incorrectfeedback>  \n')
         #f.write('<shownumcorrect/>  \n')
         #f.write('<answer fraction="100" format="html">  \n')
         #f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.reponse_1)
         #f.write('<feedback format="html">  \n')
         #f.write('<text></text>  \n')
         #f.write('</feedback>  \n')
         #f.write('</answer>  \n')
         #f.write('<answer fraction="0" format="html">  \n')
         #f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.reponse_2)
         #f.write('<feedback format="html">  \n')
         #f.write('<text></text>  \n')
         #f.write('</feedback>  \n')
         #f.write('</answer>  \n')
         #f.write('<answer fraction="0" format="html">  \n')
         #f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.reponse_3)
         #f.write('<feedback format="html">  \n')
         #f.write('<text></text>  \n')
         #f.write('</feedback>  \n')
         #f.write('</answer>  \n')
         #f.write('<answer fraction="0" format="html">  \n')
         #f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.reponse_4)
         #f.write('<feedback format="html">  \n')
         #f.write('<text></text>  \n')
         #f.write('</feedback>  \n')
         #f.write('</answer>  \n')
         #f.write('</question>  \n')
         #i+=1
     #f.write('</quiz>\n')
     #f.close()
