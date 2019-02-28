#!/usr/bin/env python3.4

import re
import urllib.request
import time
from pprint import pprint

p = "./traficoResults.txt"
url="http://infocar.dgt.es/etraffic/Incidencias?ca=13&provIci=28&caracter=acontecimiento&accion_consultar=Consultar&IncidenciasRETENCION=IncidenciasRETENCION&IncidenciasPUERTOS=IncidenciasPUERTOS&IncidenciasMETEOROLOGICA=IncidenciasMETEOROLOGICA&IncidenciasEVENTOS=IncidenciasEVENTOS&IncidenciasOTROS=IncidenciasOTROS&IncidenciasRESTRICCIONES=IncidenciasRESTRICCIONES&ordenacion=fechahora_ini-DESC"
result = urllib.request.urlopen(url)
pagina = (result.read().decode('utf8'))
patron1 = '<.*?>'
patronEspacio = '\s+'
pttrn = '<tr.*?p1TablaIncidencias.*?(\d\d:\d\d)</span.*?(\d\d/\d\d/\d\d\d\d).*?(Nivel.*?)/.*?<b>.*?</b>.*?<b>(.*?)</b>.*?nombreIncidencia.*?span style="margin-top:10px; float:left; clear:both">(.*?)</tr>'

with open(p, 'a', encoding='utf-8') as file:
#    print (pagina)
    elements = re.findall(pttrn, pagina, re.DOTALL | re.MULTILINE | re.IGNORECASE)
    pprint (elements)
    elementos = [
        [line[0], line[1], line[2], line[3],re.sub(patron1, ' ', line[4])]
        for line in elements
    ]
    elementos1 = [
        [line[0], line[1], line[2], line[3], re.sub(patronEspacio, ' ', line[4])]
        for line in elementos
    ]

    for element in elementos1:
        if (element[3]=="M-40"):
            pprint(element[0])
            pprint(element[1])
            pprint(element[2])
            pprint(element[3])
            pprint(element[4])


"""
file.write(element[0])
file.write(element[1])
file.write(element[2])
file.write(element[3])
file.write(element[4])
file.write(element[5])
"""
