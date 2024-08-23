# quiz/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.quiz_interface, name='quiz_interface'),
    path('save-draft/', views.save_draft, name='save_draft'),
    path('submit-quiz/', views.submit_quiz, name='submit_quiz'),
    path('results/<int:session_id>/', views.quiz_results, name='quiz_results'),
]

# Add this to your project's urls.py
from django.urls import include, path

urlpatterns = [
    # ... other URL patterns ...
    path('quiz/', include('quiz.urls')),
]
