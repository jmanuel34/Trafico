# Lectura desde fichero
import re
from pprint import pprint
patron1 = '<.*?>'
patronEspacio = '\s+'
pttrn = '<tr.*?p1TablaIncidencias.*?(\d\d:\d\d)</span.*?(\d\d/\d\d/\d\d\d\d).*?alt=(.*?)/(.*?)/.*?>M-40<.*?nombreIncidencia.*?span style="margin-top:10px; float:left; clear:both">(.*?)</tr>'

p = './trafico.html'
with open(p, 'r', encoding='utf-8') as file:
    pagina = file.read()
    elements = re.findall(pttrn, pagina, re.DOTALL | re.MULTILINE | re.IGNORECASE)

    elementos = [
        [line[0], line[1], line[2], line[3], re.sub(patron1, ' ', line[4])]
        for line in elements
    ]
 #   print (elementos)

    elementos1 = [
        [line[0], line[1], line[2], line[3], re.sub(patronEspacio, ' ', line[4])]
        for line in elementos
    ]
#    print (elementos1)
    for element in elementos1:
        pprint(element[0])
        pprint(element[1])
        pprint(element[2])
        pprint(element[3])
        pprint(element[4])
 #       pprint(element[5])
