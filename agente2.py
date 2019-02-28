import re
import urllib.request
from pprint import pprint

p='/Users/jmanuel/Desktop/Ai/trafico/trafico1.txt'
request= urllib.request.Request("http://infocar.dgt.es/etraffic/Incidencias?caracter=acontecimiento&orden=fechahora_ini%20DESC&IncidenciasOTROS=IncidenciasOTROS&IncidenciasEVENTOS=IncidenciasEVENTOS&IncidenciasRETENCION=IncidenciasRETENCION&IncidenciasPUERTOS=IncidenciasPUERTOS&IncidenciasMETEOROLOGICA=IncidenciasMETEOROLOGICA&IncidenciasRESTRICCIONES=IncidenciasRESTRICCIONES")
result = urllib.request.urlopen(request)
pagina= (result.read().decode('utf8'))
#pttrn = '<tr.*?p1TablaIncidencias.*?(\d\d:\d\d)*?ACCIDENTE.*?</tr>'
#pttrn = '<tr.*?p1TablaIncidencias.*?(\d\d:\d\d)</span.*?(\d\d/\d\d/\d\d\d\d).*?.*?<b>(.*?)</b>.*?nombreIncidencia.*?ACCIDENTE.*?'
#pttrn = '<tr.*?p1TablaIncidencias.*?(\d\d:\d\d).*?(\d\d/\d\d/\d\d\d\d).*?(Nivel.*?)/.*?/.*?<b>(.*?)</b>.*?p2TablaIncidencias.*?;">(.*?)</a>.*?nombreIncidencia.*?</tr>'
pttrn = '<tr.*?p1TablaIncidencias.*?(\d\d:\d\d)</span.*?(\d\d/\d\d/\d\d\d\d).*?alt=(.*?)/(.*?)/(.*?)/.*?nombreIncidencia.*?span style="margin-top:10px; float:left; clear:both">(.*?)</tr>'

elements = re.findall(pttrn, pagina, re.DOTALL | re.MULTILINE)
pprint(elements)
pprint(pagina)