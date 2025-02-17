

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20220324_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='products.ProductCategory', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Краткое описание продукта'),
        ),
    ]
