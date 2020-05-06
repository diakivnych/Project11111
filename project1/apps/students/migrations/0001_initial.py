# Generated by Django 3.0.6 on 2020-05-06 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('job', models.CharField(max_length=20, verbose_name='Робота')),
                ('hobby', models.TextField(verbose_name='Хобби')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=20, verbose_name='Имя автора')),
                ('comment_text', models.CharField(max_length=200, verbose_name='Текст комментария')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации комментария')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Person')),
            ],
        ),
    ]