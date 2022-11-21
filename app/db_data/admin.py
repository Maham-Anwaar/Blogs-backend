# Django
# Backend Apps
from db_data.models.assignment import Assignment
from db_data.models.assignment_file import AssignmentFile
from db_data.models.attendance import Attendance
from db_data.models.base_user import BaseUser
from db_data.models.lecture import Lecture
from db_data.models.material import Material
from db_data.models.score import Score
from db_data.models.workshop import Workshop
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# from db_data.inlines.material_inline_admin import MaterialInlineAdmin
# from db_data.inlines.assignment_file_inline_admin \
#     import AssignmentFileInlineAdmin
# from db_data.inlines.lecture_inline_admin import LectureInlineAdmin
# from db_data.inlines.assignemt_inline_admin import AssignmenteInlineAdmin


class AccountCreationForm(forms.ModelForm):

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = BaseUser
        fields = ("email", "full_name")

    def clean_password2(self):
        """Check that the two password entries match."""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        """Save the provided password in hashed format."""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class AccountChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text=(
            "Raw passwords are not stored, so there is no way to see "
            "this user's password, but you can change the password "
            'using <a href="../password/">this form</a>.'
        ),
    )

    class Meta:
        model = BaseUser
        fields = ("password",)

    def clean_password(self):

        return self.initial["password"]


class BaseAccountAdmin(BaseUserAdmin):
    """This custom user model is to modify the detail view of a user."""

    form = AccountChangeForm
    add_form = AccountCreationForm
    readonly_fields = ["id", "created_at", "modified_at"]
    ordering = ["id"]
    list_display = [
        "id",
        "email",
        "full_name",
        "is_active",
    ]
    fieldsets = (
        (
            "Credentials",
            {
                "fields": (
                    "id",
                    "email",
                    "password",
                    "full_name",
                    "phone_number",
                    "role",
                )
            },
        ),
        (
            "Access control",
            {"fields": ("is_active", "is_staff", "is_superuser")},
        ),
        ("Important times", {"fields": ("created_at", "modified_at", "timezone_name")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "full_name",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    filter_horizontal = ()
    list_filter = ()


class MaterialAdmin(admin.ModelAdmin):
    """Custom admin class for Notes model."""

    list_display = ["file", "file_name", "file_type"]
    readonly_fields = [
        "id",
    ]


class AssignmentFileAdmin(admin.ModelAdmin):
    """Custom admin class for Notes model."""

    list_display = ["file", "file_name", "file_type"]
    readonly_fields = [
        "id",
    ]


class LectureAdmin(admin.ModelAdmin):
    """Custom admin class for Notes model."""

    list_display = ["name", "url", "workshop"]
    readonly_fields = [
        "id",
    ]
    # inlines = [
    #     # MaterialInlineAdmin
    # ]


class AssignmentAdmin(admin.ModelAdmin):
    """Custom admin class for Notes model."""

    list_display = ["name", "total_marks"]
    readonly_fields = [
        "id",
    ]
    # inlines = [
    #     # AssignmentFileInlineAdmin
    # ]


class WorkshopAdmin(admin.ModelAdmin):
    """Custom admin class for Notes model."""

    list_display = ["name", "level", "start_date", "end_date", "mode"]
    readonly_fields = [
        "id",
    ]
    # inlines = [
    #     # AssignmenteInlineAdmin, LectureInlineAdmin
    # ]


class ScoreAdmin(admin.ModelAdmin):
    """Custom admin class for Notes model."""

    list_display = ["score", "assignment", "student"]
    readonly_fields = [
        "id",
    ]


class AttendanceAdmin(admin.ModelAdmin):
    """Custom admin class for Notes model."""

    list_display = ["present", "lecture", "student"]
    readonly_fields = [
        "id",
    ]


admin.site.register(Material, MaterialAdmin)
admin.site.register(AssignmentFile, AssignmentFileAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(BaseUser, BaseAccountAdmin)
