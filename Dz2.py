import subprocess
import string

def check_command_output(command, text, word_mode=False):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout

    if word_mode:
        words = out.split()
        translator = str.maketrans('', '', string.punctuation)
        words = [word.translate(translator) for word in words]
        return text in words
    else:
        return text in out

if __name__ == '__main__':
    command = 'cat /etc/os-release'
    text = 'VERSION="22.04.1 LTS (Jammy Jellyfish)"'

    if check_command_output(command, text):
        print('SUCCESS')
    else:
        print('FAIL')

    word_text = 'Jammy'
    if check_command_output(command, word_text, word_mode=True):
        print('Word found in output')
    else:
        print('Word not found in output')