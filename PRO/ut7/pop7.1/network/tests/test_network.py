import os

import pytest

if os.path.exists('solution.py'):
    from solution import Host, IPAddressError
else:
    from main import Host, IPAddressError


ERR_BASE_MSG = 'IP address is invalid'


@pytest.fixture
def host1():
    return Host(192, 168, 1, 5, mask=24)


@pytest.fixture
def host2():
    return Host(172, 16, 1, 5, mask=16)


@pytest.fixture
def host3():
    return Host(10, 0, 1, 5, mask=8)


def test_build_host():
    host = Host(192, 168, 1, 5, mask=24)
    assert isinstance(host, Host)
    assert host.mask == 24
    assert host.ip_octets == (192, 168, 1, 5)


def test_build_host_fails_when_has_too_many_octets():
    with pytest.raises(IPAddressError) as err:
        Host(192, 168, 1, 5, 9, 30, mask=16)
    assert str(err.value) == f'{ERR_BASE_MSG}: Only 4 octets are allowed'


def test_build_host_fails_when_has_too_few_octets():
    with pytest.raises(IPAddressError) as err:
        Host(192, 168, 1, mask=16)
    assert str(err.value) == f'{ERR_BASE_MSG}: Only 4 octets are allowed'


def test_build_host_fails_when_octets_are_out_of_range():
    with pytest.raises(IPAddressError) as err:
        Host(192, 168, 1, 300, mask=24)
    assert str(err.value) == f'{ERR_BASE_MSG}: Octet is out of range'


def test_build_host_fails_when_mask_is_out_of_range():
    with pytest.raises(IPAddressError) as err:
        Host(192, 168, 1, 5, mask=40)
    assert str(err.value) == f'{ERR_BASE_MSG}: Mask is out of range'


def test_build_host_from_sip():
    host = Host.build_from_sip('192.168.1.5', mask=24)
    assert isinstance(host, Host)
    assert host.mask == 24
    assert host.ip_octets == (192, 168, 1, 5)


def test_build_host_from_sip_fails_when_has_too_many_octets():
    with pytest.raises(IPAddressError) as err:
        Host.build_from_sip('192.168.1.5.9.30', mask=16)
    assert str(err.value) == f'{ERR_BASE_MSG}: Only 4 octets are allowed'


def test_build_host_from_sip_fails_when_has_too_few_octets():
    with pytest.raises(IPAddressError) as err:
        Host.build_from_sip('192.168.1', mask=16)
    assert str(err.value) == f'{ERR_BASE_MSG}: Only 4 octets are allowed'


def test_build_host_from_sip_fails_when_octets_are_out_of_range():
    with pytest.raises(IPAddressError) as err:
        Host.build_from_sip('192.168.1.300', mask=24)
    assert str(err.value) == f'{ERR_BASE_MSG}: Octet is out of range'


def test_build_host_from_sip_fails_when_mask_is_out_of_range():
    with pytest.raises(IPAddressError) as err:
        Host.build_from_sip('192.168.1.5', mask=40)
    assert str(err.value) == f'{ERR_BASE_MSG}: Mask is out of range'


def test_host_ip(host1: Host, host2: Host, host3: Host):
    assert host1.ip == '192.168.1.5'
    assert host2.ip == '172.16.1.5'
    assert host3.ip == '10.0.1.5'


def test_host_bip(host1: Host, host2: Host, host3: Host):
    assert host1.bip == '11000000101010000000000100000101'
    assert host2.bip == '10101100000100000000000100000101'
    assert host3.bip == '00001010000000000000000100000101'


def test_addr_bmask(host1: Host, host2: Host, host3: Host):
    assert host1.addr_bmask == '110000001010100000000001'
    assert host2.addr_bmask == '1010110000010000'
    assert host3.addr_bmask == '00001010'


def test_addr_bhost(host1: Host, host2: Host, host3: Host):
    assert host1.addr_bhost == '00000101'
    assert host2.addr_bhost == '0000000100000101'
    assert host3.addr_bhost == '000000000000000100000101'


def test_has_network_addr():
    host = Host(192, 168, 0, 0, mask=24)
    assert host.has_network_addr is True
    host = Host(192, 168, 1, 0, mask=23)
    assert host.has_network_addr is False


def test_has_broadcast_addr():
    host = Host(192, 168, 0, 255, mask=24)
    assert host.has_broadcast_addr is True
    host = Host(192, 168, 0, 255, mask=23)
    assert host.has_broadcast_addr is False


def test_network_class(host1: Host, host2: Host, host3: Host):
    assert host1.nclass == 'C'
    assert host2.nclass == 'B'
    assert host3.nclass == 'A'


def test_network_class_returns_None():
    assert Host(224, 0, 0, 1, mask=8).nclass is None


def test_addr_host_size(host1: Host, host2: Host, host3: Host):
    assert host1.addr_host_size == 8
    assert host2.addr_host_size == 16
    assert host3.addr_host_size == 24


def test_num_hosts(host1: Host, host2: Host, host3: Host):
    assert host1.num_hosts == 254
    assert host2.num_hosts == 65534
    assert host3.num_hosts == 16777214


def test_ping_hosts():
    host1 = Host(192, 168, 77, 99, mask=24)
    host2 = Host(192, 168, 77, 103, mask=24)
    host3 = Host(192, 168, 77, 88, mask=23)
    assert host1.ping(host2) is True
    assert host1.ping(host3) is False


def test_host_repr(host1: Host, host2: Host, host3: Host):
    assert repr(host1) == '192.168.1.5/24'
    assert repr(host2) == '172.16.1.5/16'
    assert repr(host3) == '10.0.1.5/8'


def test_build_host_from_bip():
    host = Host.build_from_bip('11000000101010000000000100000101', mask=24)
    assert repr(host) == '192.168.1.5/24'
    host = Host.build_from_bip('10101100000100000000000100000101', mask=16)
    assert repr(host) == '172.16.1.5/16'
    host = Host.build_from_bip('00001010000000000000000100000101', mask=8)
    assert repr(host) == '10.0.1.5/8'


def test_build_host_fails_when_bip_is_too_long():
    with pytest.raises(IPAddressError) as err:
        Host.build_from_bip('011000000101010000000000100000101', mask=24)
    assert str(err.value) == f'{ERR_BASE_MSG}: Binary address is too long'


def test_build_base_ip_adress_error():
    err = IPAddressError()
    assert str(err) == ERR_BASE_MSG


def test_network_iterator(host1: Host):
    niter = iter(host1)
    for ip_seg in range(1, 255):
        ip = f'192.168.1.{ip_seg}'
        host = next(niter)
        assert host.ip == ip
    with pytest.raises(StopIteration):
        next(niter)


def test_add_hosts(host1: Host, host2: Host, host3: Host):
    result = host1 + host2
    assert result.ip_octets == (255, 184, 2, 10)
    assert result.mask == 32

    result = host2 + host3
    assert result.ip_octets == (182, 16, 2, 10)
    assert result.mask == 24
