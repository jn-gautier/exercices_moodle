#! /usr/bin/python3
# -*- coding: utf-8 -*- 

import random
import math

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
        if self.p<0:self.signe_p="-"
        if self.p>0:self.signe_p="+"
        #
        self.reponse_vraie="<p>\(F isequv y=%sx%s%s \)</p>"%(self.m,self.signe_p,math.abs(self.p))
        
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
        
        s
        
        