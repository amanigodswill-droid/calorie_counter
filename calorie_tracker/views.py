from django.shortcuts import redirect, render

from .forms import FoodItemForm
from .models import FoodItem

def food_list(request):
    food_items = FoodItem.objects.order_by('-date_added', '-id')
    total_calories = sum(
        food_item.calories for food_item in food_items
    )

    context = {
        'food_items': food_items,
        'total_calories': total_calories,
    }

    return render(request, 'calorie_tracker/food_list.html', context)


def add_food(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodItemForm()
    return render(
        request,
        'calorie_tracker/add_food.html',
        {'form': form}
    )

def delete_food(request, food_id):
    if request.method == 'POST':
        food_item = FoodItem.objects.get(id=food_id)
        food_item.delete()
    return redirect('food_list')

def reset_calories(request):
    if request.method == 'POST':
        FoodItem.objects.all().delete()

    return redirect('food_list')
