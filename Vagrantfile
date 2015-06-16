Vagrant.configure(2) do |config|
  config.vm.define :summit_demo do | host |
    host.vm.box = "f22-cloud"
    host.vm.synced_folder ".", "/home/vagrant/sync", type: "rsync",
                          rsync__exclude: [ ".git/", ".#*", "*~", "*qcow*" ]
    host.vm.provision 'shell', inline: "sudo yum install -y python-pip"
  end
end
