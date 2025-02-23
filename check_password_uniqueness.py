from probables import BloomFilter

# Перевірка, чи password уже існує у фільтрі Блума
def check_password_uniqueness(bloom, new_passwords_to_check):
    for password in new_passwords_to_check:
        if not password:
            yield (password, "некоректний")
        elif bloom.check(password):
            yield (password, "вже використаний")
        else:
            yield (password, "унікальний")

if __name__ == "__main__":
    # Ініціалізація фільтра Блума
    bloom = BloomFilter(1000, 0.1)

    # Додавання існуючих паролів
    existing_passwords = ["password123", "admin123", "qwerty123"]
    for password in existing_passwords:
        bloom.add(password)

    # Перевірка нових паролів
    new_passwords_to_check = ["password123", "newpassword", "admin123", "guest"]
    results = dict(check_password_uniqueness(bloom, new_passwords_to_check))

    # Виведення результатів
    for password, status in results.items():
        print(f"Пароль '{password}' - {status}.")
