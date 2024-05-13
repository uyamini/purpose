from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'location_state', 'location_city', 'location_address',
            'details', 'date_time_spotted', 'list_of_needs', 'status'
        ]
