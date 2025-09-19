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
                'GOL': {'x': 7, 'y': 50},      # 7% da largura, 50% da altura
                'ZAG': {'x': 23, 'y': 30},     # 23% da largura, 30% da altura
                'LAT': {'x': 24, 'y': 24},     # 24% da largura, 24% da altura
                'MEI': {'x': 50, 'y': 36},     # 50% da largura, 36% da altura
                'ATA': {'x': 89, 'y': 24}      # 89% da largura, 24% da altura
            },
            'positions': ['GOL', 'ZAG', 'ZAG', 'ZAG', 'LAT', 'LAT', 'MEI', 'MEI', 'MEI', 'MEI', 'ATA', 'ATA', 'ATA']
        },
        '3-5-2': {
            'coords': {
                'GOL': {'x': 7, 'y': 50},
                'ZAG': {'x': 23, 'y': 30},
                'MEI': {'x': 50, 'y': 30},
                'ATA': {'x': 89, 'y': 40}
            },
            'positions': ['GOL', 'ZAG', 'ZAG', 'ZAG', 'MEI', 'MEI', 'MEI', 'MEI', 'MEI', 'ATA', 'ATA']
        },
        '4-3-3': {
            'coords': {
                'GOL': {'x': 7, 'y': 50},
                'ZAG': {'x': 23, 'y': 40},
                'LAT': {'x': 24, 'y': 24},
                'MEI': {'x': 50, 'y': 36},
                'ATA': {'x': 89, 'y': 24}
            },
            'positions': ['GOL', 'ZAG', 'ZAG', 'LAT', 'LAT', 'MEI', 'MEI', 'MEI', 'ATA', 'ATA', 'ATA']
        },
        '4-4-2': {
            'coords': {
                'GOL': {'x': 7, 'y': 50},
                'ZAG': {'x': 23, 'y': 40},
                'LAT': {'x': 24, 'y': 24},
                'MEI': {'x': 50, 'y': 40},
                'ATA': {'x': 89, 'y': 40}
            },
            'positions': ['GOL', 'ZAG', 'ZAG', 'LAT', 'LAT', 'MEI', 'MEI', 'MEI', 'MEI', 'ATA', 'ATA']
        },
        '4-5-1': {
            'coords': {
                'GOL': {'x': 7, 'y': 50},
                'ZAG': {'x': 23, 'y': 40},
                'LAT': {'x': 24, 'y': 24},
                'MEI': {'x': 50, 'y': 36},
                'ATA': {'x': 89, 'y': 50}
            },
            'positions': ['GOL', 'ZAG', 'ZAG', 'LAT', 'LAT', 'MEI', 'MEI', 'MEI', 'MEI', 'MEI', 'ATA']
        },
        '5-3-2': {
            'coords': {
                'GOL': {'x': 7, 'y': 50},
                'ZAG': {'x': 23, 'y': 30},
                'LAT': {'x': 24, 'y': 24},
                'MEI': {'x': 50, 'y': 40},
                'ATA': {'x': 89, 'y': 40}
            },
            'positions': ['GOL', 'ZAG', 'ZAG', 'ZAG', 'LAT', 'LAT', 'MEI', 'MEI', 'MEI', 'ATA', 'ATA']
        },
        '5-4-1': {
            'coords': {
                'GOL': {'x': 7, 'y': 50},
                'ZAG': {'x': 23, 'y': 30},
                'LAT': {'x': 24, 'y': 24},
                'MEI': {'x': 50, 'y': 40},
                'ATA': {'x': 89, 'y': 50}
            },
            'positions': ['GOL', 'ZAG', 'ZAG', 'ZAG', 'LAT', 'LAT', 'MEI', 'MEI', 'MEI', 'MEI', 'ATA']
        }
    }
    
    return formations.get(formation, formations['4-3-3'])  # Default para 4-3-3


