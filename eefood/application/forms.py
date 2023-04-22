from django import forms
from django.forms import ModelForm
from .models import Restaurants, Reservation, Review, MenuItem
from django.core.validators import MaxLengthValidator

class PostRestaurantForm(ModelForm):
    class Meta:
        model = Restaurants
        fields = "__all__"

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time', 'num_people']
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'}),
        }

class RestaurantSearchForm(forms.Form):
    name = forms.CharField(required=False)
    genre = forms.CharField(required=False)

    class Meta:
        model = Restaurants
        fields = ('name', 'genre')

class ReviewForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), validators=[MaxLengthValidator(300)])
    image = forms.ImageField(required=False)

    class Meta:
        model = Review
        fields = ['title', 'comment', 'rate', 'image']

    def save(self, restaurant=None, author=None, commit=True):
        review = super().save(commit=False)
        review.restaurant = restaurant
        review.author = author
        if commit:
            review.save()
        return review
    
class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'image']
        labels = {'name': 'Menu Item Name', 'price': 'Price', 'image': 'Image'}
        widgets = {'image': forms.FileInput(attrs={'class': 'form-control-file'})}
