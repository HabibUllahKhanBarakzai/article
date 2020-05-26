# Generated by Django 3.0.6 on 2020-05-25 22:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='heading',
        ),
        migrations.RemoveField(
            model_name='article',
            name='text',
        ),
        migrations.AddField(
            model_name='article',
            name='availability_status',
            field=models.CharField(choices=[('open', 'article is open, and can be changed'), ('closed', 'article is closed, cannot be changed')], default='open', max_length=256),
        ),
        migrations.AlterUniqueTogether(
            name='articleevent',
            unique_together={('user', 'article')},
        ),
        migrations.RemoveField(
            model_name='articleevent',
            name='parameters',
        ),
    ]
