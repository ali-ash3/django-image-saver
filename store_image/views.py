from django.shortcuts import render, redirect
from .forms import *

# Create your views here.


def upload_image(request):

    if request.method == 'POST':
        form = ImageModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('upload_image')
            # return Response('upload_image')
    else:
        form = ImageModelForm()
    return render(request, 'image_form.html', {'form': form})
