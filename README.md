# Dependencies

### Python

1. asyncio
2. enum
3. datetime

### Other libraries

1. BitrixAsync
2. psycopg2
3. sqlalchemy

<hr>

## Base methods

### get_engine
`get_engine(user: str, password: str, host: str, port: int, db: str) -> Engine`

### async get_data
`get_data(entity_config: dict[str, str]) -> list | dict`

### get_entities()
`get_entities() -> list[dict[str, str | dict[str, str]]]`


