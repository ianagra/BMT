import xml.dom.minidom as A
import xml.sax as B
#usando DOM (processador A) para extrair os autores
raiz_autores = A.parse("cf79.xml")
autores = raiz_autores.getElementsByTagName("AUTHOR")
with open("autores.xml", "w") as x:
    for autor in autores:
        nome_autor = autor.firstChild.data
        x.write(nome_autor + "\n")
#usando SAX (processador B) para extrair os títulos
class ManipuladorTitulo(B.ContentHandler):
    def __init__(txt):
        super().__init__()
        txt.inside_title = False
        txt.title_text = ""
    def startElement(txt, nome, atrib):
        if nome == "TITLE":
            txt.inside_title = True
    def characters(txt, conteudo):
        if txt.inside_title:
            txt.title_text += conteudo.strip()
    def endElement(txt, nome):
        if nome == "TITLE":
            with open("titulo.xml", "a") as y:
                y.write(txt.title_text.replace("\n", " ") + "\n")
            txt.inside_title = False
            txt.title_text = ""
parser = B.make_parser()
parser.setFeature(B.handler.feature_external_ges, False)
manipulador = ManipuladorTitulo()
parser.setContentHandler(manipulador)
parser.parse("cf79.xml")
