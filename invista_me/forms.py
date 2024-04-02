from django.forms import ModelForm
from .models import Investimento

class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimento
        # Será exibido tudo. Caso fosse apenas alguns dados poderia ser uma lista ['data','pago']
        fields = '__all__' 
        