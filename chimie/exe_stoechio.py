#! /usr/bin/python3
# -*- coding: utf-8 -*- 
import random
import re

def convert_sci(nombre):
     nombre_sci='%.4E' %(nombre)
     nombre_sci=nombre_sci.split('E')
     base=nombre_sci[0]
     exposant=nombre_sci[1]
     
     nombre=float(base)*(10**int(exposant)) #on reformate le nombre pour ne conserver que 4 chifres signicatifs
     
     if (nombre>9999) or (nombre<0.1):
         base=base.replace('.',',')
         
         decimales=base.split(',')[1]
         arrondi=1
         for chiffre in decimales:
             if chiffre!='0':
                 arrondi=0
         if arrondi==1: #s'il n'y a pas de décimales on ne prend que la partie entière afin d'éviter les expressions du type 1,0000
             base=base.split(',')[0]
         #
         nombre_latex=('%s \\times 10^{%s}')%(base,exposant)
         
         
     else:
         nombre=round(nombre,5) #pour éviter le péril des virgules flottantes
         nombre_latex=str(nombre)
         nombre_latex=nombre_latex.replace('.',',')
         
     return (nombre,nombre_latex)

class Corps(Object):
    def __init__(self):
        self.nom="" #le nom du Corps
        self.form="" #la formule du corps au format latex
        self.moles=float()
        self.masse=float()
        self.masse_molaire=int()
        self.cc_massique=float()
        self.cc_molaire=float()
        self.volume_solution=float()
        self.volume_gaz=float()
        self.coef=int() #le coefficient stoechiometrique
        self.donnee="" #peut prendre la valeur vide,gaz,sol_mas,sol_mol,masse
        self.reponse="" #peut prendre la valeur vide,gaz,sol_mas,sol_mol,masse
        self.categorie="" #peut prendre la valeur R1,R2,R3,P1,P2,P3
    
    def resoudre(self):
        if self.donnee!="":
            if self.donnee=="masse":
                self.moles=self.masse/self.masse_molaire
            elif self.donnee=="sol_mas":
                self.moles=(self.cc_massique*self.volume_solution)/self.masse_molaire
            elif self.donnee=="sol_mol":
                self.moles=self.cc_molaire*self.volume_solution
            elif self.donnee=="gaz":
                self.moles=volume_gaz/22.4
            else:
                print("Le format de la donnée n'est pas reconnu.")
        
        elif self.reponse!="":
            if self.reponse=="masse":
                self.masse=self.moles*self.masse_molaire
            elif self.reponse=="sol_mas":
                self.cc_massique=(self.moles*self.masse_molaire)/self.volume_solution
            elif self.reponse=="sol_mol":
                self.cc_molaire=self.moles/self.volume_solution
            elif self.reponse=="gaz":
                self.volume_gaz=self.moles*22.4
            else:
                print("Le format de la réponse n'est pas reconnu.")
        else:
            pass #on ne donne et on ne demande rien pour ce corps
    
    def valeurs_to_tex(self):
        if self.moles!=0: self.moles,self.moles_tex=convert_sci(self.moles)
        if self.masse!=0: self.masse,self.masse_tex=convert_sci(self.masse)
        if self.cc_massique!=0:self.cc_massique,self.cc_massique_tex=convert_sci(self.cc_massique)
        if self.cc_molaire!=0:self.cc_molaire,self.cc_molaire_tex=convert_sci(self.cc_molaire)
        if self.volume_solution!=0:self.volume_solution,self.volume_solution_tex=convert_sci(self.volume_solution)
        if self.volume_gaz!=0:self.volume_gaz,self.volume_gaz_tex=convert_sci(self.volume_gaz)

