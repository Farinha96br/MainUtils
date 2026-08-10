# programa de setup pós instalação do uPINTO
# atualizada em 15/07/2020

# att qualq coisa q precisa
apt update
apt -y upgrade

apt install -y python3-pip python3-opencv python3-skimage python3-numpy
#math e time ja vem no python msm(?)

# Coisas do latex, e pra usar o babel
apt install -y texmaker
apt install -y texlive-full

# Bibliotecas do C/C++
apt-get install libgsl-dev # Gnu Scientific library
apt install libboost-all-dev

# coisas do OBS
add-apt-repository -y ppa:obsproject/obs-studio
apt-get update
apt-get install -y obs-studio

# minor tools
apt install pdftk

# installando o discord pelo snap
snap install discord

# vlc
apt -y install vlc
apt -y install ffmpeg

# htop, monitoramento de recursos
apt -y install htop

# steam
apt -y install steam
apt -y install flameshot 
# coisas q faltam e os links pra download


# dropbox
apt -y install nautilus-dropbox 
cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -
~/.dropbox-dist/dropboxd
