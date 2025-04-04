# Automacao do Sistema Gestão de Transportes da Teorema Sistemas com Python e BotCity

## Descricao do Projeto
Este projeto automatiza o sistema **Gestão de Transportes** utilizando **Python** e **BotCity**, permitindo a execução de tarefas repetitivas de forma eficiente e sem necessidade de intervenção manual.

## Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada para desenvolvimento.
- **BotCity**: Framework de automação para aplicações desktop.

## Requisitos
Antes de rodar a automação, instale as dependências necessárias. Requisitos incluem:

- **Python 3.x** instalado
- Bibliotecas do BotCity e outras dependências

Para instalar as bibliotecas necessárias, execute:
```sh
pip install botcity-framework-core
```

## Guia para Rodar a Automacao do Gestão de Transportes da Teorema Sistemas

### Configuracoes Iniciais
A automação utiliza a base de dados RACOES SERTANEJA 0042362
Antes de rodar a automação, siga os passos abaixo:

1. **Entrar no sistema administrador**
   - Faça login com o usuário **Teorema** ou o usuário que for testar a automação.
   - Navegue para: `Usuário -> Localiza -> Editar -> Acesso`
   - Conceda **Acesso Mestre** e clique em **Gravar**.
   - Na aba **Empresas disponíveis para Acesso do Usuário**, mova todas para o lado direito.
   - Feche o sistema.

2. **Configuração no sistema Gestão Administrativa**
   - Abra o sistema **Gestão Administrativa**.
   - Faça login com o usuário que for testar a automação.
   - Navegue para: `Cadastros -> Documentações -> Tipo de Documentos -> Incluir`
   - Caso não haja documentos cadastrados, crie um documento com o nome `teste12!`.
   - Clique em **Salvar** e feche o sistema.

3. **Rodando a Automacao**
   - Abra o sistema **Gestão de Transportes** e deixe-o na tela inicial.
   - Agora a automação pode ser executada sem erros até a tela **Parâmetros Fiscais/Regionalização**.

## Como Executar
1. Clone este repositório:
   ```sh
   git clone https://github.com/ChristianKoziel/botcity-teorema-transportes.git
   ```
2. Acesse o diretório do projeto:
   ```sh
   cd automacaoTransporte
   ```
3. Execute o script principal:
   ```sh
   python bot.py
   ```

## Estrutura do Projeto
```
📂 automacaoTransporte
├── automacaoTransporte.botproj  # Arquivo de projeto do BotCity
├── automacaoTransporte.zip  # Arquivo compactado da automação
├── bot copy.py  # Cópia auxiliar do script principal
├── bot.py  # Arquivo principal da automação
├── build.bat  # Script de build para Windows
├── build.ps1  # Script de build para PowerShell
├── build.sh  # Script de build para Linux
├── README.md  # Documentação do projeto
├── requirements.txt  # Lista de dependências
├── resources/  # Diretório de recursos
└── teste.py  # Arquivo de testes
```

## Possiveis Erros e Solucoes
- **Erro de reconhecimento da interface:** Certifique-se de que as imagens utilizadas para deteccao estao corretas.
- **Execucao interrompida:** Verifique se o sistema alvo esta aberto antes de iniciar a automacao.

## Contato
Caso tenha duvidas ou sugestoes, entre em contato:
- 📧 Email: christiankoziel@hotmail.com

