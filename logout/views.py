from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

@csrf_protect
@login_required
def cerrar_sesion(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'mensaje': 'Sesión cerrada exitosamente'})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
