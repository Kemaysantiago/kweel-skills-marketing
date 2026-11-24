---
name: followup-crm-clinica
description: Use ao montar ou revisar a régua de follow-up de leads e pacientes de uma clínica (WhatsApp, ligação, CRM ou planilha), escrever roteiros de atendimento e mensagens de recuperação, confirmação, no-show e recall. Inclui etapas do funil, prazos, scripts e os campos que o CRM precisa ter.
---

# Régua de follow-up para clínicas — método Kweel

A mídia traz o lead. Quem transforma lead em paciente é o atendimento. Na maioria das clínicas, o maior vazamento não está no anúncio: está no **lead que ninguém respondeu a tempo** e no **paciente que ninguém chamou de volta**.

Esta skill monta a régua inteira, do primeiro contato ao recall.

---

## Antes de escrever qualquer mensagem, levante

1. **Canal principal:** WhatsApp (app comum, Business ou API oficial), telefone, formulário, agendamento online.
2. **Quem atende** e em que horário. Existe atendimento fora do horário comercial?
3. **Onde o lead fica registrado:** CRM, sistema da clínica, planilha. Se não fica em lugar nenhum, comece por aí.
4. **Ticket e ciclo:** consulta simples (decide em minutos) ou procedimento caro (decide em semanas).
5. **Regras do conselho profissional** sobre comunicação com paciente e divulgação de preço.

---

## Etapas do funil e o que cada uma exige

| Etapa | Entra quando | Sai quando | Prazo máximo parado |
|---|---|---|---|
| **Novo** | Lead chegou | Primeira resposta enviada | 5 min (horário comercial) |
| **Em conversa** | Respondeu | Agendou, ou esfriou | 24 h sem retorno → régua de recuperação |
| **Agendado** | Data marcada | Compareceu ou faltou | — |
| **Compareceu** | Atendido | Fechou tratamento, ou não | 48 h para o pós-consulta |
| **Faltou (no-show)** | Não veio | Reagendou, ou perdido | 2 h para o primeiro contato |
| **Em tratamento / paciente** | Fechou | — | Recall conforme o protocolo |
| **Perdido** | Desistiu ou sumiu | Reativado | Reativação em 60–90 dias |

Todo lead parado além do prazo é alerta. Se o CRM permite, crie a tarefa automática.

---

## Campos que o CRM (ou a planilha) precisa ter

| Campo | Por quê |
|---|---|
| Data e hora de entrada | Mede tempo de resposta |
| **Origem** (Google, Meta, Instagram orgânico, indicação, site, já é paciente) | Sem isso não existe CPL Real nem custo por paciente |
| Campanha / UTM | Liga o paciente ao anúncio |
| Interesse (procedimento ou especialidade) | Segmenta a régua e o remarketing |
| Etapa | O funil acima |
| Próximo contato (data) | Ninguém fica esquecido |
| Motivo de perda | Ex.: preço, convênio, distância, horário, sem resposta |
| Paciente novo × da casa | Separa o que a mídia trouxe do que já era da clínica |

Use **listas suspensas** para origem, interesse, etapa e motivo de perda. Texto livre não vira relatório.

---

## Roteiro do primeiro contato

O objetivo da primeira resposta é **uma pergunta fácil de responder**, não um bloco de texto.

```
Oi, [nome]! Aqui é a [atendente], da [clínica]. 😊
Vi que você se interessou por [procedimento/consulta].
Você prefere atendimento de manhã ou à tarde?
```

E, em algum momento da conversa, sempre:

```
Só pra gente melhorar aqui: como você conheceu a [clínica]?
```

A resposta vai para o campo **Origem**. Esta pergunta, feita em toda conversa e ligação, é o que permite medir a mídia de verdade.

### Ligação

1. Atender com o nome da clínica e o seu.
2. Entender o que a pessoa busca antes de falar de agenda.
3. Oferecer **dois horários** concretos, não "quando você pode?".
4. Perguntar como conheceu a clínica.
5. Registrar no CRM antes de desligar o telefone ou atender a próxima ligação.

