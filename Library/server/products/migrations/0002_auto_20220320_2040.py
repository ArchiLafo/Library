

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='specifications',
            field=models.TextField(blank=True, verbose_name='Характеристики продукта'),
        ),
    ]
