from controllers.WebhookController import WebhookController
from flask import Flask
import os

from services.Worker import start_worker

app = Flask(__name__)
app.register_blueprint(WebhookController)

#teste heroku
if __name__ == "__main__":
    start_worker()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)