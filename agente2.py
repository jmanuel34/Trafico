import re
import urllib.request
from pprint import pprint

p='/Users/jmanuel/Desktop/Ai/trafico/trafico1.txt'
request= urllib.request.Request("http://infocar.dgt.es/etraffic/Incidencias?caracter=acontecimiento&orden=fechahora_ini%20DESC&IncidenciasOTROS=IncidenciasOTROS&IncidenciasEVENTOS=IncidenciasEVENTOS&IncidenciasRETENCION=IncidenciasRETENCION&IncidenciasPUERTOS=IncidenciasPUERTOS&IncidenciasMETEOROLOGICA=IncidenciasMETEOROLOGICA&IncidenciasRESTRICCIONES=IncidenciasRESTRICCIONES")
result = urllib.request.urlopen(request)
pagina= (result.read().decode('utf8'))
pttrn = '<tr.*?p1TablaIncidencias.*?(\d\d:\d\d).*?(\d\d/\d\d/\d\d\d\d).*?(Nivel.*?)/.*?/.*?<b>(.*?)</b>.*?p2TablaIncidencias.*?;">(.*?)</a>.*?<b>(.*?)</b>.*?nombreIncidencia.*?clear:both">(.*?)</tr>'
patron1 = '<.*?>'
patron2= '\s+'
elements = re.findall(pttrn, pagina, re.DOTALL | re.MULTILINE)
elementos = [
            [line[0], line[1], line[2], line[3], line[4], line[5], re.sub(patron1, ' ', line[6])]
            for line in elements
    ]
elementos1 = [
            [line[0], line[1], line[2], line[3], line[4], line[5], re.sub(patron2, ' ', line[6])]
            for line in elementos
    ]
for element in elementos1:
    if(element[5] == "M-40"):
        pprint(element)