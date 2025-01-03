install:
	uv sync

build:
	uv build

package-install:
	uv tool install --reinstall hexlet_code
	uv tool install dist/*.whl

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

make lint:
	uv run ruff check brain_games