import uuid
from django.db import migrations, models


def gen_consent_id(apps, schema_editor):
    CookieConsent = apps.get_model('config', 'CookieConsent')
    for row in CookieConsent.objects.all():
        row.consent_id = uuid.uuid4()
        row.save(update_fields=['consent_id'])


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='CookieConsent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consent_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('consent_type', models.CharField(choices=[('full', 'full'), ('essential', 'essential')], max_length=20)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('user_agent', models.CharField(blank=True, max_length=512)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'config_cookieconsent',
                'ordering': ['-created_at'],
            },
        ),
    ]
