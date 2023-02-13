from flask import Flask

from generate_entities import GenerateEntities
from utils import Settings
from fields.constants import BITRIX_METHODS


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def handle_request():
    try:
        settings = Settings()
        GenerateEntities(settings, BITRIX_METHODS)
        return 'Данные успешно обновлены'

    except Exception as error:
        return f'Произошла ошибка {error}'

if __name__ == '__main__':
    app.run()