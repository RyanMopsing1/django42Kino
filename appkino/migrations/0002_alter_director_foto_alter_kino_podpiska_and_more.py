# Generated by Django 5.1.5 on 2025-02-10 18:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appkino', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='director/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='kino',
            name='podpiska',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appkino.podpiska', verbose_name='Подписка'),
        ),
        migrations.AlterField(
            model_name='podpiska',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Подписка'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(default=1000)),
                ('podpiska', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='appkino.podpiska')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
