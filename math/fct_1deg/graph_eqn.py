#! /usr/bin/python3
# -*- coding: utf-8 -*- 

import random
import math

class Fonction:
     """Une fonction est déterminée par son équation. Cette équation est celle d'une droite"""
     def __init__(self):
         self.numero=0
         self.p=10
         while math.fabs(self.p)>9:
             self.racine=0
             while self.racine==0:
                 self.racine=random.randint(-8,8)
             
             self.m=0
             while self.m==0:
                 self.m=random.randint(-8,8)
             self.p=-1*self.racine*self.m
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
             liste_reponses=[['F_1','#ff0004'],['F_2','#289f15'],['F_3','#24119f'],['F_4','#cec403']]
             self.reponse_1=random.choice(liste_reponses)
             liste_reponses.remove(self.reponse_1)
             
             self.reponse_2=random.choice(liste_reponses)
             liste_reponses.remove(self.reponse_2)
             
             self.reponse_3=random.choice(liste_reponses)
             liste_reponses.remove(self.reponse_3)
             
             self.reponse_4=random.choice(liste_reponses)
             
             self.enonce='<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jsxgraph/0.99.5/jsxgraphcore.js"></script>'
             self.enonce+="<p>Quel est le graphique correspondant à l'équation suivante ?</p>"
             self.enonce+="<p>\(y=%s \cdot x+(%s)\)</p>"%(self.m,self.p)
             self.enonce+='<div id="box_%s" class="jxgbox" style="width:350px; height:350px;"></div>'%self.numero
             
             self.enonce+='<script type="text/javascript">'
             self.enonce+='JXG.Options.axis.ticks.drawLabels = false;'
             self.enonce+="var board = JXG.JSXGraph.initBoard('box_%s', {boundingbox: [-10, 10, 10, -10], axis:true,showCopyright:false});"%self.numero
             self.enonce+="xaxis = board.create('axis', [[0, 0], [1,0]], {name:'x', withLabel: true,label: {position: 'rt'}});"
             self.enonce+="yaxis = board.create('axis', [[0, 0], [0,1]], {name:'y', withLabel: true,label: {position: 'rt'}});"
             self.enonce+="var f = board.create('functiongraph', [function(x){return x*%s+(%s);}],{strokeColor:'%s',strokeWidth:1});"%(self.m,self.p,self.reponse_1[1])
             self.enonce+="var g = board.create('functiongraph', [function(x){return x*%s-(%s);}],{strokeColor:'%s',strokeWidth:1});"%(self.m,self.p,self.reponse_2[1])
             self.enonce+="var h = board.create('functiongraph', [function(x){return x*-1*(%s)+(%s);}],{strokeColor:'%s',strokeWidth:1});"%(self.m,self.p,self.reponse_3[1])
             self.enonce+="var i = board.create('functiongraph', [function(x){return x*-1*(%s)-(%s);}],{strokeColor:'%s',strokeWidth:1});"%(self.m,self.p,self.reponse_4[1])
             
             liste_reponses=[self.reponse_1,self.reponse_2,self.reponse_3,self.reponse_4]
             random.shuffle(liste_reponses)
             
             reponse=random.choice(liste_reponses)
             liste_reponses.remove(reponse)
             self.enonce+="txt_1 = board.createElement('text', [-9,-2,'%s'],{fontSize:14,color:'%s'});"%(reponse[0],reponse[1])
             
             reponse=random.choice(liste_reponses)
             liste_reponses.remove(reponse)
             self.enonce+="txt_2 = board.createElement('text', [-9,-4,'%s'],{fontSize:14,color:'%s'});"%(reponse[0],reponse[1])
             
             reponse=random.choice(liste_reponses)
             liste_reponses.remove(reponse)
             self.enonce+="txt_3 = board.createElement('text', [-9,-6,'%s'],{fontSize:14,color:'%s'});"%(reponse[0],reponse[1])
             
             reponse=random.choice(liste_reponses)
             liste_reponses.remove(reponse)
             self.enonce+="txt_4 = board.createElement('text', [-9,-8,'%s'],{fontSize:14,color:'%s'});"%(reponse[0],reponse[1])
             
             self.enonce+="</script>"
             
             self.feedback=""
             if self.m<0:
                 self.feedback+="<p>La pente est négative (m=%s) donc la fonction est décroissante.</p>"%self.m
             else:
                 self.feedback+="<p>La pente est positive (m=%s) donc la fonction est croissante.</p>"%self.m
             
             if self.p<0:
                 self.feedback+="<p>L'ordonnée à l'origine est négative (p=%s) donc le graphique de la fonction coupe l'axe des ordonnées en dessous de l'axe des abscisses.</p>"%self.p
             else:
                 self.feedback+="<p>L'ordonnée à l'origine est positive (p=%s) donc le graphique de la fonction coupe l'axe des ordonnées au dessus de l'axe des abscisses.</p>"%self.p
         
         if choix==2:
             liste_reponses=[['F_1','#ff0004'],['F_2','#289f15'],['F_3','#24119f'],['F_4','#cec403']]
             self.reponse_1=random.choice(liste_reponses)
             liste_reponses.remove(self.reponse_1)
             
             self.reponse_2=random.choice(liste_reponses)
             liste_reponses.remove(self.reponse_2)
             
             self.reponse_3=random.choice(liste_reponses)
             liste_reponses.remove(self.reponse_3)
             
             self.reponse_4=random.choice(liste_reponses)
             
             self.enonce='<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jsxgraph/0.99.5/jsxgraphcore.js"></script>'
             self.enonce+="<p>Quel est le graphique correspondant à l'équation suivante ?</p>"
             self.enonce+="<p>\(y=%s \cdot x+(%s)\)</p>"%(self.m,self.p)
             self.enonce+='<div id="box_%s" class="jxgbox" style="width:350px; height:350px;"></div>'%self.numero
             
             self.enonce+='<script type="text/javascript">'
             self.enonce+='JXG.Options.axis.ticks.drawLabels = false;'
             self.enonce+="var board = JXG.JSXGraph.initBoard('box_%s', {boundingbox: [-10, 10, 10, -10], axis:true,showCopyright:false});"%self.numero
             self.enonce+="xaxis = board.create('axis', [[0, 0], [1,0]], {name:'x', withLabel: true,label: {position: 'rt'}});"
             self.enonce+="yaxis = board.create('axis', [[0, 0], [0,1]], {name:'y', withLabel: true,label: {position: 'rt'}});"
             self.enonce+="var f = board.create('functiongraph', [function(x){return x*%s+(%s);}],{strokeColor:'%s',strokeWidth:1});"%(self.m,self.p,self.reponse_1[1])
             self.enonce+="var g = board.create('functiongraph', [function(x){return x*%s-(%s);}],{strokeColor:'%s',strokeWidth:1});"%(self.m,self.p,self.reponse_2[1])
             self.enonce+="var h = board.create('functiongraph', [function(x){return x*-1*(%s)+(%s);}],{strokeColor:'%s',strokeWidth:1});"%(self.m,self.p,self.reponse_3[1])
             self.enonce+="var i = board.create('functiongraph', [function(x){return x*-1*(%s)-(%s);}],{strokeColor:'%s',strokeWidth:1});"%(self.m,self.p,self.reponse_4[1])
             
             liste_reponses=[self.reponse_1,self.reponse_2,self.reponse_3,self.reponse_4]
             random.shuffle(liste_reponses)
             
             reponse=random.choice(liste_reponses)
             liste_reponses.remove(reponse)
             self.enonce+="txt_1 = board.createElement('text', [-9,-2,'%s'],{fontSize:14,color:'%s'});"%(reponse[0],reponse[1])
             
             reponse=random.choice(liste_reponses)
             liste_reponses.remove(reponse)
             self.enonce+="txt_2 = board.createElement('text', [-9,-4,'%s'],{fontSize:14,color:'%s'});"%(reponse[0],reponse[1])
             
             reponse=random.choice(liste_reponses)
             liste_reponses.remove(reponse)
             self.enonce+="txt_3 = board.createElement('text', [-9,-6,'%s'],{fontSize:14,color:'%s'});"%(reponse[0],reponse[1])
             
             reponse=random.choice(liste_reponses)
             liste_reponses.remove(reponse)
             self.enonce+="txt_4 = board.createElement('text', [-9,-8,'%s'],{fontSize:14,color:'%s'});"%(reponse[0],reponse[1])
             
             self.enonce+="</script>"
             
             self.feedback=""
             if self.m<0:
                 self.feedback+="<p>La pente est négative (m=%s) donc la fonction est décroissante.</p>"%self.m
             else:
                 self.feedback+="<p>La pente est positive (m=%s) donc la fonction est croissante.</p>"%self.m
             
             if self.p<0:
                 self.feedback+="<p>L'ordonnée à l'origine est négative (p=%s) donc le graphique de la fonction coupe l'axe des ordonnées en dessous de l'axe des abscisses.</p>"%self.p
             else:
                 self.feedback+="<p>L'ordonnée à l'origine est positive (p=%s) donc le graphique de la fonction coupe l'axe des ordonnées au dessus de l'axe des abscisses.</p>"%self.p
             
     #


