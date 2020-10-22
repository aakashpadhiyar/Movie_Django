# Generated by Django 3.1.2 on 2020-10-17 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoviesList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Video', models.URLField()),
                ('Description', models.TextField()),
                ('Image', models.URLField()),
                ('Date', models.DateField(auto_now=True)),
            ],
        ),
    ]
