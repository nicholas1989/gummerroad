from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .models import UserLibrary
from .forms import UserChangeForm, UserCreationForm

User = get_user_model()

# Unregister the default User model admin if already registered
if admin.site.is_registered(User):
    admin.site.unregister(User)

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions"
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "email", "get_name", "is_superuser"]
    search_fields = ["username", "email", "name"]
    
    def get_name(self, obj):
        return obj.name
    get_name.short_description = 'Name'

@admin.register(UserLibrary)
class UserLibraryAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user__username', 'user__email']
    filter_horizontal = ['products']
