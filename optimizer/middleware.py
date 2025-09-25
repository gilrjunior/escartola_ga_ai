"""
Middleware para forçar idioma português brasileiro
"""
from django.utils import translation

class ForcePortugueseMiddleware:
    """
    Middleware que força o idioma para português brasileiro
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Força o idioma para português brasileiro
        translation.activate('pt-br')
        request.LANGUAGE_CODE = 'pt-br'
        
        response = self.get_response(request)
        
        # Mantém o idioma ativo na resposta
        response['Content-Language'] = 'pt-br'
        
        return response
