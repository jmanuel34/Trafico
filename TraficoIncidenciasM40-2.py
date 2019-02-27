import re
import urllib.request
from pprint import pprint

p='/Users/jmanuel/Desktop/Ai/trafico/trafico1.txt'
request= urllib.request.Request("http://infocar.dgt.es/etraffic/Incidencias?caracter=acontecimiento&orden=fechahora_ini%20DESC&IncidenciasOTROS=IncidenciasOTROS&IncidenciasEVENTOS=IncidenciasEVENTOS&IncidenciasRETENCION=IncidenciasRETENCION&IncidenciasPUERTOS=IncidenciasPUERTOS&IncidenciasMETEOROLOGICA=IncidenciasMETEOROLOGICA&IncidenciasRESTRICCIONES=IncidenciasRESTRICCIONES")
result = urllib.request.urlopen(request)
pagina= (result.read().decode('utf8'))
#pttrn = '<tr.*?p1TablaIncidencias.*?(\d\d:\d\d)</span.*?(\d\d/\d\d/\d\d\d\d).*?.*?<b>(.*?)</b>.*?<b>(.*?)</b>.*?<b>(.*?)</b>.*?'
pttrn = '<tr.*?p1TablaIncidencias.*?(\d\d:\d\d)</span.*?(\d\d/\d\d/\d\d\d\d).*?<b>(.*?)</b>.*?(ACCIDENTE).*?'
elements = re.findall(pttrn, pagina, re.DOTALL | re.MULTILINE)
pprint(elements)
for element in elements:
    pprint(element)
