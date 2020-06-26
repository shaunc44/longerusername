from django.db import migrations, models
from longerusername import MAX_USERNAME_LENGTH

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.AlterField(
            model_name='auth_user',
            name='username',
            field=models.CharField(max_length=MAX_USERNAME_LENGTH()),
        )
    ]