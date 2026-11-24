---
name: relatorio-quinzenal-kweel
description: Use para montar o relatório de resultados de um cliente (quinzenal, mensal ou de call) no padrão visual e de comunicação da Agência Kweel, em PDF. Cobre a apuração dos números, a separação entre resultado de mídia e o que já era da casa, o tom com o cliente e o layout.
---

# Relatório de resultados para o cliente — padrão Kweel

O relatório não serve para mostrar trabalho. Serve para o cliente sair da leitura sabendo **três coisas**: quanto entrou, o que mudou e o que vem agora.

Esta skill é a versão **para o cliente**. A leitura técnica interna (o que foi feito, o que deu errado, hipóteses) fica no card do Trello e não entra aqui.

---

## Passo 1 — Apurar os números

Para o período e para o período anterior de mesmo tamanho:

| Métrica | Fonte |
|---|---|
| Investimento por plataforma | Google Ads, Meta Ads (gasto real, não orçamento) |
| Resultados por plataforma | Conversões principais de cada conta |
| Leads reais | CRM ou planilha de controle da clínica |
| Agendamentos e comparecimentos | Sistema da clínica |
| **Pacientes novos × da casa** | Sistema da clínica ou campo de origem do CRM |

KPIs que vão para o documento:

- **CPL Real** = investimento total ÷ leads reais (conversas Meta + agendamentos/leads Google, deduplicados)
- **Custo por agendamento** e, se houver o dado, **custo por paciente novo**
- Variação contra o período anterior, em % e em número absoluto

### Regra de atribuição (obrigatória)

Antes de atribuir qualquer ganho à campanha, **separe o que já era da casa**: retorno de paciente, busca pelo nome da clínica que existiria sem anúncio, indicação. Se não for possível separar, diga no documento que o número inclui pacientes da casa.

### Regras de honestidade

- Amostra pequena (menos de ~30 conversões) não sustenta conclusão por recorte. Mostre o número e não tire lição dele.
- Período de reaprendizado depois de mudança grande de lance ou de meta piora antes de melhorar. Avise antes de o cliente perguntar.
- Sazonalidade: compare com o mesmo período do ano anterior quando houver dado.

---

## Passo 2 — Escrever no tom certo

1. **Não reenfatize o negativo.** O que piorou entra como **frente de otimização**, com a ação correspondente.
2. **Soluções aparecem como implementadas.** "Reestruturamos os grupos de anúncios por especialidade", não "precisamos reestruturar".
3. **Pergunte antes de afirmar.** Quando um dado depende da operação da clínica (atendimento, agenda, preço), traga o dado e uma **pergunta de validação**, não a conclusão cravada.
   - ❌ "A recepção não está respondendo os leads."
   - ✅ "Das 120 conversas iniciadas, 31 viraram agendamento (26%). Hoje, em quanto tempo a equipe costuma responder no WhatsApp?"
4. **Sem jargão sem tradução.** "CPL Real" sempre com a definição na primeira vez.
5. **Fora do documento:** achado técnico, erro de configuração interno, pendência da agência, hipótese não confirmada. Isso vai para o Trello.

---

## Passo 3 — Estrutura do documento

1. **Capa:** logo da Kweel (pena), nome do cliente em roxo e caixa-alta, "Resultados & Estratégia", período em itálico.
2. **Caixa "Este documento consolida:"** com 3 a 5 itens do que o leitor vai encontrar.
3. **Resumo executivo:** 4 cards de KPI (fundo bege) e 3 a 5 frases que respondem "como foi o período".
4. **Seções numeradas:**
   1. Resultados do período (tabela por plataforma)
   2. Origem dos pacientes (mídia × casa)
   3. Frentes de otimização (o que foi implementado e o efeito esperado)
   4. Próximos passos (com data e responsável)
   5. Perguntas de validação (para a call)
5. **Cabeçalho de página:** `CLIENTE | RESULTADOS & ESTRATÉGIA | CONFIDENCIAL KWEEL`
6. **Rodapé:** `Agência Kweel · <e-mail> · Pág. N`

### Identidade visual

| Uso | Cor |
|---|---|
| Texto principal | `#2d2d2d` |
| Destaque, títulos, nome do cliente | `#8a6d9e` (roxo) |
| Cabeçalho de tabela | roxo escuro `#5e4a6e` |
| Cards de KPI, caixas | `#f5f1e6` (bege) |

---

## Passo 4 — Gerar o PDF

O modelo pronto está em `assets/modelo-relatorio.html`, com dados fictícios para referência. Copie, substitua o conteúdo e o caminho do logo, e gere o PDF:

```bash
# Chromium/Chrome headless
chromium --headless --no-pdf-header-footer --print-to-pdf=relatorio.pdf modelo-relatorio.html

# ou Playwright (Python)
python3 scripts/gerar_pdf.py modelo-relatorio.html relatorio.pdf "CLIENTE" "contato@agencia.com.br"
```

O script `scripts/gerar_pdf.py` aplica o cabeçalho e o rodapé com o número de página em todas as páginas, exceto a capa.

Depois de gerar, **abra o PDF e confira** página por página: quebra de tabela no meio, card cortado, número com casa decimal errada, nome do cliente com grafia certa.

---

## Checklist final

- [ ] Todo número confere com a fonte (planilha, conta de anúncios, sistema da clínica)
- [ ] Período anterior comparável (mesmo número de dias, mesmo objetivo de otimização)
- [ ] Pacientes da casa separados ou sinalizados
- [ ] Nenhum achado técnico interno no documento
- [ ] Toda frente de otimização tem ação e efeito esperado
- [ ] Perguntas de validação no fim
- [ ] Nome do cliente e período corretos na capa e no cabeçalho
