## 🧾 Descrição do Script

Este script automatiza o preenchimento de um formulário online no Microsoft Forms com dados de placas de veículos extraídos de um arquivo Excel (`placas.xlsx`).

### 🔧 Funcionalidades

- **Leitura de dados**: Utiliza a biblioteca `pandas` para ler uma lista de placas da primeira coluna de um arquivo Excel.
- **Abertura do formulário**: Abre automaticamente o link do Microsoft Forms em um navegador.
- **Automação do preenchimento**: Usa `pyautogui` e `pyperclip` para simular ações do teclado, colando e enviando cada placa no campo apropriado do formulário.
- **Controle de tempo**: Utiliza `time.sleep()` para garantir que as ações ocorram no tempo certo, respeitando o carregamento da página e o ritmo da interface.

### 📌 Observações

- O layout do formulário deve estar exatamente como esperado (número de TABs, posição dos campos etc.).
- O navegador padrão será utilizado para abrir o formulário.
- Não utilize o computador durante a execução, pois o `pyautogui` simula ações diretamente na interface gráfica.
- Certifique-se de que o arquivo `placas.xlsx` esteja na mesma pasta do script e contenha as placas na **primeira coluna**.
- **Dependências**:
  - `pandas`
  - `pyautogui`
  - `pyperclip`
  - `openpyxl` (para leitura do arquivo `.xlsx`)

### ▶️ Execução

Para executar o script:

```bash
pip install pandas pyautogui pyperclip openpyxl
python nome_do_script.py
