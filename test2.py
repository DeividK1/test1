from hdwallet import BIP84HDWallet
from hdwallet.cryptocurrencies import BitcoinMainnet
from concurrent.futures import ProcessPoolExecutor, as_completed

def проверка_на_мнемоник(passphrase):
    try:
        wallet = BIP84HDWallet(cryptocurrency=BitcoinMainnet)
        wallet.from_mnemonic(mnemonic='blossom educate state course sick fresh color divide number soap please pull glide weather join grit depart dynamic tenant leopard alter piano slight room', passphrase=passphrase)
        address = wallet.address()
        return passphrase, address
    except Exception as e:
        print(f"Грешка при проверка на passphrase {passphrase}: {e}")
        return passphrase, None

def main():
    print("Започва обработката на ключовите думи...")  # Съобщение, че програмата работи
    
    wallet = BIP84HDWallet(cryptocurrency=BitcoinMainnet)

    data_keys = []
    try:
        with open('words2.txt', "r") as f:
            for line in f:
                data_keys.extend(line.split())
    except FileNotFoundError:
        print("Файлът words2.txt не беше намерен.")
        return
    except Exception as e:
        print(f"Грешка при четене на файла: {e}")
        return

    if not data_keys:
        print("Файлът words2.txt е празен.")
        return

    print(f"Намерени ключови думи: {len(data_keys)}")

    num_workers = 6

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        future_to_passphrase = {executor.submit(проверка_на_мнемоник, passphrase): passphrase for passphrase in data_keys}
        completed = 0

        for future in as_completed(future_to_passphrase):
            passphrase = future_to_passphrase[future]
            try:
                резултат_passphrase, address = future.result()
                if address == 'bc1qcyrndzgy036f6ax370g8zyvlw86ulawgt0246r':
                    print("Успех", passphrase)
                    return
                else:
                    print("адрес:", address)
            except Exception as e:
                print(f"Грешка при получаване на резултат за passphrase {passphrase}: {e}")

            # Обновяване на напредъка
            completed += 1
            progress = (completed / len(data_keys)) * 100
            print(f"\rНапредък: {progress:.2f}% ({completed}/{len(data_keys)})", end='')

if __name__ == "__main__":
    main()
