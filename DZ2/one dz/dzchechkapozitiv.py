import subprocess

def checkout(cnd, text):
    result = subprocess.run(cnd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')

    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

