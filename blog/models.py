from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User


class Post(models.Model):
    STATUS = (
            ('rascunho', 'Rascunho'),
            ('publicado', 'Publicado'),
        ) # Tupla estruturada com keys e values servindo para delimitar as escolhas do usuario

    title = models.CharField(max_length = 250)
    slug  = models.SlugField(max_length = 250)
    auth  = models.ForeignKey(User, 
                                on_delete = models.CASCADE) # Cascade define o que fazer quando o autor for excluido dos registros
    content = models.TextField()

    published = models.DateTimeField(default=timezone.now)
    created    = models.DateTimeField(auto_now_add=True) # Assim que criado, irá pegar data e hora atual
    altered  = models.DateTimeField(auto_now=True) # Assim que alterado, irá pegar data e hora
    status    = models.CharField(max_length=10,
                                    choices=STATUS,
                                    default='rascunho') # CharField com possibilidade de escolhas que são definidas em tuplas

    class Meta: # classe para algumas configuracoes de Post
        ordering = ('-published',) #"-" indica do mais antigo para o mais atual

    def __str__(self):
        return '{} - {}'.format(self.title, self.status)