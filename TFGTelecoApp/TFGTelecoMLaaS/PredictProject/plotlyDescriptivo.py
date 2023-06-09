# Importamos las librerias mínimas necesarinoatasdas
import numpy as np
import pandas as pd
import plotly.express as px


def plotMultiple(df,variable1,variable2,variableColor): 
    """
    This function plots a scatter plot or a box plot depending on the type of the variables.
    If both variables are numeric, it plots a scatter plot.
    If one of the variables is numeric, it plots a box plot.
    If both variables are categorical, it plots a bar plot.
    NO HACE PLOTS EN FUNCION DEL TIEMPO
    
    Parameters
    ----------
    df: DataFrame
        The dataframe to be plotted.
    variable1: str
        The name of the first variable.
    variable2: str
        The name of the second variable.
    
    Returns
    -------
    fig: Plotly figure
        The figure to be plotted.
    
    Examples
    --------
    >>> plotMultiple(df2,"MaritalDesc","RaceDesc")
    >>> plotMultiple(df2,"Age","YearlyIncome")
    >>> plotMultiple(df2,"Gender","Education")
    """
    df = df.copy()
    j           = df.copy()
    j["num1"]   = 1
    fig         = 0
    
    print(df.dtypes)
    
    if variable1==variable2:
        if np.issubdtype(df[variable1].dtype, np.number):
            if np.issubdtype(df[variableColor].dtype, np.number):
                fig = px.histogram(data_frame=df, x=variable1,nbins=60)
            else:
                fig = px.histogram(data_frame=df, x=variable1,color=variableColor,facet_row=variableColor,nbins=60)
            #fig = px.histogram(data_frame=df, x=variable1,color=variableColor,barmode="overlay",nbins=60)
            fig.update_yaxes(matches=None)
            fig.for_each_yaxis(lambda yaxis: yaxis.update(showticklabels=True))
            fig.update_layout(title="Histograma en total de la variable: "+variable1)
        else:
            fig = px.pie(data_frame=j.groupby(variable1,as_index=False).count(),names=variable1,values='num1',
                         color=variable1,color_discrete_map=getColorsforVariable(df,variable1,colorATener),category_orders=getOrden(df,variable1))  
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(title="Porcentage de observaciones por cada valor de la variable: "+variable1)            
    else:
        if np.issubdtype(df[variable1].dtype, np.number) & np.issubdtype(df[variable2].dtype, np.number): 
            fig = px.scatter(data_frame=j, x=variable1, y=variable2, color=variableColor)
            fig.update_layout(title="Correlacion entre "+variable1+" y "+variable2) 

        elif np.issubdtype(df[variable1].dtype, np.number): 
            #print(df[variable2].dtype)
            if "datetime" in str(df[variable2].dtype):
                fig = px.line(data_frame=j, x=variable2, y=variable1)
                fig.update_layout(title="Evolución de "+variable1+" ")
                
            else:
                fig = px.box(data_frame=j, x=variable1, y=variable2,orientation='h',
                            color=variable2,color_discrete_map=getColorsforVariable(df,variable2,colorATener),category_orders=getOrden(df,variable2))
                fig.update_layout(title="Box Plot de la distribucion de "+variable1+" por cada valor de "+variable2)

        elif np.issubdtype(df[variable2].dtype, np.number): 
            if "datetime" in str(df[variable1].dtype):
                fig = px.line(data_frame=j, x=variable1, y=variable2)
                fig.update_layout(title="Evolución de "+variable2+" ")
            else: 
                fig = px.violin(data_frame=j, y=variable2, x=variable1,orientation='v',
                            color=variable1,color_discrete_map=getColorsforVariable(df,variable1,colorATener),category_orders=getOrden(df,variable1))
                fig.update_layout(title="Violin Plot de la distribucion de "+variable2+" por cada valor de "+variable1)
        else: 
            j[variable1] = j[variable1].astype("object")
            j[variable2] = j[variable2].astype("object")
            if (j[variable2].nunique()>10) & (j[variable1].nunique()>10):
                fig = px.pie(data_frame=j.groupby(variable1,as_index=False).count(),names=variable1,values='num1',
                         color=variable1,color_discrete_map=getColorsforVariable(df,variable1,colorATener),category_orders=getOrden(df,variable1))  
                fig.update_traces(textposition='inside', textinfo='percent+label')
                fig.update_layout(title="Porcentage de observaciones por cada valor de la variable: "+variable1)            
            else:
                if (df[variable1].nunique()>10):        
                    fig = px.bar(j,x=variable1,y="num1",color=variableColor,barmode="group",facet_col=variable2)
                    fig.update_layout(title="Numero de muestras observadas de "+variable2+" por cada valor de "+variable1,yaxis_title="Numero de muestras observadas")
                else:
                    fig = px.bar(j,x=variable2,y="num1",color=variableColor,barmode="group",facet_col=variable1)
                    fig.update_layout(title="Numero de muestras observadas de "+variable1+" por cada valor de "+variable2,yaxis_title="Numero de muestras observadas")
                    

    return fig

def getOrden(df,variableColoreadaAOrdenar):
    """
    This function returns a dictionary with the unique values of a variable and the order in which they appear in the dataframe.

    Parameters
    ----------
    df : pandas dataframe
        The dataframe with the data.
    variableColoreadaAOrdenar : string
        The name of the variable to be ordered.

    Returns
    -------
    diccionario : dictionary
        The dictionary with the unique values of the variable and the order in which they appear in the dataframe.
    """    
    df = df.copy()
    diccionario = {}
    lista = list(np.sort(df[variableColoreadaAOrdenar].unique()))
    diccionario[variableColoreadaAOrdenar] = lista
    return diccionario


def getColorsforVariable(df,columnaCategorica,i=1):
    """
    This function takes a dataframe and a column name as input and returns a dictionary with the unique values of the column as keys and the corresponding colors as values.

    Parameters
    ----------
    df : pandas dataframe
        The dataframe containing the column of interest.
    columnaCategorica : string
        The name of the column of interest.

    Returns
    -------
    diccionario : dictionary
        A dictionary with the unique values of the column as keys and the corresponding colors as values.
    """
    df = df.copy()
    diccionario = {}
    
    for count,variable in enumerate(np.sort(list(df[columnaCategorica].unique()))):
        if i==0:
            diccionario[variable] = px.colors.qualitative.Safe[count-len(px.colors.qualitative.Safe)*int(count/len(px.colors.qualitative.Safe))]
        elif i==1:
            diccionario[variable] = px.colors.qualitative.Alphabet[count-len(px.colors.qualitative.Alphabet)*int(count/len(px.colors.qualitative.Alphabet))]
        elif i==2:
            diccionario[variable] = px.colors.qualitative.Bold[count-len(px.colors.qualitative.Bold)*int(count/len(px.colors.qualitative.Bold))]
        elif i==3:
            diccionario[variable] = px.colors.qualitative.Dark24[count-len(px.colors.qualitative.Dark24)*int(count/len(px.colors.qualitative.Dark24))]
        else:
            diccionario[variable] = px.colors.qualitative.Plotly[count-len(px.colors.qualitative.Plotly)*int(count/len(px.colors.qualitative.Plotly))]
    return diccionario

colorATener = 2
