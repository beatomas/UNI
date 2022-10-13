
def DetectarParaules(resposta,prohibides):
    c_resposta = set(resposta.lower().split(" "))
    c_out = c_resposta & prohibides
    if (c_out == set()):
        c_out = None
    return (c_out)