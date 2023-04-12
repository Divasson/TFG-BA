from django.shortcuts import redirect
from createOpenProject.models import Project
from django.contrib import messages
import json
import pandas as pd
from django.conf import settings



def isUserLoggedIn_or_hisProject(request,id_project):
    user = request.user
    print(user)
    if not user.is_authenticated:
        return redirect('/index.html')
    
    try:
        project = request.user.projects.get(id=id_project)
        return project
    except Project.DoesNotExist:
        #messages.error(request, 'Project not found')
        return redirect('/index.html')
    
    return project







   
""" def sacarDatosProyecto(project):
    print( (project.archivoDatosNA))
    print("hola")
    if project.archivoDatosNA:
        if (project.project_state>=4) :
            df = open_file(str(settings.BASE_DIR)+str(project.archivoDatosNA.url),
                   dtypes=str(settings.BASE_DIR)+str(project.tiposDatosProcesados.url))
            return df
    
    if project.tiposDatosProcesados:
        df = open_file(str(settings.BASE_DIR)+str(project.archivoDatos.url),
                dtypes=str(settings.BASE_DIR)+str(project.tiposDatosProcesados.url))
        return df
    else:
        df = open_file(str(settings.BASE_DIR)+str(project.archivoDatos.url))
    return df
def open_file(filex,dtypes=None):
    
    if dtypes:
        with open(dtypes, 'r') as j:
            tipos = json.loads(j.read())
        if filex.endswith('.csv'):
            return pd.read_csv(filex,dtype=tipos)
        else:
            return pd.read_excel(filex,dtype=tipos)
    else:
        if filex.endswith('.csv'):
            return pd.read_csv(filex)
        else:
            return pd.read_excel(filex) """