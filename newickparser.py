#!/usr/bin/env python3
# -*- coding: utf-8 -*

import node
import re

#ouvertrure des fichiers, conversion en String et vérification de l'integrité du format newick
def lectureArbre(fichier):
    global index
    with open(fichier) as f:
        arbre = f.read()
    #corps = arbre.replace(re.findall("\w;", arbre)[0], "")
    index = len(arbre) - 2 
    if not arbre.strip().endswith(";"):
        print("error, wrong format file")
        return (1)
    if  arbre == "":
        print("error, empty file")
        return (1)
    if arbre.count("(")!=arbre.count(")"):
        print("error, wrong format : parenthesis mismatch")
        return(1)
    return arbre

#création d'un dictionnaire de correspondance entre gène et espèce
#prend en paramètre un fichier de correspondance avec "=" en délimiteur
def mapParser(mapfile):
    dictmap ={}
    with  open(mapfile) as m:
        mapline = m.readlines()
    for line in mapline:
        splitline = line.split("=")
        dictmap[splitline[0].strip()]=splitline[1].strip()
    return dictmap

#permutation du nom de géne par nom d'espèce dans un arbre.
#prend en parametre la racine d'un arbre et un dictionnaire de correspondance
def gene_to_species(tree, dictmap):
    if tree.name in dictmap:
        tree.name = dictmap[tree.name]
    for node in tree.enfants:
        gene_to_species(node, dictmap)

#crée une structure d'arbre à partir de la class node
#prend en parametre 2 nodes, un entier représentant la génération et la string newick
def parser(parent, courant, niveau, arbre):
    global index
    strtmp = ""
    while index >= 0 :
        if arbre[index] == ")" :
            if strtmp != "" : courant.name=strtmp[::-1].strip('\'')
            nouvelenfant = node.node(parent = courant, enfants = [], gen = niveau+1)
            courant.enfants.append(nouvelenfant)
            strtmp = ""
            index -= 1
            parser(courant, nouvelenfant, niveau+1, arbre)
        elif arbre[index] == ",":
            if strtmp != "" : parent.enfants[-1].name = strtmp[::-1].strip('\'')
            nouveaufrere = node.node(parent = parent, enfants = [], gen = niveau)
            parent.enfants.append(nouveaufrere)
            courant = nouveaufrere
            strtmp = ""
            index -= 1
        elif arbre[index] == "(":
            index -= 1
            parent.enfants[-1].name=strtmp[::-1].strip('\'')
            return
        elif arbre[index] == ":":
            parent.enfants[-1].dist=float(strtmp[::-1])
            strtmp = ""
            index -= 1
        elif arbre[index] == ";":
            index -= 1
            pass
        else : 
            strtmp = strtmp+arbre[index]
            index -= 1