if __name__=="__main__":
     questionnaire=[]
     for i in range(30):
         question=Fonction()
         question.numero=i
         #print (question.enonce,question.reponse)
         questionnaire.append(question)
         
     
     
     f = open('./exe_graphe_eqn.xml','w')
     
     f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
     f.write('<quiz>\n')
     f.write('<question type="category">\n')
     f.write('<category>\n')
     f.write('<text>Défaut pour math 4TQ/Équation et graphique</text>\n')
     f.write('</category>\n')
     f.write('</question>\n')
     for question in questionnaire:
        #f.write('<!-- question: %s  -->\n'%i)
         f.write('<question type="multichoice">  \n')
         f.write('<name>  \n')
         f.write('<text>Associer graphique et équation</text>  \n')
         f.write('</name>  \n')
         f.write('<questiontext format="html">  \n')
         f.write('<text><![CDATA[%s]]></text>  \n'% question.enonce)
         f.write('</questiontext>  \n')
         f.write('<generalfeedback format="html">  \n')
         f.write('<text><![CDATA[%s]]></text>  \n'%question.feedback)
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
         f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.reponse_1[0])
         f.write('<feedback format="html">  \n')
         f.write('<text></text>  \n')
         f.write('</feedback>  \n')
         f.write('</answer>  \n')
         f.write('<answer fraction="0" format="html">  \n')
         f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.reponse_2[0])
         f.write('<feedback format="html">  \n')
         f.write('<text></text>  \n')
         f.write('</feedback>  \n')
         f.write('</answer>  \n')
         f.write('<answer fraction="0" format="html">  \n')
         f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.reponse_3[0])
         f.write('<feedback format="html">  \n')
         f.write('<text></text>  \n')
         f.write('</feedback>  \n')
         f.write('</answer>  \n')
         f.write('<answer fraction="0" format="html">  \n')
         f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.reponse_4[0])
         f.write('<feedback format="html">  \n')
         f.write('<text></text>  \n')
         f.write('</feedback>  \n')
         f.write('</answer>  \n')
         f.write('</question>  \n')
     f.write('</quiz>\n')
     
     f.close()
     
    
