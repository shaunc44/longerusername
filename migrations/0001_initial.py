# from south.db import db
# from south.v2 import SchemaMigration

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

    # Old - South method
    # def forwards(self, orm):
    #     # Changing field 'User.username'
    #     db.alter_column('auth_user', 'username', models.CharField(max_length=MAX_USERNAME_LENGTH()))

    # def backwards(self, orm):
    #     # Changing field 'User.username'
    #     db.alter_column('auth_user', 'username', models.CharField(max_length=35))

    # models = {}
    # complete_apps = ['django_monkeypatches']



