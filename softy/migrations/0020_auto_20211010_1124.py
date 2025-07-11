# Generated by Django 3.1.2 on 2021-10-10 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softy', '0019_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='books/covers/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(upload_to='books/pdfs/'),
        ),
    ]
