from django.shortcuts import render, redirect
from .models import Student

def student_login(request):
    if request.method == 'POST':
        enrollment_no = request.POST['enrollment_no']
        password = request.POST['password']
        try:
            student = Student.objects.get(enrollment_no=enrollment_no, password=password)
            # Redirect to the student profile page with student information
            return redirect('studmod1.html', student_id=student.id)
        except Student.DoesNotExist:
            # Handle login failure
            return render(request, 'stulog.html', {'error_message': 'Invalid credentials'})

    return render(request, 'stulog.html')

