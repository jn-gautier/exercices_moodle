#! /usr/bin/python3
# -*- coding: utf-8 -*- 

import random

"""A faire : 
convertir les questions en cloze pour gérer les unités
réécrire les feedback en respectant la présentation DIER
écrire les dernière questions
"""

def convert_sci(nombre):
     if (nombre>1000) or (nombre<0.1):
         nombre_sciE='%.4E' %(nombre)
         nombre_sciE=nombre_sciE.split('E')
         #
         base=nombre_sciE[0]
         base=base.replace('.',',')
         exposant=nombre_sciE[1]
         #
         decimales=base.split(',')[1]
         arrondi=1
         for chiffre in decimales:
             if chiffre!='0':
                 arrondi=0
         if arrondi==1: #s'il n'y a pas de décimales
             base=base.split(',')[0]
         #
         nombre_sci=base+'\\times 10^{'+exposant+'}'
         
     else:
         nombre_str=str(nombre)
         nombre_str=nombre_str.replace('.',',')
         partie_entiere=nombre_str.split(',')[0]
         entiers_significatifs=len(partie_entiere)
         if partie_entiere=='0':
             entiers_significatifs=0
         #decimaux_significatifs=0
         partie_decimale=''
         if (len(nombre_str.split(','))>1):#s'il y a une partie decimale
             partie_decimale=nombre_str.split(',')[1]
             #decimaux_significatifs=len(partie_decimale)
         
         decimaux_a_prendre=4-entiers_significatifs
         decimaux_pris=partie_decimale[0:decimaux_a_prendre]
         
         if decimaux_pris!='':
             nombre_sci=partie_entiere+','+decimaux_pris
         else:
             nombre_sci=partie_entiere
     return nombre_sci


#

#Quelle est l'intensité du courant dans une résistance de ### ohms si la différence de potentiel aux bornes de celle-ci est de ### [V]?

#Quelle devrait être la valeur d'une résistance soumise à une tension de ### [V] pour que l'intensité du courant qui la traverse soit de ### [A]?

"""





P=U/R
U=PR
R=U/P
E=U*dt/R
"""




