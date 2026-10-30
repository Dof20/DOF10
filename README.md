# DOF10

## Serveur MCP Perplexity

Le fichier `.mcp.json` déclare le serveur MCP Perplexity au niveau du projet
(équivalent de `claude mcp add perplexity --scope project ...`).

La clé n'est **jamais** stockée dans le dépôt : elle est lue depuis la variable
d'environnement `PERPLEXITY_API_KEY`.

### En local

```bash
export PERPLEXITY_API_KEY="votre_cle"
claude            # approuver le serveur "perplexity" au premier lancement
```

Vérifier avec `claude mcp list` ou `/mcp` dans Claude Code.

### Sur Claude Code (cloud)

Ajouter `PERPLEXITY_API_KEY` dans les paramètres de l'environnement cloud
(menu de l'environnement → Edit → variables / secrets), puis ouvrir une
nouvelle session. Le réseau de l'environnement doit autoriser `registry.npmjs.org`
et `api.perplexity.ai`.
