import os

# Configuração
pasta_dos_blocos = r"C:\Users\curad\OneDrive\Área de Trabalho\musica\played_musics\played_musics"  # Altere para o caminho correto
musicas_a_procurar = [
    "Joga Pra Lua",
    "Paradinha",
    "rap da felicidade",
    "Trem das Onze",
    "Oyá",
    "Esperanças Perdidas",
    "Amor de Pai",
    "Vai Doer",
    # Adicione mais músicas aqui
]

arquivo_historico = "historico_busca.txt"

# Função para verificar músicas em um arquivo
def verificar_musicas(arquivo, musicas):
    musicas_encontradas = []
    with open(arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read().lower()
        for musica in musicas:
            if musica.lower() in conteudo:
                musicas_encontradas.append(musica)  # Adiciona a música encontrada na lista
    return musicas_encontradas

# Função para salvar o histórico da busca
def salvar_historico(resultados_gerais):
    with open(arquivo_historico, "a", encoding="utf-8") as f:
        for arquivo, musicas_encontradas in resultados_gerais.items():
            if musicas_encontradas:
                f.write(f"Arquivo: {arquivo} - Encontradas: {', '.join(musicas_encontradas)}\n")
                print(f"Arquivo: {arquivo} - Músicas encontradas: {', '.join(musicas_encontradas)}")
            else:
                f.write(f"Arquivo: {arquivo} - Não encontrada\n")
                print(f"Arquivo: {arquivo} - Não encontrada")

# Processar todos os arquivos na pasta
arquivos_processados = 0
resultados_gerais = {}

for nome_arquivo in os.listdir(pasta_dos_blocos):
    caminho_arquivo = os.path.join(pasta_dos_blocos, nome_arquivo)
    if os.path.isfile(caminho_arquivo) and nome_arquivo.endswith(".log"):  # Alterar para arquivos .log
        arquivos_processados += 1
        musicas_encontradas = verificar_musicas(caminho_arquivo, musicas_a_procurar)
        resultados_gerais[nome_arquivo] = musicas_encontradas

# Salvar o histórico da busca
if arquivos_processados == 0:
    print("Nenhum arquivo .log foi encontrado na pasta.")
    with open(arquivo_historico, "a", encoding="utf-8") as f:
        f.write("Nenhum arquivo .log foi encontrado na pasta.\n")
else:
    salvar_historico(resultados_gerais)
    print(f"O histórico da busca foi salvo em '{arquivo_historico}'.")