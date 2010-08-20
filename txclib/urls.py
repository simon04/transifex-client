# These are the Transifex API urls

API_URLS = {
    'project_get' : '%(hostname)s/api/project/%(project)s/',
    'get_resources': '%(hostname)s/api/project/%(project)s/resources/',
    'push_file': '%(hostname)s/api/storage/',  #'%(hostname)s/api/project/%(project)s/files/',
    'pull_file': '%(hostname)s/projects/p/%(project)s/resource/%(resource)s/l/%(language)s/download/',
    'extract_translation': '%(hostname)s/api/project/%(project)s/resource/%(resource)s/%(language)s/',
    'extract_source': '%(hostname)s/api/project/%(project)s/files/'  #'%(hostname)s/api/project/%(project)s/files/',
}