class Question:
     def __init__(self):
         #
         self.resistance=random.randint(2,30)
         self.intensite=random.randint(1,20)
         self.duree=random.randint(10,120)
         
         self.potentiel=self.resistance*self.intensite
         self.charge=self.intensite*self.duree
         self.puissance=self.potentiel*self.intensite
         self.energie=self.potentiel*self.intensite*self.duree
         
         self.energie_str=convert_sci(self.energie)
         
         #self.ponderateur=random.choice([[0.4,0.5,0.7,0.8],[0.5,0.7,0.8,1.1],[0.7,0.8,1.1,1.2],[0.8,1.1,1.2,1.4],[1.1,1.2,1.4,1.6]])
         #
     def type_1(self):
         """U=R*I """
         self.enonce="Quelle devrait être la différence de potentiel aux bornes d'une résistance de %s [ohm] pour que l'intensité du courant qui la traverse soit de %s [A]?"%(self.resistance,self.intensite)
         
         self.reponse=self.potentiel
         self.feedback="<p>\(U=R \cdot I\) </p>"
         self.feedback+="<p>\(U=%s \cdot %s \) </p>"%(self.resistance,self.intensite)
         self.feedback+="<p>U= %s [V]</p>"%(self.potentiel)
         
         self.unites='[V]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
     
     def type_2(self):
         """R=U/I """
         self.enonce="Quelle devrait être la valeur de la résistance d'une ampoule soumise à une tension de %s [V] si l'intensité du courant qui la traverse ne peut pas dépasser %s [A]?"%(self.potentiel,self.intensite)
         
         self.reponse=self.resistance
         self.feedback="<p>\(U=R \cdot I \\rightarrow R=\\frac{U}{I}\) </p>"
         self.feedback+="<p>\(R=\\frac{%s}{%s} \) </p>"%(self.potentiel,self.intensite)
         self.feedback+="<p>\(R= %s [\omega] \)</p>"%(self.resistance)
         
         self.unites='[ohm]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
         
     def type_3(self):
         """ U=Rq/dt """
         self.enonce="À quelle différence de potentiel faut-il soumettre une résistance de %s [ohm] pour qu'une charge total de %s [C] la traverse dans un intervalle de %s [s]?"%(self.resistance,self.charge,self.duree)
         
         self.reponse=self.potentiel
         self.feedback="<p>\(U=R \cdot I \\ ; \\ I=\\frac{q}{\Delta t} \)</p>"
         self.feedback+="<p>\( \\rightarrow U=\\frac{R \cdot q}{\Delta t} \)</p>"
         self.feedback+="<p>\(U=\\frac{%s \cdot %s}{ %s} \) </p>"%(self.resistance,self.charge,self.duree)
         self.feedback+="<p>U= %s [V]</p>"%(self.potentiel)
         
         self.unites='[V]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
     
     def type_4(self):
         """ R=U*dt/q """
         self.enonce="On souhaite qu'une charge totale de %s [C] puisse passer au travers d'une résistance de soumise à une différence de potentiel de %s [V] dans un intervalle de %s [s]. Quelle doit être la valeur de cette résistance?"%(self.charge,self.potentiel,self.duree)
         
         self.reponse=self.resistance
         self.feedback="<p>\(U=R \cdot I \\ ; \\ I=\\frac{q}{\Delta t} \)</p>"
         self.feedback+="<p>\( \\rightarrow R=\\frac{U \cdot \Delta t}{q} \)</p>"
         self.feedback+="<p>\( R=\\frac{%s \cdot %s}{%s} \) </p>"%(self.potentiel,self.duree,self.charge)
         self.feedback+="<p>\(R= %s [\omega] \)</p>"%(self.resistance)
         
         self.unites='[ohm]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
     
     def type_5(self):
         """ I=U/R """
         self.enonce="Une résistance de %s [ohm] est soumise à une différence de potentiel de %s [V]. Quelle est l'intensité du courant qui traverse la résistance?"%(self.resistance,self.potentiel)
         
         self.reponse=self.intensite
         self.feedback="<p>\(U=R \cdot I \\rightarrow I=\\frac{U}{R}\) </p>"
         self.feedback+="<p>\(I=\\frac{%s}{%s} \) </p>"%(self.potentiel,self.resistance)
         self.feedback+="<p>\(I= %s [A] \)</p>"%(self.intensite)
         
         self.unites='[A]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
     
     def type_6(self):
         """ q=(U*dt)/R """
         self.enonce="Quelle quantité de charges aura traversé une résistance de %s [ohm] soumise à une différence de potentiel de %s [V] durant %s [s]?"%(self.resistance,self.potentiel,self.duree)
         
         self.reponse=self.charge
         self.feedback="<p>\(U=R \cdot I \\ ; \\ I=\\frac{q}{\Delta t} \)</p>"
         self.feedback+="<p>\( \\rightarrow q=\\frac{U \cdot \Delta t}{R} \)</p>"
         self.feedback+="<p>\( q=\\frac{%s \cdot %s}{%s} \) </p>"%(self.potentiel,self.duree,self.resistance)
         self.feedback="<p>\(q= %s [C] \)</p>"%(self.charge)
         
         self.unites='[C]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
         
     def type_7(self):
         """ P=U*I """
         self.enonce="Dans un circuit simple constitué d'un générateur et d'un récepteur, le récepteur est traversé par un courant de %s [A] lorsque la différence de potentiel aux bornes du générateur est de %s [V]. Quelle est la puissance du récepteur?"%(self.intensite,self.potentiel)
         self.reponse=self.puissance
         self.feedback="<p>\(P=U \cdot I\) </p>"
         self.feedback+="<p>\(P=%s \cdot %s \) </p>"%(self.potentiel,self.intensite)
         self.feedback+="<p>P= %s [W]</p>"%(self.puissance)
         
         self.unites='[W]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
         
     
     def type_8(self):
         """ P=Uq/dt """
         self.enonce="Une batterie contenant une charge totale de %s [C] est capable de générer une différence de potentiel de %s [V]. Un récepteur alimenté par cette batterie peut fonctionner durant %s [s]. Quelle est la puissance de cette batterie?"%(self.charge,self.potentiel,self.duree)
         self.reponse=self.puissance
         self.feedback="<p>\(P=U \cdot I \\ ; \\ I=\\frac{q}{\Delta t} \)</p>"
         self.feedback+="<p>\( \\rightarrow P=\\frac{U \cdot q}{\Delta t} \)</p>"
         self.feedback+="<p>\(P=\\frac{%s \cdot %s}{%s} \) </p>"%(self.potentiel,self.charge,self.duree)
         self.feedback+="<p>P= %s [W]</p>"%(self.puissance)
         
         self.unites='[W]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
    
     def type_9(self):
         """ U=P/I """
         self.enonce="Un générateur fonctionne avec une puissance de %s [W], il alimente une ampoule et l'intensité du courant dans celle-ci est de %s [A]. Quelle est la différence de potentiel aux bornes du générateur."%(self.puissance,self.intensite)
         self.reponse=self.potentiel
         self.feedback="<p>\(P=U \cdot I \\rightarrow U=\\frac{P}{I}\) </p>"
         self.feedback+="<p>\(U=\\frac{%s}{%s}\) </p>"%(self.puissance,self.intensite)
         self.feedback+="<p>U= %s [V]</p>"%(self.potentiel)
         
         self.unites='[V]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
     
     def type_10(self):
         """ U=P*dt/q """
         self.enonce="Une batterie contenant une charge totale de %s [C] se décharge avec une puissance de %s [W] en %s [s]. Quelle est la différence de potentiel maximale aux bornes de cette batterie?"%(self.charge,self.puissance,self.duree)
         self.reponse=self.potentiel
         
         self.feedback="<p>\(P=U \cdot I  \\ ; \\ I=\\frac{q}{\Delta t} \)</p>"
         self.feedback+="<p>\( \\rightarrow U=\\frac{P \cdot \Delta t}{q} \)</p>"
         self.feedback+="<p>\(U=\\frac{%s \cdot %s}{%s} \)</p>"%(self.puissance,self.duree,self.charge)
         self.feedback+="<p>U= %s [V]</p>"%(self.potentiel)
         
         self.unites='[V]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
         
     def type_11(self):
         """ I=P/U """
         self.enonce="Un récepteur thermique d'une puissance de %s [W] engendre une différence de potentiel de %s [V]. Quelle est l'intensité du courant qui traverse ce générateur?"%(self.puissance,self.potentiel)
         self.reponse=self.intensite
         
         self.feedback="<p>\(P=U \cdot I \\rightarrow I=\\frac{P}{U}\) </p>"
         self.feedback+="<p>\(I=\\frac{%s}{%s} \) </p>"%(self.puissance,self.potentiel)
         self.feedback+="<p>I= %s [A]</p>"%(self.intensite)
         
         self.unites='[A]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
         
     
     def type_12(self):
         """ q=(P*dt)/U """
         self.enonce="Un récepteur est alimenté par un générateur d'une puissance de %s [W]. La différence de potentiel aux bornes du récepteur est de %s [V]. Si le circuit électrique fonctionne durant %s [s], quelle quantité de charges aura traversé le récepteur?"%(self.puissance,self.potentiel,self.duree)
         self.reponse=self.charge
         
         self.feedback="<p>\(P=U \cdot I  \\ ; \\ I=\\frac{q}{\Delta t} \)</p>"
         self.feedback+="<p>\( \\rightarrow q=\\frac{P \cdot \Delta t}{U} \)</p>"
         self.feedback+="<p>\(q=\\frac{%s \cdot %s}{%s} \)</p>"%(self.puissance,self.duree,self.potentiel)
         self.feedback+="<p>q= %s [C]</p>"%(self.charge)
         
         self.unites='[C]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
        
     def type_13(self):
         """ E=UI*dt """
         self.potentiel=230
         self.energie=self.potentiel*self.intensite*self.duree
         
         self.enonce="Dans une maison, un appareil branché dans une prise normale est traverssé par un courant de %s [A]. Si cet appareil fonctionne durant %s [s], quelle énergie aura-t-il consommé?"%(self.intensite,self.duree)
         self.reponse=self.energie
         
         self.feedback="<p>\(P=U \cdot I  \\ ; \\ P=\\frac{E}{\Delta t} \)</p>"
         self.feedback+="<p>\( \\rightarrow E=U \cdot I \cdot \Delta t} \)</p>"
         self.feedback+="<p>\(E=%s \cdot %s \cdot %s \)</p>"%(self.potentiel,self.intensite,self.duree)
         self.feedback+="<p>E= %s [J]</p>"%(self.energie)
         
         self.unites='[J]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
         
     def type_14(self):
         """ P=R*I² """
         self.enonce="Avec quelle puissance une résistance de %s [ohm] dissipe-t-elle la chaleur si l'intensité du courant qui la traverse est de %s [A]?"%(self.resistance,self.intensite)
         self.reponse=self.puissance
         
         self.feedback="<p>\(P=R \cdot I^{2} \)</p>"
         self.feedback+="<p>\(P=%s \cdot %s^{2} \)</p>"%(self.resistance,self.intensite)
         self.feedback+="<p>P= %s [W]</p>"%(self.puissance)
         
         self.unites='[W]'
         self.unites_fausses=['[C]','[s]','[A]','[V]','[ohm]','[J]']
         random.shuffle(self.unites_fausses)
     
     def type_15(self):
         """ R=P/I² """
         self.enonce="Une résistance dissipe de l'énergie thermique avec une puissance de %s [W] lorsqu'elle est traversée par un courant de %s [A]. Quelle est la valeur de cette résistance?"%(self.puissance,self.intensite)
         self.reponse=self.resistance
         
         self.feedback="<p>\(P=R \cdot I^{2} \\rightarrow  R=\\frac{P}{I^{2}}\)</p>"
         self.feedback+="<p>\(R=\\frac{%s}{%s^{2}} \)</p>"%(self.puissance,self.intensite)
         self.feedback+="<p>\(R= %s [\omega]\)</p>"%(self.resistance)
         
         self.unites='[ohm]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
         
     def type_16(self):
         """I=sqrt(P/R) """
         self.enonce="Une résistance de %s [ohm] dissipe de l'énergie thermique avec une puissance de %s [W]. Quelle est l'intensité du courant qui traversse cette résistance?"%(self.resistance,self.puissance)
         self.reponse=self.intensite
         
         self.feedback="<p>\(P=R \cdot I^{2} \\rightarrow  I=\sqrt{\\frac{P}{R}}\)</p>"
         self.feedback+="<p>\( I=\sqrt{\\frac{%s}{%s}} \)</p>"%(self.puissance,self.resistance)
         self.feedback+="<p>\(I= %s [A]\)</p>"%(self.intensite)
         
         self.unites='[A]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
         
     def type_17(self):
         """ q=dt*sqrt(P/R) """
         self.enonce="Une résistance de %s [ohm] dissipe de l'énergie thermique avec une puissance de %s [W]. Quelle quantité de charges électriques a traverssé ce récepteur lorsqu'il a fonctionné durant %s [s]?"%(self.resistance,self.puissance,self.duree)
         self.reponse=self.charge
         
         self.feedback="<p>\(P=R \cdot I^{2} \\ ; \\ I=\\frac{q}{\Delta t}}\)</p>"
         self.feedback+="<p>\(\\rightarrow  q=\Delta t \cdot \sqrt{\\frac{P}{R}}\)</p>"
         self.feedback+="<p>\( q=%s \cdot \sqrt{\\frac{%s}{%s}} \)</p>"%(self.duree,self.puissance,self.resistance)
         self.feedback+="<p>\(q= %s [C]\)</p>"%(self.charge)
         
         self.unites='[C]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
     
     def type_18(self):
         """ E=RI²*dt """
         self.enonce="Quelle quantité d'énergie électrique aura été transformée par un récepteur soumis à une différence de potentiel de %s [V] et parcouru par un courant de %s [A] durant %s [s]?"%(self.potentiel,self.intensite,self.duree)
         self.reponse=self.energie
         
         self.feedback="<p>\(P=R \cdot I^{2} \\ ; \\ E=P \cdot \Delta t\)</p>"
         self.feedback+="<p>\(\\rightarrow E=R \cdot I^{2} \cdot \Delta t\)</p>"
         self.feedback+="<p>\(E=%s \cdot %s^{2} \cdot %s\)</p>"%(self.resistance,self.intensite,self.duree)
         self.feedback+="<p>E= %s [J]</p>"%(self.energie)
         
         self.unites='[J]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
         
     def type_19(self):
         """ P=U²/R """
         self.enonce="Avec quelle puissance une résistance de %s [ohm] dissipe-t-elle la chaleur lorsqu'elle soumise à une différence de potentiel de %s [V]?"%(self.resistance,self.potentiel)
         self.reponse=self.puissance
         
         self.feedback="<p>\(P=U \cdot I  \\ ; \\ U=R \cdot I\) </p>"
         self.feedback+="<p>\(\\rightarrow P=\\frac{U^{2}}{R}\)</p>"
         self.feedback+="<p>\(P=\\frac{%s^{2}}{%s} \) </p>"%(self.potentiel,self.resistance)
         self.feedback+="<p>P= %s [W]</p>"%(self.puissance)
         
         self.unites='[W]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
     
     def type_20(self):
         """ U=sqrt(PR) """
         self.enonce="Quelle différence de potentiel faut-il développer aux bornes d'une résistance de %s [ohm] pour qu'elle dissipe l'énergie sous forme de chaleur avec une puissance de %s [W]?"%(self.resistance,self.puissance)
         self.reponse=self.potentiel
         
         self.feedback="<p>\(P=U \cdot I  \\ ; \\ U=R \cdot I\) </p>"
         self.feedback+="<p>\(\\rightarrow U=\sqrt{P \cdot R\})</p>"
         self.feedback+="<p>\(U=\sqrt{%s \cdot %s }\) </p>"%(self.puissance,self.resistance)
         self.feedback+="<p>U= %s [V]</p>"%(self.potentiel)
         
         self.unites='[V]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
     
     def type_21(self):
         """ R=U²/P """
         self.enonce="Quelle résistance faudrait-il placer en parallèle avec un générateur de %s [V] pour qu'elle dissipe de la chaleur avec une puissance de %s [W]?"%(self.potentiel,self.puissance)
         self.reponse=self.resistance
         
         self.feedback="<p>\(P=U \cdot I  \\ ; \\ U=R \cdot I\) </p>"
         self.feedback+="<p>\(\\rightarrow R=\\frac{U^{2}}{P}\)</p>"
         self.feedback+="<p>\(R=\\frac{%s^{2}}{%s}\) </p>"%(self.potentiel,self.puissance)
         self.feedback+="<p>\(R= %s [\omega]\)</p>"%(self.resistance)
         
         self.unites='[ohm]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)
     
     def type_22(self):
         """ E=U*dt/R """
         self.enonce="Une résistance de %s [ohm] est branchée en parallèle avec un générateur de %s [V] durant %s [s]. Quelle quantité d'énergie est transformée en chaleur durant ce temps?"%(self.resistance,self.potentiel,self.duree)
         self.reponse=self.energie
         
         self.feedback="<p>\(P=U \cdot I  \\ ; \\ U=R \cdot I \\ ; \\ E=P \cdot \Delta t \)</p>"
         self.feedback+="<p>\(\\rightarrow E=\\frac{U^{2} \cdot \Delta t}{R}\)</p>"
         self.feedback+="<p>\(E=\\frac{%s^{2} \cdot %s}{%s} \) </p>"%(self.potentiel,self.duree,self.resistance)
         self.feedback+="<p>E= %s [J]</p>"%(self.energie)
         
         self.unites='[J]'
         self.unites_fausses=['[C]','[s]','[A]','[ohm]','[W]','[J]','[V]']
         random.shuffle(self.unites_fausses)



