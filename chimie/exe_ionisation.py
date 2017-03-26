#! /usr/bin/python3
# -*- coding: utf-8 -*- 
import random





class Exercice():
    def __init__(self):
         self.liste_propositions_fausses=[]
         self.proposition_exacte=''
       








if __name__=="__main__":
     questionnaire=[]
     
     myfile=open('./eqn_ionisation', "r")
     exercice=Exercice()
     for ligne in myfile:
         ligne=ligne.rstrip('\n\r')
         if ligne!='':
             if ligne[0]=='*':
                 exercice.proposition_exacte=ligne[1:]
                 print(exercice.proposition_exacte)
             else:
                 #print(ligne)
                 exercice.liste_propositions_fausses.append(ligne)
         else:
             #print(ligne)
             #print (exercice.liste_propositions_fausses)
             #print('############')
             exercice.liste_propositions_fausses=random.sample(exercice.liste_propositions_fausses,5)
             questionnaire.append(exercice)
             exercice=Exercice()
     
     f = open('./exe_ionisation_moodle.xml','w')
     
     f.write('<?xml version="1.0" encoding="UTF-8"?> \n')
     f.write("<quiz> \n")
     f.write('<question type="category"> \n')
     f.write("<category> \n")
     f.write("<text>$course$/Chimie/Ionisation</text> \n")
     f.write("</category> \n")
     f.write("</question> \n")
     for question in questionnaire:
         f.write('<question type="multichoice"> \n')
         f.write("<name> \n")
         f.write("<text>Équations d'ionisation</text> \n")
         f.write("</name> \n")
         f.write('<questiontext format="html"> \n')
         f.write("<text><![CDATA[<p>Parmi les propositions ci-dessous, laquelle est une équation d'ionisation correcte?</p>]]></text> \n")
         f.write("</questiontext> \n")
         f.write('<generalfeedback format="html"> \n')
         f.write("<text></text> \n")
         f.write("</generalfeedback> \n")
         f.write("<defaultgrade>1.0000000</defaultgrade> \n")
         f.write("<penalty>0.3333333</penalty> \n")
         f.write("<hidden>0</hidden> \n")
         f.write("<single>true</single> \n")
         f.write("<shuffleanswers>true</shuffleanswers> \n")
         f.write("<answernumbering>abc</answernumbering> \n")
         f.write('<correctfeedback format="html"> \n')
         f.write("<text>Votre réponse est correcte.</text> \n")
         f.write("</correctfeedback> \n")
         f.write('<incorrectfeedback format="html"> \n')
         f.write("<text>Votre réponse est incorrecte.</text> \n")
         f.write("</incorrectfeedback> \n")
         f.write("<shownumcorrect/> \n")
         f.write('<answer fraction="100" format="html"> \n')
         f.write("<text><![CDATA[<p>\(%s \)</p>]]></text> \n"%question.proposition_exacte)
         f.write('<feedback format="html"> \n')
         f.write("<text></text> \n")
         f.write("</feedback> \n")
         f.write("</answer> \n")
         for proposition in question.liste_propositions_fausses:
             f.write('<answer fraction="0" format="html"> \n')
             f.write("<text><![CDATA[<p> \(%s\) </p>]]></text> \n"%proposition)
             f.write('<feedback format="html"> \n')
             f.write("<text></text> \n")
             f.write("</feedback> \n")
             f.write("</answer> \n")
         f.write("</question> \n")
     f.write('</quiz> \n')
     f.close()
     
