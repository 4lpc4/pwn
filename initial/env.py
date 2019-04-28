!#/usr/bin/env python
import os
os.system('sudo apt-get install git zsh curl python-pip python-dev build-essential -y')
os.system('sudo pip install --upgrade pip')
os.system('sudo pip install --upgrade setuptools')
os.system('sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"')
os.system('sudo apt-get install autojump')
os.system('echo ". /usr/share/autojump/autojump.sh" >> ~/.zshrc')
os.system('git clone https://github.com/zsh-users/zsh-syntax-highlighting.git && echo "source ${(q-)PWD}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc')
os.system('sudo chsh -s /bin/zsh')
os.system('source ~/.zshrc')
os.system('pip install pwntools ipython')