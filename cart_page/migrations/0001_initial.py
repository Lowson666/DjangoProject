# Generated by Django 2.0.3 on 2018-03-27 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods_page', '0001_initial'),
        ('user_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods_page.GoodsInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_page.UserInfo')),
            ],
        ),
    ]
