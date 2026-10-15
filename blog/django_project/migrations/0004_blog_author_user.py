import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def clear_author_names(apps, schema_editor):
    schema_editor.execute("UPDATE django_project_blog SET author = NULL")


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("django_project", "0003_alter_blog_author_alter_blog_headline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="author",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.RunPython(clear_author_names, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="blog",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
