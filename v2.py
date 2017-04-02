import queue as Q
class Paire():
    """Objet paire ordonnable"""
    def __init__(self, element, priorité):
        self.element = element
        self.priorité = priorité

    def __lt__(self, other):
        return int.__lt__(self.priorité, other.priorité)

    def __gt__(self, other):
        return int.__gt__(self.priorité, other.priorité)

    def __eq__(self, other):
        return int.__eq__(self.priorité, other.priorité) and self.element == other.element

    def __le__(self, other):
        return  int.__le__(self.priorité, other.priorité)

    def __ge__(self, other):
        return  int.__ge__(self.priorité, other.priorité)

    def __str__(self):
        return "(" + self.element.__str__() + self.priorité.__str__() + ")"

    def __repr__(self):
        return self.__str__()

class File_de_prio():
    def __init__(self):
        self.donnes = []


    def qsize(self):
        return len(self.donnes)

    def get(self):
        return self.donnes.pop()


    def put(self, elem):
        for i, el in enumerate(self.donnes):
            if elem > el:
                self.donnes = self.donnes[:i ] + [elem] + self.donnes[i :]
                return None
        self.donnes =  self.donnes + [elem]


    def __str__(self):
        return self.donnes.__str__()
class Arbre():
    """Objet Arbre simple
    """
    def __init__(self, valeur):
        """creer un arbre non vide avec une valeur au noeud"""
        self.noeud = valeur
        self.gauche = None
        self.droite = None


    def __str__(self):
        return  "(" + self.gauche.__str__() + self.noeud.__str__() + self.droite.__str__() + ")"



def creer_arbre(densité_lettres):
    """
    argument prend un dictionaire des densités
    returns l'arbre de codage

    """
    file_de_prio = File_de_prio()

    for lettre in densité_lettres.keys():
        file_de_prio.put(Paire(Arbre(lettre), densité_lettres[lettre]))
    print(file_de_prio)
    while file_de_prio.qsize() > 1:
        gauche = file_de_prio.get()
        droite = file_de_prio.get()
        nouveau_arbre = Arbre(None)
        nouveau_arbre.gauche = gauche.element
        nouveau_arbre.droite = droite.element
        file_de_prio.put(Paire(nouveau_arbre, gauche.priorité + droite.priorité))

    return file_de_prio.get().element


def creer_densite(texte):
    """Renvoi un dictionaire des occurences des lettres """
    densité_lettres = {}
    for lettre in texte:
        if lettre in densité_lettres:
            densité_lettres[lettre] += 1
        else:
            densité_lettres[lettre] = 1
    return densité_lettres


def creer_dict(arbre, parcours, dico):
    """Renvoi un dictionaire correspondant a l'arbre par récusion"""
    if arbre.noeud != None:
        print("h",parcours)
        dico[arbre.noeud] = parcours
        print(dico[arbre.noeud])
        return None
    if arbre.gauche != None:
        parcours = parcours + "0"
        creer_dict(arbre.gauche, parcours, dico)
        print("p",parcours)
        parcours = parcours[:-1]
        print("p", parcours)
    if arbre.droite != None:
        parcours = parcours + "1"
        creer_dict(arbre.droite, parcours, dico)

if __name__ == "__main__":

    dens = creer_densite("chabadabada")
    print(dens)
    arbre = creer_arbre(dens)
    dico = {}
    creer_dict(arbre, "", dico)
    print(dico)