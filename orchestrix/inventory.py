import configparser

class Inventory:
    def __init__(self,filename):
        self.filename=filename
        self.hosts=self._load()

    def _load(self):
        config=configparser.ConfigParser(
            allow_no_value=True,
            delimiters=(" ",)
        )

        config.optionxform=str  # preserve case of keys
        config.read(self.filename)

        hosts={}

        for group in config.sections():
            for host_key,host_value in config[group].items():
                parts=host_value.split()
                host_data={"group":group}

                for part in parts:
                    key,value=part.split('=')
                    host_data[key]=value

                hosts[host_key]=host_data

        return hosts

    def get_host(self,hostname):
        return self.hosts.get(hostname)

    def get_all_hosts(self):
        return self.hosts



    