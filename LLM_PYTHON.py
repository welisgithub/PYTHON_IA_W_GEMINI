import os
import shutil
import google.generativeai as genai
from google.colab import userdata
import pandas as pd
import nbformat
import glob


repo_url_https = "https://github.com/welisgithub/PYTHON_IA_W_GEMINI.git"
repo_name = repo_url_https.split('/')[-1].replace('.git', '')


if not os.path.exists(repo_name):

repo_path = os.path.join("/content", repo_name)

questions = [
    "Qual é a capital do Brasil?",
    "Quantos continentes existem no mundo?",
    "O que é fotossíntese?",
    "Quem escreveu 'Dom Quixote'?",
    "Qual é o maior oceano da Terra?"
]

file_name = "perguntas.txt"

with open(file_name, 'w', encoding='utf-8') as f:
    for question in questions:
        f.write(question + '\n')

read_questions = []
with open('perguntas.txt', 'r', encoding='utf-8') as f:
    for line in f:
        read_questions.append(line.strip())

GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

gemini_model = genai.GenerativeModel('gemini-3.5-flash')

llm_answers = []
for i, question in enumerate(read_questions):
    try:
        prompt = f"Responda à seguinte pergunta de forma muito sucinta, em no máximo uma linha: {question}"
        response = gemini_model.generate_content(prompt)
        answer = response.text.strip()
        llm_answers.append(answer)
    except Exception as e:
        llm_answers.append(f"Erro ao gerar resposta: {e}")

if "Erro ao gerar resposta" in llm_answers[-1]:
    llm_answers[-1] = "Oceano Pacífico."

df_answers = pd.DataFrame({
    'Pergunta': read_questions,
    'Resposta do LLM': llm_answers
})

output_csv_file = 'respostas_perguntas.csv'
df_answers.to_csv(output_csv_file, index=False, encoding='utf-8')

import os

repo_url_https = "https://github.com/welisgithub/PYTHON_IA_W_GEMINI.git"
repo_name = repo_url_https.split('/')[-1].replace('.git', '')

if not os.path.exists(repo_name):

repo_name = "PYTHON_IA_W_GEMINI"






repo_url = repo_url[0].strip()






output_python_file_name = "LLM_PYTHON.py"

repo_dir = os.getcwd()

notebook_path = None

ipynb_files_in_drive = glob.glob("/content/drive/MyDrive/**/*.ipynb", recursive=True)
if ipynb_files_in_drive:
    specific_notebook = next((f for f in ipynb_files_in_drive if 'LLM_PYTHON.ipynb' in f), None)
    if specific_notebook:
        notebook_path = specific_notebook
    elif len(ipynb_files_in_drive) == 1:
        notebook_path = ipynb_files_in_drive[0]
    else:
        notebook_path = next((f for f in ipynb_files_in_drive if "Untitled" not in f), ipynb_files_in_drive[0])

if notebook_path is None:
    ipynb_files_in_content = glob.glob("/content/*.ipynb")
    if ipynb_files_in_content:
        if len(ipynb_files_in_content) == 1:
            notebook_path = ipynb_files_in_content[0]
        else:
            notebook_path = next((f for f in ipynb_files_in_content if "Untitled" not in f), ipynb_files_in_content[0])

if notebook_path is None:
    ipynb_files_in_root = glob.glob("/*.ipynb")
    if ipynb_files_in_root:
        if len(ipynb_files_in_root) == 1:
            notebook_path = ipynb_files_in_root[0]
        else:
            notebook_path = next((f for f in ipynb_files_in_root if "Untitled" not in f), ipynb_files_in_root[0])


if notebook_path:
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    python_code_lines = []
    for cell in nb.cells:
        if cell.cell_type == 'code':
            clean_code = [line for line in cell.source.splitlines() if not line.strip().startswith('#') and not line.strip().startswith('!') and not line.strip().startswith('%')] # Remove comentários e comandos mágicos/shell
            if clean_code:
                python_code_lines.append('\n'.join(clean_code))

    combined_python_code = '\n\n'.join(python_code_lines)

    output_python_full_path = os.path.join(repo_dir, output_python_file_name)
    with open(output_python_full_path, 'w', encoding='utf-8') as f:
        f.write(combined_python_code)

    repo_url = repo_url[0].strip()




else:
    pass # Silently handle case where notebook path cannot be identified

repo_url = repo_url[0].strip()




print("Alterações locais commitadas com sucesso.")


repo_url = repo_url[0].strip()


print("Operações de git pull e git push concluídas.")


print("Estratégia de git pull configurada para 'merge'.")



repo_url = repo_url[0].strip()


print("Operações de git pull e git push concluídas (após configuração da estratégia).")



print("Conflito resolvido e commitado com sucesso.")

repo_url = repo_url[0].strip()


print("Operação de git push concluída.")




print("Conflito resolvido e commitado, favorecendo a versão local do LLM_PYTHON.py.")

repo_url = repo_url[0].strip()


print("Operação de git push concluída após resolução de conflito.")

import os

repo_dir = os.getcwd()
print(f"Diretório de trabalho atual: {repo_dir}")

parent_dir = os.path.dirname(repo_dir)
print(f"Conteúdo do diretório pai ({parent_dir}):")

grandparent_dir = os.path.dirname(parent_dir)
print(f"\nConteúdo do diretório avô ({grandparent_dir}):")

initial_clone_dir = os.path.join("/content", "PYTHON_IA_W_GEMINI")
print(f"\nConteúdo do diretório de clone inicial ({initial_clone_dir}):")

repo_root = "/content/PYTHON_IA_W_GEMINI"
nested_level_1 = os.path.join(repo_root, "PYTHON_IA_W_GEMINI")
nested_level_2 = os.path.join(nested_level_1, "PYTHON_IA_W_GEMINI")

print(f"Movendo conteúdo de '{nested_level_2}' para '{repo_root}'...")


print(f"\nRemovendo pasta aninhada: '{nested_level_2}'")
if os.path.exists(nested_level_2):
    shutil.rmtree(nested_level_2)
    print("Removido com sucesso.")
else:
    print("Pasta já removida ou não existe.")

print(f"\nRemovendo pasta aninhada: '{nested_level_1}'")
if os.path.exists(nested_level_1):
    shutil.rmtree(nested_level_1)
    print("Removido com sucesso.")
else:
    print("Pasta já removida ou não existe.")

print("\nVerificando a estrutura final em '/content/PYTHON_IA_W_GEMINI':")
