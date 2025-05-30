from django.contrib import admin
from .models import Departments,Doctors,Booking

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display=('dep_name','dep_description')
admin.site.register(Departments,DepartmentAdmin)

class DoctorsAdmin(admin.ModelAdmin):
    list_display=('doc_name','doc_spec','dep_spec','doc_image')
admin.site.register(Doctors,DoctorsAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display=('p_name','p_phone','p_email','doc_name','booking_date','booked_time')
admin.site.register(Booking,BookingAdmin)
 