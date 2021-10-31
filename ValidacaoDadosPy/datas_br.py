from datetime import datetime, timedelta


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def mes_cadastro(self):
        meses = [
            'Janeiro', 'Fevereiro', 'Março', 'Abril',
            'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
            'Outubro', 'Novembro', 'Dezembro'
        ]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses[mes_cadastro]

    def dia_semana(self):
        dias = [
            'Segunda', 'Terça', 'Quarta',
            'Quinta', 'Sexta', 'Sábado', 'Domingo'
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dias[dia_semana]

    def formata_data(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y %H:%M')
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro
    