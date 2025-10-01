import datetime

from django.shortcuts import render

from dict.models import Word, Language, Meaning


def index(request):
    languages = Language.objects.all()
    words = Word.objects.all()
    context = {
        'languages': languages,
        'words': words,
    }
    return render(request, 'index.html', context)


def meaning(request):
    word1 = request.POST.get('word')
    word = Word.objects.filter(title=word1).first()
    std = '<p>ممد</p>'
    num2 = 20

    date1 = datetime.date.today()
    print(date1.year)
    context = {
        'word': word,
        'original_word': word1,
        'std': std,
        'num2': num2,
    }
    return render(request, 'words.html', context)

def reverse_meaning(request):
    meaning1 = request.POST.get('meaning')
    m = Meaning.objects.filter(meaning=meaning1).first()
    word = m.wordrn.all()

    context = {
        'word2': word,

    }
    return render(request, 'base_template.html', context)

def words_by_language(request,pk):
    language = Language.objects.get(id=pk)
    words = Word.objects.filter(language=language)
    context = {
        'words': words,
    }
    return render(request, 'words.html', context)
