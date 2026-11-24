---
name: auditoria-meta-clinica
description: Use ao assumir, diagnosticar ou revisar uma conta de Meta Ads (Facebook/Instagram) de clínica de saúde, estética ou odontologia. Audita rastreamento, estrutura, públicos, criativos, políticas de saúde e o caminho conversa → agendamento, e entrega um diagnóstico priorizado.
---

# Auditoria de conta Meta Ads para clínicas — método Kweel

Clínica não vende clique nem conversa. Vende **paciente que senta na cadeira**. A auditoria responde a uma pergunta só:

> **Quanto custa um paciente novo vindo do Meta, e o que está impedindo esse número de cair?**

Tudo que não ajuda a responder isso é detalhe.

---

## Passo 0 — Antes de abrir qualquer métrica

- [ ] Acesso de **administrador** à conta de anúncios, ao Business Manager e à página/Instagram. Sem admin, metade dos itens abaixo fica invisível.
- [ ] Filtro de status em **Todas** nas três camadas: campanhas, conjuntos e anúncios. Pausado também conta história.
- [ ] Rodar em **duas janelas**: últimos 30 dias e últimos 90 (ou "máximo"). Janela curta esconde o que funcionou e foi desligado.
- [ ] Janela de atribuição registrada: a padrão é 7 dias após o clique + 1 dia após visualização. Anote se alguém mudou.
- [ ] Moeda e fuso da conta. Fuso errado desloca a conversão de dia.

---

## Passo 1 — Rastreamento (o resto não vale nada se isso estiver errado)

| Item | O que verificar | Sinal de problema |
|---|---|---|
| Dataset / Pixel | Um único pixel por site, instalado (de preferência via GTM) | Dois pixels disparando, ou pixel de agência antiga |
| API de Conversões | CAPI ativa, com qualidade de correspondência ≥ 6 | Só navegador; correspondência baixa |
| Domínio | Verificado no Business Manager | Não verificado = eventos limitados |
| Eventos | `Contact` (clique no WhatsApp), `Lead` (formulário), `Schedule` (agendamento concluído) | Otimização em `PageView` ou em evento que dispara duas vezes |
| Conversa no WhatsApp | Campanha de mensagens conta "conversas iniciadas" — isso **não** é agendamento | Conta reportando conversa como resultado final |
| Retorno da conversão real | Agendamento/comparecimento volta para o Meta (conversão offline ou CRM) | Nenhum sinal de paciente real volta para a plataforma |

**Teste prático obrigatório:** clique num anúncio ativo, percorra o caminho até o fim (WhatsApp ou agendamento) e confira no Gerenciador de Eventos se o evento chegou, uma vez só, com os parâmetros certos.

---

## Passo 2 — Do resultado da plataforma ao paciente

Monte esta escada com números reais do período:

```
Investimento                          R$ ____
Resultados reportados pelo Meta        ____   (conversas / leads)
Leads que viraram contato no CRM       ____
Agendamentos                           ____
Comparecimentos                        ____
Pacientes NOVOS (excluir retorno)      ____
```

E calcule:

- **CPL plataforma** = investimento ÷ resultados do Meta
- **CPL Real** = investimento ÷ leads que de fato entraram no atendimento
- **Custo por agendamento** e **custo por paciente novo**
- **Taxa conversa → agendamento.** Em clínica bem atendida, fica tipicamente entre 20% e 40%. Abaixo de 15%, o gargalo é atendimento, não mídia.

**Regra de honestidade:** paciente que já é da casa (retorno, procedimento recorrente) **não** é mérito da campanha. Separe antes de atribuir qualquer ganho.

Se a clínica não tem esses números, a primeira recomendação da auditoria é criar o controle (planilha ou CRM com a origem de cada lead). Sem isso, toda otimização é chute.

---

## Passo 3 — Estrutura

- **Objetivo da campanha** bate com o que a clínica mede? Mensagens → conversas; Leads → formulário; Vendas/Conversões → `Schedule` ou `Lead` no site.
- **Quantidade de conjuntos** coerente com a verba. Regra prática: cada conjunto precisa de ~50 eventos de otimização por semana para sair do aprendizado. Verba pequena dividida em muitos conjuntos = tudo em "Aprendizado limitado".
- **CBO × ABO:** CBO para escalar o que já é validado; ABO para testar público ou oferta com verba controlada.
- **Sobreposição de públicos** entre conjuntos da mesma campanha (ferramenta de sobreposição de públicos).
- **Geografia:** raio coerente com o deslocamento real do paciente. Clínica de bairro com raio de 40 km paga por quem nunca vai aparecer. Exclua áreas que a clínica não atende.
- **Idade e gênero** compatíveis com o procedimento. Mas atenção: em público amplo, o algoritmo costuma achar melhor que a segmentação manual. Restrinja só o que é regra de negócio.
- **Posicionamentos:** Advantage+ em geral; olhe se Audience Network está consumindo verba com CTR anormal (clique acidental).
- **Nomenclatura** no padrão da agência (ver skill `nomenclatura-campanhas-kweel`).

