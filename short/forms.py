from django import forms
from .models import ShortURL

class ShortURLForm(forms.ModelForm):
    custom_key = forms.CharField(required=False, max_length=30)
    expires_at = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = ShortURL
        fields = ['original_url'] 

    def clean_custom_key(self):
        key = self.cleaned_data.get('custom_key')
        if key is None:
            return ""

        key = key.strip()

        if key == "":
            return ""

        if " " in key:
            raise forms.ValidationError("Custom short URL cannot contain spaces.")

        exists = ShortURL.objects.filter(short_key=key).exists()
        if exists:
            raise forms.ValidationError("This custom short URL is already taken.")

        return key
