"""
Script untuk membuat database PostgreSQL secara otomatis.
Jalankan script ini untuk membuat database matakuliah_db.

Usage:
    python create_database.py
"""

import sys
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Konfigurasi default
DEFAULT_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'user': 'postgres',
    'password': 'postgres',  # Ganti dengan password PostgreSQL Anda
    'database': 'postgres'  # Connect ke database default untuk membuat database baru
}

TARGET_DATABASE = 'matakuliah_db'


def create_database(config=None):
    """Membuat database PostgreSQL"""
    if config is None:
        config = DEFAULT_CONFIG.copy()
    
    print("=" * 50)
    print("Script Pembuat Database PostgreSQL")
    print("=" * 50)
    print(f"\nMencoba membuat database: {TARGET_DATABASE}")
    print(f"Host: {config['host']}")
    print(f"Port: {config['port']}")
    print(f"User: {config['user']}")
    print()
    
    # Connect ke database default (postgres)
    try:
        print("Menghubungkan ke PostgreSQL...")
        conn = psycopg2.connect(
            host=config['host'],
            port=config['port'],
            user=config['user'],
            password=config['password'],
            database=config['database']
        )
        
        # Set isolation level untuk bisa membuat database
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        print("✓ Berhasil terhubung ke PostgreSQL")
        
        # Cek apakah database sudah ada
        cursor.execute(
            "SELECT 1 FROM pg_database WHERE datname = %s",
            (TARGET_DATABASE,)
        )
        
        if cursor.fetchone():
            print(f"\n⚠ Database '{TARGET_DATABASE}' sudah ada!")
            response = input("Hapus dan buat ulang? (y/N): ").strip().lower()
            if response == 'y':
                # Terminate semua koneksi ke database
                cursor.execute(
                    sql.SQL("""
                        SELECT pg_terminate_backend(pg_stat_activity.pid)
                        FROM pg_stat_activity
                        WHERE pg_stat_activity.datname = %s
                        AND pid <> pg_backend_pid()
                    """),
                    (TARGET_DATABASE,)
                )
                # Hapus database
                cursor.execute(
                    sql.SQL("DROP DATABASE {}").format(
                        sql.Identifier(TARGET_DATABASE)
                    )
                )
                print(f"✓ Database '{TARGET_DATABASE}' dihapus")
            else:
                print("Operasi dibatalkan.")
                cursor.close()
                conn.close()
                return
        
        # Buat database
        print(f"\nMembuat database '{TARGET_DATABASE}'...")
        cursor.execute(
            sql.SQL("CREATE DATABASE {}").format(
                sql.Identifier(TARGET_DATABASE)
            )
        )
        print(f"✓ Database '{TARGET_DATABASE}' berhasil dibuat!")
        
        # Verifikasi
        cursor.execute(
            "SELECT 1 FROM pg_database WHERE datname = %s",
            (TARGET_DATABASE,)
        )
        if cursor.fetchone():
            print(f"✓ Verifikasi: Database '{TARGET_DATABASE}' ada di sistem")
        
        cursor.close()
        conn.close()
        
        print("\n" + "=" * 50)
        print("SUKSES! Database berhasil dibuat.")
        print("=" * 50)
        print(f"\nDatabase: {TARGET_DATABASE}")
        print(f"Host: {config['host']}:{config['port']}")
        print(f"User: {config['user']}")
        print("\nLangkah selanjutnya:")
        print("1. Edit development.ini dengan kredensial database")
        print("2. Edit alembic.ini dengan kredensial yang sama")
        print("3. Jalankan: alembic revision --autogenerate -m 'Initial migration'")
        print("4. Jalankan: alembic upgrade head")
        print("5. Jalankan: pserve development.ini")
        
    except psycopg2.OperationalError as e:
        print(f"\n✗ Error koneksi: {e}")
        print("\nKemungkinan penyebab:")
        print("1. PostgreSQL service tidak berjalan")
        print("2. Host/port salah")
        print("3. Username/password salah")
        print("\nSolusi:")
        print("- Pastikan PostgreSQL service berjalan")
        print("- Edit konfigurasi di script ini (variabel DEFAULT_CONFIG)")
        print("- Atau gunakan pgAdmin untuk membuat database")
        sys.exit(1)
        
    except psycopg2.Error as e:
        print(f"\n✗ Error database: {e}")
        sys.exit(1)
        
    except KeyboardInterrupt:
        print("\n\nOperasi dibatalkan oleh user.")
        sys.exit(1)


def get_config_from_user():
    """Minta konfigurasi dari user"""
    print("=" * 50)
    print("Konfigurasi Database PostgreSQL")
    print("=" * 50)
    print("\nTekan Enter untuk menggunakan nilai default")
    print()
    
    config = DEFAULT_CONFIG.copy()
    
    host = input(f"Host [{config['host']}]: ").strip()
    if host:
        config['host'] = host
    
    port = input(f"Port [{config['port']}]: ").strip()
    if port:
        config['port'] = int(port)
    
    user = input(f"Username [{config['user']}]: ").strip()
    if user:
        config['user'] = user
    
    password = input(f"Password [{config['password']}]: ").strip()
    if password:
        config['password'] = password
    
    return config


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Membuat database PostgreSQL untuk aplikasi matakuliah'
    )
    parser.add_argument(
        '--interactive', '-i',
        action='store_true',
        help='Mode interaktif untuk memasukkan konfigurasi'
    )
    parser.add_argument(
        '--host',
        help='Host PostgreSQL (default: localhost)'
    )
    parser.add_argument(
        '--port',
        type=int,
        help='Port PostgreSQL (default: 5432)'
    )
    parser.add_argument(
        '--user', '-u',
        help='Username PostgreSQL (default: postgres)'
    )
    parser.add_argument(
        '--password', '-p',
        help='Password PostgreSQL'
    )
    
    args = parser.parse_args()
    
    if args.interactive:
        config = get_config_from_user()
    else:
        config = DEFAULT_CONFIG.copy()
        if args.host:
            config['host'] = args.host
        if args.port:
            config['port'] = args.port
        if args.user:
            config['user'] = args.user
        if args.password:
            config['password'] = args.password
    
    create_database(config)

