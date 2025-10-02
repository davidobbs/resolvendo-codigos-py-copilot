# Resolvendo Codigos em Python com GitHub Copilot

Projeto pratico inspirado no desafio da DIO para exercitar resolucao de algoritmos em Python com apoio de IA. A proposta combina GitHub Copilot (ou outra IA generativa) e GitHub Codespaces para mostrar como acelerar iteracoes de codigo, testes e documentacao.

## Objetivos do desafio
- Reproduzir e aprimorar solucoes de algoritmos baseadas no conteudo das aulas.
- Praticar fluxo de trabalho com GitHub (fork, commits, README claro).
- Utilizar Copilot para propor trechos de codigo, validar alternativas e revisar erros.
- Registrar as decisoes tecnicas e aprendizados de maneira organizada.

## Conteudo do repositorio
- `main.py`: ponto de entrada simples que expande um menu interativo no terminal.
- `resolucoes_code/`: modulos com funcoes puras e helpers interativos para cada exercicio.
- `tests/`: verificacoes automatizadas usando `pytest`.
- `requirements-dev.txt`: dependencias opcionais para rodar os testes localmente.

### Estrutura de pastas
```
resolvendo-codigos-py-copilot/
├── main.py
├── requirements-dev.txt
├── resolucoes_code/
│   ├── __init__.py
│   ├── cli.py
│   ├── concat_dados.py
│   ├── media_notas.py
│   ├── ope_mat.py
│   ├── palindromo.py
│   ├── paridade.py
│   └── repet_txt.py
└── tests/
    └── test_algorithms.py
```

### Detalhes dos algoritmos

#### palindromo.py
Verifica se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente).

**Funcionalidades:**
- `is_palindrome(text: str) -> bool`: Função principal que verifica se o texto é um palíndromo. Ignora maiúsculas, minúsculas, espaços e caracteres especiais.
- `_normalize_text(text: str) -> str`: Função auxiliar que normaliza o texto removendo caracteres não alfanuméricos e convertendo para minúsculas.
- `prompt_and_check() -> bool`: Função interativa que solicita entrada do usuário e exibe o resultado.

**Exemplos de palíndromos:**
- "arara" → É um palíndromo!
- "A base do teto desaba" → É um palíndromo!
- "python" → Não é um palíndromo.

**Execução:**
```bash
python -m resolucoes_code.palindromo
```

## Preparacao do ambiente local
1. Crie ou ative um ambiente virtual (recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # PowerShell: .venv\\Scripts\\Activate.ps1
   ```
2. Instale as dependencias de desenvolvimento caso deseje rodar os testes:
   ```bash
   pip install -r requirements-dev.txt
   ```

## Executando os algoritmos localmente
- Menu interativo completo:
  ```bash
  python main.py
  ```
- Voce tambem pode chamar modulos isolados:
  ```bash
  python -m resolucoes_code.concat_dados
  python -m resolucoes_code.repet_txt
  python -m resolucoes_code.ope_mat
  ```
  Cada modulo oferece prompts rapidos para praticar entradas e validar resultados.

## Rodando no GitHub Codespaces
1. Clique em **Code > Create codespace on main** (ou abra o fork no Codespaces).
2. Aguarde o container finalizar o build. O Python ja vem configurado na imagem padrao.
3. Ative o ambiente virtual (caso deseje) e instale `pytest` com o comando indicado acima.
4. Use o terminal integrado para executar `python main.py` ou rode arquivos individuais.
5. Aproveite a extensao do Copilot para gerar snippets, comentarios e testes automatizados.

## Como aproveitar o GitHub Copilot
- Gere funcoes intermediarias (ex.: validacao de entrada, formatacao de strings) a partir de comentarios descritivos.
- Solicite melhorias de legibilidade ou alternativas de algoritmo diretamente no editor.
- Use o chat para explicar erros, mensagens de excecao e sugerir testes adicionais.
- Compare versoes sugeridas com a sua solucao manual e registre o que mudou.

Se o acesso ao Copilot nao estiver disponivel, use qualquer outra IA (como o ChatGPT) para simular o fluxo colaborativo e anote as sugestoes aceitas ou rejeitadas no README ou nos commits.

## Testes automatizados
Execute os testes com `pytest`:
```bash
pytest
```
Caso `pytest` nao esteja instalado, utilize `pip install -r requirements-dev.txt` ou rode `python -m compileall resolucoes_code` para apenas validar sintaxe rapidamente.

## Documentando suas decisoes
- Registre no README (ou nos commits) o que foi gerado pela IA e o que voce ajustou manualmente.
- Mencione dificuldades enfrentadas e como foram resolvidas.
- Adicione capturas de tela ou snippets demonstrando a interacao com o Copilot/Codespaces, se julgar util.

## Ideias de extensao
- Criar uma interface web simples (Flask ou FastAPI) para expor os algoritmos.
- Adicionar novos desafios ao pacote, como calculadora de juros compostos ou validacao de CPF.
- Incluir testes de ponta a ponta usando `pytest` + `capfd` para validar as funcoes interativas.
- Configurar GitHub Actions para rodar lint e testes nos commits.

Bom estudo e bons commits!
