import time
from datetime import datetime



x = time.time()

print(f'Local time: {time.ctime(x)}')

# Converte o tempo para um objeto datetime
dt_obj = datetime.fromtimestamp(x)

# Formata o objeto datetime para o modelo brasileiro de hora e data
formato_brasileiro = dt_obj.strftime('%d/%m/%Y %H:%M:%S')

print(f'Horário local (Brasil): {formato_brasileiro}')