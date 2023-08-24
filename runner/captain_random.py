#!/usr/bin/env python3
from base64 import b64decode
from gzip import decompress
data = b''
data += b'H4sIABgDp18C/+1WTY/bRgy961dwsQdJXa033vRjYdS5pJcAabpIFujBEIyRhrbHlmcEzc'
data += b'iyUPS/lxzJluxt01x6qw+2xCEfH8knysEtfFI5JtCaGiTmSqIEZ6BE3IHSdOU2CCtV4A3A'
data += b'y0a40EJuTHET3NKtsqCsDh3sUWjHcRmCxbyusGgBdV61pSNAU4HQrdsovU4ocFtbx6eGk6'
data += b'E29XpDaYRjEqGEjTggY+3FDkFQOm1zZWpLkbhamconqlBIz41RJsEtHX5EJtJVoiRYQ5S/'
data += b'YMWhRZuArEwJRiOYFdQWohem9T4mZgy8F6qAAp0jjny806bxUCtTa86k7ATgdwyLgossCx'
data += b'QWJVfzAXKhQVhLVXMEuc3iILi9eaht9ZAp/YD6ACWVb/TbIFhVZk+kiwJzp6g0UPuSa5K4'
data += b'EnXhpMpd5+Pakrn0xy81pUzgV1GyNYGPyrqgP6uElmZ/unNqj0Hwy4fPX2AOi0geE9nGVE'
data += b'YF8kgjZe81RvfT5LG3ttdWtWJXf5QGvz0/E84fYRPOIMzChL/oqgn/pBrhvdEHpKQZugZR'
data += b'g3UVkyZCLJNKKi0ccpq9DahCKI1dksxoZhFdzsg9hvt3XXUL0lvCoktnAdCnQldXGiKCYe'
data += b'fFmzS+5+tQhHGcDPbpyT4l+zlLp69IbWdX4D4hJb5IEoosp8j1JlyoLWVK4Q7C6ePb73/4'
data += b'8acnb5umKRf8bKzq5uYV25i6kLAqVMldi1SypfZZfmAK0nbWklBEi9XE0/LOS3aOMiMqOe'
data += b'unuRgYMsGE2dG3mnnO2+6nAzp3jOd/Fde3jfEtjz71t6YsSfT0dM6BRrnoYKgU7+pFkXQK'
data += b'YMV0CH3YCOTkbB2Wg1qmCTzFQwh/jrRJKEzdsed3hA3b/rK98KNmHX9+wxo7vps/8W/b3b'
data += b'Z0O4OMHu/ddYDv2eKYtCnM5xCGl5n58zoMi1eBp4a8DueaJzQS1DKKyJ3U9C9Y/VBeIXUz'
data += b'uPPJ7Fdo9urz7oHXyEEUSi735oD2m0TyzbLwwMNEeZq9XDVtCa7W20Yr4qmztGNLOtR6bg'
data += b'ahpDNe07Q7axyfXwueNE2COJG+ko4neG4/U4vHPfLHQZAXtGnhMy2Y51HvuXPLpdLKLZeR'
data += b'xWKVQNb4pgw52DzJGmpB1lwZmRvZRys44tgzdF1KWmM98NDxBE47bNQVKpCgLvdcfPEQRf'
data += b'yQ+L6P+jMQ+WqTBrcFo6Rw0uDfVLRgnCsPrmaNzgvM57zchqN+j3Zo936Z5BtDfxWisULH'
data += b'rPv+xjS2wLdZ6bJ2URzQwPwrovFS694hTZgGJb0qXBSaXRgHPgXFDIONCCpoNvTPA16qGj'
data += b't+haL394DMJmd2qHlV8dnEloU6nZAAu0Pa535jMOfR1sgaP0AK7d2m9Dz1l4/D3vPUJr0E'
data += b'+pgugV8Ilymot6MMXYUdwLnr8T8GS9pLY35+TfBL5/+/aP/FX7S/ABXc+6n8CgAA'
exec(decompress(b64decode(data)).decode("utf-8"))