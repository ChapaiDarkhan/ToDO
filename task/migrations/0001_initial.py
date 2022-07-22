# Generated by Django 3.1.5 on 2022-07-22 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('execution_period', models.DateTimeField()),
                ('is_executed', models.BooleanField(default=False)),
            ],
        ),
    ]
