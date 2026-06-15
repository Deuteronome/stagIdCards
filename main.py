import pandas as pd
import openpyxl
from jinja2 import Template
from weasyprint import HTML

from pathlib import Path

directory = Path('./src')
logo_path = Path('./model/logoE2Ctrans.png').resolve().as_uri()
font_path = Path('./model/CaviarDreams.ttf').resolve().as_uri()
bold_font_path = Path('./model/CaviarDreams_Bold.ttf').resolve().as_uri()

for file in directory.glob('*.xlsx'):
    file_name = file.stem
    df = pd.read_excel(file)
    df = df.rename(columns={
        "Nom" : "nom",
        "Prénom" : "prenom",
        "Compte Kwartz": "kwartz",
        "mdp mail" : "mdp"
    })
    #print(df.axes)
    template = Template(open('./model/template.html').read())
    html = template.render(users=df.to_dict(orient="records"),image=logo_path, font=font_path, bfont=bold_font_path)
    HTML(string=html).write_pdf(f"./output/{file_name}.pdf")

