# Generated by Django 5.0.6 on 2024-08-09 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_post_author_alter_post_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('SP', 'Спорт'), ('PLT', 'Политика'), ('EDU', 'Образование'), ('ECO', 'Экономика')], max_length=10, unique=True),
        ),
    ]
