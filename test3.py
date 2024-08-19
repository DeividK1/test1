from hdwallet import BIP84HDWallet
from hdwallet.cryptocurrencies import BitcoinMainnet
from concurrent.futures import ProcessPoolExecutor, as_completed
import itertools
import string

def проверка_на_мнемоник(passphrase):
    try:
        wallet = BIP84HDWallet(cryptocurrency=BitcoinMainnet)
        wallet.from_mnemonic(mnemonic='blossom educate state course sick fresh color divide number soap please pull glide weather join grit depart dynamic tenant leopard alter piano slight room', passphrase=passphrase)
        address = wallet.address()
        return passphrase, address
    except Exception as e:
        print(f"Грешка при проверка на passphrase {passphrase}: {e}")
        return passphrase, None

def парола_генератор(min_length=1, max_length=5):
    characters = string.ascii_lowercase + string.digits  # малки букви и цифри
    for length in range(min_length, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            yield ''.join(combination)

def main():
    print("Започва обработката на паролите...")  # Съобщение, че програмата работи

    num_workers = 12

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        future_to_passphrase = {}
        completed = 0
        total_combinations = sum(len(string.ascii_lowercase + string.digits) ** i for i in range(1, 20))  # Общо пароли от дължина 1 до 19

        for passphrase in парола_генератор(min_length=1, max_length=5):
            future = executor.submit(проверка_на_мнемоник, passphrase)
            future_to_passphrase[future] = passphrase

            # Проверка на завършените задачи
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
                progress = (completed / total_combinations) * 100
                print(f"\rНапредък: {progress:.2f}% ({completed}/{total_combinations})", end='')

if __name__ == "__main__":
    main()
    input ()
