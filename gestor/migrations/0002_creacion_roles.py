from django.db import migrations

def crear_roles_por_defecto(apps, schema_editor):
    Rol = apps.get_model('gestor', 'Rol')
    roles_por_defecto = [
        {'id_rol': 1, 'nom_rol': 'Cliente'},
        {'id_rol': 2, 'nom_rol': 'Técnico'},
    ]
    for rol in roles_por_defecto:
        Rol.objects.get_or_create(id_rol=rol['id_rol'], defaults={'nom_rol': rol['nom_rol']})

class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(crear_roles_por_defecto),
    ]

