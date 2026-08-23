cd ~/projects/library-system

cat > README.md << 'EOF'
# library-system

A library loan management domain, modeling books, users, and loans with
proper encapsulation and business rules — no persistence layer yet
(in-memory domain only).

## Design

- `Book` and `User` compose independently — `User` delegates borrowing
  validation to `Book` instead of duplicating rules.
- `Loan` composes `Book` and `User` (has-a, not is-a) and owns its own
  rules: due dates, overdue detection, and late fees.
- All state changes go through methods that enforce business rules —
  no attribute is publicly mutable without validation.

## Development

```bash
uv sync
uv run pytest -v
uv run pytest --cov=library_system --cov-report=term-missing
uv run ruff check src/ tests/
```
EOF
