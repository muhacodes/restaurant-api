# Generated by Django 4.2.7 on 2023-12-15 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_selectedchoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectedchoice',
            name='order_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='orders.orderitem'),
            preserve_default=False,
        ),
    ]