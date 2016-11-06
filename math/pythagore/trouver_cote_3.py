#! /usr/bin/python3
# -*- coding: utf-8 -*- 

import random
import math

     
     #
class Triangle:
     """Un triangle est déterminé par la longueur de ses trois côtés. Le premier sommet se trouve aux coordonnées (0,0). 
     les coordonnées des autres sommets sont déterminées à partir des côtés et du premier sommet."""
     def __init__(self):
         self.numero=0
         self.coteAC=random.randint(1,5)
         self.coteAB=random.randint(1,7)
         self.coteBC=math.sqrt(self.coteAC**2+self.coteAB**2)
         self.coteBC=round(self.coteBC,4)
         
         self.xA=0
         self.yA=0
         self.xB=self.coteAB
         self.yB=0
         self.xC=0
         self.yC=self.coteAC
         
         
         self.liste_sommets=[['A','B','C'],['D','E','F'],['I','J','K'],['M','N','O'],['R','S','T'],['X','Y','Z']]
         self.sommets=random.choice(self.liste_sommets)
         self.nom=self.sommets[0]+self.sommets[1]+self.sommets[2]
         self.A=random.choice(self.sommets)
         self.sommets.remove(self.A)
         self.B=random.choice(self.sommets)
         self.sommets.remove(self.B)
         self.C=random.choice(self.sommets)
         
         self.ponderateur=random.choice([[0.4,0.5,0.7,0.8],[0.5,0.7,0.8,1.1],[0.7,0.8,1.1,1.2],[0.8,1.1,1.2,1.4],[1.1,1.2,1.4,1.6]])
        
     def exe_1(self):
         self.enonce='<script type="text/javascript" src="http://www.vf-bxl-moodle.be/lib/jsxgraph/jsxgraphcore.js"> </script>'
         self.enonce+="<p>Le triangle %s est rectangle en %s. %s%s mesure %s cm et %s%s mesure %s cm.</p>"%(self.nom,self.A,self.A,self.B,self.coteAB,self.A,self.C,self.coteAC)
         self.enonce+="<p>Combien mesure l'hypothénuse du triangle %s ?</p>"%self.nom
         self.enonce+='<div id="box_%s" class="jxgbox" style="width:350px; height:350px;"></div>'%self.numero
         
         self.enonce+='<script type="text/javascript">'
         self.enonce+="var b1 = JXG.JSXGraph.initBoard('box_%s', {boundingbox: [-2, 9, 9, -2], grid:true,showCopyright:false});"%self.numero
         self.enonce+="var p1 = b1.create('point', [%s,%s],{name:'%s',fixed:true});"%(self.xA,self.yA,self.A)
         self.enonce+="p2 = b1.create('point', [%s,%s],{name:'%s',fixed:true});"%(self.xB,self.yB,self.B)
         self.enonce+="p3 = b1.create('point', [%s,%s],{name:'%s',fixed:true});"%(self.xC,self.yC,self.C)
         self.enonce+="rect = b1.create('polygon',[p1,p3,p2],{hasInnerPoints:false});"
         
         self.enonce+="</script>"
         
         self.feedback="<p>Le triangle %s est rectangle en %s et son hypothénuse est %s%s.</p>"%(self.nom,self.A,self.B,self.C)
         self.feedback+="<p>Donc, d'après le théorème de Pythagore, \({%s%s}^2+{%s%s}^2={%s%s}^2\)</p>"%(self.A,self.B,self.A,self.C,self.B,self.C)
         self.feedback+="<p>Par conséquent, \({%s}^2+{%s}^2={%s%s}^2\)</p>"%(self.coteAB,self.coteAC,self.B,self.C)
         self.feedback+="<p>\({%s}+{%s}={%s%s}^2\)</p>"%(self.coteAB**2,self.coteAC**2,self.B,self.C)
         self.feedback+="<p>\(%s={%s%s}^2\)</p>"%(self.coteAB**2+self.coteAC**2,self.B,self.C)
         self.feedback+="<p>\(%s%s=\sqrt{%s}\)</p>"%(self.B,self.C,self.coteAB**2+self.coteAC**2)
         self.feedback+="<p>\(%s%s=%s cm\)</p>"%(self.B,self.C,round(self.coteBC,4))
         
         self.reponse="<p>\(%s%s=%s cm\)</p>"%(self.B,self.C,self.coteBC)
         
         self.reponses_fausses=[]
         for facteur in self.ponderateur:
             self.reponses_fausses.append("<p>\(%s%s=%s cm\)</p>"%(self.B,self.C,round(self.coteBC*facteur,4)))
         
         
     def exe_2(self):
         self.coteAB=random.randint(1,5)
         self.coteBC=random.randint(2,7)
         while self.coteBC<=self.coteAB:
             self.coteBC=random.randint(2,7)
         
         self.coteAC=math.sqrt(self.coteBC**2-self.coteAB**2)
         self.coteAC=round(self.coteAC,4)
     
         self.xA=float(0)
         self.yA=float(0)
         self.xB=float(self.coteAB)
         self.yB=float(0)
         self.xC=float(0)
         self.yC=float(self.coteAC)
         
         alpha=random.randint(10,15)
         
         self.xA_rot=self.xA
         self.yA_rot=self.yA
         self.xB_rot=self.xB*math.cos(math.radians(alpha))+self.yB*math.sin(math.radians(alpha))
         self.yB_rot=-1*self.xB*math.sin(math.radians(alpha))+self.yB*math.cos(math.radians(alpha))
         self.xC_rot=self.xC*math.cos(math.radians(alpha))+self.yC*math.sin(math.radians(alpha))
         self.yC_rot=-1*self.xC*math.sin(math.radians(alpha))+self.yC*math.cos(math.radians(alpha))
         
         self.enonce='<script type="text/javascript" src="http://www.vf-bxl-moodle.be/lib/jsxgraph/jsxgraphcore.js"> </script>'
         self.enonce+="<p>Le triangle %s est rectangle en %s. %s%s mesure %s cm et %s%s mesure %s cm.</p>"%(self.nom,self.A,self.A,self.B,self.coteAB,self.B,self.C,self.coteBC)
         self.enonce+="<p>Quelle est la longueur du troisième côté de ce triangle ?</p>"
         self.enonce+='<div id="box_%s" class="jxgbox" style="width:350px; height:350px;"></div>'%self.numero
         
         self.enonce+='<script type="text/javascript">'
         self.enonce+="var b1 = JXG.JSXGraph.initBoard('box_%s', {boundingbox: [-2, 9, 9, -2], grid:true,showCopyright:false});"%self.numero
         self.enonce+="var p1 = b1.create('point', [%s,%s],{name:'%s',fixed:true});"%(self.xA,self.yA,self.A)
         self.enonce+="p2 = b1.create('point', [%s,%s],{name:'%s',fixed:true});"%(self.xB_rot,self.yB_rot,self.B)
         
         self.enonce+="p3 = b1.create('point', [%s,%s],{name:'%s',fixed:true});"%(self.xC_rot,self.yC_rot,self.C)
         self.enonce+="rect = b1.create('polygon',[p1,p3,p2],{hasInnerPoints:false});"
         
         self.enonce+="</script>"
         
         self.feedback="<p>Le triangle %s est rectangle en %s et son hypothénuse est %s%s.</p>"%(self.nom,self.A,self.B,self.C)
         self.feedback+="<p>Donc, d'après le théorème de Pythagore, \({%s%s}^2+{%s%s}^2={%s%s}^2\)</p>"%(self.A,self.B,self.A,self.C,self.B,self.C)
         self.feedback+="<p>Et : \({%s%s}^2-{%s%s}^2={%s%s}^2\)</p>"%(self.B,self.C,self.A,self.B,self.A,self.C)
         self.feedback+="<p>Par conséquent, \({%s}^2-{%s}^2={%s%s}^2\)</p>"%(self.coteBC,self.coteAB,self.A,self.C)
         self.feedback+="<p>\({%s}-{%s}={%s%s}^2\)</p>"%(self.coteBC**2,self.coteAB**2,self.A,self.C)
         self.feedback+="<p>\(%s={%s%s}^2\)</p>"%(self.coteBC**2-self.coteAB**2,self.A,self.C)
         self.feedback+="<p>\(%s%s=\sqrt{%s}\)</p>"%(self.A,self.C,self.coteBC**2-self.coteAB**2)
         self.feedback+="<p>\(%s%s=%s cm\)</p>"%(self.A,self.C,round(self.coteAC,4))
         
         self.reponse="<p>\(%s%s=%s cm\)</p>"%(self.A,self.C,self.coteAC)
         
         self.reponses_fausses=[]
         for facteur in self.ponderateur:
             self.reponses_fausses.append("<p>\(%s%s=%s cm\)</p>"%(self.A,self.C,round(self.coteAC*facteur,4)))
     #


