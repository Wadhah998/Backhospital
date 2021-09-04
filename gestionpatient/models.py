from django.db.models import BooleanField, CASCADE, DateField, DateTimeField, ForeignKey, Model, OneToOneField, \
    TextField
import django.utils.timezone as timezone
from common.models import create_model_serializer

app_label = 'gestionpatient'
doctor_model = 'gestionusers.Doctor'


class Patient(Model):
    name: TextField = TextField(db_column='name', null=False)
    familyName = TextField(db_column='family_name', null=False)
    birthdate: DateField = DateField()
    school: TextField = TextField(null=False)
    parent = ForeignKey(to='gestionusers.Parent', on_delete=CASCADE, null=True)

    class Meta:
        db_table = 'patients'
        unique_together = (('name', 'familyName', 'school', 'parent_id', 'birthdate'),)


class Supervise(Model):
    patient: ForeignKey = ForeignKey(to='Patient', on_delete=CASCADE, null=False)
    doctor: ForeignKey = ForeignKey(to=doctor_model, on_delete=CASCADE, null=False)
    validated: BooleanField = BooleanField(null=False, default=False)

    class Meta:
        db_table = 'supervises'


class Consultation(Model):
    patient: ForeignKey = ForeignKey(to='Patient', on_delete=CASCADE, null=False)
    doctor: ForeignKey = ForeignKey(to=doctor_model, on_delete=CASCADE, null=False)
    parent: ForeignKey = ForeignKey(to='gestionusers.Parent', on_delete=CASCADE, null=False)
    date: DateTimeField = DateTimeField(null=False, default=timezone.now())
    accepted: BooleanField = BooleanField(null=False, default=False)

    class Meta:
        db_table = 'consulations'


class Diagnostic(Model):
    consultation: OneToOneField = OneToOneField(to='Consultation', on_delete=CASCADE)
    diagnostic: TextField = TextField(null=False)

    class Meta:
        db_table = 'diagnostics'


PatientSerializer = create_model_serializer(model=Patient, name='PatientSerializer', app_label=app_label, options={
    'fields': ['id', 'name', 'familyName', 'birthdate', 'school', 'parent', 'behaviortroubleparent',
               'impulsivitytroubleparent', 'learningtroubleparent', 'anxitytroubleparent', 'somatisationtroubleparent',
               'hyperactivitytroubleparent', 'extratroubleparent'],
    'depth': 1
})

SuperviseSerializer = create_model_serializer(model=Supervise, app_label=app_label, name='SuperviseSerializer')
ConsultationSerializer = create_model_serializer(model=Consultation, name='Consultation', app_label=app_label)
DiagnosticSerializer = create_model_serializer(model=Diagnostic, name='DiagnosticSerializer', app_label=app_label)
