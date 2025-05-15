
# 🐧 PenguinMiner

Um bot simples de mineração automática para jogos como o **Club Penguin (Cave Mine)**.  
Simula movimentação, cliques aleatórios e pressionamento da tecla `D`, permitindo minerar automaticamente enquanto o jogo está aberto.

---

## 1. ✨ Funcionalidades

- Define a área de mineração com o mouse
- Anda aleatoriamente em 4 direções (↑ ↓ ← →)
- Evita cliques muito próximos ao anterior
- Pressiona a tecla `D` automaticamente (3x) após cada ciclo
- Mostra número de ações realizadas e tempo em execução no título da janela
- Liga/desliga com uma tecla personalizada (`J` por padrão)

---

## 2. 💻 Requisitos

- Python 3.7 ou superior
- Sistema Windows
- Resolução mínima recomendada: **1920x1080**
- O jogo precisa estar **em modo janela**

---

## 3. 🚀 Como Usar

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/PenguinMiner.git
   cd PenguinMiner
   ```

2. **(Opcional) Crie um ambiente virtual**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```bash
   pip install pyautogui keyboard
   ```

4. **Execute o script**
   ```bash
   python miner.py
   ```

5. **Siga as instruções no terminal**:
   - Mova o mouse até o **canto superior esquerdo** da área de mineração → aguarde 5 segundos
   - Depois até o **canto inferior direito** → aguarde 5 segundos
   - Pressione `J` para ligar/desligar o bot

---

## 4. ⚙️ Configuração (`config.json`)

Gerado automaticamente após a primeira execução:

```json
{
  "enabled": true,
  "key": "j",
  "coordinates": null
}
```

- `enabled`: define se o bot começa ligado
- `key`: tecla usada para ativar/desativar o bot
- `coordinates`: área de mineração clicável. Será definida na primeira execução

---

## 5. ⚠️ Aviso Legal

> Este projeto é apenas para fins **educacionais**.  
> O uso de automações em jogos pode violar os termos de serviço da plataforma.  
> **Use por sua conta e risco.**

---

## 6. 📝 Licença

Distribuído sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
