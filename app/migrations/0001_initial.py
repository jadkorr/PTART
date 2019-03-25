# Generated by Django 2.1.7 on 2019-03-18 11:15

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('added', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('note', models.TextField(blank=True, default='')),
                ('asset', models.CharField(blank=True, default='', max_length=256)),
                ('done', models.BooleanField(default=False)),
                ('added', models.DateTimeField(default=datetime.datetime.now)),
                ('assessment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Assessment')),
                ('assignee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=7)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Methodology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('methodology', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Methodology')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('scope', models.TextField(blank=True, default='')),
                ('added', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenshot', models.ImageField(upload_to='screenshots')),
            ],
        ),
        migrations.CreateModel(
            name='Sh0t',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField(blank=True, default='')),
                ('asset', models.CharField(blank=True, default='', max_length=256)),
                ('added', models.DateTimeField(default=datetime.datetime.now)),
                ('severity', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('cvss', models.CharField(default='---', max_length=4)),
                ('assessment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Assessment')),
            ],
            options={
                'ordering': ('severity', '-cvss', 'title'),
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('severity', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('body', models.TextField(blank=True, default='')),
                ('asset', models.CharField(blank=True, default='', max_length=256)),
            ],
            options={
                'ordering': ('severity', 'name'),
            },
        ),
        migrations.AddField(
            model_name='screenshot',
            name='sh0t',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Sh0t'),
        ),
        migrations.AddField(
            model_name='case',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Module'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Project'),
        ),
    ]
