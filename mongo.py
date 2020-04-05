from pymongo import MongoClient
from schema import *
from marshmallow import ValidationError


def schema_loader(collection):
    schema_switcher = {
        'Assignment': AssignmentSchema,
        'Classes': ClassesSchema,
        'Classroom': ClassroomSchema,
        'Employee': EmployeeSchema,
        'Student': StudentSchema,
        'StudentGroup': StudentGroupSchema,
        'Subject': SubjectSchema,
        'SubjectGroup': SubjectGroupSchema,
        'StudyDiscipline': StudyDisciplineSchema,
        'StudyArea': StudyAreaSchema
    }
    return schema_switcher.get(collection)()


class MongoDb:
    def __init__(self):
        mongo_url = 'mongodb://localhost:27017/'
        self.db = MongoClient(mongo_url).uczelnia

    def read_all(self, collection, selector):
        return self.db[collection].find(selector)

    def read(self, collection, selector):
        return self.db[collection].find_one(selector)

    def create(self, collection, data):
        try:
            schema = schema_loader(collection)
            schema.load(data)
            self.db[collection].insert_one(data)
            return self.dump(schema, data)
        except ValidationError as error:
            print(error.messages)
            print(error.valid_data)

    def update(self, collection, selector, data):
        try:
            schema_loader(collection).load(data)
            return self.db[collection].replace_one(selector, data).inserted_id
        except ValidationError as error:
            print(error.messages)
            print(error.valid_data)

    def delete(self, collection, selector):
        return self.db[collection].delete_one(selector).deleted_count

    def dump(self, schema, data):
        return schema.dump(data)


db = MongoDb()

student1 = db.create("Student", {
    "first_name": "Joe",
    "last_name": "Doe",
    "schema_version": "1"
})
print("Dodano student1: ", student1)

employee1 = db.create("Employee", {
    "first_name": "Aneta",
    "last_name": "Gajdowska",
    "schema_version": "1"
})
print("Dodano employee1: ", employee1)

employee2 = db.create("Employee", {
    "first_name": "Artur",
    "last_name": "Jackowski",
    "schema_version": "1"
})

print("Dodano employee2: ", employee2)

study_discipline = db.create("StudyDiscipline", {
    "schema_version": "1",
    "name": "Informatyka",
    "areas": [
        {
            "schema_version": "1",
            "name": "Informatyka Techniczna"
        }
    ]
})
subject1 = db.create("Subject", {
    "name": "Teoria sprezystosci",
    "employee_id": employee1,
    "schema_version": "1",
    "syllabus": [
        {
            "schema_version": "1",
            "ects": "10",
            "has_exam": True,
            "hours": [
                {
                    "type": "lecture",
                    "value": 40
                },
                {
                    "type": "lab",
                    "value": 30
                }
            ],
            "bibliography": [
                {
                    "author": "Stephen Hawking",
                    "title": "Krotka Historia Wszechswiata"
                }
            ]
        }
    ],
    "study_discipline": [
        {
            "schema_version": "1",
            "name": "Informatyka Techniczna"
        }
    ]
})

print("Dodano subject1: ", subject1)

subject2 = db.create("Subject", {
    "name": "Teoria plastycznosci",
    "employee_id": employee1,
    "schema_version": "1",
    "syllabus": [
        {
            "schema_version": "1",
            "ects": "10",
            "has_exam": True,
            "hours": [
                {
                    "type": "lecture",
                    "value": 40
                },
                {
                    "type": "lab",
                    "value": 30
                }
            ],
            "bibliography": [
                {
                    "author": "Stephen Hawking",
                    "title": "Krotka Historia Wszechswiata"
                }
            ]
        }
    ],
    "study_discipline": [
        {
            "schema_version": "1",
            "name": "Informatyka Techniczna"
        }
    ]
})
print("Dodano subject2: ", subject2)

assignment1 = db.create("Assignment", {
    "student_id": student1,
    "subject_id": subject1,
    "grade": 5,
    "schema_version": "1"
})

print("Dodano assignment1: ", assignment1)

classroom1 = db.create("Classroom", {
    "name": "H24",
    "description": "Cloudy space and cheating supportive",
    "schema_version": "1"
})
print("Dodano classroom1: ", classroom1)

classes1 = db.create("Classes", {
    "class_no": "Grupa4",
    "schedule": [
        {
            "date_time": "2020-07-30"
        },
        {
            "classroom_id": classroom1
        }
    ],
    "group_subject_id": subject1,
    "schema_version": "1"
})

print("Dodano classes1: ", classes1)

subjectgroup1 = db.create("SubjectGroup", {
    "group_name": "Mehchanika",
    "employee_id": employee1,
    "subject_id": subject1,
    "schema_version": "1"
})
print("Dodano subjectgroup1: ", subjectgroup1)

studentgroup1 = db.create("StudentGroup", {
    "group_subject_id": subjectgroup1,
    "schema_version": "1"
})

print("Dodano studentgroup1: ", studentgroup1)
