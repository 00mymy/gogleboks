from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(), label='')

    class Meta:
        model = Review
        fields = ('comment',)
