from django.db import models

# Create your models here.

STATUS_CHOICES = [('active', 'Active'), ('blocked', 'Blocked')]


class Guest(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Name')
    email = models.EmailField(max_length=100, null=False, blank=False, verbose_name='Email')
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")
    status = models.CharField(max_length=15, default='active', choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.pk}. {self.name}: {self.email}"

    class Meta:
        db_table = 'Guests'
        verbose_name = 'guest'
        verbose_name_plural = 'guests'