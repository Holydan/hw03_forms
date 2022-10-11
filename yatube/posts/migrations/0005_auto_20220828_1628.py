from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20220828_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='name',
            new_name='title',
        ),
    ]
