from django.forms import ModelForm

from myapp.models import MyModel


class MyModelForm(ModelForm):
    class Meta:
        model = MyModel
        fields = ['color']