import requests

addresses = ["0xfd22004806a6846ea67ad883356be810f0428793","0xf0d6999725115e3ead3d927eb3329d63afaec09b","0xd6a984153acb6c9e2d788f08c2465a1358bb89a7", "0x762b35b809ac4266beb076ff0f28547ad571201e", "0x7d4823262bd2c6e4fa78872f2587dda2a65828ed"]
nftList = []
nftCountDict = {}
OncePerResultList = []

for addy in addresses:
    url = "https://api.etherscan.io/api?module=account&action=tokennfttx&address="+addy+"&page=1&offset=100&startblock=13399670&endblock=13445170&sort=asc&apikey=PGHPWYQ2STMYUK2PVJN27UY4HFS6Q5IZVX"
    response = requests.get(url)
    ac = response.json()
    result = ac.get("result")
    for item in result:
        name = item["tokenName"]
        nftList.append(name)


            
for nft in nftList:
    count = nftList.count(nft)
    nftCountDict.update({nft:count})

print(sorted(nftCountDict.items(), key=lambda t:t[1], reverse=True))

