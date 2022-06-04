from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
import requests
from main.models import Word
from .models import Lesson, Yword

def index(request):
    lessons = Lesson.objects.all
    return render(request, 'user/lessons.html', {'lessons': lessons})
    pass

def create(request):
    if request.method == "POST":
        try:
            Lesson.objects.get(name = request.POST.get("name"))
            return render(request, 'user/addlesson.html', {'exist': 1})
        except:
            lesson = Lesson.objects.create(name=request.POST.get("name"))
            return HttpResponseRedirect(f"/user/lesson/{lesson.id}/edit")

    return render(request, 'user/addlesson.html', {'exist': 0})
    pass

def editlesson(request, pk):
    words = Word.objects.all()
    yword = Lesson.objects.get(id=pk).yword.all()
    lesson = Lesson.objects.get(id = pk)
    return render(request, 'user/editlesson.html', {'lesson': lesson, 'words': words, 'yword':yword})
    pass

def addword(request, pk, id):
    word = Word.objects.get(id=id)
    lesson = Lesson.objects.get(id=pk)
    try:
        Lesson.objects.get(id=pk).yword.get(eng=word.eng)
        return HttpResponseRedirect(f"/user/lesson/{pk}/edit")
        pass
    except:
        try:
            yword = Yword.objects.get(eng=word.eng)
            yword.lesson_set.add(lesson)
            return HttpResponseRedirect(f"/user/lesson/{pk}/edit")
            pass
        except:
            lesson.yword.create(eng=word.eng, ru=word.ru)
            return HttpResponseRedirect(f"/user/lesson/{pk}/edit")
        
