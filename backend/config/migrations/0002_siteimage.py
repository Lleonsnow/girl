from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_cookie_consent'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(db_index=True, max_length=20)),
                ('image', models.ImageField(upload_to='site/%Y/%m/')),
                ('order', models.PositiveIntegerField(db_index=True, default=0)),
            ],
            options={
                'db_table': 'config_siteimage',
                'ordering': ['category', 'order', 'pk'],
            },
        ),
    ]