class Exercice():
    def __init__(self):
        self.enonce=""
        self.feedback=""
        
        choix=random.randint(1,2)
        choix=3
        if choix==1 : self.exe_1()
        if choix==2 : self.exe_2()
        if choix==3 : self.exe_3()
        if choix==4 : self.exe_4()
        if choix==5 : self.exe_5()
    
    def valeurs(self):
        #
        self.valeurs={}
        self.valeurs["R1_nom"]=""
        self.valeurs["R1_form"]=""
        self.valeurs["R1_moles"]=float()
        self.valeurs["R1_masse"]=float()
        self.valeurs["R1_masse_molaire"]=float()
        self.valeurs["R1_cc_massique"]=float()
        self.valeurs["R1_cc_molaire"]=float()
        self.valeurs["R1_volume_solution"]=float()
        self.valeurs["R1_volume_gaz"]=float()
        self.valeurs["R1_coef"]=int()
        
        self.valeurs["R2_nom"]=""
        self.valeurs["R2_form"]=""
        self.valeurs["R2_moles"]=float()
        self.valeurs["R2_masse"]=float()
        self.valeurs["R2_masse_molaire"]=float()
        self.valeurs["R2_cc_massique"]=float()
        self.valeurs["R2_cc_molaire"]=float()
        self.valeurs["R2_volume_solution"]=float()
        self.valeurs["R2_volume_gaz"]=float()
        self.valeurs["R2_coef"]=int()
        
        self.valeurs["R3_nom"]=""
        self.valeurs["R3_form"]=""
        self.valeurs["R3_moles"]=float()
        self.valeurs["R3_masse"]=float()
        self.valeurs["R3_masse_molaire"]=float()
        self.valeurs["R3_cc_massique"]=float()
        self.valeurs["R3_cc_molaire"]=float()
        self.valeurs["R3_volume_solution"]=float()
        self.valeurs["R3_volume_gaz"]=float()
        self.valeurs["R3_coef"]=int()
        
        self.valeurs["P1_nom"]=""
        self.valeurs["P1_form"]=""
        self.valeurs["P1_moles"]=float()
        self.valeurs["P1_masse"]=float()
        self.valeurs["P1_masse_molaire"]=float()
        self.valeurs["P1_cc_massique"]=float()
        self.valeurs["P1_cc_molaire"]=float()
        self.valeurs["P1_volume_solution"]=float()
        self.valeurs["P1_volume_gaz"]=float()
        self.valeurs["P1_coef"]=int()
        
        self.valeurs["P2_nom"]=""
        self.valeurs["P2_form"]=""
        self.valeurs["P2_moles"]=float()
        self.valeurs["P2_masse"]=float()
        self.valeurs["P2_masse_molaire"]=float()
        self.valeurs["P2_cc_massique"]=float()
        self.valeurs["P2_cc_molaire"]=float()
        self.valeurs["P2_volume_solution"]=float()
        self.valeurs["P2_volume_gaz"]=float()
        self.valeurs["P2_coef"]=int()
        
        self.valeurs["P3_nom"]=""
        self.valeurs["P3_form"]=""
        self.valeurs["P3_moles"]=float()
        self.valeurs["P3_masse"]=float()
        self.valeurs["P3_masse_molaire"]=float()
        self.valeurs["P3_cc_massique"]=float()
        self.valeurs["P3_cc_molaire"]=float()
        self.valeurs["P3_volume_solution"]=float()
        self.valeurs["P3_volume_gaz"]=float()
        self.valeurs["P3_coef"]=int()
    
    def valeurs_to_tex(self):
        for param,valeur in self.valeurs.items():
             if (type(valeur)==float) & (valeur!=0):
                 param_tex=param+"_tex"
                 self.valeurs[param],self.valeurs[param_tex]=convert_sci(param)
    
    def feedback(self):
        self.feedback="<style>table {{border-collapse: collapse;border: 1px solid black;}} th, td {{border: 1px solid black;height:30px}}</style><p><table>"
        self.feedback+="<tr>" #1° ligne : la réaction pondérée
        self.feedback+="<td></td>"#la première cellule est vide
        self.feedback+="<td>\({R1_coef} \\ {R1_form}\)</td>"
        if self.valeurs["R2_form"]!="" :self.feedback+="<td>\({R2_coef} \\ {R2_form}\)</td>"
        if self.valeurs["R3_form"]!="" :self.feedback+="<td>\({R3_coef} \\ {R3_form}\)</td>"
        if self.valeurs["P1_form"]!="" :self.feedback+="<td>\(\\rightarrow \\ {P1_coef} \\ {P1_form}\)</td>" 
        if self.valeurs["P2_form"]!="" :self.feedback+="<td>\({P2_coef} \\ {P2_form}\)</td>"
        if self.valeurs["P3_form"]!="" :self.feedback+="<td>\({P3_coef} \\ {P3_form}\)</td>"
        
        self.feedback+="</tr><tr><td>\(n[mol]\)</td>"#2° ligne : le nombre de mole
        if self.valeurs["R1_moles_tex"]!="" :self.feedback+="<td>\({R1_moles_tex}\)</td>"
        if self.valeurs["R2_moles_tex"]!="" :self.feedback+="<td>\({R2_moles_tex}\)</td>"
        if self.valeurs["R3_moles_tex"]!="" :self.feedback+="<td>\({R3_moles_tex}\)</td>"
        if self.valeurs["P1_moles_tex"]!="" :self.feedback+="<td>\({P1_moles_tex}\)</td>"
        if self.valeurs["P2_moles_tex"]!="" :self.feedback+="<td>\({P2_moles_tex}\)</td>"
        if self.valeurs["P3_moles_tex"]!="" :self.feedback+="<td>\({P3_moles_tex}\)</td>"
        
        self.feedback+="</tr><tr><td>\(m[g]\)</td>"#3° ligne : la masse
        if self.valeurs["R1_masse_tex"]!="" :self.feedback+="<td>\({R1_masse_tex}\)</td>"
        if self.valeurs["R2_masse_tex"]!="" :self.feedback+="<td>\({R2_masse_tex}\)</td>"
        if self.valeurs["R3_masse_tex"]!="" :self.feedback+="<td>\({R3_masse_tex}\)</td>"
        if self.valeurs["P1_masse_tex"]!="" :self.feedback+="<td>\({P1_masse_tex}\)</td>"
        if self.valeurs["P2_masse_tex"]!="" :self.feedback+="<td>\({P2_masse_tex}\)</td>"
        if self.valeurs["P3_masse_tex"]!="" :self.feedback+="<td>\({P3_masse_tex}\)</td>"
        
        self.feedback+="</tr><tr><td>\(M[g \cdot mol^{{-1}}]\)</td>"#4° ligne : la masse molaire
        if self.valeurs["R1_masse_molaire_tex"]!="" :self.feedback+="<td>\({R1_masse_molaire_tex}\)</td>"
        if self.valeurs["R2_masse_molaire_tex"]!="" :self.feedback+="<td>\({R2_masse_molaire_tex}\)</td>"
        if self.valeurs["R3_masse_molaire_tex"]!="" :self.feedback+="<td>\({R3_masse_molaire_tex}\)</td>"
        if self.valeurs["P1_masse_molaire_tex"]!="" :self.feedback+="<td>\({P1_masse_molaire_tex}\)</td>"
        if self.valeurs["P2_masse_molaire_tex"]!="" :self.feedback+="<td>\({P2_masse_molaire_tex}\)</td>"
        if self.valeurs["P3_masse_molaire_tex"]!="" :self.feedback+="<td>\({P3_masse_molaire_tex}\)</td>"
        
        self.feedback+="</tr><tr><td>\(C_{{M}}[mol \cdot L^{{-1}}]\)</td>"#5° ligne : la concentration molaire
        if self.valeurs["R1_concentration_molaire_tex"]!="" :self.feedback+="<td>\({R1_cc_molaire_tex}\)</td>"
        if self.valeurs["R2_concentration_molaire_tex"]!="" :self.feedback+="<td>\({R2_cc_molaire_tex}\)</td>"
        if self.valeurs["R3_concentration_molaire_tex"]!="" :self.feedback+="<td>\({R3_cc_molaire_tex}\)</td>"
        if self.valeurs["P1_concentration_molaire_tex"]!="" :self.feedback+="<td>\({P1_cc_molaire_tex}\)</td>"
        if self.valeurs["P2_concentration_molaire_tex"]!="" :self.feedback+="<td>\({P2_cc_molaire_tex}\)</td>"
        if self.valeurs["P3_concentration_molaire_tex"]!="" :self.feedback+="<td>\({P3_cc_molaire_tex}\)</td>"
        
        self.feedback+="</tr><tr><td>\(\gamma[g \cdot L^{{-1}}]\)</td>"#6° ligne : la concentration massique
        if self.valeurs["R1_concentration_massique_tex"]!="" :self.feedback+="<td>\({R1_cc_massique_tex}\)</td>"
        if self.valeurs["R2_concentration_massique_tex"]!="" :self.feedback+="<td>\({R2_cc_massique_tex}\)</td>"
        if self.valeurs["R3_concentration_massique_tex"]!="" :self.feedback+="<td>\({R3_cc_massique_tex}\)</td>"
        if self.valeurs["P1_concentration_massique_tex"]!="" :self.feedback+="<td>\({P1_cc_massique_tex}\)</td>"
        if self.valeurs["P2_concentration_massique_tex"]!="" :self.feedback+="<td>\({P2_cc_massique_tex}\)</td>"
        if self.valeurs["P3_concentration_massique_tex"]!="" :self.feedback+="<td>\({P3_cc_massique_tex}\)</td>"
        
        self.feedback+="</tr><tr><td>\(V_{{sol}}[L]\)</td>"#7° ligne : le volume de solution
        if self.valeurs["R1_volume_solution_tex"]!="" :self.feedback+="<td>\({R1_volume_solution_tex}\)</td>"
        if self.valeurs["R2_volume_solution_tex"]!="" :self.feedback+="<td>\({R2_volume_solution_tex}\)</td>"
        if self.valeurs["R3_volume_solution_tex"]!="" :self.feedback+="<td>\({R3_volume_solution_tex}\)</td>"
        if self.valeurs["P1_volume_solution_tex"]!="" :self.feedback+="<td>\({P1_volume_solution_tex}\)</td>"
        if self.valeurs["P2_volume_solution_tex"]!="" :self.feedback+="<td>\({P2_volume_solution_tex}\)</td>"
        if self.valeurs["P3_volume_solution_tex"]!="" :self.feedback+="<td>\({P3_volume_solution_tex}\)</td>"
        
        self.feedback+="</tr><tr><td>\(V_{{gaz}}[L]\)</td>"#8° ligne : le volume gazeux
        if self.valeurs["R1_volume_gaz_tex"]!="" :self.feedback+="<td>\({R1_volume_gaz_tex}\)</td>"
        if self.valeurs["R2_volume_gaz_tex"]!="" :self.feedback+="<td>\({R2_volume_gaz_tex}\)</td>"
        if self.valeurs["R3_volume_gaz_tex"]!="" :self.feedback+="<td>\({R3_volume_gaz_tex}\)</td>"
        if self.valeurs["P1_volume_gaz_tex"]!="" :self.feedback+="<td>\({P1_volume_gaz_tex}\)</td>"
        if self.valeurs["P2_volume_gaz_tex"]!="" :self.feedback+="<td>\({P2_volume_gaz_tex}\)</td>"
        if self.valeurs["P3_volume_gaz_tex"]!="" :self.feedback+="<td>\({P3_volume_gaz_tex}\)</td>"
        self.feedback+="</tr>"
        
        
    #
    def exe_1(self):
        masse_CaOH2=float(random.randint(30,300))/100
        mole_CaOH2=masse_CaOH2/74
        cc_molaire_HCl=float(random.randint(30,150))/100
        vol_HCl=mole_CaOH2*2/cc_molaire_HCl
        cc_massique_CaCl2=(masse_CaOH2*110)/(74*vol_HCl)
        
        mole_HCl=mole_CaOH2*2
        mole_HCl,mole_HCl_latex=convert_sci(mole_HCl)
        
        masse_CaCl2=masse_CaOH2*110/74
        masse_CaCl2,masse_CaCl2_latex=convert_sci(masse_CaCl2)
        
        masse_CaOH2,masse_CaOH2_latex=convert_sci(masse_CaOH2)
        mole_CaOH2,mole_CaOH2_latex=convert_sci(mole_CaOH2)
        cc_molaire_HCl,cc_molaire_HCl_latex=convert_sci(cc_molaire_HCl)
        vol_HCl,vol_HCl_latex=convert_sci(vol_HCl)
        cc_massique_CaCl2,cc_massique_CaCl2_latex=convert_sci(cc_massique_CaCl2)
        
        self.enonce="<p>On fait réagir complètement une solution \(%s [M]\) d'acide chlorhydrique avec \(%s [g]\) d'hydroxyde de calcium solide.<br/><br/>"%(cc_molaire_HCl_latex,masse_CaOH2_latex)
        self.enonce+="Quel volume d'acide chlorhydrique est nécessaire, quelle est la concentration massique en sel dans la solution obtenue?</p>"
        self.enonce+="<p>\(V_{HCl} \)={2:NUMERICAL:=%s:%s}"%(vol_HCl,vol_HCl*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~[g]~=[L]~[g/L]~[mol/L]}</p>"
        self.enonce+="<p>\( \gamma_{CaCl_2}\)={2:NUMERICAL:=%s:%s}"%(cc_massique_CaCl2,cc_massique_CaCl2*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~[g]~[L]~=[g/L]~[mol/L]}</p>"
        
        self.feedback="<style>table {border-collapse: collapse;border: 1px solid black;} th, td {border: 1px solid black;height:30px}</style>"
        self.feedback+='<p><table>'
        self.feedback+='<tr><td></td><td>\(2 \\ HCl\)</td><td>\(+ \\ Ca(OH)_2 \\ \\rightarrow\)</td><td>\(CaCl_2\)</td><td>\(+ \\ 2 \\ H_{2} O \)</td></tr>'
        self.feedback+='<tr><td>n[mol]</td><td> \(%s\)</td> <td>\(%s\)</td> <td>\(%s\)</td> <td></td></tr>'%(mole_HCl_latex,mole_CaOH2_latex,mole_CaOH2_latex)
        self.feedback+='<tr><td>m[g]</td><td> </td> <td>\(%s\)</td> <td>\(%s\)</td> <td></td></tr>'%(masse_CaOH2_latex,masse_CaCl2_latex)
        self.feedback+='<tr><td>M[g/mol]</td><td> </td> <td>\(%s\)</td> <td>\(%s\)</td> <td></td></tr>'%("74","110")
        self.feedback+='<tr><td>\(C_M\)[mol/L]</td><td>\(%s\) </td> <td></td> <td></td> <td></td></tr>'%(cc_molaire_HCl_latex)
        self.feedback+='<tr><td>\(C_m\)[g/L]</td><td> </td> <td></td> <td>\(%s\)</td> <td></td></tr>'%(cc_massique_CaCl2_latex)
        self.feedback+='<tr><td>\(V_{sol}\)[L]</td><td> \(%s\)</td> <td></td> <td>\(%s\)</td> <td></td></tr>'%(vol_HCl_latex,vol_HCl_latex)
        self.feedback+="</table></p>"
        
        self.feedback+="<p><b>Données</b><br/><br/>"
        self.feedback+="\(m_{Ca(OH)_2}=%s[g]\)<br/><br/>"%masse_CaOH2_latex
        self.feedback+="\(M_{Ca(OH)_2}=74[g \cdot mol^{-1}]\)<br/><br/>"
        self.feedback+="\(M_{CaCl_2}=110[g \cdot mol^{-1}]\)<br/><br/>"
        self.feedback+="\(C_{M_{HCl}}=%s[mol \cdot L^{-1}]\)"%cc_molaire_HCl_latex
        
        self.feedback+="</p><br/><br/>"
        
        self.feedback+="<p><b>Inconnues</b><br/><br/>"
        self.feedback+="\(\gamma_{CaCl_2}\)=?<br/><br/>"
        self.feedback+="\(V_{HCl}\)=?</p>"
        
        self.feedback+="<br/><br/>"
        
        self.feedback+="<p><b>Équations</b><br/><br/>"
        self.feedback+="\(n_{Ca(OH)_2}=\\frac{m_{Ca(OH)_2} }{M_{Ca(OH)_2}  }\)<br/><br/>"
        self.feedback+="\(n=C_M \cdot V_Sol \\ \\rightarrow \\ V_{HCl}=\\frac{n_{HCl}} {C_{M_{HCl}}}  \)<br/><br/>"
        self.feedback+="\(\gamma_{CaCl_2}=\\frac{m_{CaCl_2}}{V_{sol}} \)"
        self.feedback+="</p>"
        self.feedback+="<br/><br/>"
        
        self.feedback+="<p><b>Résolution</b><br/><br/>"
        self.feedback+="\(n_{Ca(OH)_2}=\\frac{m_{Ca(OH)_2} }{M_{Ca(OH)_2}  }  \\ \\rightarrow \\ n_{Ca(OH)_2}=\\frac{%s}{%s} \\ \\rightarrow \\ n_{Ca(OH)_2}=%s[mol] \)<br/><br/>"%(masse_CaOH2_latex,"74",mole_CaOH2_latex)
        self.feedback+="\( n_{HCl}=2 \cdot n_{Ca(OH)_2}  \\ \\rightarrow \\ n_{HCl}=%s[mol]\) <br/><br/>"%mole_HCl_latex
        self.feedback+="\(V_{HCl}=\\frac{n_{HCl}} {C_{M_{HCl}}}  \\ \\rightarrow \\ V_{HCl}=\\frac{%s}{%s}  \\ \\rightarrow \\ V_{HCl}=%s[L] \)<br/><br/>"%(mole_HCl_latex,cc_molaire_HCl_latex,vol_HCl_latex)
        self.feedback+="\( n_{CaCl_{2}}=n_{Ca(OH)_2}  \\ \\rightarrow \\ n_{CaCl_{2}}=%s[mol]\)<br/><br/>"%mole_CaOH2_latex
        self.feedback+="\(\gamma_{CaCl2}=\\frac{m_{CaCl_2}}{V_{sol}} \\ \\rightarrow \\ \gamma_{CaCl_{2}}=\\frac{%s}{%s} \\ \\rightarrow \\ \gamma_{CaCl_{2}}=%s[mol] \)"%(masse_CaCl2_latex,vol_HCl_latex,cc_massique_CaCl2_latex)
        self.feedback+="</p>"
        self.feedback+="<br/><br/>"
        
        self.feedback+="<p><b>Réponses</b><br/><br/>"
        self.feedback+="Le volume d'acide chlorhydrique vaut : \( V_{HCl}=%s[L]\).<br/><br/>"%vol_HCl_latex
        self.feedback+="La concentration massique en chlorure de calcium vaut : \( \gamma_{CaCl_{2}}=%s[g \cdot L^{-1}]\).</p>"%cc_massique_CaCl2_latex
    #
    def exe_2(self):
        #2H3PO4 + 6Na => 2Na3PO4 + 3H2
        masse_Na=float(random.randint(30,300))/100
        mole_Na=masse_Na/23
        cc_molaire_H3PO4=float(random.randint(30,150))/100
        vol_H3PO4=(2*masse_Na)/(6*23*cc_molaire_H3PO4)
        vol_H2=(3*masse_Na*22.4)/(6*23)
        
        mole_H3PO4=mole_Na*2/6
        mole_H3PO4,mole_H3PO4_latex=convert_sci(mole_H3PO4)
        mole_H2=mole_Na/2
        mole_H2,mole_H2_latex=convert_sci(mole_H2)
        
        masse_Na,masse_Na_latex=convert_sci(masse_Na)
        mole_Na,mole_Na_latex=convert_sci(mole_Na)
        cc_molaire_H3PO4,cc_molaire_H3PO4_latex=convert_sci(cc_molaire_H3PO4)
        vol_H3PO4,vol_H3PO4_latex=convert_sci(vol_H3PO4)
        vol_H2,vol_H2_latex=convert_sci(vol_H2)
        
        self.enonce="<p>Quelle masse de sodium faut-il utiliser pour faire complètement réagir \(%s [L]\) d'une solution \(%s [M]\) d'acide phosphorique ?<br>"%(vol_H3PO4_latex,cc_molaire_H3PO4_latex)
        self.enonce+="Quel est le volume (CNTP) de gaz libéré au cours de cette réaction?</p>"
        self.enonce+="<p>\(m_{Na} \)={2:NUMERICAL:=%s:%s}"%(masse_Na,masse_Na*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~[g]~=[L]~[g/L]~[mol/L]}</p>"
        self.enonce+="<p>\( V_{H_2}\)={2:NUMERICAL:=%s:%s}"%(vol_H2,vol_H2*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~[g]~=[L]~[g/L]~[mol/L]}</p>"
        
        self.feedback="<style>table {border-collapse: collapse;border: 1px solid black;} th, td {border: 1px solid black;height:30px}</style>"
        self.feedback+='<p><table>'
        self.feedback+='<tr><td></td><td>\(2 \\ H_{3}PO_4\)</td><td>\(+ \\ 6 \\ Na \\ \\rightarrow\)</td><td>\(2 \\ Na_{3}PO_4\)</td><td>\(+ \\ 3 \\ H_{2}\)</td></tr>'
        self.feedback+='<tr><td>\(n[mol]\)</td><td> \(%s\)</td> <td>\(%s\)</td> <td></td> <td>\(%s\)</td></tr>'%(mole_H3PO4_latex,mole_Na_latex,mole_H2_latex)
        self.feedback+='<tr><td>\(m[g]\)</td><td> </td> <td>\(%s\)</td> <td></td> <td></td></tr>'%(masse_Na_latex)
        self.feedback+='<tr><td>\(M[g/mol]\)</td><td> </td> <td>\(%s\)</td> <td></td> <td></td></tr>'%("23")
        
        self.feedback+='<tr><td>\(C_M[mol/L]\)</td><td>\(%s\) </td> <td></td> <td></td> <td></td></tr>'%(cc_molaire_H3PO4_latex)
        self.feedback+='<tr><td>\(V_{sol}[L]\)</td><td> \(%s\)</td> <td></td> <td></td> <td></td></tr>'%(vol_H3PO4_latex)
        self.feedback+='<tr><td>\(V_{gaz}[L]\)</td><td></td> <td></td> <td></td> <td>\(%s\)</td></tr>'%(vol_H2_latex)
        self.feedback+="</table></p>"
        
        self.feedback+="<p><b>Données</b><br/><br/>"
        self.feedback+="\(V_{H_{3}PO_4}=%s[L]\)<br/><br/>"%vol_H3PO4_latex
        self.feedback+="\(C_{M_{H_{3}PO_4}}=%s[mol \cdot L^{-1}]\)<br/><br/>"%cc_molaire_H3PO4_latex
        self.feedback+="\(M_{Na}=23[g \cdot mol^{-1}]\)<br/><br/>"
        #self.feedback+="\(_{CaCl_2}=110[g \cdot mol^{-1}]\)<br/><br/>"
        
        
        self.feedback+="</p><br/><br/>"
        
        self.feedback+="<p><b>Inconnues</b><br/><br/>"
        self.feedback+="\(m_{Na}\)=?<br/><br/>"
        self.feedback+="\(V_{H_2}\)=?</p>"
        
        self.feedback+="<br/><br/>"
        
        self.feedback+="<p><b>Équations</b><br/><br/>"
        self.feedback+="\(n_{H_{3}PO_4}=C_{M_{H_{3}PO_4}} \cdot V_{H_{3}PO_4}\)<br/><br/>"
        self.feedback+="\(n=\\frac{m}{M} \\ \\rightarrow \\ m_{Na}=n_{Na} \cdot M_{Na}  \)<br/><br/>"
        self.feedback+="\(n=\\frac{V_{gaz}}{22,4} \\ \\rightarrow \\ V_{H_2}=n_{H_2} \cdot 22,4\)"
        self.feedback+="</p>"
        self.feedback+="<br/><br/>"
        
        self.feedback+="<p><b>Résolution</b><br/><br/>"
        self.feedback+="\(n_{H_{3}PO_4}=C_{M_{H_{3}PO_4}} \cdot V_{H_{3}PO_4} \\ \\rightarrow \\ n_{H_{3}PO_4}=%s \cdot %s \\ \\rightarrow \\ n_{H_{3}PO_4}=%s[mol]\)<br/><br/>"%(cc_molaire_H3PO4_latex,vol_H3PO4_latex,mole_H3PO4_latex)
        self.feedback+="\(n_{Na}=3 \cdot n_{H_{3}PO_4} \\ \\rightarrow \\ n_{Na}=%s[mol] \)<br/><br/>"%mole_Na_latex
        self.feedback+="\(m_{Na}=n_{Na} \cdot M_{Na}  \\ \\rightarrow \\ m_{Na}=%s \cdot 23 \\ \\rightarrow \\ m_{Na}=%s[g]\)<br/><br/>"%(mole_Na_latex,masse_Na_latex)
        self.feedback+="\(n_{H_2}=\\frac{3}{2} \cdot n_{H_{3}PO_4} \\ \\rightarrow \\ n_{H_2}=%s[mol] \)<br/><br/>"%mole_H2_latex
        self.feedback+="\(V_{H_2}=n_{H_2} \cdot 22,4 \\ \\rightarrow \\ V_{H_2}=%s \cdot 22,4 \\ \\rightarrow \\ V_{H_2}=%s[L]\)"%(mole_H2_latex,vol_H2_latex)
        self.feedback+="</p>"
        self.feedback+="<br/><br/>"
        
        self.feedback+="<p><b>Réponses</b><br/><br/>"
        self.feedback+="Le volume de dihydrogène vaut : \( V_{H_2}=%s[L]\).<br/><br/>"%vol_H2_latex
        self.feedback+="La masse de sodium vaut : \( m_{Na}=%s[g]\).</p>"%masse_Na_latex
    #
    
    def exe_3(self):
        #On souhaite produire %s L %s [g] d'oxyde de bore, quelle masse de bore et quel volume CNTP de dioxygène faut-il utiliser?
        #3O2+4B=>2B2O3
        #solubilité de B203=36g/L
        
        self.valeurs={}
        
        self.valeurs["P1_nom"]="oxyde de bore"
        self.valeurs["P1_form"]="B_{2}O_{3}"
        self.valeurs["P1_masse"]=float(random.randint(30,300))/100
        self.valeurs["P1_masse_molaire"]=70
        self.valeurs["P1_moles"]=self.valeurs["P1_masse"]/self.valeurs["P1_masse_molaire"]
        self.valeurs["P1_coef"]=2
        self.valeurs["P1_cc_massique"]=float(random.randint(10,36))
        self.valeurs["P1_volume_solution"]=self.valeurs["P1_masse"]/self.valeurs["P1_cc_massique"]
        
        self.valeurs["R1_nom"]="dioxygène"
        self.valeurs["R1_form"]="O_{2}"
        self.valeurs["R1_moles"]=(self.valeurs["P1_moles"]/2)*3
        self.valeurs["R1_volume_gaz"]=self.valeurs["R1_moles"]*22.4
        self.valeurs["R1_coef"]=3
        
        self.valeurs["R2_nom"]="bore"
        self.valeurs["R2_form"]="B"
        self.valeurs["R2_masse_molaire"]=11
        self.valeurs["R2_moles"]=self.valeurs["P1_moles"]*2
        self.valeurs["R2_masse"]=self.valeurs["R2_moles"]*self.valeurs["R2_masse_molaire"]
        self.valeurs["R2_coef"]=4
        
        self.valeurs_to_tex()
        
        self.enonce="<p>On souhaite produire \({P1_volume_solution_tex} [L]\) d'une solution \({P1_cc_massique_tex} [g \cdot L^{{-1}}]\) d'oxyde de bore, quelle masse de bore et quel volume CNTP de dioxygène faut-il utiliser?</p>"
        self.enonce+="<p>\(m_{{B}} \)={{2:NUMERICAL:={R2_masse}:%s}}"%self.valeurs["R2_masse"]*3/100
        self.enonce+="{1:MC:[g/mol]~[mol]~=[g]~[L]~[g/L]~[mol/L]}</p>"
        self.enonce+="<p>\( V_{{O_2}}\)={{2:NUMERICAL:={R1_volume_gaz}:%s}}"%self.valeurs["R1_volume_gaz"]*3/100
        self.enonce+="{1:MC:[g/mol]~[mol]~[g]~=[L]~[g/L]~[mol/L]}</p>"
        self.enonce.format(**self.valeur)
        
        
        
        #self.feedback+="<p><b>Données</b><br/><br/>"
        #self.feedback+="\(V_{H_{3}PO_4}=%s[L]\)<br/><br/>"%vol_H3PO4_latex
        #self.feedback+="\(C_{M_{H_{3}PO_4}}=%s[mol \cdot L^{-1}]\)<br/><br/>"%cc_molaire_H3PO4_latex
        #self.feedback+="\(M_{Na}=23[g \cdot mol^{-1}]\)<br/><br/>"
        ##self.feedback+="\(_{CaCl_2}=110[g \cdot mol^{-1}]\)<br/><br/>"
        
        
        #self.feedback+="</p><br/><br/>"
        
        #self.feedback+="<p><b>Inconnues</b><br/><br/>"
        #self.feedback+="\(m_{Na}\)=?<br/><br/>"
        #self.feedback+="\(V_{H_2}\)=?</p>"
        
        #self.feedback+="<br/><br/>"
        
        #self.feedback+="<p><b>Équations</b><br/><br/>"
        #self.feedback+="\(n_{H_{3}PO_4}=C_{M_{H_{3}PO_4}} \cdot V_{H_{3}PO_4}\)<br/><br/>"
        #self.feedback+="\(n=\\frac{m}{M} \\ \\rightarrow \\ m_{Na}=n_{Na} \cdot M_{Na}  \)<br/><br/>"
        #self.feedback+="\(n=\\frac{V_{gaz}}{22,4} \\ \\rightarrow \\ V_{H_2}=n_{H_2} \cdot 22,4\)"
        #self.feedback+="</p>"
        #self.feedback+="<br/><br/>"
        
        #self.feedback+="<p><b>Résolution</b><br/><br/>"
        #self.feedback+="\(n_{H_{3}PO_4}=C_{M_{H_{3}PO_4}} \cdot V_{H_{3}PO_4} \\ \\rightarrow \\ n_{H_{3}PO_4}=%s \cdot %s \\ \\rightarrow \\ n_{H_{3}PO_4}=%s[mol]\)<br/><br/>"%(cc_molaire_H3PO4_latex,vol_H3PO4_latex,mole_H3PO4_latex)
        #self.feedback+="\(n_{Na}=3 \cdot n_{H_{3}PO_4} \\ \\rightarrow \\ n_{Na}=%s[mol] \)<br/><br/>"%mole_Na_latex
        #self.feedback+="\(m_{Na}=n_{Na} \cdot M_{Na}  \\ \\rightarrow \\ m_{Na}=%s \cdot 23 \\ \\rightarrow \\ m_{Na}=%s[g]\)<br/><br/>"%(mole_Na_latex,masse_Na_latex)
        #self.feedback+="\(n_{H_2}=\\frac{3}{2} \cdot n_{H_{3}PO_4} \\ \\rightarrow \\ n_{H_2}=%s[mol] \)<br/><br/>"%mole_H2_latex
        #self.feedback+="\(V_{H_2}=n_{H_2} \cdot 22,4 \\ \\rightarrow \\ V_{H_2}=%s \cdot 22,4 \\ \\rightarrow \\ V_{H_2}=%s[L]\)"%(mole_H2_latex,vol_H2_latex)
        #self.feedback+="</p>"
        #self.feedback+="<br/><br/>"
        
        #self.feedback+="<p><b>Réponses</b><br/><br/>"
        #self.feedback+="Le volume de dihydrogène vaut : \( V_{H_2}=%s[L]\).<br/><br/>"%vol_H2_latex
        #self.feedback+="La masse de sodium vaut : \( m_{Na}=%s[g]\).</p>"%masse_Na_latex
        
        
    def exe_4(self):
        
        self.enonce="<p>Quelle est la masse de %s [L] (CNTP) de %s?</p>"%(self.volume_gaz_litre_latex,self.nom)
        self.enonce+="<p>m={2:NUMERICAL:=%s:%s}"%(self.masse,self.masse*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~=[g]~[L]~[g/L]~[mol/L]}</p>"
        
        self.feedback="<p><b>Données</b><br/><br/>"
        self.feedback+="Formule : \( %s \)<br/><br/>"%self.latex
        self.feedback+="\(M=%s[g \cdot mol^{-1}]\)<br/><br/>"%(self.masse_molaire)
        self.feedback+="\(V_{gaz}=%s[L]\) </p>"%self.volume_gaz_litre_latex
        self.feedback+="<br/><br/>"
        
        self.feedback+="<p><b>Inconnue</b><br/><br/>"
        self.feedback+="m=?</p>"
        self.feedback+="<br/><br/>"
        
        self.feedback+="<p><b>Équations</b>s<br/><br/>"
        self.feedback+="\(n=\\frac{V_{gaz}}{22,4}\)<br/><br/>"
        self.feedback+="\(n=\\frac{m}{M} \\ \\rightarrow \\ m=n \cdot M\)</p>"
        self.feedback+="<br/><br/>"
        
        self.feedback+="<p><b>Résolution</b><br/><br/>"
        self.feedback+="\(n=\\frac{V_{gaz}}{22,4} \\ \\rightarrow \\ n=\\frac{%s}{22,4} \\ \\rightarrow \\ n=%s[mol]\)<br/><br/>"%(self.volume_gaz_litre_latex,self.mole_latex)
        self.feedback+="\(m=n \cdot M \\ \\rightarrow \\ m=%s \cdot %s \\ \\rightarrow \\ m=%s [g]\)</p>"%(self.mole_latex,self.masse_molaire,self.masse_latex)
        self.feedback+="<br/><br/>"
        
        self.feedback+="<p><b>Réponse</b><br/><br/>"
        self.feedback+="La masse vaut : \(m=%s[g]\).</p>"%self.masse_latex
        
    def exe_5(self):
        
        self.enonce="<p>Quel est le volume (CNTP) occupé par %s [g] de %s?</p>"%(self.masse_latex,self.nom)
        self.enonce+="<p>V={2:NUMERICAL:=%s:%s}"%(self.volume_gaz_litre,self.volume_gaz_litre*3/100)
        self.enonce+="{1:MC:[g/mol]~[mol]~[g]~=[L]~[g/L]~[mol/L]}</p>"
        
        self.feedback="<p><b>Données</b><br/><br/>"
        self.feedback+="Formule : \( %s \)<br/><br/>"%self.latex
        self.feedback+="\(M=%s[g \cdot mol^{-1}]\)<br/><br/>"%(self.masse_molaire)
        self.feedback+="\(m=%s[g] \)</p>"%self.masse_latex
        self.feedback+="<br/><br/>"
        
        self.feedback+="<p><b>Inconnue</b><br/><br/>"
        self.feedback+="\(V_{gaz}\)=?</p>"
        self.feedback+="<br/><br/>"
        
        self.feedback+="<p><b>Équations</b>s<br/><br/>"
        self.feedback+="\(n=\\frac{m}{M}\)<br/><br/>"
        self.feedback+="\(n=\\frac{V_{gaz}}{22,4}  \\ \\rightarrow \\ V_{gaz}=n \cdot 22,4\)</p>"
        self.feedback+="<br/><br/>"
        
        
        self.feedback+="<p><b>Résolution</b><br/><br/>"
        self.feedback+="\(n=\\frac{m}{M} \\ \\rightarrow \\ n=\\frac{%s}{%s} \\ \\rightarrow \\ n=%s[mol]\)<br/><br/>"%(self.masse_latex,self.masse_molaire,self.mole_latex)
        self.feedback+="\(V_{gaz}=n \cdot 22,4 \\ \\rightarrow \\ V_{gaz}=%s \cdot 22,4 \\ \\rightarrow \\ V_{gaz}=%s [L]\)</p>"%(self.mole_latex,self.volume_gaz_litre_latex)
        self.feedback+="<br/><br/>"
        
        self.feedback+="<p><b>Réponse</b><br/><br/>"
        self.feedback+="Le volume vaut : \(V_{gaz}\)=%s[L].</p>"%self.volume_gaz_litre_latex
    #
    
    
    
    

