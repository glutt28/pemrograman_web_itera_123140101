def includeme(config):
    """Include routes configuration."""
    # HTTP method ditangani oleh @view_config decorator di views
    config.add_route('matakuliah_list', '/api/matakuliah')
    config.add_route('matakuliah_create', '/api/matakuliah')
    config.add_route('matakuliah_detail', '/api/matakuliah/{id}')
    config.add_route('matakuliah_update', '/api/matakuliah/{id}')
    config.add_route('matakuliah_delete', '/api/matakuliah/{id}')

