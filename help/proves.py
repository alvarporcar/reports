#!/usr/bin/env python
 
from suds.client import Client
url = 'https://incidencias.dipcas.es/api/soap/mantisconnect.php?wsdl'
client = Client(url)
print client

incidencia = client.service.mc_issue_get("aporcar","","4757")
print incidencia.description
print incidencia.reporter.name



