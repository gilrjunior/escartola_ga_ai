from django.shortcuts import render, redirect
from django.http import HttpResponseServerError
from django.http import Http404
from django.contrib import messages
from .formations import get_formation_config, get_position_coords, get_available_formations
from optimizer.cartola_services import fecth_team_formations, check_market_status

def home(request):
    """
    Página inicial do Escartola - Landing page
    """
    # Verificar status do mercado
    market_status = check_market_status()
    
    context = {
        'market_status': market_status
    }
    
    return render(request, "optimizer/home.html", context)

def map_cartola_formation_to_standard(cartola_formations):
    """
    Mapeia formações do Cartola para o formato padrão usado no sistema
    """
    formation_mapping = {
        '3-4-3': '3-4-3',
        '3-5-2': '3-5-2', 
        '4-3-3': '4-3-3',
        '4-4-2': '4-4-2',
        '4-5-1': '4-5-1',
        '5-3-2': '5-3-2',
        '5-4-1': '5-4-1'
    }
    
    mapped_formations = []
    for formation in cartola_formations:
        formation_name = formation['name']
        if formation_name in formation_mapping:
            mapped_formations.append(formation_mapping[formation_name])
    
    return mapped_formations

def add_field_coordinates(team, formation):
    """
    Adiciona coordenadas de campo para cada atleta baseado na formação tática
    Usa porcentagem do campo (0-100%)
    """
    # Adicionar coordenadas para cada atleta
    for i, athlete in enumerate(team):
        if athlete.position == 'TEC':
            # Técnico fica fora do campo (canto superior esquerdo)
            athlete.field_x = 5  # 5% da largura
            athlete.field_y = 5  # 5% da altura
        else:
            # Contar quantos jogadores da mesma posição já foram processados
            position_count = 0
            for j in range(i):
                if team[j].position == athlete.position:
                    position_count += 1
            
            # Obter coordenadas base da formação
            formation_config = get_formation_config(formation)
            base_coords = formation_config['coords'].get(athlete.position, {'x': 50, 'y': 50})
            
            # Ajustar coordenadas para múltiplos jogadores da mesma posição
            specific_coords = get_position_coords(athlete.position, position_count, formation)
            
            athlete.field_x = specific_coords['x']
            athlete.field_y = specific_coords['y']
    
    return team

def best_team_view(request):
    """
    Lê parâmetros simples da querystring (opcional),
    chama seu GA (em src/escartola/...) e renderiza a escalação.
    """
    # Verificar status do mercado antes de permitir otimização
    market_status = check_market_status()
    
    # Se mercado fechado, redirecionar para home com mensagem
    if not market_status['is_open']:
        messages.warning(request, market_status['message'])
        return redirect('home')
    
    try:
        # 1) parâmetros (pode vir da URL ou usar defaults)
        budget = float(request.GET.get("budget", 100))
        alpha = float(request.GET.get("alpha", 0.5))
        formation_name = request.GET.get("formation", "4-3-3")
        
        # Buscar formações do Cartola
        try:
            cartola_formations = fecth_team_formations()
            available_formations = map_cartola_formation_to_standard(cartola_formations)
            if not available_formations:  # Se não encontrou formações válidas
                available_formations = get_available_formations()
        except Exception as e:
            print(f"Erro ao buscar formações do Cartola: {e}")
            # Fallback para formações hardcoded
            available_formations = get_available_formations()
        
        # Validar formação
        if formation_name not in available_formations:
            formation_name = available_formations[0] if available_formations else "4-3-3"

        # 2) importar seu código já pronto (ajuste os caminhos conforme sua árvore)
        from optimizer.genetic_algorithm import GeneticAlgorithm

        # 3) rodar seu GA (exemplo genérico: adapte assinatura ao seu)
        ga = GeneticAlgorithm(budget=budget, alpha=alpha, team_formation=formation_name)
        ga.run(generations=500)  # deve retornar algo como Team(athletes=[...])

        # 4) preparar dados pro template
        if ga.best_individual is not None:
            team = ga.best_individual.get_athletes()
            total_cost = ga.best_individual.get_total_price()
            total_score = ga.best_individual.get_total_score()
            
            # Adicionar coordenadas de campo para cada atleta
            team = add_field_coordinates(team, formation_name)
        else:
            team = []
            total_cost = 0
            total_score = 0

        ctx = {
            "team": team,
            "budget": int(budget),  
            "spent": round(total_cost, 2),
            "score": round(total_score, 2),
            "alpha": alpha,
            "one_minus_alpha": 1 - alpha,
            "formation": formation_name,
            "available_formations": available_formations,
        }

        return render(request, "optimizer/team.html", ctx)

    except Exception as e:
        # logaria o erro de verdade; aqui só mostra
        print(f"Erro ao otimizar: {e}")
        return HttpResponseServerError(f"Erro ao otimizar: {e}")

def custom_404(request, exception=None):
    """
    View personalizada para erro 404
    Captura qualquer URL que não corresponda às rotas definidas
    """
    # Lista de URLs válidas
    valid_paths = ['/', '/admin/', '/team/']
    
    # Se a URL atual não está na lista de válidas, mostra 404
    if request.path not in valid_paths:
        return render(request, 'optimizer/404.html', status=404)
    
    # Se chegou aqui, é uma URL válida mas não deveria estar aqui
    # Redireciona para home
    from django.shortcuts import redirect
    return redirect('home')

