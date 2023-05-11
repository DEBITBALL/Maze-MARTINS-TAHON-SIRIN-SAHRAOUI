import random
import datetime
import numpy as np
 

LARGEUR = input("Veuillez spécifier la largeur du labyrinthe.")  # Largeur du labyrinthe
HAUTEUR = input("Veuillez spécifier la hauteur du labyrinthe.")   # Hauteur du labyrinthe
compteur = []

LARGEUR = int(LARGEUR)
HAUTEUR = int(HAUTEUR)
 
# Représentation de chaque cellule du labyrinthe
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}
 
def get_edges():
    edges = []
    for x in range(LARGEUR):
        for y in range(HAUTEUR):
            if x > 0:
                edges.append(((x, y), (x-1, y)))
            if y > 0:
                edges.append(((x, y), (x, y-1)))
    return edges
 
def generer_labyrinthe():
    grid = [[Cell(x, y) for y in range(HAUTEUR)] for x in range(LARGEUR)]
    edges = get_edges()
    random.shuffle(edges)
    disjoint_set = [{(x, y)} for x in range(LARGEUR) for y in range(HAUTEUR)]
 
    for edge in edges:
        c1 = edge[0]
        c2 = edge[1]
 
        set1 = None
        set2 = None
        for s in disjoint_set:
            if c1 in s:
                set1 = s
            if c2 in s:
                set2 = s
        if set1 != set2:
            if c1[0] < c2[0]:
                grid[c1[0]][c1[1]].walls['E'] = False
                grid[c2[0]][c2[1]].walls['W'] = False
            elif c1[0] > c2[0]:
                grid[c1[0]][c1[1]].walls['W'] = False
                grid[c2[0]][c2[1]].walls['E'] = False
            elif c1[1] < c2[1]:
                grid[c1[0]][c1[1]].walls['S'] = False
                grid[c2[0]][c2[1]].walls['N'] = False
            elif c1[1] > c2[1]:
                grid[c1[0]][c1[1]].walls['N'] = False
                grid[c2[0]][c2[1]].walls['S'] = False
 
            disjoint_set.remove(set1)
            disjoint_set.remove(set2)
            new_set = set1.union(set2)
            disjoint_set.append(new_set)
 
    return grid
 
def resoudre_labyrinthe(maze):
    stack = [(0, 0)]
    visited = set()
    prev = {(0, 0): None}
 
    while stack:
        x, y = stack.pop()
        if (x, y) == (LARGEUR-1, HAUTEUR-1):
            path = []
            while (x, y) != (0, 0):
                path.append((x, y))
                x, y = prev[(x, y)]
            path.append((0, 0))
            path.reverse()
            return path
        if (x, y) in visited:
            continue
        visited.add((x, y))
        cell = maze[x][y]
        if not cell.walls['N'] and (x, y-1) not in visited:
            stack.append((x, y-1))
            prev[(x, y-1)] = (x, y)
        if not cell.walls['S'] and (x, y+1) not in visited:
            stack.append((x, y+1))
            prev[(x, y+1)] = (x, y)
        if not cell.walls['E'] and (x+1, y) not in visited:
            stack.append((x+1, y))
            prev[(x+1, y)] = (x, y)
        if not cell.walls['W'] and (x-1, y) not in visited:
            stack.append((x-1, y))
            prev[(x-1, y)] = (x, y)
 
 
 

def afficher_labyrinthe(maze, path=None):
    for y in range(HAUTEUR):
        for x in range(LARGEUR):
            cell = maze[x][y]
            if cell.walls['N']:
                print("+--", end="")
            else:
                print("+- ", end="")
        print("+")
        for x in range(LARGEUR):
            cell = maze[x][y]
            if path and (x, y) in path:
                print("|██", end="")
                compteur.append("1")
            elif cell.walls['W']:
                print("|  ", end="")
            else:
                print("   ", end="")
            if x == LARGEUR - 1:
                print("|")
        if y == HAUTEUR - 1:
            for x in range(LARGEUR):
                print("+--", end="")
            print("+")
    
       




print("       ")
print("Labyrinthe d'origine: ") 
 
maze = generer_labyrinthe()
afficher_labyrinthe(maze)

print("       ")
print("Labyrinthe résolu: ") 

path = resoudre_labyrinthe(maze)
afficher_labyrinthe(maze, path)

nombredecoups = len(compteur)

maintenant = datetime.datetime.now()

jour = maintenant.day
mois = maintenant.month
annee = maintenant.year

heure_formattee = maintenant.strftime("%d/%m/%Y à %H:%M:%S")


print("       ")
print("Résumé:")
print("       ")
print("Labyrinthe généré le:", heure_formattee)
print("Méthode utilisée: Kruskal")
print("Largeur du labyrinthe:", LARGEUR)
print("Hauteur du labyrinthe:", HAUTEUR)
print("Labyrinthe résolu en", nombredecoups, "coups.")