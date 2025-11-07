# main/views.py
from django.shortcuts import render, redirect, get_object_or_404
# UPDATED: Added update_session_auth_hash
from django.contrib.auth import login as auth_login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# --- Import all forms ONCE ---
from .forms import (
    CustomRegistrationForm, 
    CustomLoginForm, 
    CollectionRequestForm, 
    IllegalDumpingReportForm,
    ReviewForm,
    UserProfileForm,              # <-- ADDED THIS
    CustomPasswordChangeForm      # <-- ADDED THIS
)
# --- Import all models needed ---
from .models import (
    CollectionRequest, 
    Review, 
    WasteType, 
    IllegalDumpingReport, 
    UserProfile
)


# --- Original Page Views ---

def home(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# --- Authentication Views ---

def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
            
    form = CustomRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
            
    form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')

# --- UPDATED/NEW VIEWS FOR SERVICE PAGE AND DASHBOARD ---

@login_required # User must be logged in
def service(request):
    # Handle Form Submissions
    if request.method == 'POST':
        # Check which form was submitted
        if 'submit_request' in request.POST:
            request_form = CollectionRequestForm(request.POST)
            if request_form.is_valid():
                new_request = request_form.save(commit=False)
                new_request.user = request.user 
                new_request.save()
                messages.success(request, 'Your collection request has been submitted!')
                return redirect('service')
        
        elif 'submit_report' in request.POST:
            report_form = IllegalDumpingReportForm(request.POST, request.FILES)
            if report_form.is_valid():
                new_report = report_form.save(commit=False)
                new_report.reported_by = request.user
                new_report.save()
                messages.success(request, 'Your report has been submitted. Thank you!')
                return redirect('service')

    # Handle GET request (just show the forms)
    request_form = CollectionRequestForm()
    report_form = IllegalDumpingReportForm()
    
    # Get latest 3 requests for the "Collection Status" box
    # Check if user is authenticated before filtering
    latest_requests = []
    if request.user.is_authenticated:
        latest_requests = CollectionRequest.objects.filter(user=request.user).order_by('-requested_at')[:3]

    context = {
        'request_form': request_form,
        'report_form': report_form,
        'latest_requests': latest_requests
    }
    return render(request, 'service.html', context)


@login_required
def dashboard(request):
    # Get all requests for the currently logged-in user
    user_requests = CollectionRequest.objects.filter(user=request.user).order_by('-requested_at')
    context = {
        'user_requests': user_requests
    }
    return render(request, 'dashboard.html', context)


@login_required
def cancel_request(request, request_id):
    # Get the request object, ensuring it belongs to the logged-in user
    req_to_cancel = get_object_or_404(CollectionRequest, id=request_id, user=request.user)
    
    # Only allow cancellation if it's pending
    if req_to_cancel.status == 'Pending':
        req_to_cancel.status = 'Cancelled'
        req_to_cancel.save()
        messages.info(request, 'Your request has been cancelled.')
    else:
        messages.error(request, 'This request cannot be cancelled.')
        
    return redirect('dashboard')


@login_required
def add_review(request, request_id):
    req_to_review = get_object_or_404(CollectionRequest, id=request_id, user=request.user)
    
    # Check if a review already exists
    if Review.objects.filter(request=req_to_review).exists():
        messages.error(request, 'You have already reviewed this request.')
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.request = req_to_review
            new_review.user = request.user
            new_review.save()
            messages.success(request, 'Thank you for your review!')
            return redirect('dashboard')
    else:
        form = ReviewForm()
        
    context = {
        'form': form,
        'req_to_review': req_to_review
    }
    return render(request, 'add_review.html', context)

@login_required
def profile_edit(request):
    # The form is pre-filled with the user's existing profile data
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=request.user.profile)
        
    return render(request, 'profile_edit.html', {'form': form})


@login_required
def password_change(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            # Important! Updates the user's session so they don't get logged out
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = CustomPasswordChangeForm(user=request.user)
        
    return render(request, 'password_change.html', {'form': form})