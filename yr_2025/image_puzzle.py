import requests

session = requests.Session()

# Replace with the real cookie‐name you saw in DevTools:
cookie_name  = 'connect.sid'  
cookie_value = 'OwA6Qb_BynhSUAO7iX7jRFiRRmAc9sGC2cditArCqePG_5yoCAw2-jomJyWGdzjjyPQ6IsB3mJpekcER57Dsj4eQ721jfjaSHuv-Ypi2QSZexGm4uXKjASLfSCaCoYvl_4or96i42OUYZGHIv9ZlOl2CmhPhiwfyW0xMKVl_0c0='

# Attach it to your target host and path
session.cookies.set(
    name   = cookie_name,
    value  = cookie_value,
    domain = '34.55.69.223',   # must match exactly
    path   = '/api'            # or '/' if that’s how it was set
)

resp = session.get('http://34.55.69.223:14001/api/newpuzzle')
print(resp.status_code, resp.text)