import os
from googleapiclient.discovery import build

# Obter a chave da API
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
if not YOUTUBE_API_KEY:
    raise ValueError("A chave da API do YouTube não foi encontrada nas variáveis de ambiente.")

# Inicializar o cliente YouTube
def get_youtube_client(chave_api):
    return build("youtube", "v3", developerKey=chave_api)

youtube_client = get_youtube_client(YOUTUBE_API_KEY)

def pesquisar_videos_youtube(consulta, num_resultados=5):
    """
    Pesquisa vídeos no YouTube e retorna os resultados, excluindo Shorts.

    Args:
        consulta (str): A consulta de pesquisa.
        num_resultados (int, opcional): Número máximo de vídeos. Padrão: 5.

    Returns:
        list: Lista de dicionários contendo título, descrição, URL e canal.
    """
    try:
        requisicao = youtube_client.search().list(
            part="snippet",
            maxResults=num_resultados * 2,  # Solicita mais para compensar filtros
            q=consulta,
            type="video",
            videoDuration="medium",  # Filtra vídeos com pelo menos 4 minutos
            order="relevance"
        )
        resposta = requisicao.execute()
    except Exception as e:
        print(f"Erro ao buscar vídeos no YouTube: {e}")
        return []

    videos = []
    for item in resposta.get("items", []):
        if item["id"]["kind"] == "youtube#video":
            titulo = item["snippet"]["title"]
            descricao = item["snippet"]["description"]
            url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            canal = item["snippet"]["channelTitle"]

            # Remover Shorts pelo título e descrição
            if "Shorts" not in titulo and "Shorts" not in descricao:
                videos.append({
                    "Título": titulo,
                    "Descrição": descricao,
                    "URL": url,
                    "Canal": canal
                })

            # Para evitar retornar menos vídeos do que o necessário
            if len(videos) >= num_resultados:
                break

    return videos