if __name__=="__main__":
     questionnaire=[]
     for i in range(40):
         question=Triangle()
         question.numero=i
         choix=random.randint(1,2)
         if choix==1:question.exe_1()
         if choix==2:question.exe_2()
         questionnaire.append(question)
         
     
     
     f = open('./exe_pythagore.xml','w')
     
     f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
     f.write('<quiz>\n')
     f.write('<question type="category">\n')
     f.write('<category>\n')
     f.write('<text>$course$/Théorème de Pythagore</text>\n')
     f.write('</category>\n')
     f.write('</question>\n')
     for question in questionnaire:
         f.write('<question type="multichoice">  \n')
         f.write('<name>  \n')
         f.write('<text>Pythagore</text>  \n')
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
         f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%question.reponse)
         f.write('<feedback format="html">  \n')
         f.write('<text></text>  \n')
         f.write('</feedback>  \n')
         f.write('</answer>  \n')
         for reponse_fausse in question.reponses_fausses:
             f.write('<answer fraction="0" format="html">  \n')
             f.write('<text><![CDATA[<p> %s </p>]]></text>  \n'%reponse_fausse)
             f.write('<feedback format="html">  \n')
             f.write('<text></text>  \n')
             f.write('</feedback>  \n')
             f.write('</answer>  \n')
         f.write('</question>  \n')
     f.write('</quiz>\n')
     
     f.close()
