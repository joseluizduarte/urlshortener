# Generated by Django 3.2.5 on 2021-08-21 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shorturl', '0003_auto_20210817_0019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('ip', models.GenericIPAddressField()),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shorturl.newurl')),
            ],
        ),
    ]
