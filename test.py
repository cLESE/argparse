import argparse
import logging
logging.basicConfig(filename="monLog.log",level=logging.DEBUG)
parser = argparse.ArgumentParser()

'''argument positionnel'''
parser.add_argument("temps", help="durer de la playlist en minute", type=int)
parser.add_argument("nomfichier", help="nom donner a la playlist")
parser.add_argument("formatfichier", help="extension de la playlist", choices=['m3u', 'xspf', 'pls'])

'''argument optionnel'''
parser.add_argument("-G", "--genre", help="genre et pourcentage du genre voulu dans la playlist", nargs=2)
parser.add_argument("-g", "--sousgenre", help="sous genre et pourcentage du sous genre voulu dans la playlist", nargs=2)
parser.add_argument("-A", "--artiste", help="artiste et pourcentage de l'artiste voulu dans la playlist", nargs=2)
parser.add_argument("-a", "--album", help="album voulu dans la playlist")
parser.add_argument("-t", "--titre", help="titre voulu dans la playlist")

args = parser.parse_args()


'''Fonction de vérification des poucentages'''
def checkArg(arg):
    logging.info("verifie argument 2")
    try:
        nb = int(arg[1])
        if nb<0:
            nb = abs(nb)
            logging.warning('La quantité saisie doit etre positive')
            logging.info('Nombre négatif transformé en positif: ' + str(nb))
        elif nb>100:
            nb = None
            logging.warning('La quantité saisie est supérieur à 100')
            logging.info('Nombre supérieur à 100 transformé en : ' + str(nb))
        return True
    except ValueError:
        print ("Impossible de convertir \"" + arg[1] + "\" en nombre entier !")
        logging.error('Impossible de convertir ' + arg[1] + ' en nombre entier !')
        logging.debug(' *****************************************')
        exit(1)


for ARG in ['titre','genre','sousgenre','artiste','album']:
    if getattr(args, ARG) is not None:
        logging.info(' Argument --' + ARG + ' :\t' + getattr(args, ARG)[0] + ' ; ' + getattr(args, ARG)[1])
# On vérifie que le 2em sous argument de genre est bien un entier naturel
if checkArg(args.genre) == True:
    print ('ok')

logging.debug(' *****************************************')

'''Si les attributs sont renseignés on va vérifier le pourcentage
if args.genre:
    checkArg(args.genre[1])

if args.sousgenre:
    checkArg(args.sousgenre[1])

if args.artiste:
    checkArg(args.artiste[1])'''


'''Affichage
print("Création de la playlist " + (args.nomfichier) + "." + (args.formatfichier) + " d'une durée de " + str(args.temps) + " minutes")
if args.genre:
    print("La playlist contient " + str(args.genre[1]) + "% du genre " + (args.genre[0]))
if args.sousgenre:
    print("La playlist contient " + str(args.sousgenre[1]) + "% du sous genre " + (args.sousgenre[0]))
if args.artiste:
    print("La playlist contient " + str(args.artiste[1]) + "% de l'artiste " + (args.artiste[0]))
if args.album:
    print("La playlist contient l'album " + (args.album))
if args.titre:
    print("La playlist contient le titre " + (args.titre))'''

