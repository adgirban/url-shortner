from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import ShortURL
from .forms import ShortURLForm
from .utils import generate_key


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'auth/register.html', {'form': form})


@login_required
def dashboard(request):
    urls = ShortURL.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'short/dashboard.html', {'urls': urls})


@login_required
def create_url(request):
    from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ShortURLForm
from .models import ShortURL
from .utils import generate_key

@login_required
def create_url(request):
    if request.method == 'POST':
        form = ShortURLForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user

            custom_key = form.cleaned_data.get('custom_key')
            expires_at = form.cleaned_data.get('expires_at')

            if custom_key is not None and custom_key.strip() != "":
                obj.short_key = custom_key.strip()
            else:
                key = generate_key(6)
                while ShortURL.objects.filter(short_key=key).exists():
                    key = generate_key(6)
                obj.short_key = key

            obj.expires_at = expires_at
            obj.save()

            return redirect('dashboard')
    else:
        form = ShortURLForm()

    return render(request, 'short/create.html', {'form': form})



@login_required
def delete_url(request, pk):
    obj = get_object_or_404(ShortURL, pk=pk, user=request.user)

    if request.method == 'POST':
        obj.delete()
        return redirect('dashboard')

    return render(request, 'short/delete.html', {'obj': obj})


def go(request, key):
    obj = get_object_or_404(ShortURL, short_key=key)

    if obj.is_expired():
        return render(request, 'short/expired.html', {'obj': obj})

    obj.clicks = obj.clicks + 1
    obj.save()

    return redirect(obj.original_url)
