from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Skill(models.Model):
    skill_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    class Meta:
        db_table = "skills"

    def __str__(self):
        return self.name

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.CharField(max_length=500, null=True)
    demo_url = models.CharField(max_length=500, null=True)
    github_url = models.CharField(max_length=500, null=True)
    skills = models.ManyToManyField(
        Skill,
        through="ProjectSkill",
        related_name="projects"
    )

    class Meta:
        db_table = "projects"

    def __str__(self):
        return self.name

class ProjectSkill(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        db_column="project_id"
    )

    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        db_column="skill_id"
    )

    pk = models.CompositePrimaryKey("project", "skill")

    class Meta:
        db_table = "project_skills"


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    level = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ]
    )

    class Meta:
        db_table = "languages"

    def __str__(self):
        return self.name

class Education(models.Model):
    education_id = models.AutoField(primary_key=True)
    degree = models.CharField(max_length=200)
    university_name = models.CharField(max_length=100)
    start_at = models.DateField()
    end_at = models.DateField(null=True)
    image = models.CharField(max_length=500, null=True)
    content = models.CharField(max_length=500, null=True)

    class Meta:
        db_table = "education"

    def __str__(self):
        return self.degree


class Experience(models.Model):
    experience_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    start_at = models.DateField()
    end_at = models.DateField(null=True)

    class Meta:
        db_table = "experience"

    def __str__(self):
        return self.job_title
