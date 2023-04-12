
def get_modelo_params(modelo,tipoModelo):
    if str(tipoModelo).lower() == "knn":
        params = modelo.get_params()
        dict_response = {}
        dict_response["n_neighbours"] = params["n_neighbors"]
        dict_response["weights"] = params["weights"]
        dict_response["metric"] = params["metric"]
        return dict_response
    elif str(tipoModelo).lower() == "svc":
        params = modelo.get_params()
        dict_response = {}
        dict_response["kernel"] = params["kernel"]
        dict_response["C"] = params["C"]
        dict_response["gamma"] = params["gamma"]
        return dict_response
    return False

