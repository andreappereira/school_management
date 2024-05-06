from registration.models import Registration


def validate_existing_registration(student, course, period):
    queryset = Registration.objects.filter(
        student_id=student,
        course_id=course,
        period=period
    ).exists()

    return queryset
