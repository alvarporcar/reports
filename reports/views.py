# -*- coding: utf-8 -*-

from reportlab.pdfgen import canvas
from django.http import HttpResponse
import csv
from forms import FormLlistatAnual
from django.shortcuts import render
from suds.client import Client

# Create your views here.

# Es declara un diccionari per a allotjar les variables del fitxer de configuració
diccionari_vars = {}
with open('config.ini') as fitxer:
	for linia in fitxer:
		if (linia[0] <> '#') and (linia[0]<>'\n'):
			variable = linia.split(' ')
			diccionari_vars[variable[0]] = variable[1].rstrip('\n')
		

client = Client(diccionari_vars['url'])

def proves1(request):
	incidencies_informatica = client.service.mc_project_get_issues(diccionari_vars['usuari'],diccionari_vars['password'],13,0,0)
	return render(request,'resposta.html',{'incidencies_informatica':incidencies_informatica,}) 

def incidencies2015(request):
	form = FormLlistatAnual()
	if request.method == 'POST':
		form = FormLlistatAnual(request.POST)
        if form.is_valid():
            any = request.POST.get('any')
            projecte = request.POST.get('projecte')

			try:
    			result = {'1': "Result 1", '2': "Result 2", 'N': "Result N"}[var]
			except KeyError
    			result = "Default result"

            incidencies_2015 = client.service.mc_filter_get_issues(diccionari_vars['usuari'],diccionari_vars['password'],13,diccionari_vars['llistat_2015'],1,1000) 
            return render(request,'incidencies_2015.html',{'incidencies':incidencies_2015}) 
	return render(request, 'form_llistat_anual.html', {'form': form}) 


def incidencies2015_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="exemple.csv"'
    writer = csv.writer(response)

    writer.writerow(['Identificador', 'Informador', 'Data', 'Categoria','Descripcio'])
    # Comprova que les pàgines de incidències estan amb contingut fins que ja no en queden
    pagina = 1
    while client.service.mc_filter_get_issues(diccionari_vars['usuari'],diccionari_vars['password'], 13, diccionari_vars['llistat_2015'], pagina, 20):
    	incidencies_2015 = client.service.mc_filter_get_issues(diccionari_vars['usuari'],diccionari_vars['password'], 13, diccionari_vars['llistat_2015'], pagina, 20)
    	for incidencia in incidencies_2015:
    		#data = incidencia.last_updated
    		#print str(data.day)+"/"+str(data.month)+"/"+str(data.year)
    		writer.writerow([incidencia.id, incidencia.reporter.name, incidencia.last_updated, incidencia.category, incidencia.summary])
    
    	pagina = pagina + 1
    
    return response

def categories(request):
	categories = client.service.mc_project_get_categories(diccionari_vars['usuari'],diccionari_vars['password'], 13)
	return render(request,'categories.html',{'categories':categories,}) 

def genera_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="exemple.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(1, 800, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

