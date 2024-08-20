from mnemonic import Mnemonic

# SHA-256 хеш от изображението
sha256_hash = "df215e08fb9dd5a08e0e7fbc9d8b44fde2451614957d3ccf3f52fc9205af5a06"

# Инициализирайте BIP39 генератора
mnemo = Mnemonic("english")

# Генерирайте мнемоничната фраза
mnemonic = mnemo.to_mnemonic(bytes.fromhex(sha256_hash))

print(mnemonic)
