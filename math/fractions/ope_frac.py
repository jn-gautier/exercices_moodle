#! /usr/bin/python
# -*- coding: utf-8 -*- 

import random

class Fraction:
     def __init__(self):
         self.num=0
         while self.num==0:
             self.num=random.randint(-15,15)
         self.den=0
         while (self.den==0) or (self.den==1) or (self.den==self.num):
             self.den=random.randint(-15,15)
     
     def simplification(self):
         diviseurs_a=[]
         diviseurs_b=[]
         diviseurs_commun=[]
         a=float(self.num)
         b=float(self.den)
         
         max_num_den=max([abs(self.num),abs(self.den)])
         
         for div in xrange(max_num_den):
             if (div !=0) & (div!=1) & (a!=0) & (b!=0):
                 if (a/div==round(a/div)):
                     diviseurs_a.append(div)
                 if (b/div==round(b/div)):
                     diviseurs_b.append(div)
         
         for div in diviseurs_a:
             if div in diviseurs_b:
                 diviseurs_commun.append(div)
         if len (diviseurs_commun)!=0:
             pgdc=max(diviseurs_commun)
             self.num=self.num/pgdc
             self.den=self.den/pgdc
         if (self.num>0) & (self.den<0):
             self.num=self.num*-1
             self.den=self.den*-1
         if (self.num<0) & (self.den<0):
             self.num=self.num*-1
             self.den=self.den*-1
         

class Exe_simple:
     def __init__(self):
         fraction_a=Fraction()
         fraction_b=Fraction()
         
         operation=random.choice(['+','-','*','/'])
         if operation=='+':
             self.enonce="$${ "
             self.enonce_court="\\frac{%s}{%s}" %(fraction_a.num,fraction_a.den)
             self.enonce_court+=" + "
             self.enonce_court+="\\frac{%s}{%s}" %(fraction_b.num,fraction_b.den)
             self.enonce=self.enonce+self.enonce_court
             self.enonce+=" = x"
             self.enonce+="}$$"
             self.reponse=Fraction()
             self.reponse.num=(fraction_a.num*fraction_b.den)+(fraction_b.num*fraction_a.den)
             self.reponse.den=(fraction_a.den*fraction_b.den)
             self.reponse.simplification()
             self.reponse_1="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num,self.reponse.den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_2="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_3="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_4="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
             
             
         if operation=='-':
             self.enonce="$${ "
             self.enonce_court="\\frac{%s}{%s}" %(fraction_a.num,fraction_a.den)
             self.enonce_court+=" - "
             self.enonce_court+="\\frac{%s}{%s}" %(fraction_b.num,fraction_b.den)
             self.enonce=self.enonce+self.enonce_court
             self.enonce+=" = x"
             self.enonce+="}$$"
             self.reponse=Fraction()
             self.reponse.num=(fraction_a.num*fraction_b.den)-(fraction_b.num*fraction_a.den)
             self.reponse.den=(fraction_a.den*fraction_b.den)
             self.reponse.simplification()
             self.reponse_1="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num,self.reponse.den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_2="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_3="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_4="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
             
         if operation=='*':
             self.enonce="$${ "
             self.enonce_court="\\frac{%s}{%s}" %(fraction_a.num,fraction_a.den)
             self.enonce_court+=" \\times "
             self.enonce_court+="\\frac{%s}{%s}" %(fraction_b.num,fraction_b.den)
             self.enonce=self.enonce+self.enonce_court
             self.enonce+=" = x"
             self.enonce+="}$$"
             self.reponse=Fraction()
             self.reponse.num=(fraction_a.num*fraction_b.num)
             self.reponse.den=(fraction_a.den*fraction_b.den)
             self.reponse.simplification()
             self.reponse_1="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num,self.reponse.den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_2="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_3="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_4="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
             
         if operation=='/':
             self.enonce="$${ "
             self.enonce_court="\\frac{%s}{%s}" %(fraction_a.num,fraction_a.den)
             self.enonce_court+=" \div "
             self.enonce_court+="\\frac{%s}{%s}" %(fraction_b.num,fraction_b.den)
             self.enonce=self.enonce+self.enonce_court
             self.enonce+=" = x"
             self.enonce+="}$$"
             self.reponse=Fraction()
             self.reponse.num=(fraction_a.num*fraction_b.den)
             self.reponse.den=(fraction_a.den*fraction_b.num)
             self.reponse.simplification()
             self.reponse_1="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num,self.reponse.den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_2="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_3="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_4="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
         #print self.enonce

