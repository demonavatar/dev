from django import forms
from .models import CD


class ExchangeForm(forms.Form):
    GENRE_CHOICES = (
                    ("R", "Рок"),
                    ("E", "Электроника"),
                    ("P", "Поп"),
                    ("C", "Классика"),
                    ("O", "Саундтреки"),
    )
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    title = forms.CharField(max_length=100)
    artist = forms.CharField(max_length=40)
    genre = forms.ChoiceField(choices=GENRE_CHOICES)
    price = forms.DecimalField(required=False)
    comment = forms.CharField(widget=forms.Textarea, required=False)

    # Метод-валидатор для поля subject
    def clean_artist(self):
        data = self.cleaned_data['artist']
        artists = CD.objects.filter(artist=data)
        if not artists.exists():
            raise forms.ValidationError('Такого исполнителя нет на сайте!')
        return data

# class ExchangeForm(forms.ModelForm):
#     class Meta:
#         model = CD
#         fields = ('name', 'email', 'title', 'artist', 'genre', 'price', 'comment')

#     # Метод-валидатор для поля subject
#     def clean_artist(self):
#         data = self.cleaned_data['artist']
#         artists = CD.objects.filter(artist=data)
#         if not artists.exists():
#             raise forms.ValidationError('Такого исполнителя нет на сайте!')
#         return data
