import json

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Question, UserResponse, UserSession


@login_required
def quiz_interface(request):
    questions = Question.objects.all()
    session = UserSession.objects.create(user=request.user)
    return render(request, 'app1/interface.html', {'questions': questions, 'session_id': session.id})

@login_required
def save_draft(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question_id = data.get('question_id')
        response_text = data.get('response')
        session_id = data.get('session_id')

        question = Question.objects.get(id=question_id)
        session = UserSession.objects.get(id=session_id)

        UserResponse.objects.update_or_create(
            user=request.user,
            question=question,
            session=session,
            defaults={'response': response_text, 'is_draft': True}
        )

        return JsonResponse({'status': 'success'})


@login_required
def submit_quiz(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        session = get_object_or_404(UserSession, id=session_id)

        # Ensure the user can only submit their own quiz
        if session.user != request.user:
            raise PermissionDenied

        session.end_time = timezone.now()
        session.save()

        UserResponse.objects.filter(session=session).update(is_draft=False)

        return redirect('quiz_results', session_id=session_id)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@login_required
def quiz_results(request, session_id):
    responses = UserResponse.objects.filter(session_id=session_id, user=request.user)
    return render(request, 'app1/results.html', {'responses': responses})