class Exe_complexe():
     def __init__(self):
         partie1=Exe_simple()
         partie2=Exe_simple()
         operation=random.choice(['+','-','*','/'])
         if operation=='+':
             self.enonce="$${ ( "
             self.enonce+=partie1.enonce_court
             self.enonce+=" ) + ( "
             self.enonce+=partie2.enonce_court
             self.enonce+=") = x }$$"
             self.reponse=Fraction()
             self.reponse.num=(partie1.reponse.num*partie2.reponse.den)+(partie2.reponse.num*partie1.reponse.den)
             self.reponse.den=(partie1.reponse.den*partie2.reponse.den)
             self.reponse.simplification()
             self.reponse_1="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num,self.reponse.den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_2="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_3="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_4="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
         if operation=='-':
             self.enonce="$${ ( "
             self.enonce+=partie1.enonce_court
             self.enonce+=" ) - ( "
             self.enonce+=partie2.enonce_court
             self.enonce+=") = x }$$"
             self.reponse=Fraction()
             self.reponse.num=(partie1.reponse.num*partie2.reponse.den)-(partie2.reponse.num*partie1.reponse.den)
             self.reponse.den=(partie1.reponse.den*partie2.reponse.den)
             self.reponse.simplification()
             self.reponse_1="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num,self.reponse.den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_2="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_3="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_4="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
         if operation=='*':
             self.enonce="$${ ( "
             self.enonce+=partie1.enonce_court
             self.enonce+=" ) \\times ( "
             self.enonce+=partie2.enonce_court
             self.enonce+=") = x }$$"
             self.reponse=Fraction()
             self.reponse.num=(partie1.reponse.num*partie2.reponse.num)
             self.reponse.den=(partie1.reponse.den*partie2.reponse.den)
             self.reponse.simplification()
             self.reponse_1="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num,self.reponse.den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_2="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_3="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_4="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
         if operation=='/':
             self.enonce="$${ ( "
             self.enonce+=partie1.enonce_court
             self.enonce+=" ) \div ( "
             self.enonce+=partie2.enonce_court
             self.enonce+=") = x }$$"
             self.reponse=Fraction()
             self.reponse.num=(partie1.reponse.num*partie2.reponse.den)
             self.reponse.den=(partie1.reponse.den*partie2.reponse.num)
             self.reponse.simplification()
             self.reponse_1="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num,self.reponse.den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_2="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_3="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)
             if abs(self.reponse.num )>6 : modif_num=random.choice([-3,-2,-1,1,2,3])
             else : modif_num=self.reponse.num
             if self.reponse.den >6 : modif_den=random.choice([-3,-2,-1,1,2,3])
             else : modif_den=0
             self.reponse_4="$$ x= \\frac{%s}{%s} $$" %(self.reponse.num+modif_num,self.reponse.den+modif_den)


