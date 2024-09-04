import os
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

    r_val = os.system('sudo pacman --needed -Suy ' + formatted)
    return r_val

def run_post_configs():
    os.system('cd ~')

    #slack
    slack = os.system('yay -S slack-desktop')
    if(slack !=0):
        return slack

    #neovim
    neo1 = os.system('curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux64.tar.gz')
    neo2 = os.system('sudo rm -rf /opt/nvim')
    neo3 = os.system('sudo tar -C /opt -xzf nvim-linux64.tar.gz')
    if(neo1 !=0 or neo2 !=0 or neo3 != 0):
        return neo1 + neo2 + neo3
    os.system('rm -rf nvim-linux64.tar.gz')

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
    
    #nvm
    os.system('cd ~')
    nvm = os.system('curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash')
    if(nvm != 0):
        return nvm

    #install node
    os.system('source .zshrc')
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
    dirs = os.system('mkdir ~/Art && mkdir ~/Art/Projects && mkdir ~/Art/Lessons')
    if(dirs != 0):
        return dirs

    #clone repos
    nvim =os.system('cd ~/.configs && gh repo clone nvim')
    if(nvim != 0):
        return nvim

    done =os.system('cd ~')
    return 0

def update(text, color):
    print(colored('---------------------------',color))
    print(colored(text,color))
    print(colored('---------------------------',color))

main()

