# Generated by Django 3.1.2 on 2020-10-19 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0012_auto_20201019_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='static/default-profile.png', upload_to='static/images/')),
            ],
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pet_image', to='pets.petimage'),
        ),
    ]
