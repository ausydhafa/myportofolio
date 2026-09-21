from django.shortcuts import render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import EducationForm
from main.models import Experience, Education


def show_main(request):
    context = {
        "name": "Ausy Dhafa Adhitama",
        "npm": "2406417954",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Sistem Infromasi Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Ausy Dhafa Adhitama",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    json_response = get_education_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [education.object for education in educations]
    school_query = request.GET.get("school", "").strip()

    context = {
        "name": "Ausy Dhafa Adhitama",
        "education_list": educations,
        "school_query": school_query,
    }
    return render(request, "education.html", context)

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat Pendidikan berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Ausy Dhafa Adhitama",
        "form": form,
    }
    return render(request, "education_form.html", context)

def get_education_json(request):
    school_query = request.GET.get("school", "").strip()
    education = Education.objects.all()

    if school_query:
        education = education.filter(school__icontains=school_query)

    education_json = serializers.serialize("json", education)
    return HttpResponse(education_json, content_type="application/json")

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Pendidikan berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

def update_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat Pendidikan berhasil diperbarui!")
        return redirect("main:show_education")

    context = {
        "name": "Ausy Dhafa Adhitama",
        "form": form,
        "education": education,
    }

    return render(request, "education_update_form.html", context)