---

## Régua de recuperação (lead que parou de responder)

| Quando | Mensagem |
|---|---|
| +2 h | "Conseguiu ver os horários, [nome]? Se ficar mais fácil, me diz o melhor dia que eu procuro pra você." |
| +1 dia | Responder a dúvida mais comum daquele procedimento em 2 linhas + "Quer que eu reserve um horário?" |
| +3 dias | Prova social curta: "Essa semana atendemos [n] pacientes com [queixa]." Use só número real. |
| +7 dias | Última tentativa, porta aberta: "Vou deixar seu contato aqui. Quando quiser retomar, é só me chamar." |

Depois da última mensagem → etapa **Perdido**, motivo "sem resposta". Pare. Insistência além disso queima a marca e o número.

---

## Confirmação e no-show

| Quando | Ação |
|---|---|
| Ao agendar | Confirmação com data, hora, endereço, link do mapa e o que levar |
| D-1 | "Confirmando seu horário amanhã às [hora]. Posso manter?" (pede resposta) |
| 2 h antes | Lembrete curto, com o link do mapa |
| Faltou, +2 h | "Sentimos sua falta hoje! Aconteceu alguma coisa? Consigo te encaixar em [dois horários]." |
| Faltou, +3 dias | Segunda tentativa de reagendar; depois → Perdido, motivo "no-show" |

Meça a **taxa de comparecimento**. Abaixo de ~75%, a confirmação D-1 não está funcionando ou não está sendo feita.

---

## Pós-consulta e recall

| Quando | Ação |
|---|---|
| D+1 | "Como você está depois da consulta? Ficou alguma dúvida?" |
| D+1 (quem não fechou tratamento) | Retomar a proposta com uma pergunta: "Ficou alguma dúvida sobre o plano de tratamento?" |
| Conforme protocolo | Recall de retorno (ex.: 15 dias, 30 dias, 6 meses, anual), definido **pelo profissional**, não pelo marketing |
| Avaliação | Pedido de avaliação no Google para paciente satisfeito, depois do pós-consulta |

---

## Reativação de perdidos (60–90 dias)

Segmente pelo **motivo de perda** e mande algo que responda a esse motivo:

- **Preço** → condição de pagamento, avaliação inicial
- **Horário** → horário novo, sábado, novo profissional
- **Distância** → nova unidade, teleconsulta, se aplicável
- **Sem resposta** → conteúdo útil sobre a queixa, sem pressão

Uma mensagem por ciclo de reativação. Quem pedir para não receber sai da lista na hora.

---

## Regras que não se quebram

- **WhatsApp API oficial:** fora da janela de 24 h desde a última mensagem do paciente, só é possível enviar **template aprovado**. Escreva os templates da régua já pensando nisso.
- **LGPD:** dado de saúde é dado sensível. Não peça diagnóstico por mensagem sem necessidade, não exponha a condição do paciente em grupo ou lista, e respeite o pedido de descadastro.
- **Sem promessa de resultado** e sem linguagem que crie urgência falsa ("só hoje") quando não for verdade.
- **Preço por mensagem** depende da política da clínica e das normas do conselho. Pergunte antes.
- **Toda mensagem tem que soar como gente da clínica.** Tom, emoji e tratamento (você/senhor) seguem o padrão do atendimento, não o do marketing.

---

## Entrega

1. **Mapa da régua:** etapas, prazos e responsável por cada passo.
2. **Biblioteca de mensagens:** cada mensagem com nome, etapa, gatilho e versão de template (para API).
3. **Configuração do CRM ou planilha:** campos, listas suspensas e alertas de prazo.
4. **Indicadores para acompanhar toda semana:** tempo médio de primeira resposta, taxa conversa → agendamento, taxa de comparecimento, taxa de fechamento e pacientes novos por origem.

Achado de processo da clínica (ex.: "ninguém responde depois das 18h") vai para o card interno e vira **pergunta de validação** no material do cliente, não acusação.
