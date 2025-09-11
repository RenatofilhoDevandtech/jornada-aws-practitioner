import json
import os

def juntar_quizzes():
    pasta = 'docs/quizzes'  # pasta onde ficam os JSONs modulares
    quizzes = {}

    # Procura apenas arquivos JSON na pasta
    for arquivo in os.listdir(pasta):
        if arquivo.endswith('.json'):
            caminho = os.path.join(pasta, arquivo)
            with open(caminho, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                quizzes.update(dados)

    # Cria o JSON final para o mkdocs_quiz
    with open('quizzes.json', 'w', encoding='utf-8') as out:
        json.dump({"quizzes": quizzes}, out, ensure_ascii=False, indent=2)

    print("Arquivo quizzes.json gerado com sucesso!")

if __name__ == '__main__':
    juntar_quizzes()
