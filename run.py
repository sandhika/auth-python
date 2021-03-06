# -*- encoding: utf-8 -*-

"""
Copyright (c) 2021 - sandhika.yogaswara@gmail.com
"""


from api import app, db


@app.shell_context_processor
def make_shell_context():
    return {"app": app,
            "db": db
            }


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3010, debug=True, threaded=True)
