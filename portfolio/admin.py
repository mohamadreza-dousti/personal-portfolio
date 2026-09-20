from django.contrib import admin
from .models import Skill, Project, Language, Education, Experience, ProjectSkill

class ProjectSkillInline(admin.TabularInline):
    model = ProjectSkill
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectSkillInline]

admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(Education)
admin.site.register(Experience)
