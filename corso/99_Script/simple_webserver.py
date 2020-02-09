import argparse
import logging
from flask import Flask, jsonify, request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)



@app.route("/")
def index():
    return jsonify({
        "status" : "ok"
    }), 200

@app.route("/metrics")
def index():
    
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", dest="debug", action="store_true", default=False)
    parser.add_argument("--host", dest="host")
    parser.add_argument("--port", dest="port", type=int, default=9999)
    args = parser.parse_args()
    
    if args.debug:
        logger.setLevel(logging.DEBUG)

    app.run(host=args.host, port=args.port, debug=args.debug)


if __name__ == "__main__":    
    main()
