from django.forms import ModelForm
from .models import Todo
#So user can creATE FORM/MODELS
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']
        
