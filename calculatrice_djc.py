import pgzrun

#taille de la fenêtre
WIDTH = 600  #Dans ce bloc je definis toutes les variables.
HEIGHT = 852

#variables d'état
splash = True  #message d'acceuil
get_operation = True

#variables d'expression mathématique
expr = '' #expression nulle au début
op = '' #opération nulle au début
ans = '0.0' # reponse nulle au début

#zones actives
BOX = Rect((30, 50), (550, 180))
SBOX7 = Rect((45, 295), (110, 110)) #Ce bloc definit les rectangles qui serviront de bouttons pour entrer des nombres dans la calculatrice.
SBOX8 = Rect((185, 295), (110, 110))
SBOX9 = Rect((315, 295), (110, 110))
SBOX4 = Rect((45, 430), (110, 110))
SBOX5 = Rect((185, 430), (110, 110))
SBOX6 = Rect((315, 430), (110, 110))
SBOX1 = Rect((45, 565), (110, 110))
SBOX2 = Rect((185, 565), (110, 110))
SBOX3 = Rect((315, 565), (110, 110))
SBOX0 = Rect((45, 700), (110, 110))
SBOXN = Rect((450, 700), (110, 110))
SBOXM = Rect((450, 430), (110, 110))
SBOXD = Rect((450, 295), (110, 110))
SBOXP = Rect((450, 565), (110, 110))
SBOXV = Rect((185, 700), (110, 110))
SBOXE = Rect((315, 700), (110, 110))


def draw():
    screen.clear()
    screen.blit('background', (0,0))
    
    if splash: 
        # affiche le message d'acceuil avec le résultat
        to_show = 'Press Enter. Old ans -> ' + str(ans) 
    else: 
        # affiche l'expression mathématique
        to_show = expr

    screen.draw.text(to_show, topleft=(35, 130), color=(0, 0, 0), fontsize=48)


def on_key_down(key):
    global splash

    if key == keys.RETURN: # debute la calculatrice
        splash = False


def on_mouse_down(pos):
    global splash, get_operation, expr, op, ans

    if not splash:
        # pavé numérique (0-9.)
        if SBOX0.collidepoint(pos):
            expr += '0'
        elif  SBOX1.collidepoint(pos):
            expr += '1'
        elif  SBOX2.collidepoint(pos):
            expr += '2'
        elif  SBOX3.collidepoint(pos):
            expr += '3'
        elif  SBOX4.collidepoint(pos):
            expr += '4'
        elif  SBOX5.collidepoint(pos):
            expr += '5'
        elif  SBOX6.collidepoint(pos):
            expr += '6'
        elif  SBOX7.collidepoint(pos):
            expr += '7'
        elif  SBOX8.collidepoint(pos):
            expr += '8'
        elif  SBOX9.collidepoint(pos):
            expr += '9'
        elif  SBOXV.collidepoint(pos):
            expr += '.'
        #opérateurs (+-*/)
        elif  SBOXP.collidepoint(pos) and get_operation: # "and get_operation" limite l'ajout à seulement 1 opérateur
            expr += '+'
            op = '+'
            get_operation = False
        elif  SBOXN.collidepoint(pos) and get_operation:
            expr += '-'
            op = '-'
            get_operation = False
        elif  SBOXM.collidepoint(pos) and get_operation:
            expr += '*'
            op = '*'
            get_operation = False
        elif SBOXD.collidepoint(pos) and get_operation:
            expr += '/'
            op = '/'
            get_operation = False
        #calcule (=)
        elif  SBOXE.collidepoint(pos):
            if get_operation: # doit entrer un opérateur avant d'utiliser =
                pass

            else:
                # utilise l'opérateur comme séparateur de texte, produisant une liste de 2 éléments
                nums = expr.split(op)

                # effectue le calcul sur la liste avec l'opérateur choisie
                ans = calculate(nums, op)

                # remettre les variables à la condition de départ pour un nouveau calcul
                splash = True
                get_operation = True
                expr = ''
                op = ''
    

def calculate(two_numbers, op):

    # convertir les éléments de texte en valeurs décimales
    a = float(two_numbers[0])
    
    if two_numbers[1] == '': # si le 2e chiffre n'a pas été entré
        b = 0.0
    else:
        b = float(two_numbers[1])
    
    # le calcul
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        if b == 0.0: # vérifie pour l'erreur de division par 0
            return 'DIV/0 error'
        else:
            return a / b

pgzrun.go()