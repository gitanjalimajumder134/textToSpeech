from django.shortcuts import render
from gtts.tts import gTTS
import PyPDF4
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
import io
# 
# Create your views here
def TextRoSpeech(self, request):
    language = 'en'
    music = ''
    if request.method == 'POST':
        text = request.POST.get('text')
        lang = request.POST.get('lang')
        pdf = request.FILES['pdf'].read()
        if pdf:
            pdfreader = PyPDF4.PdfFileReader(io.BytesIO(pdf))
            content = ''
            for i in range(int(pdfreader.numPages)):
                content += pdfreader.getPage(i).extractText() + "\n"
            text = content
            myobj = gTTS(text=text, lang=lang, slow= False)
            myobj.save("static/speech.mp3")
            music = 'ok'
            context = {
                'music': music
            }
            return render(self.request, context)
        myobj = gTTS(text=text, lang=lang, slow= False)
        myobj.save("static/speech.mp3")
        music = 'ok'
        context = {
            'music': music
        }
        return render(self.request, context)
    else:
        pass
    context = {
        'music': music
    }
    return render(self.request, context)