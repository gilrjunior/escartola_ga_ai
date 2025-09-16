"""
Módulo para gerenciar formações táticas do futebol
Contém todas as formações disponíveis e suas configurações
"""

def get_formation_config(formation):
    """
    Retorna a configuração de uma formação tática específica
    
    Args:
        formation (str): Nome da formação (ex: '4-3-3', '3-5-2', etc.)
    
    Returns:
        dict: Configuração da formação com coordenadas base e posições
    """
    
    formations = {
        '3-4-3': {
            'coords': {
                'GOL': {'x': 50, 'y': 250},
                'ZAG': {'x': 160, 'y': 150},
                'LAT': {'x': 170, 'y': 120},
                'MEI': {'x': 350, 'y': 180},
                'ATA': {'x': 620, 'y': 120}
            },
            'positions': ['GOL', 'ZAG', 'ZAG', 'ZAG', 'LAT', 'LAT', 'MEI', 'MEI', 'MEI', 'MEI', 'ATA', 'ATA', 'ATA']
        },
        '3-5-2': {
            'coords': {
                'GOL': {'x': 50, 'y': 250},
                'ZAG': {'x': 160, 'y': 150},
                'MEI': {'x': 350, 'y': 150},
                'ATA': {'x': 620, 'y': 200}
            },
            'positions': ['GOL', 'ZAG', 'ZAG', 'ZAG', 'MEI', 'MEI', 'MEI', 'MEI', 'MEI', 'ATA', 'ATA']
        },
        '4-3-3': {
            'coords': {
                'GOL': {'x': 50, 'y': 250},
                'ZAG': {'x': 160, 'y': 200},
                'LAT': {'x': 170, 'y': 120},
                'MEI': {'x': 350, 'y': 180},
                'ATA': {'x': 620, 'y': 120}
            },
            'positions': ['GOL', 'ZAG', 'ZAG', 'LAT', 'LAT', 'MEI', 'MEI', 'MEI', 'ATA', 'ATA', 'ATA']
        },
        '4-4-2': {
            'coords': {
                'GOL': {'x': 50, 'y': 250},
                'ZAG': {'x': 160, 'y': 200},
                'LAT': {'x': 170, 'y': 120},
                'MEI': {'x': 350, 'y': 200},
                'ATA': {'x': 620, 'y': 200}
            },
            'positions': ['GOL', 'ZAG', 'ZAG', 'LAT', 'LAT', 'MEI', 'MEI', 'MEI', 'MEI', 'ATA', 'ATA']
        },
        '4-5-1': {
            'coords': {
                'GOL': {'x': 50, 'y': 250},
                'ZAG': {'x': 160, 'y': 200},
                'LAT': {'x': 170, 'y': 120},
                'MEI': {'x': 350, 'y': 180},
                'ATA': {'x': 620, 'y': 250}
            },
            'positions': ['GOL', 'ZAG', 'ZAG', 'LAT', 'LAT', 'MEI', 'MEI', 'MEI', 'MEI', 'MEI', 'ATA']
        },
        '5-3-2': {
            'coords': {
                'GOL': {'x': 50, 'y': 250},
                'ZAG': {'x': 160, 'y': 150},
                'LAT': {'x': 170, 'y': 120},
                'MEI': {'x': 350, 'y': 200},
                'ATA': {'x': 620, 'y': 200}
            },
            'positions': ['GOL', 'ZAG', 'ZAG', 'ZAG', 'ZAG', 'ZAG', 'LAT', 'LAT', 'MEI', 'MEI', 'MEI', 'ATA', 'ATA']
        },
        '5-4-1': {
            'coords': {
                'GOL': {'x': 50, 'y': 250},
                'ZAG': {'x': 160, 'y': 150},
                'LAT': {'x': 170, 'y': 120},
                'MEI': {'x': 350, 'y': 200},
                'ATA': {'x': 620, 'y': 250}
            },
            'positions': ['GOL', 'ZAG', 'ZAG', 'ZAG', 'ZAG', 'ZAG', 'LAT', 'LAT', 'MEI', 'MEI', 'MEI', 'MEI', 'ATA']
        }
    }
    
    return formations.get(formation, formations['4-3-3'])  # Default para 4-3-3


