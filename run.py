import os
import shutil
from termcolor import colored

def main():
    update('Setting up Mirrors.', 'yellow')
    code = os.system('sudo pacman-mirrors --geoip')
    if(code == 0):
        update('Mirrors set successfully!!!', 'green')
        update('Installing Packages', 'yellow')
        code_s = install_packages()
        if(code_s == 0):
            update('Packages installed successfully!!!', 'green')
            update('Running post install configs...', 'yellow')
            code_c = run_post_configs()
            if(code_c == 0):
                update('Post install scripts ran successfully!!!', 'green')
            else:
                update('Failed running post install scripts. please see errors and re-run the script', 'red')
        else:
            update('Failed installing packages. please see errors and re-run the script', 'red')
    else:
        update('Failed setting up Mirrors. please see errors and re-run the script', 'red')

    return 0


def install_packages():
    formatted= ''
    with open('package.txt') as f:
        s = f.read()
        formatted += s.replace('\n', ' ')

    r_val = os.system('sudo pacman -Suyy ' + formatted)
    return r_val

def run_post_configs():
    os.system('cd ~')
    #install oh myzsh
    zsh = os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')

    if(zsh != 0):
        return zsh
    #set git
    git = os.system('git config --glablal user.name "Kwanele Gamedze"')
    git = os.system('git config --glablal user.email "kwanelegamedze4@gmial.com"')
    gh = os.system('gh auth login')
    con = os.system('cd ~ && gh repo clone Configs && cd ~Configs && python run.py pull')
    if(con != 0):
        return con
    
    os.system('cd ~')

    #nvm
    nvm = os.system('curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash')

    if(nvm != 0):
        return nvm
    os.system('source .zshrc')

    #install node
    node = os.system('nvm install 22')
    if(node != 0):
        return node

    #vim plug
    plug = os.system('sh -c \'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim\'')

    if(plug != 0):
        return plug
    #dotnet-ef
    ef =os.system('dotnet tool install --global dotnet-ef')
    if(ef != 0):
        return ef

    #mkdir
    dirs =os.system('mkdir ~/Art && mkdir ~/Art/Projects && mkdir ~/Art/Lessons')

    #clone repos
    nvim =os.system('cd ~/.configs && gh repo clone nvim')
    done =os.system('cd ~')
    return 0

def update(text, color):
    print(colored('---------------------------',color))
    print(colored(text,color))
    print(colored('---------------------------',color))

main()

