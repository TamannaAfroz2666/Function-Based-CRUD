from django.contrib import admin
from .models import Student, Teacher, Post


# Register your models here.
@admin.register(Student)
class StusentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')



@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'Teacher_Name', 'Teacher_Email', 'Teacher_Gender')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'email', 'salary', 'details', 'available', 'category', 'detail_time',)




