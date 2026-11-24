---
name: nomenclatura-campanhas-kweel
description: Use ao criar, renomear ou auditar campanhas, grupos/conjuntos e anúncios no Google Ads ou Meta Ads, e ao montar UTMs e modelos de rastreamento. Aplica o padrão de nomenclatura da Agência Kweel, que alimenta dashboards e o GA4.
---

# Nomenclatura de campanhas e rastreamento — padrão Kweel

O nome de uma campanha não é rótulo. É o dado que o dashboard, o GA4 e o CRM vão ler depois. Se o nome sai fora do padrão, o relatório quebra em silêncio.

Use esta skill **antes** de nomear qualquer coisa e **sempre** que for auditar uma conta herdada.

---

## As três camadas

| Camada | Modelo |
|---|---|
| Campanha | `[kweel][nome-da-campanha][etapa][tipo-de-campanha]` |
| Grupo / conjunto | `[cpc][tipo-de-campanha][etapa][tipo-de-publico][idade-persona-local][objetivo]` |
| Anúncio | `[objetivo][sobre-o-anuncio][cta][identificador]` |

### Regras de escrita

- Tudo em **minúsculas**, cada bloco entre colchetes, sem espaço entre blocos.
- Dentro do bloco, palavras separadas por **hífen**. Sem acento, sem cedilha, sem espaço.
- O primeiro bloco da campanha é sempre `[kweel]`: identifica que a campanha é gerida pela agência.
- O primeiro bloco do grupo é sempre `[cpc]`: identifica mídia paga no `utm_medium`.
- O identificador do anúncio tem dois dígitos: `[01]`, `[02]`…

---

## Vocabulário de cada bloco

**`[etapa]`** — etapa do funil
- `[topo]` público frio: interesse, engajamento, semelhante, pageview
- `[meio]` público morno: quem interagiu com o site, remarketing
- `[fundo]` público quente: já converteu, já é paciente, busca com intenção alta (ex.: "clínica + bairro")

**`[tipo-de-campanha]`**
`[pesquisa]` `[pmax]` `[display]` `[video]` `[conversao]` `[trafego]` `[engajamento]` `[whatsapp]` `[mensagens]` `[cadastro]`

**`[tipo-de-publico]`**

| Código | Significado |
|---|---|
| `[pi]` | Público de interesse (inclui palavra-chave de pesquisa) |
| `[pp]` | Público personalizado sem ser remarketing de site: engajou no perfil, viu vídeo, seguidores |
| `[ll]` | Lookalike / semelhante, criado a partir de PP ou RMKT |
| `[rmkt]` | Remarketing de site: visitou LP, clicou no WhatsApp, iniciou agendamento |
| `[lista]` | Lista de clientes/pacientes enviada (CRM) |
| `[adv]` | Público Advantage+ / segmentação ampla automática |

**`[idade-persona-local]`** — idade mínima-máxima, depois a persona ou o tema, depois a praça.
Exemplos: `[25-60-implante-rj]` · `[18-65-alergia-zona-norte]` · `[30-55-harmonizacao-barra]` · `[18-60-pgv30d-brasil]`

**`[objetivo]`** — o que conta como resultado
`[lead]` `[agendamento]` `[whatsapp]` `[ligacao]` `[venda]` `[cadastro]` `[posicionamento]`

**`[sobre-o-anuncio]`** — o ângulo do criativo, em 1 a 3 palavras: `[autoridade]` `[depoimento]` `[bastidor]` `[oferta-avaliacao]` `[sazonal-inverno]` `[duvida-frequente]`

**`[cta]`** — a chamada: `[agende-agora]` `[fale-no-whatsapp]` `[saiba-mais]` `[ultimas-vagas]`

---

## Exemplos completos

```
Campanha  [kweel][implante-dentario][fundo][pesquisa]
Grupo     [cpc][pesquisa][fundo][pi][30-65-implante-niteroi][agendamento]
Anúncio   [agendamento][autoridade][agende-agora][01]

Campanha  [kweel][harmonizacao][topo][mensagens]
Conjunto  [cpc][mensagens][topo][ll][28-50-harmonizacao-barra][whatsapp]
Anúncio   [whatsapp][depoimento][fale-no-whatsapp][03]
```

Campanha de marca: `[kweel][branding][fundo][pesquisa]`. O nome da clínica **não** entra no nome da campanha; o bloco `branding` já diz o que é.

---

## UTMs

| Parâmetro | Google Ads | Meta Ads |
|---|---|---|
| `utm_source` | `google` | `meta` |
| `utm_medium` | nome do grupo | `{{adset.name}}-{{placement}}` |
| `utm_campaign` | nome da campanha | `{{campaign.name}}` |
| `utm_content` | nome do anúncio | `{{ad.name}}` |

No Meta, use os parâmetros dinâmicos em **Parâmetros de URL** do anúncio. No Google, coloque a string em **Configurações da campanha → Opções de URL → Modelo de rastreamento ou Sufixo do URL final**. Nunca edite a URL final do anúncio para isso.

### Codificação automática do Google Ads: fica LIGADA

O manual antigo mandava desligar. A decisão atual é **ligar e somar UTM por cima**: a codificação automática gera o GCLID, e sem ele a conversão offline/WhatsApp não volta para o Google Ads. A UTM por cima mantém o dashboard recebendo o padrão.

### Exemplo de sufixo (Google)

```
utm_source=google&utm_medium=[cpc][pesquisa][fundo][pi][30-65-implante-niteroi][agendamento]&utm_campaign=[kweel][implante-dentario][fundo][pesquisa]&utm_content={adgroupid}-{creative}
```

Se a conta tem muitos anúncios, use `{creative}` (ID) no `utm_content` e cruze com o nome pelo relatório. O nome legível vem do grupo e da campanha.

---

## Fluxo

1. **Ler o que existe.** Liste campanhas, grupos e anúncios com status "Todas" (pausadas aparecem). Anote o que está fora do padrão.
2. **Gerar os nomes.** Use `scripts/nomear.py` para montar e validar:
   ```bash
   python3 scripts/nomear.py campanha implante-dentario fundo pesquisa
   python3 scripts/nomear.py grupo pesquisa fundo pi 30-65-implante-niteroi agendamento
   python3 scripts/nomear.py anuncio agendamento autoridade agende-agora 1
   python3 scripts/nomear.py validar "[kweel][Implante][fundo][pesquisa]"
   ```
3. **Renomear sem quebrar histórico.** Renomear não reseta aprendizado nem histórico em nenhuma das duas plataformas. Mas o GA4 e o dashboard vão mostrar o nome novo daqui para frente: registre a data da troca no card.
4. **Aplicar o rastreamento.** Sufixo/modelo no Google, parâmetros no Meta.
5. **Testar.** Clique no anúncio pela pré-visualização, confira a URL que chega na página, e veja o evento no GA4 em tempo real.
6. **Registrar no Trello.** Lista de nomes aplicados e a data.

---

## Armadilhas

- **Nome com acento ou espaço** vira `%C3%A7` e `%20` na UTM e o filtro do dashboard não pega. Normalize antes.
- **Conjunto do Meta com `[cpc]`** faltando: o `utm_medium` deixa de ser identificável como pago.
- **Nome bonito, URL sem UTM.** O nome só vira dado se a UTM estiver aplicada. Confira a URL real, não o caminho de exibição.
- **Campanha de marca e não-marca com o mesmo nome-base.** Diferencie sempre pelo segundo bloco (`[branding]` × `[implante-dentario]`).
- **Recomendação automática do Google** pode criar grupos com nome genérico ("Grupo de anúncios 1"). Desligue a autoaplicação e renomeie.
