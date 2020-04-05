from marshmallow import Schema, fields


class StudentSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    schema_version = fields.Str(require=True)


class AssignmentSchema(Schema):
    student_id = fields.Dict(required=True)
    subject_id = fields.Dict(required=True)
    grade = fields.Int(required=True)
    schema_version = fields.Str(require=True)


class ClassroomSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    schema_version = fields.Str(require=True)


class StudentGroupSchema(Schema):
    group_subject_id = fields.Dict(required=True)
    schema_version = fields.Str(require=True)


class ClassesSchema(Schema):
    class_no = fields.Str(required=True)
    schedule = fields.List(fields.Dict(), required=True)
    group_subject_id = fields.Dict(required=True)
    schema_version = fields.Str(require=True)


class EmployeeSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    schema_version = fields.Str(require=True)


class SubjectGroupSchema(Schema):
    group_name = fields.Str(required=True)
    employee_id = fields.Dict(required=True)
    subject_id = fields.Dict(required=True)
    schema_version = fields.Str(require=True)


class SyllabusSchema(Schema):
    schema_version = fields.Str(required=True)
    ects = fields.Int(required=True)
    has_exam = fields.Bool(required=True)
    hours = fields.List(fields.Dict, required=True)
    bibliography = fields.List(fields.Dict, required=True)


class StudyDisciplineSchema(Schema):
    schema_version = fields.Str(required=True),
    name = fields.Str(required=True),
    areas = fields.List(fields.Dict, required=True)


class StudyAreaSchema(Schema):
    schema_version = fields.Str(required=True),
    name = fields.Str(required=True)


class SubjectSchema(Schema):
    name = fields.Str(required=True)
    employee_id = fields.Dict(required=True)
    schema_version = fields.Str(required=True)
    syllabus = fields.List(fields.Dict, required=True)
    study_discipline = fields.List(fields.Dict, required=True)
