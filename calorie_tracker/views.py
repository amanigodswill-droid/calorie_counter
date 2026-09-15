from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import FoodItemForm
from .models import FoodItem

def food_list(request):
    today = timezone.localdate()
    food_items = FoodItem.objects.filter(date_added=today).order_by('-id')
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
        today = timezone.localdate()
        FoodItem.objects.filter(date_added=today).delete()

    return redirect('food_list')

def edit_food(request, food_id):
    food_item = FoodItem.objects.get(id=food_id)

    if request.method == 'POST':
        form = FoodItemForm(request.POST, instance=food_item)

        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodItemForm(instance=food_item)

    return render(
        request,
        'calorie_tracker/edit_food.html',
        {'form': form}
    )
