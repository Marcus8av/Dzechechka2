import subprocess

def check_command_output(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout

    if not result.returncode and text in out:
        return True
    else:
        return False

if __name__ == '__main__':
    command = 'cat /etc/os-release'
    text = 'VERSION="22.04.1 LTS (Jammy Jellyfish)"'

    if check_command_output(command, text):
        print('SUCCESS')
    else:
        print('FAIL')