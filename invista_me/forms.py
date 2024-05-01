from django.forms import ModelForm
from .models import Investimentos

# Cria um formulário que pega como parâmetro a tabela de investimentos e o fields pega todos os campos
class InvestimentosForm(ModelForm):
    class Meta:
        model = Investimentos
        fields = '__all__'