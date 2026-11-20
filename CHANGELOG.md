# Changelog

All notable changes to SolveAI will be documented in this file.

## [0.1.3] - 2026-11-20

### Changed
- Database-first architecture: Offline knowledge base is always prioritized before Ollama
- Added shorthand input syntax support: `bar plot,py`, `histogram,r`, etc.
- Removed persistent startup error state on status bar so offline questions work with 0 latency
- Included complete optimized solutions for all main Python & R visualization practical questions

## [0.1.0] - 2024-01-01

### Added
- Initial V1 release
- Native VS Code status-bar Solve button
- Solve with AI command (Ctrl+Alt+S)
- Fix with AI command (Ctrl+Alt+F)
- Explain with AI command
- Ollama HTTP API integration
- LAN/Wi-Fi laptop Ollama support
- Configurable server URL, model, timeout
- Model selection from installed Ollama models
- Connection checker
- Code fence stripping
- Auto-apply option
- Right-click context menu integration
- Input dialog for no-selection use
- Large input protection
