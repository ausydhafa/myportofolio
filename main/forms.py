from django.forms import ModelForm, NumberInput, TextInput, Textarea, URLInput

from main.models import Education, Project

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "school",
            "year",
            "level",
        ]

        labels = {
            "school": "Nama Instansi Pendidikan",
            "year": "Tahun Selesai",
            "level": "Tingkat Pendidikan",
        }

        widgets = {
            "school": TextInput(
                attrs={
                    "placeholder": "Nama",
                    "maxlength": 255,
                }
            ),
            "year": NumberInput(
                attrs={
                    "placeholder": "Tahun",
                }
            ),
            "level": TextInput(
                attrs={
                    "placeholder": "Tingkat",
                    "maxlength": 100,
                }
            ),
        }

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }