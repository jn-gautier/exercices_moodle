#! /usr/bin/python3
# -*- coding: utf-8 -*- 

import random
import math


class SolutionUnique:
     def __init__(self):
         self.x=random.randint(-50,50)
         self.y=random.randint(-50,50)

class Membre:
     """Un membre est une expression du type : ay+bx+c"""
     def __init__(self):
         self.a=0
         self.b=0
         self.c=0
     #
     def necessaire (self,solution):
         self.a=-1
         self.b=random.randint(-15,15)
         self.c=(-1*self.a*solution.y)-(self.b*solution.x)
     
     
     #
class Equation:
     """Une équation est une égalité entre deux membres"""
     def __init__(self,membre_gauche,membre_droite):
         self.membre_gauche=membre_gauche
         self.membre_droite=membre_droite
     #
     def modif_equivalente(self):
         a=random.randint(-15,15)
         #print "a : ",a
         self.membre_gauche.a+=a
         self.membre_droite.a+=a
         b=random.randint(-15,15)
         #print "b : ",b
         self.membre_gauche.b+=b
         #print 'mbg b : ',self.membre_gauche.b
         self.membre_droite.b+=b
         
         c=random.randint(-15,15)
         #print "c : ",c
         self.membre_gauche.c+=c
         self.membre_droite.c+=c
         d=0
         while (d==0):
             d=random.randint(-5,5)
         #print "d : ",d
         self.membre_gauche.a=self.membre_gauche.a*d
         self.membre_droite.a=self.membre_droite.a*d
         self.membre_gauche.b=self.membre_gauche.b*d
         #print 'mbg b : ',self.membre_gauche.b
         self.membre_droite.b=self.membre_droite.b*d
         self.membre_gauche.c=self.membre_gauche.c*d
         self.membre_droite.c=self.membre_droite.c*d
     #
     def param2enonce(self):
         #print type(self.membre_gauche.a)
         if self.membre_gauche.a<0:
             signe_a_mbg='-'
             str_a_mbg=str(abs(self.membre_gauche.a))
             str_a_mbg+='y'
         elif self.membre_gauche.a==0:
             signe_a_mbg=''
             str_a_mbg=''
         elif self.membre_gauche.a>0:
             signe_a_mbg=''
             str_a_mbg=str(abs(self.membre_gauche.a))
             str_a_mbg+='y'
         if self.membre_gauche.a==(1):
             signe_a_mbg=''
             str_a_mbg='y'
         if self.membre_gauche.a==-1:
             signe_a_mbg='-'
             str_a_mbg='y'
         ###
         if self.membre_gauche.b<0:
             signe_b_mbg='-'
             str_b_mbg=str(abs(self.membre_gauche.b))
             str_b_mbg+='x'
         elif self.membre_gauche.b==0:
             signe_b_mbg=''
             str_b_mbg=''
         elif self.membre_gauche.b>0:
             signe_b_mbg='+'
             str_b_mbg=str(abs(self.membre_gauche.b))
             str_b_mbg+='x'
         if self.membre_gauche.b==(1):
             signe_b_mbg='+'
             str_b_mbg=''
             str_b_mbg+='x'
         if self.membre_gauche.b==-1:
             signe_b_mbg='-'
             str_b_mbg=''
             str_b_mbg+='x'
         ###
         if self.membre_gauche.c<0:
             signe_c_mbg='-'
             str_c_mbg=str(abs(self.membre_gauche.c))
         elif self.membre_gauche.c==0:
             signe_c_mbg=''
             str_c_mbg=''
         elif self.membre_gauche.c>0:
             signe_c_mbg='+'
             str_c_mbg=str(abs(self.membre_gauche.c))
         if self.membre_gauche.c==1:
             signe_c_mbg='+'
             str_c_mbg='1'
         if self.membre_gauche.c==-1:
             signe_c_mbg='-'
             str_c_mbg='1'
         ###
         ###
         if self.membre_droite.a<0:
             signe_a_mbd='-'
             str_a_mbd= str(abs(self.membre_droite.a)) 
             str_a_mbd+='y'
         elif self.membre_droite.a==0:
             signe_a_mbd=''
             str_a_mbd=''
         elif self.membre_droite.a>0:
             signe_a_mbd=''
             str_a_mbd= str(abs(self.membre_droite.a)) 
             str_a_mbd+='y'
         if self.membre_droite.a==(1):
             signe_a_mbd=''
             str_a_mbd=''
             str_a_mbd+='y'
         if self.membre_droite.a==-1:
             signe_a_mbd='-'
             str_a_mbd=''
             str_a_mbd+='y'
         ###
         if self.membre_droite.b<0:
             signe_b_mbd='-'
             str_b_mbd= str(abs(self.membre_droite.b)) 
             str_b_mbd+='x'
         elif self.membre_droite.b==0:
             signe_b_mbd=''
             str_b_mbd=''
         elif self.membre_droite.b>0:
             signe_b_mbd='+'
             str_b_mbd= str(abs(self.membre_droite.b)) 
             str_b_mbd+='x'
         if self.membre_droite.b==(1):
             signe_b_mbd='+'
             str_b_mbd=''
             str_b_mbd+='x'
         if self.membre_droite.b==-1:
             signe_b_mbd='-'
             str_b_mbd=''
             str_b_mbd+='x'
         ###
         if self.membre_droite.c<0:
             signe_c_mbd='-'
             str_c_mbd= str(abs(self.membre_droite.c)) 
         elif self.membre_droite.c==0:
             signe_c_mbd=''
             str_c_mbd=''
         elif self.membre_droite.c>0:
             signe_c_mbd='+'
             str_c_mbd= str(abs(self.membre_droite.c)) 
         if self.membre_droite.c==1:
             signe_c_mbd='+'
             str_c_mbd= '1' 
         if self.membre_droite.c==-1:
             signe_c_mbd='-'
             str_c_mbd= '1' 
         ###
         #
         
         
         enonce_mbg='%s %s %s %s %s %s' %(signe_a_mbg,str_a_mbg,signe_b_mbg,str_b_mbg,signe_c_mbg,str_c_mbg)
         enonce_mbd='%s %s %s %s %s %s' %(signe_a_mbd,str_a_mbd,signe_b_mbd,str_b_mbd,signe_c_mbd,str_c_mbd)
         
         
         
         
         self.enonce=enonce_mbg+' = '+enonce_mbd
         return self.enonce
     #
