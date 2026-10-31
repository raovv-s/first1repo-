import subprocess
import sqlite3
import yaml


def run_report(name):
    # runs a report script chosen by the user
    subprocess.run(f"python reports/{name}.py", shell=True)


def find_user(db, username):
    cur = db.cursor()
    cur.execute(f"SELECT * FROM users WHERE name = '{username}'")
    return cur.fetchone()


def load_config(path):
    with open(path) as f:
        return yaml.load(f)
