from django.shortcuts import render, redirect 
#from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from .forms import TableAndUrlColumnsForm 
from .models import DocFile, TableAndUrlColumns
#from .utils import total_result
from .utils import read_doc, total_result
from django.conf import settings
 
# Воображаемая функция для обработки загруженного файла:
###
 
# Create your views here:
def upload_file(request):
    #context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        #print(uploaded_file.name)
        #print(uploaded_file.size)
        #fs = FileSystemStorage()
        #name = fs.save(uploaded_file.name, uploaded_file)
        #context['url'] = fs.url(name)
    #return render(request, 'upload_file.html', context)
        doc = DocFile(docfile = uploaded_file)
        doc.save()
        read_doc(doc.docfile.path)
        return redirect(to='table')
    else:
        return render(request, 'upload_file.html')
    
def table(request):
    row = TableAndUrlColumns.objects.all()
    res1, res2 = total_result()
    context_1 = {
        'row_list': row,
        'result_1': res1,
        'result_2': res2,
    }
    #context_2 = read_doc.A_dict
    #return render(request, 'table.html', context_1, context_2)
    return render(request, 'table.html', context_1)
    
def test_page(request):
    #context_2 = read_doc(settings.MEDIA_ROOT / 'contractors_and_suppliers.xlsx')
    context_2 = read_doc(settings.MEDIA_ROOT / DocFile.objects.all()[0].docfile.name)
    return render(request, 'test_page.html', {
        'A_dict': context_2
    })
    
def redirect_result(request):
    return redirect('table.html')