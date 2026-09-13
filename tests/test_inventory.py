from orchestrix.inventory import Inventory

def test_inventory_loads_hosts(tmp_path):

    # tmp_path is a special built in fixture from pytest. it automatically buits a unique, temporary directory just for this test, ensuring the tests don't leave permanent junk files on drive

    inventory_file = tmp_path / "inventory.ini"

    # write mock data into the temporary file
    inventory_file.write_text(
        """
[webservers]
server1 host=192.168.1.100 user=testuser
server2 host=192.168.1.101 user=testuser
"""
    )

    inventory=Inventory(str(inventory_file))

    hosts=inventory.get_all_hosts()

    assert "server1" in hosts
    assert "server2" in hosts

    assert hosts["server1"]["host"] == "192.168.1.100"
    assert hosts["server2"]["host"] == "192.168.1.101"


def test_get_host(tmp_path):
    inventory_file=tmp_path / "inventory.ini"

    inventory_file.write_text("""

[webservers]
server1 host=192.168.1.100 user=testuser
""")

    inventory=Inventory(str(inventory_file))

    host=inventory.get_host("server1")

    assert host["host"]=="192.168.1.100"
    assert host["user"]=="testuser"

def test_unknown_host(tmp_path):
    inventory_file = tmp_path / "inventory.ini"

    inventory_file.write_text("""
[webservers]
server1 host=192.168.1.100 user=testuser
""")

    inventory=Inventory(str(inventory_file))

    assert inventory.get_host("server9") is None