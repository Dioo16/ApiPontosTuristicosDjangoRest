# Generated by Django 3.2.8 on 2021-10-28 23:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='data',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rating',
            name='note',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]