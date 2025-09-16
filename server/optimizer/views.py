from django.shortcuts import render
from django.http import HttpResponseServerError
from .formations import get_formation_config, get_position_coords, get_available_formations

def add_field_coordinates(team, formation):
    """
    Adiciona coordenadas de campo para cada atleta baseado na formação tática
    """
    # Adicionar coordenadas para cada atleta
    for i, athlete in enumerate(team):
        if athlete.position == 'TEC':
            # Técnico fica fora do campo (canto superior esquerdo)
            athlete.field_x = 30
            athlete.field_y = 30
        else:
            # Contar quantos jogadores da mesma posição já foram processados
            position_count = 0
            for j in range(i):
                if team[j].position == athlete.position:
                    position_count += 1
            
            # Obter coordenadas base da formação
            formation_config = get_formation_config(formation)
            base_coords = formation_config['coords'].get(athlete.position, {'x': 350, 'y': 250})
            
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
    try:
        # 1) parâmetros (pode vir da URL ou usar defaults)
        budget = float(request.GET.get("budget", 110))
        alpha = float(request.GET.get("alpha", 0.6))
        formation_name = request.GET.get("formation", "4-3-3")
        
        # Validar formação
        available_formations = get_available_formations()
        if formation_name not in available_formations:
            formation_name = "4-3-3"  # Default se formação inválida

        # 2) importar seu código já pronto (ajuste os caminhos conforme sua árvore)
        from escartola.genetic_algorithm.GeneticAlgorithm import GeneticAlgorithm

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
            "budget": budget,
            "spent": total_cost,
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

