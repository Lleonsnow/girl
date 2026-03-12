from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_siteimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteimage',
            name='category',
            field=models.CharField(choices=[('hero', 'Главное фото (герой)'), ('miniature', 'Миниатюра CTA'), ('carousel', 'Карусель на главной'), ('photo', 'Страница «Фото»')], db_index=True, max_length=20),
        ),
    ]
