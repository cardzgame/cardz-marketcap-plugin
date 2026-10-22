# CARDZ — Collectibles & TCG

Version 1.1.2 is deployed at https://mcp.cardz.game/mcp. Compatible hosts can display the MCP Apps view. Standard MCP hosts continue to receive the same three tools with matching text and structured results; they do not need to load the interface. Marketplace review and approval are separate.

CARDZ is a brand for collectible cards, trading card games and collectibles. This release's data coverage is Pokémon and One Piece PSA 10 cards.

Public Pokémon and One Piece PSA 10 reference prices, population, daily history and market rankings. Operated by Jackz Intelligent Technology Co., Ltd. in Japan. Contact: alex@jackz.ai.

Connect the Streamable HTTP MCP at https://mcp.cardz.game/mcp with no authentication. This package uses Agent Plugins 1.0 and contains connection metadata only.

Three read-only tools:

- `search_cards`: find candidate card printings.
- `get_card`: read exact-card metrics and daily history.
- `get_market`: read published market rankings.

Results preserve USD, metric dates and unavailable values.
Daily reference prices are not executable quotes.
This package has no player account or transaction tools.

Examples: “Find the different printings of OP05-119”; “Show the selected card's seven-day history”; “Show the top five One Piece cards by published market cap”.

[Service and publisher](https://mcp.cardz.game/) · [Privacy](https://mcp.cardz.game/privacy) · [Terms](https://mcp.cardz.game/terms) · [Support](https://mcp.cardz.game/support)

Directory acceptance is platform-specific. This public repository and a working endpoint do not mean that a marketplace listing has been approved.
