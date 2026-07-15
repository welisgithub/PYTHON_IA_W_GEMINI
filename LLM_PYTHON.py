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

import google.generativeai as genai
from google.colab import userdata

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

import pandas as pd

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





from google.colab import userdata

GH_PAT = userdata.get('GH_PAT')

repo_url = !git remote get-url origin
repo_url = repo_url[0].strip()

git_username = !git config user.name
git_username = git_username[0].strip()

auth_repo_url = repo_url.replace('https://github.com', f'https://{git_username}:{GH_PAT}@github.com')




import nbformat
import os
import glob
from google.colab import userdata

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

    GH_PAT = userdata.get('GH_PAT')
    git_username = !git config user.name
    git_username = git_username[0].strip()
    repo_url = !git remote get-url origin
    repo_url = repo_url[0].strip()
    auth_repo_url = repo_url.replace('https://github.com', f'https://{git_username}:{GH_PAT}@github.com')




else:
    print("ERRO: Não foi possível identificar o arquivo .ipynb do notebook atual.")
    print("Isso pode acontecer se o notebook não está salvo no ambiente do Colab de forma padrão, ou se o nome foi alterado.")
    print("Por favor, certifique-se de que o notebook está salvo (por exemplo, no Google Drive) ou execute 'ls -R /' para verificar onde o arquivo '.ipynb' pode estar.")