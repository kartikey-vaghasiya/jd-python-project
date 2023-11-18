from django.shortcuts import render, redirect
from .forms import UploadFileForm  
import os

# for old code
# from .utils import generate_charts_and_save_images

# for new code
from .newutils import analyze_and_visualize
def upload_csv(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_instance = form.save()
            print(csv_instance.file.path)

            analyze_and_visualize(csv_instance.file.path)

            return redirect('chart')
    else:

        form = UploadFileForm()

    return render(request, 'upload_file.html', {'form': form})

def chart(request):

    # for new code
    return render(request, 'charts.html')


    # for old code
    # return render(request, 'result.html')
