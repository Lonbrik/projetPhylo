#!/usr/bin/env python3
#-*- coding Utf-8 -*-

import sys, os, re
import node
import newickparser
from ete3 import Tree, TreeStyle

#récupération des paramètres
os.system("clear")
filegene = sys.argv[1]          #fichier de l'arbre de gènes
filespecies = sys.argv[2]       #fichier de l'arbre d'espces
filemap = sys.argv[3]           #fichier de correspondance entre gene et espece

#generation des structures d'arbres à partir des fichiers
dictmap = newickparser.mapParser(filemap)
rootgene = node.node(name ="root", gen = 0, enfants = [])
rootspecies = node.node(name = "root", gen =0, enfants = [])
arbrespecies = newickparser.lectureArbre(filespecies)
if arbrespecies != 1 :
    newickparser.parser(None, rootspecies, 0, arbrespecies.strip())
arbregene = newickparser.lectureArbre(filegene)
if arbregene != 1 :
    newickparser.parser(None, rootgene, 0, arbregene.strip())
newickparser.gene_to_species(rootgene, dictmap)

print (rootgene,"\n")
print (rootspecies)

#affichage graphique des arbres et generation des fichiers svg
genetree = Tree(arbregene)
spectree = Tree(arbrespecies)
ts = TreeStyle()
ts.mode = "r"
ts.orientation = 1
genetree.show()
spectree.show(tree_style=ts)
genetree.render("genetree.svg")
spectree.render("spectree.svg")