---

## Passo 4 — Públicos

- Lista de pacientes subida como **público personalizado** (para excluir de aquisição e para criar semelhante).
- **Remarketing** de quem visitou o site ou interagiu com o perfil nos últimos 30–90 dias.
- **Exclusões:** pacientes atuais fora das campanhas de aquisição; quem já converteu fora do remarketing de conversão.
- Públicos com menos de ~1.000 pessoas não entregam de forma estável.

---

## Passo 5 — Criativos

Abra os anúncios com mais gasto nos 90 dias e meça:

| Métrica | Leitura |
|---|---|
| Frequência (7 dias) | Acima de ~3 em público frio com CTR caindo = fadiga |
| CTR no link | Compare com o histórico da própria conta, não com média de mercado |
| Taxa de retenção de 3s (vídeo) | Gancho fraco se a maioria sai antes |
| Custo por resultado por anúncio | Verba concentrada em 1 anúncio que piora = risco |

**Diversidade:** a conta tem ângulos diferentes ou cinco versões da mesma arte? O mínimo saudável são três ângulos rodando: **autoridade** (profissional, estrutura, tempo de casa), **prova** (depoimento autorizado, número de pacientes) e **dúvida resolvida** (o que é, como funciona, quanto tempo leva).

**Rosto do profissional** costuma performar melhor em saúde do que arte de banco de imagem. Verifique se existe material assim e se está sendo usado.

---

## Passo 6 — Políticas de saúde (risco de bloqueio)

Conta de clínica bloqueada custa semanas. Verifique em todos os anúncios ativos:

- **Atributos pessoais (Meta):** o texto não pode afirmar ou insinuar que a pessoa tem uma condição. ❌ "Você sofre com rinite?" · ✅ "Rinite tem tratamento. Conheça as opções."
- **Antes e depois / imagem corporal:** a Meta restringe imagens que gerem percepção negativa do corpo; procedimento estético é o caso mais comum de reprovação.
- **Promessa de resultado** e garantia de cura: proibidas pela Meta e pelos conselhos profissionais.
- **Normas do conselho da profissão** (CFM, CFO, CRF, conselhos de biomedicina e estética): confira as regras vigentes de publicidade antes de aprovar preço em anúncio, depoimento, antes/depois ou selfie de procedimento. Elas mudam; não confie em memória.
- **Histórico da conta:** reprovações recentes, restrições de pagamento, qualidade da conta (Account Quality). Muitas reprovações em sequência aumentam o risco de restrição da conta inteira.
- **Segurança:** administradores do BM, autenticação em dois fatores, administradores antigos (ex-funcionários, agência anterior).

---

## Passo 7 — Do clique ao atendimento

Faça o caminho como paciente:

1. O anúncio leva para onde promete?
2. Se for WhatsApp: a mensagem pré-preenchida identifica a origem? Quanto tempo a clínica leva para responder? (Teste em horário comercial e fora dele.)
3. Se for site: carrega em menos de 3s no celular? O botão de agendar aparece sem rolar?
4. O atendimento pergunta "como nos conheceu" e registra?

Tempo de resposta acima de 15 minutos derruba a conversão de forma relevante. Esse achado vale mais do que qualquer ajuste de lance.

---

## Passo 8 — Diagnóstico e prioridade

Classifique cada achado:

| Prioridade | Critério |
|---|---|
| 🔴 Agora | Rastreamento quebrado, risco de bloqueio, verba indo para lugar errado |
| 🟠 Esta semana | Estrutura que impede o aprendizado, criativo em fadiga, público sobreposto |
| 🟢 Próximo ciclo | Testes novos, expansão de público, novos ângulos |

Para cada item: **o que é, evidência (número), ação, efeito esperado e como medir**. Item sem efeito esperado não é auditável.

---

## Entrega

**Para o time (Trello):** o diagnóstico completo, com os números, os achados técnicos e as pendências internas.

**Para o cliente:** não reenfatize o negativo. Enquadre os achados como **frentes de otimização**, traga as soluções já aplicadas como implementadas, e mande as **perguntas de validação** em vez de conclusões cravadas. Exemplo: "Notamos que 40% das conversas não viram agendamento. Hoje, quem responde o WhatsApp e em quanto tempo?" Documento de cliente segue o padrão da skill `relatorio-quinzenal-kweel`.

---

## Armadilhas

- **Conversa não é paciente.** Campanha de mensagens otimiza para gente que inicia conversa, não para quem agenda. Se o CRM mostra conversão baixa, mude o sinal de otimização antes de mudar o criativo.
- **Mexer em tudo de uma vez.** Cada edição relevante (orçamento > ~20%, público, evento de otimização) reinicia o aprendizado. Uma alavanca por vez, registrada com data.
- **Comparar períodos com objetivo diferente.** Se a otimização mudou de conversa para agendamento, os números de antes e depois não são comparáveis.
- **Atribuir sazonalidade à campanha.** Inverno em alergia, verão em estética, dezembro fraco para eletiva: compare com o mesmo período do ano anterior antes de concluir.
