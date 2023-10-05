# Generated by Django 4.2.5 on 2023-10-05 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('REMOVED', 'Removed')], default='ACTIVE', max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('REMOVED', 'Removed')], default='ACTIVE', max_length=10)),
                ('role', models.CharField(choices=[('OWNER', 'Owner'), ('ADMIN', 'Admin'), ('MANAGER', 'Manager'), ('HR', 'HR')], default='OWNER', max_length=10)),
                ('is_default', models.BooleanField(default=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
