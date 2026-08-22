# AI Labs Relations Obsidian plugin

This plugin renders the YAML `relations` frontmatter as navigable links at the
bottom of a note's Reading view. The Markdown/YAML files remain the source of
truth; the plugin only provides a presentation layer.

## Install for development

1. Run `npm install` in this directory.
2. Run `npm run build`.
3. Copy this directory into the vault's `.obsidian/plugins/ai-labs-relations/`.
4. Enable **AI Labs Relations** in Obsidian's Community plugins settings.

The plugin currently renders canonical `ailabs:` IDs as internal Obsidian links
and leaves unresolved IDs visible for debugging.
