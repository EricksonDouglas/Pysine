# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  config.vm.box = "ubuntu/trusty64"

  config.vm.synced_folder ".", "/vagrant"

  config.vm.provider "virtualbox" do |vb|
    vb.gui = false

    # Customize the amount of memory on the VM:
    vb.memory = "512"
  end

  config.vm.provision "shell", inline: <<-SHELL
    cd /vagrant
    echo "cd /vagrant" >> /home/vagrant/.bashrc
    echo "alias python=python3" >> /home/vagrant/.bashrc
    sudo apt-get update
    sudo apt-get -y install python-pip git
    pip install -r requisitos.txt

  SHELL
end
