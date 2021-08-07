from django import forms
from . import models as reviews_models

class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = reviews_models.Review
        fields = (
            "text",
            "rating",           
        )
        widgets = {
            "text": forms.Textarea(attrs={"placeholder": "text"}),
            "rating": forms.NumberInput(attrs={"placeholder": "rating"}),            
        }   

    def save(self):
        review = super().save(commit=False)
        return review