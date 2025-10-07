from django.forms import ModelForm
from main.models import Product, Car
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured"]
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_content(self):
        content = self.cleaned_data["content"]
        return strip_tags(content)
        
class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["name", "brand", "stock"]