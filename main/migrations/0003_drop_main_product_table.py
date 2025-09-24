from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_user'),  # ubah sesuai migration terakhirmu
    ]

    operations = [
        migrations.RunSQL(
            sql="DROP TABLE IF EXISTS main_product CASCADE;",
            reverse_sql=migrations.RunSQL.noop
        ),
    ]
