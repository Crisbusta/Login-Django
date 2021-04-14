# Generated by Django 3.1.7 on 2021-04-10 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default='No indica', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='No indica', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer'), ('O', 'Otro')], default='N', max_length=1),
        ),
    ]