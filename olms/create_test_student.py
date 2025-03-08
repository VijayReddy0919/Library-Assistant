from olmsapp.models import CustomUser, Student

# Create a new user
user = CustomUser(
    first_name='Test',
    last_name='User',
    username='testuser',
    email='testuser@example.com',
    user_type=2
)
user.set_password('password123')
user.save()

# Create a corresponding student entry
student = Student(
    admin=user,
    studentid='SS1234',
    mobilenumber='1234567890'
)
student.save()

print("Test student created successfully.")
