from django.contrib import admin

from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'created_at')  # noqa: WPS226
    search_fields = ('id', 'email')  # noqa: WPS226
