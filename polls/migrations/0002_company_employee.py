# Generated by Django 2.2.4 on 2019-08-30 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Company')),
            ],
        ),
    ]
