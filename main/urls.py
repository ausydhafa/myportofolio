from django.urls import path

from main.views import (create_project_ajax, get_projects_json, login_user, 
                        logout_user, 
                        register, 
                        show_main, 
                        show_experience, 
                        show_education, 
                        create_education, 
                        get_education_json, 
                        delete_education, 
                        update_education,
                        toggle_star, 
                        show_projects,
                        create_project,
                    )
app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path("api/education/", get_education_json, name="get_education_json"),
    path("education/<uuid:education_id>/delete/", delete_education, name="delete_education"),
    path("education/<uuid:education_id>/edit/", update_education, name="update_education"),    
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("education/<uuid:education_id>/star/", toggle_star, name="toggle_education_star",),
    path("projects/add/", create_project, name="create_project"),
    path("projects/", show_projects, name="show_projects"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/star/", toggle_star,name="toggle_project_star",),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
]