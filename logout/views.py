from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth import logout

@require_POST
@login_required
def cerrar_sesion(request):
    logout(request)
    return JsonResponse({'mensaje': 'Sesión cerrada exitosamente'})
