from django.forms import ModelForm
from app.models import Pessoa

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['Nome', 'email', 'telefone']