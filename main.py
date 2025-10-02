import os
import platform

if os.environ.get('DISPLAY') and platform.system() == 'Linux':
    os.environ['KIVY_GL_BACKEND'] = 'sdl2'
    os.environ['KIVY_WINDOW'] = 'sdl2'
    os.environ['KIVY_INPUT'] = 'mouse'

import spacy
import pandas as pd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.config import Config

Config.set('kivy', 'log_level', 'info')
Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

nlp = spacy.load("pt_core_news_sm")

df = pd.read_csv("datasets/dicionario_cultural2.csv")

glossario = {}
for _, row in df.iterrows():
    termo = str(row["termo"]).lower().strip()
    glossario[termo] = {
        "significado": row["significado"],
        "explicacao": row["explicacao"],
        "exemplo": row["exemplo"],
        "contextualizacao": row["contextualizacao"],
    }

contador_traducoes = 0

def traduzir_frase(frase):
    doc = nlp(frase)
    explicacoes = []

    for token in doc:
        termo = token.text.lower()
        if termo in glossario:
            g = glossario[termo]
            explicacoes.append(
                f"'{termo}' → {g['significado']}\n"
                f"Explicação: {g['explicacao']}\n"
                f"Exemplo: {g['exemplo']}\n"
                f"Contextualização: {g['contextualizacao']}\n"
            )

    return explicacoes if explicacoes else ["Nenhuma gíria encontrada."]

class TradutorCulturalApp(App):
    def build(self):
        self.title = 'Tradutor Cultural com IA'
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        title_label = Label(
            text='Tradutor Cultural Angolano',
            size_hint=(1, 0.08),
            font_size='20sp',
            bold=True
        )
        main_layout.add_widget(title_label)
        
        input_label = Label(
            text='Digite uma frase em português:',
            size_hint=(1, 0.05),
            font_size='14sp'
        )
        main_layout.add_widget(input_label)
        
        self.text_input = TextInput(
            hint_text='Ex: Eu tenho bué de dinheiro',
            multiline=True,
            size_hint=(1, 0.15),
            font_size='16sp'
        )
        main_layout.add_widget(self.text_input)
        
        button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.08))
        
        translate_button = Button(
            text='Traduzir',
            font_size='16sp',
            background_color=(0.2, 0.6, 0.8, 1),
            on_press=self.on_translate
        )
        button_layout.add_widget(translate_button)
        
        clear_button = Button(
            text='Limpar',
            font_size='16sp',
            background_color=(0.8, 0.4, 0.2, 1),
            on_press=self.on_clear
        )
        button_layout.add_widget(clear_button)
        
        main_layout.add_widget(button_layout)
        
        result_label = Label(
            text='Resultados:',
            size_hint=(1, 0.05),
            font_size='14sp'
        )
        main_layout.add_widget(result_label)
        
        scroll_view = ScrollView(size_hint=(1, 0.54))
        
        self.result_label = Label(
            text='Os resultados aparecerão aqui após a tradução.',
            size_hint=(1, None),
            font_size='14sp',
            text_size=(360, None),
            halign='left',
            valign='top',
            padding=(10, 10)
        )
        self.result_label.bind(texture_size=self.result_label.setter('size'))
        
        scroll_view.add_widget(self.result_label)
        main_layout.add_widget(scroll_view)
        
        self.counter_label = Label(
            text='Total de traduções: 0',
            size_hint=(1, 0.05),
            font_size='12sp',
            italic=True
        )
        main_layout.add_widget(self.counter_label)
        
        return main_layout
    
    def on_translate(self, instance):
        global contador_traducoes
        
        frase = self.text_input.text.strip()
        
        if not frase:
            self.result_label.text = 'Por favor, digite uma frase para traduzir.'
            return
        
        resultado = traduzir_frase(frase)
        
        resultado_texto = '\n'.join(resultado)
        resultado_texto += '\n' + '-' * 40
        
        self.result_label.text = resultado_texto
        
        contador_traducoes += 1
        self.counter_label.text = f'Total de traduções: {contador_traducoes}'
    
    def on_clear(self, instance):
        self.text_input.text = ''
        self.result_label.text = 'Os resultados aparecerão aqui após a tradução.'

if __name__ == "__main__":
    TradutorCulturalApp().run()
