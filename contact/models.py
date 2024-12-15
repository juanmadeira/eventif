from django.db import models

class Contact(models.Model):
    name = models.CharField('nome', max_length=100)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20, null=True, blank=True)
    message = models.CharField('mensagem', max_length=200)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    response = models.TextField('resposta', max_length=200, blank=True, default="")
    reply_created_at = models.DateTimeField('respondida em', blank=True, null=True)

    class Meta:
        verbose_name = 'mensagem'
        verbose_name_plural = 'mensagens'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name