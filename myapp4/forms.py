import datetime
# -*- coding: utf-8 -*-
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField( max_value=100)

    def clean_name(self):
        '''Плохой пример. Подмена параметра min_length'''
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError('Имя должно седоржать не менее 3 символов')
        return name

    def clean_email(self):
        email: str = self.cleaned_data['email']
        if not (email.endswith('@gmail.com') or email.endswith('vk.team')):
            raise forms.ValidationError('Ипользуйте корпоративную почту')
        return email

    def clean_age(self):
        age: int = self.cleaned_data['age']
        if not (age >= 18):
            raise forms.ValidationError("Влзрастное ограничение с 18-и лет")
        return age




class ManyFieldsForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18)
    height = forms.FloatField()
    is_active = forms.BooleanField(required=False)
    birthday = forms.DateField(initial=datetime.date.today)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])


class ManyFieldsForm2(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Введите имя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'user@mail.ru'}))
    age = forms.IntegerField(min_value=18, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    birthdate = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control',
                                                                                           'type': 'date'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')],
                               widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class ImageForm(forms.Form):
    image = forms.ImageField()

