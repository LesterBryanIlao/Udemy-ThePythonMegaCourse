from django.shortcuts import render
from googletrans import Translator
# Create your views here.


def translator_view(request):

    if request.method == 'POST':
        original_text = request.POST['my_textarea'].strip()
        return render(request, 'translator.html', {'original_text': original_text, 'output_text': translate(original_text)})
    else:
        return render(request, 'translator.html')


def translate(text, translate_to='ko'):
    translator = Translator()
    return translator.translate(text=text, dest=translate_to).text