###      
###      
###      

if __name__=="__main__":
     questionnaire=[]
     for i in range(500):
         question=Question()
         choix=random.randint(1,22)
         #choix=i+1
         if choix==1:
             question.type_1()
         if choix==2:
             question.type_2()
         if choix==3:
             question.type_3()
         if choix==4:
             question.type_4()
         if choix==5:
             question.type_5()
         if choix==6:
             question.type_6()
         if choix==7:
             question.type_7()
         if choix==8:
             question.type_8()
         if choix==9:
             question.type_9()
         if choix==10:
             question.type_10()
         if choix==11:
             question.type_11()
         if choix==12:
             question.type_12()
         if choix==13:
             question.type_13()
         if choix==14:
             question.type_14()
         if choix==15:
             question.type_15()
         if choix==16:
             question.type_16()
         if choix==17:
             question.type_17()
         if choix==18:
             question.type_18()
         if choix==19:
             question.type_19()
         if choix==20:
             question.type_20()
         if choix==21:
             question.type_21()
         if choix==22:
             question.type_22()
         
         questionnaire.append(question)
             
     f = open('./exe_elec.xml','w')
     
     #for question in questionnaire:
         #f.write(question.enonce)
         #f.write('\n')
         #f.write(str(question.reponse))
         #f.write('\n')
         #f.write(question.feedback)
         #f.write('\n \n')
     #f.close()
     f.write('<?xml version="1.0" encoding="UTF-8"?> \n')
     f.write('<quiz>  \n')
     f.write('<question type="category">  \n')
     f.write('<category>  \n')
     f.write('<text>$course$/Physique/Electricité (exe de base)</text>  \n')
     f.write('</category>  \n')
     f.write('</question>  \n')
     for question in questionnaire:
         

 
         
         
         f.write('<question type="numerical">  \n')
         f.write('<name>  \n')
         f.write("<text>Exercice d'électricité (I)</text>  \n")
         f.write('</name>  \n')
         f.write('<questiontext format="html">  \n')
         f.write('<text><![CDATA[<p>%s</p>]]></text>  \n'% question.enonce)
         f.write('</questiontext>  \n')
         f.write('<generalfeedback format="html">  \n')
         f.write('<text><![CDATA[%s]]></text> \n'%question.feedback)
         f.write('</generalfeedback> \n')
         
         f.write('<defaultgrade>1.0000000</defaultgrade> \n  ')
         f.write('<penalty>0.3333333</penalty>           \n  ')
         f.write('<hidden>0</hidden>                     \n  ')
         
         
         
         
         f.write('<answer fraction="100" format="moodle_auto_format">  \n')
         f.write('<text>%s</text>  \n'%question.reponse)
         f.write('<feedback format="html">  \n')
         f.write('<text></text>  \n')
         f.write('</feedback>  \n')
         f.write('<tolerance>1</tolerance>')
         f.write('</answer>  \n')
         
         f.write('<units>  \n')
         f.write('<unit>  \n')
         f.write('<multiplier>1</multiplier>  \n')
         f.write('<unit_name>%s</unit_name>  \n'%question.unites)
         f.write('</unit>  \n')
         for unite in question.unites_fausses:
             if unite!=question.unites:
                 f.write('<unit>  \n')
                 f.write('<multiplier>1000000</multiplier>  \n')
                 f.write('<unit_name>%s</unit_name>  \n'%unite)
                 f.write('</unit>  \n')
         f.write('</units>  \n')
         f.write('<unitgradingtype>1</unitgradingtype>  \n')
         f.write('<unitpenalty>0.3000000</unitpenalty>  \n')
         f.write('<showunits>2</showunits>  \n')
         f.write('<unitsleft>0</unitsleft>  \n')
         f.write('</question>  \n')
     f.write('</quiz>\n')
     f.close()
     
     ###