class Exercice_type1:
     """Exercice avec une solution unique"""
     def __init__(self):
         solution=SolutionUnique()
         #print 'solution : ',solution.x,';',solution.y
         membre_gauche=Membre()
         membre_gauche.necessaire(solution)
         equation1=Equation(membre_gauche,Membre())
         
         #print(equation1 , equation1.param2enonce())
         
         equation1.modif_equivalente()
         #print (equation1 ,equation1.param2enonce())
         #
         membre_gauche=Membre()
         membre_gauche.necessaire(solution)
         equation2=Equation(membre_gauche,Membre())
         equation2.modif_equivalente()
         
         self.enonce1=equation1.param2enonce()
         self.enonce2=equation2.param2enonce()
         
         self.enonce="<p>Détermine la solution du système d'équations suivant : </p>"
         self.enonce+="<p>\( \\begin{cases} %s \\\\ %s \\end{cases} \) </p>"%(self.enonce1,self.enonce2) 
     
         self.enonce+="<p>x={1:NUMERICAL:=%s}<br>"%(str(solution.x))
         self.enonce+="y={1:NUMERICAL:=%s}</p>"%(str(solution.y))
         
         self.reponse='\( S=\lbrace ( %s ~;~%s ) \\rbrace\)' %( str(solution.x) , str(solution.y) )
         

class Exercice_type2:
     """Exercice aux solutions indéterminées"""
     def __init__(self):
         solution=SolutionUnique()
         membre_gauche=Membre()
         membre_gauche.necessaire(solution)
         equation1=Equation(membre_gauche,Membre())
         equation2=copy.deepcopy(equation1)
         equation1.modif_equivalente()
         #
         #membre_gauche_eqn2=copy.deepcopy(membre_gauche)
         #equation2=Equation(membre_gauche_eqn2,Membre())
         #equation2=equation1.modif_equivalente()
         #equation2=copy.deepcopy(equation1)
         equation2.modif_equivalente()
         
         self.enonce1=equation1.param2enonce()
         self.enonce2=equation2.param2enonce()
         self.reponse=' S= $\left\lbrace    \mathbf{R}  \\rbrace\\right.$'
         #print 
         
class Exercice_type3:
     """Exercice sans solution"""
     def __init__(self):
         solution=SolutionUnique()
         membre_gauche=Membre()
         membre_gauche.necessaire(solution)
         equation1=Equation(membre_gauche,Membre())
         equation1.modif_equivalente()
         #
         equation2=copy.deepcopy(equation1)
         equation2.modif_equivalente()
         equation2.membre_gauche.c+=random.randint(-10,10)
         
         self.enonce1=equation1.param2enonce()
         self.enonce2=equation2.param2enonce()
         self.reponse=' S= $\left\lbrace  \\varnothing \\rbrace\\right.$'
         #print 

if __name__=="__main__":
     questionnaire=[]
     for i in range(100):
         question=Exercice_type1()
         questionnaire.append(question)
         
     
     
     f = open('./exe_sys_eqn.xml','w')
     
     f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
     f.write('<quiz>\n')
     f.write('<question type="category">\n')
     f.write('<category>\n')
     f.write("<text>$course$/Système d'équation : solution unique</text>\n")
     f.write('</category>\n')
     f.write('</question>\n')
     for question in questionnaire:
        #f.write('<!-- question: %s  -->\n'%i)
        f.write('<question type="cloze"> \n')
        f.write('<name>\n')
        f.write("<text>Trouver la solution du système d'équations</text>\n")
        f.write('</name>\n')
        f.write('<questiontext format="html">\n')
        f.write('<text><![CDATA[ ')
        f.write(question.enonce)
        f.write(']]></text>\n')
        f.write('</questiontext>\n')
        f.write('<generalfeedback format="html">\n')
        f.write('<text><![CDATA[ ')
        f.write('')
        f.write(']]></text>\n')
        f.write('</generalfeedback>\n')
        f.write('<defaultgrade>1.0000000</defaultgrade>\n')
        f.write('<penalty>0.3333333</penalty>\n')
        f.write('<hidden>0</hidden>\n')
        f.write('</question>\n')
     f.write('</quiz>\n')
     
     f.close()
    
