from django.shortcuts import render, redirect 
#from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from .forms import TableAndUrlColumnsForm 
from .models import DocFile, TableAndUrlColumns
#from .utils import total_result
from .utils import read_doc, total_result
from django.conf import settings
 
# Функция для обработки загруженного файла:
 # Create your views here:
def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
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
    return render(request, 'table.html', context_1)
    
def test_page(request):
    context_2 = read_doc(settings.MEDIA_ROOT / DocFile.objects.all()[0].docfile.name)
    return render(request, 'test_page.html', {
        'A_dict': context_2
    })
    
def redirect_result(request):
    return redirect('table.html')