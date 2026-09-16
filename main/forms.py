from django.forms import ModelForm, NumberInput, TextInput, Textarea, URLInput

from main.models import Education

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