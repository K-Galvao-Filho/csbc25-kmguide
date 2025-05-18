import os
import gradio as gr
from crewai import Task, Agent, LLM
from youtube import pesquisar_videos_youtube
import time  # Para simular a progressão

GROQ_API_KEY_01 = os.getenv("GROQ_API_KEY_01")
groqllm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY_01
)
GROQ_API_KEY_02 = os.getenv("GROQ_API_KEY_02")
groqllm2 = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY_02
)

def processar_topicos(topicos_str):
    """ Converte uma string de tópicos separada por vírgulas em uma lista tratada. """
    return [t.strip() for t in topicos_str.split(',') if t.strip()]

def executar_equipe_interface(disciplina, assunto, topicos_str, horas, dias):
    
    topicos = processar_topicos(topicos_str)

    solicitacao = f"Disciplina: {disciplina}\nAssunto: {assunto}\nTópicos: {topicos}\n"

    yield "Buscando vídeos no YouTube...", gr.update(value=10)
    entradaYoutube = pesquisar_videos_youtube(solicitacao)

    # Motivação
    yield "Criando mensagem motivacional...", gr.update(value=30)
    agentMotivador = Agent(
        role='Motivador',
        goal='Escrever uma mensagem motivacional para o estudante.',
        backstory='Você é um coach motivacional com experiência em ajudar estudantes a manterem o foco.',
        llm=groqllm,
        verbose=True
    )
    taskMotivador = Task(
        description = (
            "Escreva uma mensagem motivacional para o estudante, formatada em Markdown.\n\n"
            "A mensagem deve conter:\n"
            "## Mensagem Motivacional 🎯\n\n"
            "- Um parágrafo inicial incentivando o estudante a seguir seus estudos.\n"
            "- Frases inspiradoras para manter o foco e a disciplina.\n"
            "- Um fechamento encorajador, reforçando a importância do esforço e da dedicação.\n\n"
            "O texto deve ser positivo, motivador e adequado para estudantes de ensino médio."
        ),
        agent=agentMotivador,
        expected_output='Mensagem motivacional em markdown.'
    )
    saidaMotivador = agentMotivador.execute_task(taskMotivador)

    # Guia de Estudos
    yield "Gerando guia de estudos...", gr.update(value=50)
    agentGuia = Agent(
        role="Especialista em Guia de Estudos",
        goal="Criar um guia de estudos estruturado, explicativo e didático sobre um determinado assunto.",
        backstory="Você é um especialista em educação, com experiência na criação de guias de estudo detalhados.",
        llm=groqllm,
        verbose=True
    )
    taskGuia = Task(
        description = (
            f"Crie um Guia de Estudos para {disciplina}, abordando {assunto} e os tópicos {topicos}. "
            "O guia deve seguir a seguinte estrutura e formatação:\n\n"
            "## Guia de Estudos: {disciplina}\n\n"
            "### Introdução\n"
            "- Texto introdutório justificado sobre o tema, destacando sua importância e contexto.\n\n"
            "### Conceitos Fundamentais\n"
            "- Explicação detalhada dos principais conceitos abordados, com exemplos práticos.\n"
            "- Utilize listas não ordenadas para estruturar os conceitos.\n\n"
            "### Aplicações Práticas\n"
            "- Explique como o tema se aplica no mundo real.\n"
            "- Utilize exemplos concretos e listas para organizar as aplicações.\n\n"
            "### Técnicas de Aprendizado e Dificuldades Comuns\n"
            "- Apresente métodos eficazes para aprender o tema.\n"
            "- Liste dificuldades comuns dos alunos e estratégias para superá-las.\n\n"
            "### Indicação de Materiais Gratuitos\n"
            "- Forneça sugestões de livros, vídeos e artigos gratuitos sobre o tema.\n"
            "- Apresente os materiais em formato de lista com títulos e links quando possível.\n\n"
            "O conteúdo deve ser didático, acessível para alunos do ensino médio e utilizar texto justificado sempre que possível."
        ),
        agent=agentGuia,
        expected_output='Guia de estudos em markdown'
    )
    saidaGuia = agentGuia.execute_task(taskGuia)

    # Plano de Estudos
    yield "Criando plano de estudos...", gr.update(value=70)
    agentPlano = Agent(
        role="Especialista em Plano de Estudos",
        goal="Criar um plano de estudos eficiente para que o aluno aprenda de maneira organizada.",
        backstory="Você é um planejador educacional especialista em cronogramas de estudo eficientes.",
        llm=groqllm2,
        verbose=True
    )
    taskPlano = Task(
        description = (
            f"Crie um Plano de Estudos para {disciplina}, cobrindo {assunto} e os tópicos {topicos}. "
            f"O aluno tem {horas} horas por dia e {dias} dias para estudar.\n\n"
            "O plano deve seguir esta estrutura e formatação:\n\n"
            "## Plano de Estudos: {disciplina}\n\n"
            "### Introdução\n"
            "- Apresentação do objetivo do plano de estudos.\n"
            "- Importância da organização para otimizar o aprendizado.\n\n"
            "### Distribuição Equilibrada dos Tópicos\n"
            "- Divisão dos conteúdos de forma proporcional ao tempo disponível.\n"
            "- Sugerir uma agenda diária/semanal equilibrada.\n\n"
            "### Técnicas Ativas de Aprendizado\n"
            "- Explicação de estratégias eficazes para o estudo, incluindo:\n"
            "  - Resumos\n"
            "  - Flashcards\n"
            "  - Mapas mentais\n"
            "  - Resolução de exercícios\n\n"
            "### Revisões Programadas\n"
            "- Definir períodos estratégicos para revisão de conteúdos.\n"
            "- Sugestão de técnicas como repetição espaçada e autoavaliação.\n\n"
            "### Monitoramento do Progresso\n"
            "- Métodos para acompanhar a evolução do estudo.\n"
            "- Uso de checklists ou aplicativos para organização.\n\n"
            "### Sugestões para Pausas e Evitar Sobrecarga Mental\n"
            "- Importância das pausas regulares para manter a produtividade.\n"
            "- Sugestão de técnicas como a Técnica Pomodoro.\n"
            "- Dicas para manter o bem-estar mental durante os estudos.\n\n"
            "O plano deve ser didático, bem estruturado e adaptável para alunos do ensino médio."
        ),
        agent=agentPlano,
        expected_output='Plano de estudos estruturado em markdown'
    )
    saidaPlano = agentPlano.execute_task(taskPlano)

    # Curadoria de Vídeos
    yield "Organizando vídeos do YouTube...", gr.update(value=90)
    agentYoutube = Agent(
        role='Especialista em Curadoria de Vídeos Educacionais',
        goal='Organizar e formatar vídeos educacionais encontrados no YouTube para aprendizado eficiente.',
        backstory='Você é um especialista em curadoria de materiais educacionais, com experiência na seleção de vídeos para ensino.',
        llm=groqllm2,
        verbose=True
    )
    taskYoutube = Task(
        description = (
            f"Lista do Youtube: {entradaYoutube} "
            "Você receberá uma lista de vídeos extraída da API do YouTube. Sua tarefa é classificar e organizar os vídeos "
            "por categorias, formatando-os em Markdown. As categorias devem ser baseadas no título do vídeo.\n\n"
            f"## Vídeos sobre {assunto}\n\n"
            "### Formato de saída\n"
            "- Para cada vídeo, a saída deve seguir o formato abaixo:\n"
            "  **[Título](URL)**\n\n  _Descrição_\n\n"
            "- Se um vídeo não tiver descrição, substituir por '(Sem descrição disponível)'.\n"
            "- Se houver mais de um vídeo, repetir a estrutura para cada um.\n"
            "- Certifique-se de que a formatação Markdown esteja correta e bem organizada."
            "Caso um dos videos seja esse: https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            "a saida deverá ser:"
            "- Caso a lista de vídeos não contenha resultados relevantes,"
            "pode haver a inserção automática de um vídeo genérico (exemplo:"
            "\url{https://www.youtube.com/watch?v=dQw4w9WgXcQ}), utilizado"
            "como marcador de ausência de vídeos sobre o tema buscado."
           " Nesses casos, a saída deve ser:"
            "##Não foram encontrados vídeos sobre o assunto"
        ),
        agent=agentYoutube,
        expected_output="Lista de vídeos organizados em Markdown."
    )
    saidaYoutube = agentYoutube.execute_task(taskYoutube)

    yield "Processo concluído!", gr.update(value=100)

    saidaCompleta = f"""
# 🎯 Motivação
{saidaMotivador}

---

# 📖 Guia de Estudos
{saidaGuia}

---

# 📅 Plano de Estudos
{saidaPlano}

---

# 🎥 Vídeos Educacionais
{saidaYoutube}
"""

    yield saidaCompleta, gr.update(value=100)

# Interface Gradio
with gr.Blocks() as demo:
    gr.Markdown("# 📚 Gerador de Material de Estudos")
    with gr.Row():
        with gr.Column():
            disciplina = gr.Textbox(label="Disciplina", value="Matemática")
            assunto = gr.Textbox(label="Assunto", value="Funções")
            topicos_str = gr.Textbox(label="Tópicos", value="Função quadrática, Função exponencial, Função logarítmica")
            horas = gr.Textbox(label="Tempo diário", value="2 horas")
            dias = gr.Textbox(label="Quantos dias", value="5 dias")
            gerar_button = gr.Button("Gerar Material")
            progress = gr.Slider(minimum=0, maximum=100, step=1, value=0, label="Progresso", interactive=False)
        with gr.Column():
            resultado = gr.Markdown(label="Material Completo (Markdown)")

    gerar_button.click(fn=executar_equipe_interface,
                       inputs=[disciplina, assunto, topicos_str, horas, dias],
                       outputs=[resultado, progress])

demo.launch()
