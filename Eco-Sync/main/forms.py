# main/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# --- IMPORT YOUR MODELS ---
from .models import CollectionRequest, IllegalDumpingReport, Review, WasteType

# Define the Tailwind classes
text_input_class = "w-full bg-eco-medium-green border-eco-medium-green text-white rounded-lg p-3 focus:ring-2 focus:ring-eco-light-yellow focus:border-eco-light-yellow transition"
password_input_class = text_input_class
textarea_class = text_input_class
select_class = text_input_class

# --- (Your CustomRegistrationForm and CustomLoginForm are here) ---
# ... (keep them exactly as they are) ...
class CustomRegistrationForm(UserCreationForm):
    # ... (your existing code) ...
    pass

class CustomLoginForm(AuthenticationForm):
    # ... (your existing code) ...
    pass


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