<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1135979458298388592/1162819453743018014/flirty_wink.png?ex=653d5301&is=652ade01&hm=3bf7ea29d60d75af5008c71ba8d3ac50263182e8e3015426b714a1b8115fee48" alt="Logo" width="200">
</p>

# Clear DM para Discord

Este é um simples bot que limpa suas mensagens no Discord, que permite limpar suas mensagens em canais de texto. O bot foi criado com a intenção de ajudar os usuários a gerenciar suas mensagens de forma mais eficaz.

## Pré-requisitos

Antes de executar o bot, você precisará das seguintes dependências:

- [Python](https://www.python.org/) (para executar o bot)
- [Discord.py](https://github.com/Rapptz/discord.py) (biblioteca para interagir com a API do Discord)
- [Colorama](https://pypi.org/project/colorama/) (para melhorar a saída de cores no terminal)

## Configuração

1. Clone ou faça o download deste repositório em sua máquina.

2. Instale as dependências usando o pip:
   ```bash
   pip install discord.py colorama
3. Execute o bot
   ```bash
   python bot.py
4. O bot solicitará que você insira sua token do Discord. Cole a token no terminal usando o botão direito do mouse.
5. O bot será iniciado e estará pronto para uso.

# Uso

O bot permite limpar mensagens em canais de texto com comandos simples.

Use o comando bye para limpar as últimas 30 mensagens no canal atual.

Use o comando byedm para limpar todas as mensagens do canal atual (limite de 9999 mensagens).

Use o comando byeeveryone para limpar todas as mensagens diretas (DMs) com você.   

# Configuração para Evitar Banimento e Rate Limit
A pasta lib contém um código chamado data que é uma configuração para evitar que sua conta Discord seja banida ou sujeita a rate limiting.

