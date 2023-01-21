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

# connect_db
`connect_db(host: str, db: str, username: str, password: str) -> connection`

# async get_data
`get_data(entity_config: dict[str, str]) -> list | dict`

# get_entities()
`get_entities() -> list[dict[str, str]]`