if __name__=="__main__":
     
     choix=2
     questionnaire=[]
     if choix==1:
         for i in range(100):
             question=Exe_simple()
             while question.reponse.num==0:
                 question=Exe_simple()
             questionnaire.append(question)
         f = open('./exe_fractions_I.xml','w')
         
         f.write('<?xml version="1.0" encoding="UTF-8"?> \n')
         f.write('<quiz>  \n')
         f.write('<question type="category">  \n')
         f.write('<category>  \n')
         f.write('<text>$course$/Défaut pour math 3TQ/Opération sur les fractions (I)</text>  \n')
         f.write('</category>  \n')
         f.write('</question>  \n')
         i=1
         for question in questionnaire:
             f.write('<question type="multichoice">  \n')
             f.write('<name>  \n')
             f.write('<text>Effectue le calcul et choisi la bonne réponse</text>  \n')
             f.write('</name>  \n')
             f.write('<questiontext format="html">  \n')
             f.write('<text><![CDATA[<p>%s</p>]]></text>  \n'% question.enonce)
             f.write('</questiontext>  \n')
             f.write('<generalfeedback format="html">  \n')
             f.write('<text></text>  \n')
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
             f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.reponse_1)
             f.write('<feedback format="html">  \n')
             f.write('<text></text>  \n')
             f.write('</feedback>  \n')
             f.write('</answer>  \n')
             f.write('<answer fraction="0" format="html">  \n')
             f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.reponse_2)
             f.write('<feedback format="html">  \n')
             f.write('<text></text>  \n')
             f.write('</feedback>  \n')
             f.write('</answer>  \n')
             f.write('<answer fraction="0" format="html">  \n')
             f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.reponse_3)
             f.write('<feedback format="html">  \n')
             f.write('<text></text>  \n')
             f.write('</feedback>  \n')
             f.write('</answer>  \n')
             f.write('<answer fraction="0" format="html">  \n')
             f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.reponse_4)
             f.write('<feedback format="html">  \n')
             f.write('<text></text>  \n')
             f.write('</feedback>  \n')
             f.write('</answer>  \n')
             f.write('</question>  \n')
             i+=1
         f.write('</quiz>\n')
         f.close()
     
     if choix==2:
         for i in range(100):
             question=Exe_complexe()
             while question.reponse.num==0:
                 question=Exe_complexe()
             questionnaire.append(question)
             
         f = open('./exe_fractions_II.xml','w')
         
         f.write('<?xml version="1.0" encoding="UTF-8"?> \n')
         f.write('<quiz>  \n')
         f.write('<question type="category">  \n')
         f.write('<category>  \n')
         f.write('<text>$course$/Défaut pour math 3TQ/Opération sur les fractions (II)</text>  \n')
         f.write('</category>  \n')
         f.write('</question>  \n')
         i=1
         for question in questionnaire:
             f.write('<question type="multichoice">  \n')
             f.write('<name>  \n')
             f.write('<text>Effectue le calcul et choisi la bonne réponse</text>  \n')
             f.write('</name>  \n')
             f.write('<questiontext format="html">  \n')
             f.write('<text><![CDATA[<p>%s</p>]]></text>  \n'% question.enonce)
             f.write('</questiontext>  \n')
             f.write('<generalfeedback format="html">  \n')
             f.write('<text></text>  \n')
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
             f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.reponse_1)
             f.write('<feedback format="html">  \n')
             f.write('<text></text>  \n')
             f.write('</feedback>  \n')
             f.write('</answer>  \n')
             f.write('<answer fraction="0" format="html">  \n')
             f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.reponse_2)
             f.write('<feedback format="html">  \n')
             f.write('<text></text>  \n')
             f.write('</feedback>  \n')
             f.write('</answer>  \n')
             f.write('<answer fraction="0" format="html">  \n')
             f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.reponse_3)
             f.write('<feedback format="html">  \n')
             f.write('<text></text>  \n')
             f.write('</feedback>  \n')
             f.write('</answer>  \n')
             f.write('<answer fraction="0" format="html">  \n')
             f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.reponse_4)
             f.write('<feedback format="html">  \n')
             f.write('<text></text>  \n')
             f.write('</feedback>  \n')
             f.write('</answer>  \n')
             f.write('</question>  \n')
             i+=1
         f.write('</quiz>\n')
         f.close()



