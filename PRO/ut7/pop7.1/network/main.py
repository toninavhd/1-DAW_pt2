from __future__ import annotations


class Host:
    DEFAULT_IP_BYTES = 0
    IPV4_BYTES = 4
    IPV4_BITS = 32
    MAX_SLICES = 255
    IP_CLASSES = ('A','B','C')
    IPV4_SLICES = list(range(0, IPV4_BITS + 1, 8))
    

    def __init__(self, *ip_octets: int, mask: int):
        self.ip_octets = self.check_ip_mask(ip_octets)
        self.mask = self.validate_mask(mask)

    @staticmethod
    def check_ip_mask(*ip_octets: tuple[str|int]) -> tuple:
        if isinstance(ip_octets[0],str):
            ip_octets = tuple(int(arg)for arg in ip_octets[0].split('.'))
        if len(ip_octets) > Host.IPV4_BYTES:
            raise IPAddressError('Only 4 octets are allowed')
        return tuple(ip_octets) + (Host.DEFAULT_IP_BYTES,) * (Host.IPV4_BYTES - len(ip_octets))

    @staticmethod
    def validate_mask(mask:int) -> int:
        if not(0 <= mask <= Host.IPV4_BITS):
            raise IPAddressError('Mask is out of range')
        return mask       



    @classmethod
    def build_from_sip(cls, sip: str, *, mask: int) -> Host:
    
        return f'IP {sip}/{mask}'

    @property
    def ip(self) -> str:
        return '.'.join(str(octet) for octet in self.ip_octets)

    @property
    def bip(self) -> str:
        return '.'.join(f'{octet:08b}' for octet in self.ip_octets)

    @property
    def addr_bmask(self) -> str:
        return self.bip[:self.mask]

    @property
    def addr_bhost(self) -> str:
        return self.bip[self.mask:]
        

    @property
    def has_network_addr(self) -> bool:
        return self.addr_bhost == 0 * len(self.addr_bhost)
    @property
    def has_broadcast_addr(self) -> bool:
        return self.addr_bhost == 1 * len(self.addr_bhost)

    @property
    def nclass(self) -> str | None:
        for ip_class in range(len(Host.IP_CLASSES)):
            if len(self.addr_bmask) <= Host.IPV4_SLICES[ip_class +1]:
                return Host.IP_CLASSES[ip_class]
        return None

    @property
    def addr_host_size(self) -> int:
        return len(self.addr_bhost)

    @property
    def num_hosts(self) -> int:
        return 2 ** self.addr_host_size

    def ping(self, host: Host) -> bool:
        return self.addr_bmask == host.addr_bmask

    def __repr__(self):
        return f'{self.ip}/{self.mask}'

    @classmethod
    def build_from_bip(cls, bip: str, mask: int) -> Host:
        IPV4_SLICES = list(range(0, cls.IPV4_BITS + 1, 8))
        if len(bip) > cls.IPV4_BITS:
            raise IPAddressError ('Binary address is too long')
        new_ip = [
            int(bip[cls.IPV4_SLICES[idx]:cls.IPV4_SLICES[idx+1]],base=2)
            for idx in range(len(cls.IPV4_SLICES)-1)
        ]

        return cls(*new_ip, mask)

    def __iter__(self):
        for i in range(1,self.addr_host_size + 1):
            addr_bhost = f'{i:0{self.addr_host_size}b}'
            bip = self.addr_bmask + addr_bhost
            yield Host.build_from_bip(bip,self.mask)

    def __add__(self, other: Host) -> Host:
        new_ip_octets=[
            min(octect_1 + octect_2, Host.MAX_SLICES)
            for octect_1, octect_2 in zip(self.ip_octets, other.ip_octets)
        ]
        new_mask = min(self.mask + other.mask, Host.IPV4_BITS)
        return Host(*new_ip_octets, mask = new_mask)

class IPAddressError(Exception):
    DEFAULT_MSG = 'IP address is invalid'
    def __init__(self, message: str = ''):
        super().__init__(message)
        self.message = message
    def __str__(self):
        return f'{IPAddressError.DEFAULT_MSG}:{self.message}' if self.message else IPAddressError.DEFAULT_MSG
    
