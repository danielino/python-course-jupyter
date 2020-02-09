import argparse
import logging
from flask import Flask, jsonify, request
import psutil

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({
        "status" : "ok"
    }), 200


@app.route("/stats")
def stats():
    logger.debug("return stats")
    return jsonify({
        "cpu" : psutil.cpu_percent(),
        "memory" : dict(psutil.virtual_memory()._asdict())
        
    }), 200
    
    
@app.route("/notfound")
def ret404():
    return jsonify({}), 404

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
