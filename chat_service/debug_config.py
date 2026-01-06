# debug_config.py
import os
import sys

# Додаємо корінь в шляхи (як ми робили в env.py)
sys.path.insert(0, "/app")

print("-" * 30)
print("🔍 DEBUGGING CONFIG")
print("-" * 30)

# 1. Перевірка сирих даних
host_file = os.getenv("POSTGRES_HOST_FILE")
print(f"1. ENV 'POSTGRES_HOST_FILE': '{host_file}'")

if host_file and os.path.exists(host_file):
    with open(host_file, 'r') as f:
        print(f"2. File content: '{f.read().strip()}'")
else:
    print("2. File content: [FILE NOT FOUND OR ENV NOT SET]")

print("-" * 30)

# 2. Перевірка Pydantic
try:
    from shared_packages.core.config import PostgresSettings
    
    # Імітуємо ініціалізацію, як в auth_service
    class TestConfig(PostgresSettings):
        pass

    settings = TestConfig()
    
    print(f"3. Pydantic 'POSTGRES_HOST_FILE': '{settings.POSTGRES_HOST_FILE}'")
    print(f"4. Pydantic 'POSTGRES_HOST' (default): '{settings.POSTGRES_HOST}'")
    
    # НАЙГОЛОВНІШЕ: Що генерується в URI?
    print(f"5. FINAL URI: {settings.SQLALCHEMY_DATABASE_URI}")

except Exception as e:
    print(f"❌ ERROR in Pydantic: {e}")

print("-" * 30)