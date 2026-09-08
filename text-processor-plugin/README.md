# Text Processor Plugin

Plugin examples for text-analysis workflows built from the Unit 2 server and the Unit 3 skills.

## Skills

- **Analyze Text** — Word counts, sentence stats, vocabulary diversity
- **Extract Keywords** — Find the most frequent meaningful terms
- **Check Reading Level** — Flesch-Kincaid grade level estimation

## Claude Code and Codex

The manifest-first versions bundle:
- skills in `skills/`
- plugin metadata in `.claude-plugin/plugin.json` or `.codex-plugin/plugin.json`
- optional MCP config in `.mcp.json`

## OpenCode

The OpenCode version is a local or npm-loaded JS/TS plugin module under `.opencode/plugins/` or the `plugin` array in `opencode.json`.

## Related MCP Server

If you also connect the `text-processor` MCP server, it provides:
- `analyze_text` — Compute text statistics
- `extract_keywords` — Extract frequent terms
- `check_reading_level` — Estimate reading difficulty
- `reverse_text` — Reverse a string

## Setup

The plugin can use your local server or the deployed Spaces version:

**Local:** Ensure `text-processor-mcp/server.py` is available and the MCP runtime is installed.

**Remote:** Update the `.mcp.json` or `opencode.json` URL to your deployed Space:
`https://YOUR-USERNAME-text-processor-mcp.hf.space/gradio_api/mcp/`


**Claude Code Plugin Structure**

my-plugin/
├── .claude-plugin/
│   └── plugin.json             # Plugin manifest
├── skills/                     # Collection of skills
│   ├── analyze-text/
│   │   └── SKILL.md            # Skill definition
│   ├── extract-keywords/
│   │   └── SKILL.md
│   └── check-reading-level/
│       └── SKILL.md
├── agents/                     # Custom agents (optional)
├── .mcp.json                   # MCP server configuration
├── hooks/                      # Hook configuration (optional)
│   └── hooks.json
├── .lsp.json                   # LSP server configuration (optional)
├── settings.json               # Plugin defaults (optional)
└── README.md                   # Documentation


**our example**


text-processor-plugin/
├── .claude-plugin/
│   └── plugin.json                       # Claude Code manifest
├── .codex-plugin/
│   └── plugin.json                       # Codex manifest
├── .mcp.json                             # Shared MCP config for both
├── README.md                             # Documentation
└── skills/
    ├── analyze-text/SKILL.md
    ├── extract-keywords/SKILL.md
    └── check-reading-level/SKILL.md