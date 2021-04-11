from django.db import models

from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

from ckeditor.fields import RichTextField

from django.utils.html import mark_safe

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset() \
                                                .filter(status='publicado')

class Category(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateTimeField(default=timezone.now)
    created    = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering=['-created']

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS = (
            ('rascunho', 'Rascunho'),
            ('publicado', 'Publicado'),
        ) # Tupla estruturada com keys e values servindo para delimitar as escolhas do usuario

    title = models.CharField(verbose_name='Título', max_length = 250)
    slug  = models.SlugField(max_length = 250)
    author  = models.ForeignKey(User, 
                                on_delete = models.CASCADE) # Cascade define o que fazer quando o autor for excluido dos registros
    content = RichTextField(verbose_name='Conteúdo')
    category = models.ManyToManyField(Category,
                                            related_name='get_posts')
    image = models.ImageField(upload_to="blog", blank=True, null=True)
    published = models.DateTimeField(default=timezone.now)
    created    = models.DateTimeField(auto_now_add=True) # Assim que criado, irá pegar data e hora atual
    altered  = models.DateTimeField(auto_now=True) # Assim que alterado, irá pegar data e hora
    status    = models.CharField(max_length=10,
                                    choices=STATUS,
                                    default='rascunho') # CharField com possibilidade de escolhas que são definidas em tuplas

    objects   = models.Manager() # fará com que não se limite apenas aos publicados
    published_manager = PublishedManager() # exibirá no admin do django somente os publicados

    """
        Criando um manager eu posso personalizar consultas genericas. 
        No exemplo do published quando executarmos objects.published_manager.all() irá fazer a consulta
        somente nos publicados, filtro passando dentro da minha classe PublishedManager.

    """
    def get_absolute_url(self):
        return reverse('post_detail',args=[self.slug])

    def get_absolute_url_update(self):
        return reverse('post_edit',args=[self.slug])

    def get_absolute_url_delete(self):
        return reverse('post_delete',args=[self.pk])

    @property
    def view_image(self):
        return mark_safe('<img src="%s" width="400px" />'%self.image.url)
        view_image.short_description = "Imagem Cadastrada" 
        view_image.allow_tags = True 
        

    class Meta: # classe para algumas configuracoes de Post
        ordering = ('-published',) #"-" indica do mais antigo para o mais atual

    def __str__(self):
        return '{} - {}'.format(self.title, self.status)


@receiver(post_save, sender=Post)
def insert_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        return instance.save()
    
