
from django.contrib import admin
from django.urls import path

from dict.views import index, meaning, reverse_meaning, words_by_language

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('meaning/', meaning, name='meaning'),
    path('words_by_language/<int:pk>', words_by_language, name='words_by_language'),
    path('reverse_meaning/', reverse_meaning, name='reverse_meaning'),
]