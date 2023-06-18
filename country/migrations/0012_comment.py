# Generated by Django 4.2.1 on 2023-06-15 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('country', '0011_alter_photosdiscriptions_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('moderation', models.BooleanField(default=False)),
                ('post_cities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.cities')),
                ('post_events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.events_ditails')),
                ('post_photos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.photosdiscriptions')),
                ('post_routers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.routedetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]