# Projektarbeit Python
# 1. Tokenisiere den Text
# 2. Entferne Satzzeichen ("?",".","!",",",";",":","'","-","_") und Stop-Words
# 3. Zähle wie oft die übrig gebliebenen Worte im Text vorkommen und
# normiere dies mit dem maximalen Wert
# 4. Teile den Text in einzelne Sätze auf
# 5. Bestimme den Word Count für jeden Satz.
# 6. Wähle aus den Sätzen die 20% der Sätze aus, die den höchsten Word
# Count haben.

# Zuerst Module importieren
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import string
from collections import defaultdict

# NLTK-Ressourcen
nltk.download('punkt')
nltk.download('stopwords')

#---------------------------------------------------------------------------------------------------------
class TextAnalyzer:
    """
    Klasse für Textverarbeitung.
    """
    def __init__(self):
        self.stop_words = set(stopwords.words('english')) # Eglisch Wörter
        self.punctuation = set(string.punctuation)  # Satzzeichen

    def tokenize_text(self, text):
        """
        Tokenisiert den Text in Sätze und Wörter.
        Parameter:
            text (str): Der Eingabetext, der tokenisiert werden soll.
        Rückgabe:
            tuple: Ein Tupel aus zwei Listen:
                - sentences: Liste der Sätze.
                - words: Liste der Wörter.
        """
        sentences = sent_tokenize(text)  # Sätze
        words = word_tokenize(text)      # Wörter
        return sentences, words

    def remove_punctuation(self, words):
        """
        Entfernt Satzzeichen aus einer Liste von Wörtern.
        Parameter:
            words (list): Liste von Wörtern, die Satzzeichen enthalten.
        Rückgabe:
            list: Liste der Wörter ohne Satzzeichen.
        """
        return [word for word in words if word not in self.punctuation]

    def remove_stopwords(self, words):
        """
        Entfernt Stoppwörter aus einer Liste von Wörtern.
        Parameter:
            words (list): Liste von Wörtern, die Stoppwörter enthalten.
        Rückgabe:
            list: Liste der Wörter ohne Stoppwörter.
        """
        return [word for word in words if word.lower() not in self.stop_words]

    def preprocess_text(self, text):
        """
        Verarbeitet den Text vor: Tokenisierung, Entfernung von Satzzeichen und Stoppwörtern.
        Parameter:
            text (str): Der Eingabetext, der verarbeitet werden soll.
        Rückgabe:
            tuple: Ein Tupel aus drei Listen:
                - sentences: Liste der Sätze.
                - words: Liste der Wörter ohne Satzzeichen.
                - cleaned_words: Liste der Wörter ohne Stoppwörter.
        """
        sentences, words = self.tokenize_text(text)  # Text tokenisieren
        filtered_words = self.remove_punctuation(words)  # Satzzeichen entfernen
        cleaned_words = self.remove_stopwords(filtered_words)  # Stoppwörter entfernen
        return sentences, filtered_words, cleaned_words

    def count_word_frequencies(self, words):
        """
        Zählt die Häufigkeit jedes Wortes in der Liste.
        Parameter:
            words (list): Liste der Wörter.
        Rückgabe:
            dict: Ein Dictionary, das jedes Wort als Schlüssel und seine Häufigkeit als Wert enthält.
        """
        word_counts = defaultdict(int) # Dict mit 0
        for word in words:
            word_counts[word] += 1
        return word_counts

    def calculate_sentence_counts(self, sentences, word_counts):
        """
        Berechnet den Sentence Count für jeden Satz basierend auf den Word Counts.
        Parameter:
            sentences (list): Liste der Sätze.
            word_counts (dict): Ein Dictionary, das die Häufigkeit jedes Wortes enthält.
        Rückgabe:
            dict: Ein Dictionary, das jeden Satz als Schlüssel und seinen Sentence Count als Wert enthält.
        """
        sentence_counts = {}
        for sentence in sentences:   
            words_in_sentence = self.remove_punctuation(word_tokenize(sentence))   # Satz tokenisieren in Wörter und Satzzeichen entfernen
            count = sum(word_counts.get(word, 0) for word in words_in_sentence)    # Word Counts summieren
            sentence_counts[sentence] = count
        return sentence_counts


#---------------------------------------------------------------------------------------------------------------------------------------
def summarize_text(sentence_counts):
    """
    Wählt die 20% der Sätze mit dem höchsten Sentence Count aus und gibt sie als Zusammenfassung zurück.
    Parameter:
        sentence_counts (dict): Ein Dictionary, das jeden Satz als Schlüssel und seinen Sentence Count als Wert enthält.
    Rückgabe:
        str: Die zusammengefassten Sätze als String.
    """
    sorted_sentences = sorted(sentence_counts.items(), key=lambda x: x[1], reverse=True)  # Sätze sortieren nach Sentence Count, absteigend
    num_sentences = len(sorted_sentences)   # Anzahl der Sätze berechnen
    num_summary_sentences = max(1, int(0.2 * num_sentences))  # 20% der Gesamtzahl, mindestens 1 Satz
    summary_sentences = [sentence for sentence, count in sorted_sentences[:num_summary_sentences]]      # Obersten 20% der Sätze
    summary = " ".join(summary_sentences)  # Sätze zu einem String
    return summary

