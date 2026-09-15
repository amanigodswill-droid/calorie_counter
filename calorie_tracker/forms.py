from django import forms
from .models import FoodItem

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'calories']
        widgets = {'name': forms.TextInput(attrs={
                    'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-green-500',
                    'placeholder': 'Enter food name',
                    }),
                  'calories':forms.NumberInput(attrs={
                    'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-green-500',
                    'placeholder': 'Enter calories',
                    'min': '1',
                   }),
                }

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