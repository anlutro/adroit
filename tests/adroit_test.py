import adroit.tester
import pytest


@pytest.fixture
def tester(tmpdir):
	return adroit.tester.AnsibleRoleTester(tmpdir, 'adroit', 'debian:stretch')


def test_get_docker_name(tester):
	assert tester.get_docker_name('role', 'img') == 'adroit-img-role'
	assert tester.get_docker_name('role', 'img:tag') == 'adroit-img-tag-role'


def test_get_inventory(tester):
	assert '[docker:children]\nlocal' in tester.get_inventory()
	assert '[adroit:children]\nlocal' in tester.get_inventory()
	assert '[adroit-role:children]\nlocal' in tester.get_inventory('role')
	assert '[adroit-debian-stretch-role:children]\nlocal' in tester.get_inventory('role')
