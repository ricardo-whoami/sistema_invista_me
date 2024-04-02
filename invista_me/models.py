from django.db import models
from datetime import datetime
'''
Documentação sobre models: https://docs.djangoproject.com/en/4.2/topics/db/models/
Aqui criamos nossas colunas do banco de dados
- Investimento
- Valor
- Pago
- Data
'''

class Investimento(models.Model):
    # Criando as colunas no DB
    investimento = models.TextField(max_length=255)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)

