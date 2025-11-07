# main/forms.py
from django import forms
# UPDATED: Added PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
# UPDATED: Added UserProfile
from .models import CollectionRequest, IllegalDumpingReport, Review, WasteType, UserProfile

# Define the Tailwind classes
text_input_class = "w-full bg-eco-medium-green border-eco-medium-green text-white rounded-lg p-3 focus:ring-2 focus:ring-eco-light-yellow focus:border-eco-light-yellow transition"
password_input_class = text_input_class
textarea_class = text_input_class
select_class = text_input_class

# --- (Your CustomRegistrationForm and CustomLoginForm are here) ---
class CustomRegistrationForm(UserCreationForm):
    # We add the widgets here
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class': text_input_class,
            'placeholder': 'Your Username'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': password_input_class,
            'placeholder': 'Your Password'
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': password_input_class,
            'placeholder': 'Confirm Your Password'
        })
    )

    class Meta(UserCreationForm.Meta):
        model = UserCreationForm.Meta.model
        fields = ("username",) # The fields are handled above

class CustomLoginForm(AuthenticationForm):
    # This form is already styled from our previous step
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class': text_input_class,
            'placeholder': 'Your Username'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': password_input_class,
            'placeholder': 'Your Password'
        })
    )


# --- ADD THESE NEW FORMS ---

class CollectionRequestForm(forms.ModelForm):
    # This field will automatically query the WasteType model
    waste_type = forms.ModelChoiceField(
        queryset=WasteType.objects.all(),
        empty_label="Select waste type",
        widget=forms.Select(attrs={'class': select_class})
    )
    
    preferred_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': text_input_class, 'type': 'date'}
        )
    )
    
    preferred_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={'class': text_input_class, 'type': 'time'}
        )
    )
    
    address = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': textarea_class, 'rows': 3, 'placeholder': 'Enter your full address'}
        )
    )
    
    class Meta:
        model = CollectionRequest
        fields = ['waste_type', 'preferred_date', 'preferred_time', 'address']


class IllegalDumpingReportForm(forms.ModelForm):
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': text_input_class, 'placeholder': 'e.g., Near Marine Drive'}
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': textarea_class, 'rows': 3, 'placeholder': 'Provide any additional details...'}
        )
    )
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={'class': 'w-full text-sm text-gray-400 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-eco-medium-green file:text-eco-light-yellow hover:file:bg-eco-olive'}
        )
    )

    class Meta:
        model = IllegalDumpingReport
        fields = ['location', 'description', 'image']


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=Review.RATING_CHOICES,
        widget=forms.Select(attrs={'class': select_class})
    )
    feedback = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': textarea_class, 'rows': 4, 'placeholder': 'Tell us about your experience...'}
        )
    )
    
    class Meta:
        model = Review
        fields = ['rating', 'feedback']

class UserProfileForm(forms.ModelForm):
    full_name = forms.CharField(
        label="Full Name",
        widget=forms.TextInput(attrs={
            'class': 'w-full bg-eco-medium-green border-eco-medium-green text-white rounded-lg p-3 focus:ring-2 focus:ring-eco-light-yellow focus:border-eco-light-yellow transition',
            'placeholder': 'Your Full Name'
        })
    )
    address = forms.CharField(
        label="Address",
        widget=forms.Textarea(attrs={
            'class': 'w-full bg-eco-medium-green border-eco-medium-green text-white rounded-lg p-3 focus:ring-2 focus:ring-eco-light-yellow focus:border-eco-light-yellow transition',
            'rows': 4,
            'placeholder': 'Your Address'
        })
    )
    
    class Meta:
        model = UserProfile
        fields = ['full_name', 'address']


class CustomPasswordChangeForm(PasswordChangeForm):
    # Apply styling to the default password change form
    
    old_password = forms.CharField(
        label="Old Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full bg-eco-medium-green border-eco-medium-green text-white rounded-lg p-3 focus:ring-2 focus:ring-eco-light-yellow focus:border-eco-light-yellow transition',
            'placeholder': 'Your Old Password'
        })
    )
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full bg-eco-medium-green border-eco-medium-green text-white rounded-lg p-3 focus:ring-2 focus:ring-eco-light-yellow focus:border-eco-light-yellow transition',
            'placeholder': 'Your New Password'
        })
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full bg-eco-medium-green border-eco-medium-green text-white rounded-lg p-3 focus:ring-2 focus:ring-eco-light-yellow focus:border-eco-light-yellow transition',
            'placeholder': 'Confirm Your New Password'
        })
    )