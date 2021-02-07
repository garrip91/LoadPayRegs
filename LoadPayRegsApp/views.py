from django.shortcuts import render, redirect 
#from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from .forms import TableAndUrlColumnsForm 
from .models import TableAndUrlColumns
 
# Воображаемая функция для обработки загруженного файла:
###
 
# Create your views here:
def upload_file(request):
    # if request.method == 'POST':
        # form = UploadFileForm(request.POST, request.FILES)
        # if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            # return HttpResponseRedirect('/success/url/')
    # else:
        # form = UploadFileForm()
    # return render(request, 'upload_file.html', {'form': form})
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        #print(url)
    return render(request, 'upload_file.html', context)
    
def table(request):
    row = TableAndUrlColumns.objects.all()
    context = {'row_list': row}
    return render(request, 'table.html', context)
    
def redirect_result(request):
    return redirect('table.html')