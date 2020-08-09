# Generated by Django 3.0 on 2020-08-09 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('price', models.BigIntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('b_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Brand')),
            ],
        ),
    ]
