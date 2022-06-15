# Generated by Django 3.2 on 2022-06-14 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('phone_number', models.CharField(max_length=11, unique=True, verbose_name='phone number')),
                ('email', models.EmailField(blank=True, max_length=120, null=True, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='username')),
                ('fullname', models.CharField(blank=True, max_length=32, null=True, verbose_name='fullname')),
                ('nationality_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='nationality code')),
                ('received_news', models.BooleanField(default=False, verbose_name='received news')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='image')),
                ('city', models.CharField(blank=True, max_length=32, null=True, verbose_name='city')),
                ('is_oversea', models.BooleanField(blank=True, default=False, null=True, verbose_name='is oversea')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('is_admin', models.BooleanField(default=False, verbose_name='is admin')),
                ('score', models.PositiveIntegerField(blank=True, null=True, verbose_name='score')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]