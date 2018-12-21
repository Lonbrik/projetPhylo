#!/usr/bin/env/ python3
# -*- coding Utf-8 -*-


#class node : permet de modéliser chaque noeud de l'arbre phylo.
#un node est équivalent à un sous arbre dont il est la racine

class node:
    def __init__(self, **kwargs):

        self.name = kwargs.get('name')
        self.parent = kwargs.get('parent')
        self.enfants = kwargs.get('enfants')
        self.gen = kwargs.get('gen')
        self.dist = kwargs.get('dist')

#vérifie si le node est la racine
    def isRoot(self):
        if self.parent:
            return False
        else:
            return True

#vérifie si le node est une feuille terminale
    def isLeaf(self):
        if self.enfants:
            return False
        else:
            return True

    def __repr__(self):
                return("nom({}) generation({}) enfants({}) dist({})".format
                (self.name, self.gen, self.enfants, self.dist))

    def sameNode(self, node):
        if self.name == node.name :
            for enfant1 in self.enfants:
                congru = False
                for enfant2 in node.enfants :
                    if enfant1.name == enfant2.name:
                        congru = True
            
        else:
            return False

    def congru(self, node):
        congru = self.sameNode(node)
        if congru :
            return self
        if not congru and not self.isLeaf() and not node.isLeaf():
            for enfant1 in self.enfants:
                for enfant2 in node.enfants:
                    enfant1.sameNode(enfant2)