if __name__=="__main__":
     questionnaire=[]
     liste_molec=[]
     
     
     for i in range(10):
         exercice=Exercice()
         questionnaire.append(exercice)
     
     
         
     
     f = open('./exe_stoechio.xml','w')
    
     f.write('<?xml version="1.0" encoding="UTF-8"?> \n')
     f.write("<quiz> \n")
     f.write('<question type="category"> \n')
     f.write("<category> \n")
     f.write("<text>$course$/Chimie/Stoechiometrie(beta)</text> \n")
     f.write("</category> \n")
     f.write("</question> \n")
     for question in questionnaire:
        f.write('<question type="cloze"> \n')
        f.write("<name> \n")
        f.write("<text>Stoechiometrie</text> \n")
        f.write("</name> \n")
        f.write('<questiontext format="html"> \n')
        f.write("<text><![CDATA[ %s ]]></text>  \n" %question.enonce)
        f.write("</questiontext>  \n")
        f.write('<generalfeedback format="html">  \n')
        f.write("<text><![CDATA[ %s ]]></text>  \n" %question.feedback)
        f.write("</generalfeedback>  \n")
        f.write("<penalty>0.3333333</penalty>  \n")
        f.write("<hidden>0</hidden>  \n")
        f.write("</question>  \n")
        f.write('\n')
     f.write('</quiz>')
     f.close()
      
"""

On souhaite produire %s [L] d'une solution %s[M] de sulfate d'aluminium à partir d'hydroxyde d'aluminium solide et d'une solution %s [M] d'acide sulfurique. Quel volume d'acide sulfurique est nécessaire et quelle masse d'hydroxyde d'aluminium sont nécessaires.


On souhaite produire %s [g] d'oxyde de bore, quelle masse de bore et quel volume CNTP de dioxygène faut-il utiliser?

3) On peut produire le chlore en laboratoire selon la réaction suivante :
MnO2 + 4 HCl => MnCl2 + Cl2 + 2 H2O
Combien de grammes de chlore (Cl2) peut-on préparer à partir de 100 g de MnO2?

 5. Le sulfure d'hydrogène est un gaz qu'il est possible d'obtenir par réaction de l'acide chlorhydrique avec le sulfure de fer (II). 
 
  7. Quelle quantité de sulfure d'hydrogène gazeux (en moles) faudra-t-il faire passer dans 600 ml d'une solution de d'hydroxyde de calcium 0,7M pour faire réagir entièrement l'hydroxyde de calcium?

"""