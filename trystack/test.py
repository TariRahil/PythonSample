from trystack import create_app
from os.path import abspath
app = create_app(abspath("config.json"))
app.run
