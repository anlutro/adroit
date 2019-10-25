import adroit.tester
import pytest


@pytest.fixture
def tester(tmpdir):
    return adroit.tester.AnsibleRoleTester(tmpdir, "adroit", "debian:stretch")


def test_get_docker_name(tester):
    assert tester.get_docker_name("role", "img") == "adroit_img_role"
    assert tester.get_docker_name("role", "img:tag") == "adroit_img_tag_role"


def test_get_inventory(tester):
    assert "[docker:children]\nlocal" in tester.get_inventory()
    assert "[adroit:children]\nlocal" in tester.get_inventory()
    role_inv = tester.get_inventory("role")
    assert "[adroit_role:children]\nlocal" in role_inv
    assert "[adroit_debian_stretch_role:children]\nlocal" in role_inv
