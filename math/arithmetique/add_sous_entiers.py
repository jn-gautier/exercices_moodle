#! /usr/bin/python3
# -*- coding: utf-8 -*- 

"""Générer cet exercice par un script n'est pas très utile car on arrive au même résultat par une question calculée.
Je le garde néanmoins à titre d'exemple."""

import random


class Calcul:
    def __init__(self):
        a=0
        b=0
        while a==0:
            a=random.randint(-15,15)
        while b==0:
            b=random.randint(-15,15)

        oper=random.choice([0,1])

        if oper==1:
            if b<0:
                self.enonce='\( '+str(a)+' + ( '+str(b)+' ) = \)'
            else:
                self.enonce='\( '+ str(a)+' + '+str(b)+' = \)'
            self.reponse=str(a+b)
            self.reponse2=str(a+b*-1)
        else:
            if b<0:
                self.enonce='\( '+str(a)+' - ( '+str(b)+' ) = \)'
            else:
                self.enonce='\( '+str(a)+' - '+str(b)+' = \)'
            self.reponse=str(a-b)
            self.reponse2=str(a-b*-1)


if __name__=="__main__":
     questionnaire=[]
     for i in range(100):
         question=Calcul()
         questionnaire.append(question)
         
     
     
     f = open('./exe_add_sous.xml','w')
     
     f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
     f.write('<quiz>\n')
     f.write('<!-- question: 0  -->\n')
     f.write('<question type="category">\n')
     f.write('<category>\n')
     f.write('<text>$course$/Addition et soustraction entre entiers</text>\n')
     f.write('</category>\n')
     f.write('</question>\n')
     
     for question in questionnaire:
        f.write('<question type="numerical">\n')
        f.write('<name>\n')
        f.write('<text>Effectue le calcul suivant</text>\n')
        f.write('</name>\n')
        f.write('<questiontext format="html">\n')
        f.write('<text><![CDATA[<p>')
        f.write(question.enonce)
        f.write('</p>]]></text>\n')
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
     f.write('</quiz>\n')
     f.close()
