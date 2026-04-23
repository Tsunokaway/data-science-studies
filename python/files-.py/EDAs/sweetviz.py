import pandas as pd
import sweetviz as sv
# Carregar os dados
data = pd.read_csv('dados.csv')
# Gerar o relatório sweetviz
report = sv.analyze(data)
# Exibir o relatório
report.show_html('sweetviz_report.html')
# O código acima carrega um arquivo CSV chamado 'dados.csv', gera um relatório de análise exploratória usando a biblioteca Sweetviz e salva o relatório em um arquivo HTML chamado 'sweetviz_report.html'. Certifique-se de ter a biblioteca Sweetviz instalada em seu ambiente Python para executar este código.