#---------------------------------------------------------------------------------------------------------------------------------
# Beispielverwendung
if __name__ == "__main__":
    # Eingabetext
    text = """
Climate science is a vast and multifaceted discipline that encompasses a wide range of scientific fields and methodologies. At its core, it seeks to understand the complex interactions between the atmosphere, oceans, land surfaces, ice sheets, and living organisms that collectively determine Earth's climate. Through observation, experimentation, and modeling, climate scientists strive to unravel the intricacies of our planet's climate system and predict how it will evolve in response to natural and human-induced changes.

One of the fundamental principles of climate science is the study of greenhouse gases and their role in regulating Earth's temperature. Greenhouse gases, such as carbon dioxide (CO2), methane (CH4), and nitrous oxide (N2O), trap heat in the atmosphere, preventing it from escaping into space. This natural greenhouse effect is essential for maintaining Earth's temperature within a range that is conducive to life as we know it. However, human activities, particularly the burning of fossil fuels and deforestation, have significantly increased the concentrations of greenhouse gases in the atmosphere, leading to global warming and climate change.

Understanding the drivers of climate change is essential for devising effective strategies to mitigate its impacts and adapt to its consequences. Climate scientists use a variety of tools and techniques to study past climate variations, monitor current trends, and project future scenarios. Paleoclimate studies, for example, use geological and biological evidence to reconstruct past climates and understand the natural variability of the climate system. Instrumental records, such as temperature measurements, satellite observations, and ice core data, provide valuable insights into contemporary climate trends and help scientists identify patterns and trends over time. Climate models, complex computer simulations of Earth's climate system, allow scientists to explore how different factors, such as greenhouse gas emissions, land use changes, and volcanic eruptions, influence global and regional climate patterns.

One of the most significant contributions of climate science is its ability to inform policy decisions and guide climate action at the local, national, and international levels. The Intergovernmental Panel on Climate Change (IPCC), established by the United Nations in 1988, serves as the leading international body for assessing the science of climate change, its impacts, and potential adaptation and mitigation strategies. IPCC reports, which are based on a comprehensive review of the latest scientific literature, provide policymakers with the knowledge and evidence they need to make informed decisions about climate policy and regulation.

Climate science also plays a crucial role in fostering public awareness and understanding of climate change. By communicating the scientific consensus on climate change and its potential consequences, climate scientists help empower individuals and communities to take action to reduce their carbon footprint, advocate for climate policies, and support initiatives that promote sustainability and resilience. Education and outreach efforts, such as climate literacy programs, public lectures, and media campaigns, help raise awareness about the urgency of addressing climate change and inspire collective action at all levels of society.

In addition to its scientific and educational contributions, climate science drives innovation and technological development in sectors such as renewable energy, agriculture, transportation, and urban planning. By studying the impacts of climate change on ecosystems, agriculture, and human health, climate scientists provide valuable insights into the risks and vulnerabilities that communities and industries face in a changing climate. This knowledge informs the development of adaptive strategies and technologies that can help mitigate these risks and build resilience to climate impacts.

Renewable energy technologies, such as solar, wind, and hydroelectric power, offer sustainable alternatives to fossil fuels and play a critical role in reducing greenhouse gas emissions and mitigating climate change. Climate scientists work closely with engineers, policymakers, and industry stakeholders to advance the deployment and integration of renewable energy systems, improve energy efficiency, and promote the transition to low-carbon economies. Similarly, climate-smart agricultural practices, such as conservation tillage, crop rotation, and agroforestry, help farmers adapt to changing climate conditions, reduce emissions from agriculture, and enhance the resilience of food systems.

Urban areas, which are home to more than half of the world's population, are particularly vulnerable to the impacts of climate change, including heatwaves, floods, and sea-level rise. Climate science informs urban planning and design strategies that can help cities become more resilient, sustainable, and livable in the face of climate change. Green infrastructure, such as parks, green roofs, and permeable pavement, can help absorb stormwater, reduce urban heat island effects, and enhance biodiversity in cities. Sustainable transportation systems, including public transit, cycling infrastructure, and electric vehicles, can help reduce greenhouse gas emissions from transportation and improve air quality in urban areas.

In conclusion, climate science is a vital and indispensable field of study that provides essential insights into the causes, impacts, and solutions to climate change. By advancing our understanding of Earth's climate system and its interactions with human activities, climate scientists play a crucial role in informing policy decisions, fostering public awareness and understanding, driving technological innovation, and building resilience to climate impacts. As we confront the urgent challenges posed by climate change, climate science will continue to be a cornerstone of our efforts to create a more sustainable, equitable, and resilient future for generations to come. """

    
    processor = TextAnalyzer()  # TextAnalyzer-Instanz erstellen

    sentences, filtered_words, cleaned_words = processor.preprocess_text(text)  # Text vorverarbeiten

    word_counts = processor.count_word_frequencies(cleaned_words)  # Word Counts zählen

    sentence_counts = processor.calculate_sentence_counts(sentences, word_counts)  # Sentence Counts berechnen

    summary = summarize_text(sentence_counts)   # Textzusammenfassung erstellen
    print("\nTextzusammenfassung:")
    print(summary)
