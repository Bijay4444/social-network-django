from django.contrib import admin
from .models import CustomUser, UserProfile

# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    inlines = (UserProfileInline,)

