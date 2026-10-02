# from django.contrib import admin
# from .models import Skill, Project, Language, Education, Experience, ProjectSkill

# class ProjectSkillInline(admin.TabularInline):
#     model = ProjectSkill
#     extra = 1


# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     inlines = [ProjectSkillInline]

# admin.site.register(Skill)
# admin.site.register(Language)
# admin.site.register(Education)
# admin.site.register(Experience)

from django import forms
from django.contrib import admin

from .models import (
    Skill,
    Project,
    Language,
    Education,
    Experience,
    ProjectSkill,
)


class ProjectAdminForm(forms.ModelForm):

    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Project
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields["skills"].initial = self.instance.skills.all()

    def save(self, commit=True):
        project = super().save(commit=commit)

        if commit:
            self.save_skills(project)

        return project

    def save_skills(self, project):
        selected_skills = self.cleaned_data["skills"]

        ProjectSkill.objects.filter(
            project=project
        ).delete()

        ProjectSkill.objects.bulk_create([
            ProjectSkill(
                project=project,
                skill=skill
            )
            for skill in selected_skills
        ])


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm


admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(Education)
admin.site.register(Experience)
