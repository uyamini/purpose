from django import forms
from .models import Post
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .models import User

class PostForm(forms.ModelForm):
    date_time_spotted = forms.DateTimeField(
        widget=forms.TextInput(attrs={'class': 'datetime-input'})
    )

    class Meta:
        model = Post
        fields = [
            'location_state', 'location_city', 'location_address',
            'details', 'date_time_spotted', 'list_of_needs', 'status'
        ]


# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = UserCreationForm.Meta.fields + ('email',)

# class CustomAuthenticationForm(AuthenticationForm):
#     class Meta(AuthenticationForm.Meta):
#         model = User
#         fields = ['username', 'password']
