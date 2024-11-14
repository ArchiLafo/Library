

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220320_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='description',
            field=models.TextField(blank=True, max_length=500, verbose_name='Описание категории'),
        ),
    ]
