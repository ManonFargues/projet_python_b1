import markdown2
import argparse
import os

analyseur = argparse.ArgumentParser ( description  =  " Transformer un fichier Markdown en fichier Html " )
analyseur.add_argument ( "-i" , "--input_file" , type  =  str, metavar  =  " " , help  =  "les fichiers Markdown à convertir en HTML " )
analyseur.add_argument ( "-o" , "--output_file" , type  =  str, metavar  =  " " , help  =  " les fichiers HTML générés pour le site statique " )
#parser.add_argument ( " -k " , " --kikoo " , type  =  str , metavar  =  " " , help  =  " Ajout dans le texte du" kikoo "," lol "," mdr "," ptdr "ou qui répète des lettres comme dans Hellllo et autres déformations du français " )

args = analyseur.parse_args ()

def md_to_html():
    dossier_md = os.listdir(args.input_file)
    for fichier in dossier_md:
        with open(args.input_file + '/' + fichier, 'r+', encoding = "utf-8") as fichier_md:
            HTML = markdown2.markdown(fichier_md.read())
            html1 = open(args.output_file + '/' + fichier.replace('.md', ".html"), "w+", encoding = "utf-8")
            html1.write(HTML)

md_to_html()
