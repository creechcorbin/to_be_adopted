# Generated by Django 3.1.2 on 2020-10-19 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0013_auto_20201019_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_image',
            field=models.ImageField(default='static/default-profile.png', upload_to='static/images/'),
        ),
        migrations.DeleteModel(
            name='PetImage',
        ),
    ]