def get_position_coords(position, position_count, formation):
    """
    Retorna coordenadas específicas para múltiplos jogadores da mesma posição
    Usa porcentagem do campo (0-100%)
    
    Args:
        position (str): Posição do jogador (GOL, ZAG, LAT, MEI, ATA)
        position_count (int): Quantos jogadores da mesma posição já foram processados
        formation (str): Formação tática
    
    Returns:
        dict: Coordenadas x, y em porcentagem para o jogador
    """
    
    base_coords = {'x': 10, 'y': 50}  
    
    if position == 'ZAG':
        if formation in ['3-5-2', '3-4-3']:
            if position_count == 0:
                base_coords = {'x': 27, 'y': 30}
            elif position_count == 1:
                base_coords = {'x': 27, 'y': 50}
            elif position_count == 2:
                base_coords = {'x': 27, 'y': 70}
        elif formation in ['5-3-2', '5-4-1']:
            if position_count == 0:
                base_coords = {'x': 27, 'y': 30}
            elif position_count == 1:
                base_coords = {'x': 27, 'y': 50}
            elif position_count == 2:
                base_coords = {'x': 27, 'y': 70}
        else:  #4-3-3, 4-4-2, 4-5-1
            if position_count == 0:
                base_coords = {'x': 27, 'y': 40}
            elif position_count == 1:
                base_coords = {'x': 27, 'y': 60}
                
    elif position == 'LAT':
        if formation in ['5-3-2', '5-4-1']:
            if position_count == 0:
                base_coords = {'x': 31, 'y': 10}
            elif position_count == 1:
                base_coords = {'x': 31, 'y': 90}
        else:
            if position_count == 0:
                base_coords = {'x': 31, 'y': 24}
            elif position_count == 1:
                base_coords = {'x': 31, 'y': 76}
            
    elif position == 'MEI':
        if formation == '4-3-3':
            if position_count == 0:
                base_coords = {'x': 57, 'y': 30}
            elif position_count == 1:
                base_coords = {'x': 54, 'y': 50}
            elif position_count == 2:
                base_coords = {'x': 57, 'y': 70}
        elif formation == '4-4-2':
            if position_count == 0:
                base_coords = {'x': 57, 'y': 24}
            elif position_count == 1:
                base_coords = {'x': 54, 'y': 40}
            elif position_count == 2:
                base_coords = {'x': 54, 'y': 60}
            elif position_count == 3:
                base_coords = {'x': 57, 'y': 76}
        elif formation == '4-5-1':
            if position_count == 0:
                base_coords = {'x': 57, 'y': 10}
            elif position_count == 1:
                base_coords = {'x': 50, 'y': 30}
            elif position_count == 2:
                base_coords = {'x': 50, 'y': 50}
            elif position_count == 3:
                base_coords = {'x': 50, 'y': 70}
            elif position_count == 4:
                base_coords = {'x': 57, 'y': 90}
        elif formation == '3-5-2':
            if position_count == 0:
                base_coords = {'x': 57, 'y': 10}
            elif position_count == 1:
                base_coords = {'x': 50, 'y': 30}
            elif position_count == 2:
                base_coords = {'x': 50, 'y': 50}
            elif position_count == 3:
                base_coords = {'x': 50, 'y': 70}
            elif position_count == 4:
                base_coords = {'x': 57, 'y': 90}
        elif formation == '3-4-3':
            if position_count == 0:
                base_coords = {'x': 57, 'y': 24}
            elif position_count == 1:
                base_coords = {'x': 54, 'y': 40}
            elif position_count == 2:
                base_coords = {'x': 54, 'y': 60}
            elif position_count == 3:
                base_coords = {'x': 57, 'y': 76}
        elif formation == '5-4-1':
            if position_count == 0:
                base_coords = {'x': 57, 'y': 30}
            elif position_count == 1:
                base_coords = {'x': 54, 'y': 44}
            elif position_count == 2:
                base_coords = {'x': 54, 'y': 56}
            elif position_count == 3:
                base_coords = {'x': 57, 'y': 70}
            elif position_count == 4:
                base_coords = {'x': 57, 'y': 90}
        elif formation == '5-3-2':
            if position_count == 0:
                base_coords = {'x': 57, 'y': 25}
            elif position_count == 1:
                base_coords = {'x': 50, 'y': 50}
            elif position_count == 2:
                base_coords = {'x': 57, 'y': 75}
                
    elif position == 'ATA':
        if formation == '4-3-3':
            if position_count == 0:
                base_coords = {'x': 89, 'y': 24}
            elif position_count == 1:
                base_coords = {'x': 89, 'y': 50}
            elif position_count == 2:
                base_coords = {'x': 89, 'y': 76}
        elif formation == '4-4-2':
            if position_count == 0:
                base_coords = {'x': 89, 'y': 36}
            elif position_count == 1:
                base_coords = {'x': 89, 'y': 64}
        elif formation == '4-5-1':
            if position_count == 0:
                base_coords = {'x': 89, 'y': 50}
        elif formation == '3-5-2':
            if position_count == 0:
                base_coords = {'x': 89, 'y': 36}
            elif position_count == 1:
                base_coords = {'x': 89, 'y': 64}
        elif formation == '3-4-3':
            if position_count == 0:
                base_coords = {'x': 89, 'y': 24}
            elif position_count == 1:
                base_coords = {'x': 89, 'y': 50}
            elif position_count == 2:
                base_coords = {'x': 89, 'y': 76}
        elif formation in ['5-3-2', '5-4-1']:
            if position_count == 0:
                base_coords = {'x': 89, 'y': 40}
            elif formation == '5-3-2' and position_count == 1:
                base_coords = {'x': 89, 'y': 60}
    
    return base_coords


def get_available_formations():
    """
    Retorna lista de todas as formações disponíveis
    
    Returns:
        list: Lista com nomes das formações
    """
    return ['3-4-3', '3-5-2', '4-3-3', '4-4-2', '4-5-1', '5-3-2', '5-4-1']
