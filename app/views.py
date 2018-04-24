from django.shortcuts import render,redirect,get_object_or_404
from app.models import List
from app.forms import ListForm
# Create your views here.


def index(request):
    list = List.objects.order_by('created_at')
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = ListForm()

    return render(request,'index.html',{'list':list,
                                        'form':form})

def delete(request,pk):
    task=get_object_or_404(List,pk=pk)
    task.delete()
    return redirect('/')
