# -*- coding: utf-8 -*-
# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  #config.vm.box = "http://speechkitchen.org/boxes/mario-kaldi.box"
  config.vm.box = "file:///Volumes/EFL Virtual Machines/mario-kaldi.box"
  #config.vm.box = "file:///Users/fosler/VirtualBoxVMs/mario-kaldi.box"
  config.ssh.forward_x11 = true
  config.ssh.forward_agent = true
  #  config.ssh.password = “vagrant”

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
   config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
     vb.gui = false
  
     # Customize the amount of memory on the VM:
     vb.memory = "4096"

     # Customize the number of processors on the VM:
     vb.cpus = 2

   end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
    config.vm.provision "shell", inline: <<-SHELL
    # commented out for faster "up"; uncomment before adding provisioning cmds.
    sudo apt-get update -y

    # set up audio
    sudo usermod -a -G audio vagrant
    amixer set 'Master' 100%

    sudo apt-get install --force-yes -y xfce4-panel xterm gnome-icon-theme lxappearance thunar chromium-browser audacity ipython ipython-notebook python-pip python-dev python-virtualenv libxml2-dev libxslt-dev audacity graphviz

    export PYTHONPATH=/usr/local/lib/python2.7/dist-packages:$PYTHONPATH
    export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib/fst:
    export LC_ALL=C
    export CPLUS_INCLUDE_PATH=/usr/local/include:$CPLUS_INCLUDE_PATH

    [ -d /home/vagrant/src ] || mkdir /home/vagrant/src
    cd /home/vagrant/src

    # Install openfst 1.5.0 (can change to latest)
    wget http://www.openfst.org/twiki/pub/FST/FstDownload/openfst-1.5.0.tar.gz
    tar -xzf openfst-1.5.0.tar.gz
    rm openfst-1.5.0.tar.gz
    cd openfst-1.5.0
    LDFLAGS=-Wl,-rpath=/usr/local/lib:/usr/local/lib/fst,--enable-new-dtags ./configure --enable-pdt --enable-bin --enable-ngram-fsts --enable-shared
    make
    sudo make install
    make clean

    # Add to dynamic libraries so next login with find libs
    echo '/usr/local/lib' >> /etc/ld.so.conf
    echo '/usr/local/lib/fst' >> /etc/ld.so.conf
    /sbin/ldconfig

    # Install pyfst, which is used with ipython notebook
    cd /home/vagrant/src
    wget http://demo.clab.cs.cmu.edu/cdyer/pyfst-0.2.5.tar.gz
    tar -xzf pyfst-0.2.5.tar.gz
    rm pyfst-0.2.5.tar.gz
    cd pyfst-0.2.5
    sudo python setup.py install

    # Install megam
    apt-get install  --force-yes -y ocaml
    cd /home/vagrant/src
    wget http://hal3.name/megam/megam_src.tgz
    tar -xzf megam_src.tgz
    cd megam_0.*
    mv Makefile Makefile.orig
    sed 's/-lstr/-lcamlstr/' Makefile.orig > Makefile
    make
    install megam /usr/local/bin
    make clean

    # Install NLTK
    pip install -U nltk
    pip install -U numpy
    python -m nltk.downloader -d /usr/share/nltk_data conll2000
    python -m nltk.downloader -d /usr/share/nlkt_data brown

    # Install Octave
    apt-get install  --force-yes -y octave sox
    
    # Install SRILM
    cd /home/vagrant/src
    # srilm splats all over the place when you unpack, tsk tsk
    mkdir srilm-1.7.1
    cd srilm-1.7.1
    tar -xzf /vagrant/protected/srilm-1.7.1.tar.gz
    mv Makefile Makefile.orig
    sed 's@^# SRILM =.*@SRILM = /home/vagrant/src/srilm-1.7.1@' Makefile.orig > Makefile
    make NO_TCL=X
    cd bin
    install `find . -executable` /usr/local/bin
    cd ../man
    for i in 1 3 5 7; do
      if [ ! -d /usr/local/man/man$i ]; then
        mkdir /usr/local/man/man$i
      fi
      install -m 644 `find man$i -name '*.'$i -a -not -name 'TEMPLATE*'` /usr/local/man/man$i
    done

    # Adjust Kaldi scripts
    mv /home/vagrant/kaldi-trunk/egs/tidigits/s5/cmd.sh /home/vagrant/kaldi-trunk/egs/tidigits/s5/cmd.sh.dist
    sed -e 's/^#export decode_cmd/export decode_cmd/' -e 's/export decode_cmd="queue.pl/#export decode_cmd="queue.pl/' /home/vagrant/kaldi-trunk/egs/tidigits/s5/cmd.sh.dist > /home/vagrant/kaldi-trunk/egs/tidigits/s5/cmd.sh
    mv /home/vagrant/kaldi-trunk/egs/tidigits/s5/run.sh /home/vagrant/kaldi-trunk/egs/tidigits/s5/run.sh.dist
    sed -e 's@^tidigits=.*@tidigits=/home/vagrant/data/tidigits@' -e 's/--nj [0-9]*/--nj 2/g'  /home/vagrant/kaldi-trunk/egs/tidigits/s5/run.sh.dist > /home/vagrant/kaldi-trunk/egs/tidigits/s5/run.sh
    chmod 755 /home/vagrant/kaldi-trunk/egs/tidigits/s5/run.sh
    mkdir /home/vagrant/data
    cd /home/vagrant/data
    tar -xzf /vagrant/protected/tidigits.tgz

    
   SHELL

  #config.vm.provider :virtualbox do |vb|
  #  vb.customize ["modifyvm", :id, '--audio', 'coreaudio', '--audiocontroller', 'hda'] # choices: hda sb16 ac97
  #end
end
