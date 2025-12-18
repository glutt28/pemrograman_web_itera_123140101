"""
Script untuk menambahkan data awal matakuliah ke database.
Jalankan script ini setelah migrasi database selesai.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from matakuliah_api.models import Base, DBSession
from matakuliah_api.models.matakuliah import Matakuliah
from pyramid.paster import get_appsettings, setup_logging
import sys
import os

# Path ke development.ini
config_path = os.path.join(os.path.dirname(__file__), 'development.ini')

def init_data():
    """Menambahkan data awal matakuliah"""
    try:
        # Load settings dari development.ini
        settings = get_appsettings(config_path)
        engine = create_engine(settings['sqlalchemy.url'])
        DBSession.configure(bind=engine)
        
        # Data awal
        initial_data = [
            {
                'kode_mk': 'IF101',
                'nama_mk': 'Algoritma dan Pemrograman',
                'sks': 3,
                'semester': 1
            },
            {
                'kode_mk': 'IF102',
                'nama_mk': 'Struktur Data',
                'sks': 3,
                'semester': 2
            },
            {
                'kode_mk': 'IF103',
                'nama_mk': 'Basis Data',
                'sks': 3,
                'semester': 3
            }
        ]
        
        # Cek apakah data sudah ada
        existing = DBSession.query(Matakuliah).count()
        if existing > 0:
            print(f"Database sudah memiliki {existing} data matakuliah.")
            print("Hapus data terlebih dahulu jika ingin menambahkan data awal.")
            return
        
        # Tambahkan data
        for data in initial_data:
            matakuliah = Matakuliah(**data)
            DBSession.add(matakuliah)
        
        DBSession.commit()
        print(f"Berhasil menambahkan {len(initial_data)} data matakuliah awal!")
        
    except Exception as e:
        DBSession.rollback()
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    init_data()

