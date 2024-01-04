from django.shortcuts import render
from gtts.tts import gTTS
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
# 
# Create your views here
def TextRoSpeech(self, request):
    language = 'en'
    if request.method == 'POST':
        text = request.POST.get('text')
        myobj = gTTS(text=text, lang=language, slow= False)
        myobj.save()
        return HttpResponseRedirect(reverse('audio2speech'))
    return render(self.request)