from tkinter import Widget
from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}))
    audience = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Audience'}))
    score = forms.FloatField(required=False, max_value=5, min_value=0,
        widget=forms.NumberInput(attrs={'id':'form_homework', 'step':"0.5", 'placeholder':'Score', 'class':'field-row','style':"width: 50px;"}))
    poster_url = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Poster url', 'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descrition'}))
    release_date = forms.DateField(
    #     widget=forms.DateInput(
    #         attrs = {
    #             'class':'form-control', 
    #             'placeholder':'Select a date', 
    #             'type':'date',
    #             'style':"width: 200px;",
    #         }
    #     )
    )   
    
    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ('user',)
        

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('movie', 'user',)
