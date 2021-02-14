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
    #res1, res2 = total_result()
    zipped_result = read_doc(settings.MEDIA_ROOT / DocFile.objects.all()[0].docfile.name)
    sum1 = total_result(settings.MEDIA_ROOT / DocFile.objects.all()[0].docfile.name)[0]
    sum2 = total_result(settings.MEDIA_ROOT / DocFile.objects.all()[0].docfile.name)[1]
    context = {
        #'row_list': row,
        #'result_1': res1,
        #'result_2': res2,
        'zipped_result': zipped_result,
        'sum1': sum1,
        'sum2': sum2
    }
    return render(request, 'table.html', context)
    
def test_page(request):
    context = read_doc(settings.MEDIA_ROOT / DocFile.objects.all()[0].docfile.name)
    return render(request, 'test_page.html', {
        'A_dict': context[8]
    })
    
def redirect_result(request):
    return redirect('table.html')