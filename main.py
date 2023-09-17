import subprocess

if __name__ == '__main__':
    result = subprocess.run('cat /etc/os-release', shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout

    if not result.returncode:
        my_list = out.split('\n')
        print(my_list)

        if 'VERSION="22.04.1 LTS (Jammy Jellyfish)"' in my_list and 'VERSION_CODENAME=jammy' in my_list:
            print('SUCCESS')
        else:
            print('FAIL')
