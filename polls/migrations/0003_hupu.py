# Generated by Django 3.1.3 on 2020-12-09 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hupu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hupu_title', models.CharField(max_length=100)),
                ('hupu_content', models.TextField()),
            ],
        ),
    ]