def get_position_coords(position, position_count, formation):
    """
    Retorna coordenadas específicas para múltiplos jogadores da mesma posição
    
    Args:
        position (str): Posição do jogador (GOL, ZAG, LAT, MEI, ATA)
        position_count (int): Quantos jogadores da mesma posição já foram processados
        formation (str): Formação tática
    
    Returns:
        dict: Coordenadas x, y para o jogador
    """
    
    base_coords = {'x': 50, 'y': 250}  # Coordenada padrão
    
    if position == 'ZAG':
        if formation == '3-5-2':
            if position_count == 0:
                base_coords = {'x': 190, 'y': 180}
            elif position_count == 1:
                base_coords = {'x': 190, 'y': 250}
            elif position_count == 2:
                base_coords = {'x': 190, 'y': 320}
        elif formation in ['5-3-2', '5-4-1']:
            if position_count == 0:
                base_coords = {'x': 190, 'y': 120}
            elif position_count == 1:
                base_coords = {'x': 190, 'y': 200}
            elif position_count == 2:
                base_coords = {'x': 190, 'y': 250}
            elif position_count == 3:
                base_coords = {'x': 190, 'y': 300}
            elif position_count == 4:
                base_coords = {'x': 190, 'y': 380}
        else:  # 3-4-3, 4-3-3, 4-4-2, 4-5-1
            if position_count == 0:
                base_coords = {'x': 190, 'y': 200}
            elif position_count == 1:
                base_coords = {'x': 190, 'y': 300}
                
    elif position == 'LAT':
        if position_count == 0:
            base_coords = {'x': 220, 'y': 120}
        elif position_count == 1:
            base_coords = {'x': 220, 'y': 380}
            
    elif position == 'MEI':
        if formation == '4-3-3':
            if position_count == 0:
                base_coords = {'x': 400, 'y': 180}
            elif position_count == 1:
                base_coords = {'x': 380, 'y': 250}
            elif position_count == 2:
                base_coords = {'x': 400, 'y': 320}
        elif formation == '4-4-2':
            if position_count == 0:
                base_coords = {'x': 400, 'y': 120}
            elif position_count == 1:
                base_coords = {'x': 380, 'y': 200}
            elif position_count == 2:
                base_coords = {'x': 380, 'y': 300}
            elif position_count == 3:
                base_coords = {'x': 400, 'y': 380}
        elif formation == '4-5-1':
            if position_count == 0:
                base_coords = {'x': 400, 'y': 100}
            elif position_count == 1:
                base_coords = {'x': 380, 'y': 180}
            elif position_count == 2:
                base_coords = {'x': 380, 'y': 250}
            elif position_count == 3:
                base_coords = {'x': 380, 'y': 320}
            elif position_count == 4:
                base_coords = {'x': 400, 'y': 400}
        elif formation == '3-5-2':
            if position_count == 0:
                base_coords = {'x': 400, 'y': 50}
            elif position_count == 1:
                base_coords = {'x': 350, 'y': 150}
            elif position_count == 2:
                base_coords = {'x': 350, 'y': 250}
            elif position_count == 3:
                base_coords = {'x': 350, 'y': 350}
            elif position_count == 4:
                base_coords = {'x': 400, 'y': 450}
        elif formation == '3-4-3':
            if position_count == 0:
                base_coords = {'x': 400, 'y': 120}
            elif position_count == 1:
                base_coords = {'x': 380, 'y': 200}
            elif position_count == 2:
                base_coords = {'x': 380, 'y': 300}
            elif position_count == 3:
                base_coords = {'x': 400, 'y': 380}
        elif formation in ['5-3-2', '5-4-1']:
            if position_count == 0:
                base_coords = {'x': 400, 'y': 150}
            elif position_count == 1:
                base_coords = {'x': 380, 'y': 220}
            elif position_count == 2:
                base_coords = {'x': 380, 'y': 280}
            elif position_count == 3:
                base_coords = {'x': 400, 'y': 350}
            elif formation == '5-4-1' and position_count == 4:
                base_coords = {'x': 400, 'y': 450}
                
    elif position == 'ATA':
        if formation == '4-3-3':
            if position_count == 0:
                base_coords = {'x': 620, 'y': 120}
            elif position_count == 1:
                base_coords = {'x': 620, 'y': 250}
            elif position_count == 2:
                base_coords = {'x': 620, 'y': 380}
        elif formation == '4-4-2':
            if position_count == 0:
                base_coords = {'x': 620, 'y': 180}
            elif position_count == 1:
                base_coords = {'x': 620, 'y': 320}
        elif formation == '4-5-1':
            if position_count == 0:
                base_coords = {'x': 620, 'y': 250}
        elif formation == '3-5-2':
            if position_count == 0:
                base_coords = {'x': 620, 'y': 180}
            elif position_count == 1:
                base_coords = {'x': 620, 'y': 320}
        elif formation == '3-4-3':
            if position_count == 0:
                base_coords = {'x': 620, 'y': 120}
            elif position_count == 1:
                base_coords = {'x': 620, 'y': 250}
            elif position_count == 2:
                base_coords = {'x': 620, 'y': 380}
        elif formation in ['5-3-2', '5-4-1']:
            if position_count == 0:
                base_coords = {'x': 620, 'y': 200}
            elif formation == '5-3-2' and position_count == 1:
                base_coords = {'x': 620, 'y': 300}
    
    return base_coords


def get_available_formations():
    """
    Retorna lista de todas as formações disponíveis
    
    Returns:
        list: Lista com nomes das formações
    """
    return ['3-4-3', '3-5-2', '4-3-3', '4-4-2', '4-5-1', '5-3-2', '5-4-1']
