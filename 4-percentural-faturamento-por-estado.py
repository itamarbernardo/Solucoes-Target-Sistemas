estado_SP = 67836.43
estado_RJ = 36678.66
estado_MG = 29229.88
estado_ES = 27165.48
outros_estados = 19849.53

total_faturamento = estado_SP + estado_RJ + estado_MG + estado_ES + outros_estados

percentual_SP = estado_SP/total_faturamento
percentual_RJ = estado_RJ/total_faturamento
percentual_MG = estado_MG/total_faturamento
percentual_ES = estado_ES/total_faturamento
percentual_outros = outros_estados/total_faturamento

print('Percentual de representação no valor total mensal da distribuidora por estado:')
print('SP -  ', percentual_SP*100, '%' )
print('RJ -  ', percentual_RJ*100, '%' )
print('MG -  ', percentual_MG*100, '%' )
print('ES -  ', percentual_ES*100, '%' )
print('Outros Estados -  ', percentual_outros*100, '%' )