from django import forms
from .models import FoodItem

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'calories']

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if not name:
            raise forms.ValidationError("Food name cannot be empty.")
        return name

    def clean_calories(self):
        calories = self.cleaned_data['calories']
        if calories <= 0:
            raise forms.ValidationError("Calories must be greater than zero.")
        return calories