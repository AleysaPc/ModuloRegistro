from django.db import models

class Destinatario(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del destinatario
    cargo = models.CharField(max_length=50)    # Cargo del dest inatario
    departamento = models.CharField(max_length=100)  # Departamento al que pertenece

    def __str__(self):
        return f"{self.nombre} ({self.cargo}) - {self.departamento}"

class Registro(models.Model):
    codigo = models.CharField(primary_key=True, max_length=5)
    fecha = models.DateField()
    hora = models.TimeField()
    referencia = models.CharField(max_length=255)
    institucion = models.CharField(max_length=100)
    remitente = models.CharField(max_length=30)
    cargoRemitente = models.CharField(max_length=30)
    observacion = models.CharField(max_length=255)
    fojas = models.IntegerField()
    estado = models.CharField(max_length=20)
    
    # Relación de muchos a muchos con el modelo Destinatario
    destinatarios = models.ManyToManyField('Destinatario', related_name='documentos_recibidos')

    def __str__(self):
        return f"{self.codigo} - {self.referencia}"

