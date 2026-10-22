# CARDZ

Search public Pokémon and One Piece PSA 10 card prices, population, daily history and market rankings from Dify agents and workflows.

Public brand and publisher: **CARDZ**. Operated by **Jackz Intelligent Technology Co., Ltd.**, Japan. Business contact and support: **alex@jackz.ai**.

## Connection and setup

The plugin calls the existing public service at https://mcp.cardz.game/mcp. No CARDZ account, API key or payment is required. Allow outbound HTTPS to `mcp.cardz.game`. The runtime is Python 3.12 with `dify-plugin==0.10.2`.

Once the plugin is published, add CARDZ from Dify Marketplace and select one of the three tools. Developer source is in this repository's `dify/` directory: https://github.com/cardzgame/cardz-marketcap-plugin/tree/main/dify .

## Tools and examples

- `search_cards`: search a card name or collector number, such as `OP05-119`, with an optional game and display-language filter. The result preserves candidate printings and public card IDs.
- `get_card`: use an exact ID returned by search to read the card's metrics and daily history. For example, set `historyDays` to `7`.
- `get_market`: choose `all`, `pokemon` or `one-piece` and a result limit from 1 to 20 to read published rankings.

Results are returned as text and JSON. USD currency, source dates, canonical card links and unavailable values are preserved. Reference prices are daily observations rather than executable quotes. CARDZ's broader brand covers collectible cards, TCG and collectibles; this release covers Pokémon and One Piece PSA 10 data.

## Data and support

Only the tool parameters are sent to the fixed CARDZ endpoint. The adapter does not read conversation history or collect player account details. It has no local persistence, request logging, model access or transaction functions. See [PRIVACY.md](PRIVACY.md), [service documentation](https://mcp.cardz.game/) and [service terms](https://mcp.cardz.game/terms).

CARDZ tool failures return a bounded error. Check the card ID or supported parameters and try again after a temporary service or rate-limit error.
