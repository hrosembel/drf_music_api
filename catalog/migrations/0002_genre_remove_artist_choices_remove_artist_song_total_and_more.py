# Generated by Django 5.0.1 on 2024-01-31 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='artist',
            name='choices',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='song_total',
        ),
        migrations.AddField(
            model_name='song',
            name='duration',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=2),
        ),
        migrations.AddField(
            model_name='song',
            name='lyrics',
            field=models.TextField(blank=True, help_text='Lyrics of the song', null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='genres',
            field=models.ManyToManyField(to='catalog.genre'),
        ),
    ]
