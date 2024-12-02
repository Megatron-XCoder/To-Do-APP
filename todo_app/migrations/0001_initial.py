# Generated by Django 5.1.3 on 2024-12-02 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('WORKING', 'Working'), ('PENDING REVIEW', 'Pending Review'), ('COMPLETED', 'Completed'), ('OVERDUE', 'Overdue'), ('CANCELLED', 'Cancelled')], default='OPEN', max_length=15)),
                ('tags', models.ManyToManyField(blank=True, to='todo_app.tag')),
            ],
        ),
    ]
