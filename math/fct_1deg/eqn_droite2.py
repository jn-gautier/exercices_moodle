#! /usr/bin/python3
# -*- coding: utf-8 -*- 

import random

"""On affiche le graphique d'une fonction avec un m et un p entier et on propose 4 équations. L'élève doit choisir la bonne proposition"""

class Fonction:
    """Une fonction est déterminée par son équation. Cette équation est celle d'une droite"""
    def __init__(self):
        self.numero=0
        self.m=0
        while self.m==0:
            self.m=random.randint(-5,5)
        
        self.p=0
        while self.p==0:
            self.p=random.randint(-5,5)
        if self.p<0:
            self.signe_p="-"
            self.signe_opp_p="+"
        if self.p>0:
            self.signe_p="+"
            self.signe_opp_p="-"
        #
        self.reponse_vraie="<p>\(F isequv y=%sx%s%s \)</p>"%(self.m,self.signe_p,abs(self.p))
        self.reponses_fausses=[]
        self.reponses_fausses.append("<p>\(F isequv y=%sx%s%s \)</p>"%(self.m*(-1),self.signe_p,abs(self.p)))
        self.reponses_fausses.append("<p>\(F isequv y=%sx%s%s \)</p>"%(self.m,self.signe_opp_p,abs(self.p)))
        self.reponses_fausses.append("<p>\(F isequv y=%sx%s%s \)</p>"%(self.m*(-1),self.signe_opp_p,abs(self.p)))
        
        
        self.enonce='<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jsxgraph/0.99.5/jsxgraphcore.js"></script>'
        self.enonce+="<p>Quelle est l'équation de la droite se trouvant dans le repère ci-dessous?</p>"
        self.enonce+='<div id="box_%s" class="jxgbox" style="width:350px; height:350px;"></div>'%self.numero
        
        self.enonce+='<script type="text/javascript">'
        self.enonce+='JXG.Options.axis.ticks.drawLabels = true;'
        self.enonce+="var board = JXG.JSXGraph.initBoard('box_%s', {boundingbox: [-10, 10, 10, -10], axis:true,showCopyright:false});"%self.numero
        self.enonce+="xaxis = board.create('axis', [[0, 0], [1,0]], {name:'x', withLabel: true,label: {position: 'rt'}});"
        self.enonce+="yaxis = board.create('axis', [[0, 0], [0,1]], {name:'y', withLabel: true,label: {position: 'rt'}});"
        self.enonce+="var f = board.create('functiongraph', [function(x){return x*%s+(%s);}],{strokeWidth:1});"%(self.m,self.p,)
        self.enonce+="</script>"
        
        self.feedback=""
        self.feedback+="<p>La valeur de l'ordonnée à l'origine (p) se lit directement sur le graphique. <br/>"
        self.feedback+="p=%s</p>"%self.p
        self.feedback+="<p>Lorsqu'on avance d'une unité dans le sens des X croissants (vers la droite), il faut "
        if self.m>0 : self.feedback+="monter "
        else : self.feedback+="descendre "
        self.feedback+="de %s unité(s) pour retrouver le graphique.<br/>"%(abs(self.m))
        self.feedback+="La valeur de la pente est donc : m=%s.</p>"%self.m
        self.feedback+="<p>Par conséquent, l'équation de la fonction est : \(F isequiv y=%sx%s%s \)</p>"%(self.m,self.signe_p,self.p)
        
if __name__=="__main__":
    questionnaire=[]
    for i in range(30):
        question=Fonction()
        questionnaire.append(question)
        
    
    
    f = open('./exe_graphe_eqn_2.xml','w')
    
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<quiz>\n')
    f.write('<question type="category">\n')
    f.write('<category>\n')
    f.write('<text>$course$/Équation et graphique(II)</text>\n')
    f.write('</category>\n')
    f.write('</question>\n')
    for question in questionnaire:
        f.write('<question type="multichoice">  \n')
        f.write('<name>  \n')
        f.write("<text>Trouver l'équation à partir du graphique</text>  \n")
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
        
        f.write('<shownumcorrect/>  \n')
        f.write('<answer fraction="100" format="html">  \n')
        f.write('<text><![CDATA[%s]]></text>  \n'%question.reponse_vraie)
        f.write('<feedback format="html">  \n')
        f.write('<text></text>  \n')
        f.write('</feedback>  \n')
        f.write('</answer>  \n')
        for reponse in question.reponses_fausses:
            f.write('<answer fraction="0" format="html">  \n')
            f.write('<text><![CDATA[%s]]></text>  \n'%reponse)
            f.write('<feedback format="html">  \n')
            f.write('<text></text>  \n')
            f.write('</feedback>  \n')
            f.write('</answer>  \n')
        f.write('</question>  \n')
    f.write('</quiz>\n')
    
    f.close()
       
       
       