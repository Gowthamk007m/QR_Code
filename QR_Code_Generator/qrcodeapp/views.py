from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.conf import settings
from qrcode import *
import time

def qr_gen(request):
    if request.method == 'POST':
        data = request.POST['data']
        img = make(data)
        img_name = 'qr' + str(time.time()) + '.png'

        # Use Path.joinpath() to create a valid path
        img_path = settings.MEDIA_ROOT.joinpath(img_name)

        # Save the image to the path
        img.save(img_path)

        return render(request, 'index.html', {'img_name': img_name})
    
    return render(request, 'index.html')