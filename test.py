

# simply using global counter

# from flask import Flask
#
# app = Flask(__name__)
#
# counter = 0
#
#
# @app.route("/")
# def hello():
#     global counter
#     counter += 1
#     return str(counter)
#
# if __name__ == "__main__":
#     app.run()


######################################
# using multiprocessing

# from flask import Flask, jsonify
# from multiprocessing import Value
#
# counter = Value('i', 0)
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     with counter.get_lock():
#         counter.value += 1
#
#     return jsonify(count=counter.value)
#
#
# if __name__ == "__main__":
#     app.run(debug=True)



######################################
# using redis

import redis
from flask import Flask

app = Flask(__name__)
db = redis.Redis(host='localhost', port=6379)
db.set('hits',0)

@app.route('/')
def hello():
    try:
        count = db.incr('hits')
    except Exception as e:
        print(e)
    return "Page visited {} times".format(count)

if __name__ == "__main__":
    app.run( debug=True)



