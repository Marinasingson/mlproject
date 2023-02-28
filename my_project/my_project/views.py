from django.shortcuts import render
from . forms import DigitForm
from . models import predict_digit

def home(request):
    if request.method == 'POST':
        form = DigitForm(request.POST, request.FILES)
        if form.is_valid():
            image_path = form.cleaned_data['image']
            prediction = predict_digit(image_path)
            return render(request, 'result.html', {'predicted_digit': prediction})
    else:
        form = DigitForm()
        return render(request, 'home.html', {'form': form})
