from django.db import models


class Language(models.Model):
    title = models.CharField(max_length=100, verbose_name='زبان')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'زبان'
        verbose_name_plural = 'معرفی زبان'


class Meaning(models.Model):
    meaning = models.CharField(max_length=100, verbose_name='معنی')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='meaning', verbose_name='زبان')

    def __str__(self):
        return self.meaning

    class Meta:
        verbose_name = 'معنی'
        verbose_name_plural = 'معانی'


class Word(models.Model):
    title = models.CharField(max_length=100, verbose_name='لغت')
    meaning = models.ManyToManyField(Meaning, related_name='wordrn', blank=True, verbose_name='معنی')
    language = models.ForeignKey(Language, related_name='words', on_delete=models.CASCADE, blank=True, verbose_name='زبان')


def __str__(self):
    return self.title


class Meta:
    verbose_name = 'لغت'
    verbose_name_plural = 'لغات'

# class WordMeaning(models.Model):
#     word = models.ForeignKey(Word, on_delete=models.CASCADE)
#     meaning = models.ForeignKey(Meaning, on_delete=models.CASCADE)
