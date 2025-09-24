import requests
from optimizer.classes.Athlete import Athlete
from dotenv import load_dotenv # type: ignore
import os
from datetime import datetime

def fetch_athletes():
    """
    Busca os atletas do Cartola FC
    """
    load_dotenv()

    response = requests.get(f"{os.getenv('market_url')}")
    data = response.json()
    
    positions = list(data['posicoes'].values())
    status = list(data['status'].values())
    atletas = data['atletas']

    athletes = []

    for atleta in atletas:

        athletes.append(Athlete(atleta['atleta_id'], 
                                atleta['nome'], 
                                atleta['apelido'], 
                                fetch_position_by_id(atleta['posicao_id'], positions), 
                                atleta['preco_num'], 
                                atleta['pontos_num'], 
                                atleta['media_num'], 
                                fetch_status_by_id(atleta['status_id'], status)))


    return athletes

def fetch_position_by_id(position_id, position_list):
    for position in position_list:
        if position['id'] == position_id:
            return position['abreviacao'].upper()
    return "Indisponível"

def fetch_status_by_id(status_id, status_list):
    for status in status_list:
        if status['id'] == status_id:
            return status['nome']
    return "Indisponível"


def fecth_team_formations():

    load_dotenv()

    response = requests.get(f"{os.getenv('team_formations_url')}")
    data = response.json()

    formations = map_formation(data)

    return formations

def map_formation(data):

    formations = []

    for formation in data:
        name = formation['nome']
        positions = formation['posicoes']
        team_formation = [
            {
                'position': 'GOL',
                'quantity': positions['gol']
            },
            {
                'position': 'ZAG',
                'quantity': positions['zag']
            },
            {
                'position': 'LAT',
                'quantity': positions['lat']
            },
            {
                'position': 'MEI',
                'quantity': positions['mei']
            },
            {
                'position': 'ATA',
                'quantity': positions['ata']
            },
            {
                'position': 'TEC',
                'quantity': positions['tec']
            }
        ]

        formations.append({
            'name': name,
            'team_formation': team_formation
        })

    return formations

def check_market_status():


    load_dotenv()

    try:
        
        response = requests.get(f"{os.getenv('rounds_url')}", timeout=10)
        response.raise_for_status()
        
        rodadas = response.json()
        now = datetime.now()
        
        
        for rodada in rodadas:
            inicio = datetime.strptime(rodada['inicio'], '%Y-%m-%d %H:%M:%S')
            fim = datetime.strptime(rodada['fim'], '%Y-%m-%d %H:%M:%S')
            
            if inicio <= now <= fim:
                return {
                    'is_open': False,
                    'current_round': rodada['nome_rodada'],
                    'message': f"Mercado fechado durante {rodada['nome_rodada']}. Aguarde a rodada finalizar para obter as melhores escalações."
                }
        
        
        return {
            'is_open': True,
            'current_round': None,
            'message': "Mercado aberto - Otimização disponível"
        }
        
    except requests.RequestException as e:
        print(f"Erro ao consultar API do Cartola: {e}")
        
        return {
            'is_open': True,
            'current_round': None,
            'message': "Mercado aberto - Otimização disponível"
        }
    except Exception as e:
        print(f"Erro inesperado ao verificar mercado: {e}")
        return {
            'is_open': True,
            'current_round': None,
            'message': "Mercado aberto - Otimização disponível"
        }
