# Generated by Django 4.1 on 2022-08-11 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general_user', '0002_alter_meetpeople_user1_alter_meetpeople_user2_and_more'),
        ('public_place', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetplace',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='general_user.generaluser'),
        ),
    ]