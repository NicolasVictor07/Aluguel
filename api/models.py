from django.db import models

class Usuario(models.Model):
    
    TIPO_CHOICES = [
        ('LOCADOR', 'locator'), 
        ('LOCATARIO', 'locatario')
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(choices=TIPO_CHOICES)

    def __str__(self):
        return self.nome
    
class Imovel(models.Model):
    STATUS_CHOICES = [
        ('DISPONIVEL', 'disponivel'),
        ('ALUGADO', 'alugado')
    ]

    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    
    def __str__(self):
        return self.titulo
    
class Contrato(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='contratos')
    locador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='locador')
    locatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='locatario')

    def __str__(self):
        return f"Contrato {self.id}"

class Pagamento(models.Model):
    data_pagamento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField()
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='pagamentos')

    def __str__(self):
        return f"Pagamento {self.id} - Contrato {self.contrato.id}"
    