from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('olmsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='admin',
            field=models.OneToOneField(default=None, to='olmsapp.CustomUser', on_delete=models.CASCADE),
        ),
    ]