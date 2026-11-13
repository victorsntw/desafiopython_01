# 🔐 Desafio de Aprendizado: Login com 3 Tentativas

## 📖 Sobre o Projeto

Este projeto foi desenvolvido como parte de uma **jornada de aprendizado em Python**, com o objetivo de consolidar conceitos fundamentais de **estrutura de repetição (`while`)**, **condicionais (`if/elif/else`)**, **contadores** e **controle de fluxo com `break`**.

O programa simula um sistema simples de autenticação, onde o usuário possui **3 tentativas** para digitar a senha correta antes de ter a conta bloqueada.

---

## 🎯 Objetivo do Desafio

Praticar e fixar os seguintes conceitos:

- ✅ Laços de repetição com condição de parada (`while`)
- ✅ Uso de **contadores** para controlar o número de tentativas
- ✅ Estruturas condicionais encadeadas (`if / elif / else`)
- ✅ Interrupção controlada de loops com `break`
- ✅ Tratamento de entradas com `.strip()` para evitar falhas por espaços

---

## 🧩 Elementos do Código e Seus Objetivos

| Elemento | Objetivo Principal |
|---|---|
| `senha_correta = "python123"` | Armazena a senha válida que será usada como referência na comparação. |
| `tentativas = 0` | Inicializa o **contador** de tentativas em zero. |
| `while tentativas < 3:` | Cria um laço que se repete enquanto o usuário tiver tentativas disponíveis. |
| `input(...).strip()` | Captura a senha digitada pelo usuário e remove espaços em branco nas extremidades. |
| `tentativas += 1` | Incrementa o contador a cada tentativa, garantindo que o loop tenha fim. |
| `if senha == senha_correta:` | Verifica se a senha digitada é igual à senha correta. |
| `print("Acesso liberado!")` | Exibe mensagem de sucesso quando a senha está correta. |
| `break` | Interrompe imediatamente o loop, evitando tentativas desnecessárias. |
| `elif tentativas == 3:` | Identifica quando o usuário esgotou todas as tentativas. |
| `print("Tentativa de número 3, conta bloqueada!")` | Exibe mensagem de bloqueio ao atingir o limite de tentativas. |
| `else:` | Trata os casos intermediários (erros quando ainda há tentativas restantes). |
| `f"senha errada! tentativa {tentativas} de 3..."` | Usa **f-string** para exibir mensagens dinâmicas com o número da tentativa atual. |

---

## 💻 Como Executar

### Pré-requisitos
- Python 3.x instalado ([python.org](https://www.python.org/))

### Passos
```bash
# Salve o código em um arquivo, por exemplo: login.py
# Execute no terminal:
python login.py
```

---

## 🖥️ Exemplos de Execução

### ✅ Caso 1 — Senha correta na primeira tentativa
```
Digite aqui a sua senha: python123
Acesso liberado!
```

### ⚠️ Caso 2 — Erros seguidos de acerto
```
Digite aqui a sua senha: 123
senha errada! tentativa 1 de 3, tente novamente.
Digite aqui a sua senha: teste
senha errada! tentativa 2 de 3, tente novamente.
Digite aqui a sua senha: python123
Acesso liberado!
```

### ❌ Caso 3 — Conta bloqueada
```
Digite aqui a sua senha: abc
senha errada! tentativa 1 de 3, tente novamente.
Digite aqui a sua senha: xyz
senha errada! tentativa 2 de 3, tente novamente.
Digite aqui a sua senha: 12345
Tentativa de número 3, conta bloqueada!
```

---

## 📚 Conceitos Aprendidos

1. **Laço `while` com contador** — controle preciso do número de repetições.
2. **Interrupção com `break`** — saída antecipada e eficiente do loop.
3. **Condicionais encadeadas** — tomada de decisão baseada em múltiplos cenários.
4. **F-strings** — formatação moderna e legível de strings.
5. **Sanitização de entrada** — uso de `.strip()` para tornar o programa mais robusto.

---

## 👨‍💻 Autor

**Victor** — Estudante de Programação Python

## 📜 Licença

Projeto desenvolvido para fins educacionais. Livre para estudo e adaptação.
