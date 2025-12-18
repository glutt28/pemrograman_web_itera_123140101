from pyramid.view import view_config
from sqlalchemy.exc import IntegrityError
from ..models import DBSession
from ..models.matakuliah import Matakuliah


@view_config(route_name='matakuliah_list', renderer='json', request_method='GET')
def matakuliah_list(request):
    """Mendapatkan semua matakuliah"""
    try:
        matakuliahs = DBSession.query(Matakuliah).all()
        return {
            'matakuliahs': [mk.to_dict() for mk in matakuliahs]
        }
    except Exception as e:
        request.response.status = 500
        return {'error': str(e)}


@view_config(route_name='matakuliah_detail', renderer='json', request_method='GET')
def matakuliah_detail(request):
    """Mendapatkan detail satu matakuliah"""
    try:
        matakuliah_id = int(request.matchdict['id'])
        matakuliah = DBSession.query(Matakuliah).filter_by(id=matakuliah_id).first()
        
        if not matakuliah:
            request.response.status = 404
            return {'error': 'Matakuliah tidak ditemukan'}
        
        return matakuliah.to_dict()
    except ValueError:
        request.response.status = 400
        return {'error': 'ID tidak valid'}
    except Exception as e:
        request.response.status = 500
        return {'error': str(e)}


@view_config(route_name='matakuliah_create', renderer='json', request_method='POST')
def matakuliah_create(request):
    """Menambahkan matakuliah baru"""
    try:
        # Parse JSON body
        data = request.json_body
        
        # Validasi required fields
        required_fields = ['kode_mk', 'nama_mk', 'sks', 'semester']
        for field in required_fields:
            if field not in data:
                request.response.status = 400
                return {'error': f'Field {field} harus diisi'}
        
        # Validasi tipe data
        try:
            sks = int(data['sks'])
            semester = int(data['semester'])
        except (ValueError, TypeError):
            request.response.status = 400
            return {'error': 'SKS dan semester harus berupa angka'}
        
        # Validasi kode_mk tidak kosong
        if not data['kode_mk'] or not data['kode_mk'].strip():
            request.response.status = 400
            return {'error': 'Kode matakuliah tidak boleh kosong'}
        
        if not data['nama_mk'] or not data['nama_mk'].strip():
            request.response.status = 400
            return {'error': 'Nama matakuliah tidak boleh kosong'}
        
        # Buat matakuliah baru
        matakuliah = Matakuliah(
            kode_mk=data['kode_mk'].strip(),
            nama_mk=data['nama_mk'].strip(),
            sks=sks,
            semester=semester
        )
        
        DBSession.add(matakuliah)
        DBSession.flush()
        
        request.response.status = 201
        return matakuliah.to_dict()
        
    except IntegrityError:
        DBSession.rollback()
        request.response.status = 409
        return {'error': 'Kode matakuliah sudah ada'}
    except Exception as e:
        DBSession.rollback()
        request.response.status = 500
        return {'error': str(e)}


@view_config(route_name='matakuliah_update', renderer='json', request_method='PUT')
def matakuliah_update(request):
    """Mengupdate data matakuliah"""
    try:
        matakuliah_id = int(request.matchdict['id'])
        matakuliah = DBSession.query(Matakuliah).filter_by(id=matakuliah_id).first()
        
        if not matakuliah:
            request.response.status = 404
            return {'error': 'Matakuliah tidak ditemukan'}
        
        # Parse JSON body
        data = request.json_body
        
        # Update fields jika ada
        if 'kode_mk' in data:
            if not data['kode_mk'] or not data['kode_mk'].strip():
                request.response.status = 400
                return {'error': 'Kode matakuliah tidak boleh kosong'}
            matakuliah.kode_mk = data['kode_mk'].strip()
        
        if 'nama_mk' in data:
            if not data['nama_mk'] or not data['nama_mk'].strip():
                request.response.status = 400
                return {'error': 'Nama matakuliah tidak boleh kosong'}
            matakuliah.nama_mk = data['nama_mk'].strip()
        
        if 'sks' in data:
            try:
                matakuliah.sks = int(data['sks'])
            except (ValueError, TypeError):
                request.response.status = 400
                return {'error': 'SKS harus berupa angka'}
        
        if 'semester' in data:
            try:
                matakuliah.semester = int(data['semester'])
            except (ValueError, TypeError):
                request.response.status = 400
                return {'error': 'Semester harus berupa angka'}
        
        DBSession.flush()
        
        return matakuliah.to_dict()
        
    except IntegrityError:
        DBSession.rollback()
        request.response.status = 409
        return {'error': 'Kode matakuliah sudah ada'}
    except ValueError:
        request.response.status = 400
        return {'error': 'ID tidak valid'}
    except Exception as e:
        DBSession.rollback()
        request.response.status = 500
        return {'error': str(e)}


@view_config(route_name='matakuliah_delete', renderer='json', request_method='DELETE')
def matakuliah_delete(request):
    """Menghapus data matakuliah"""
    try:
        matakuliah_id = int(request.matchdict['id'])
        matakuliah = DBSession.query(Matakuliah).filter_by(id=matakuliah_id).first()
        
        if not matakuliah:
            request.response.status = 404
            return {'error': 'Matakuliah tidak ditemukan'}
        
        DBSession.delete(matakuliah)
        DBSession.flush()
        
        request.response.status = 200
        return {'message': 'Matakuliah berhasil dihapus'}
        
    except ValueError:
        request.response.status = 400
        return {'error': 'ID tidak valid'}
    except Exception as e:
        DBSession.rollback()
        request.response.status = 500
        return {'error': str(e)}

