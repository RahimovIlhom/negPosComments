import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


def checkText(text: str, dataFile: str = 'negPosWords') -> dict:
    # Ma'lumotlarni Pandas dataframe-ga yuklash
    data = pd.read_csv(f'{dataFile}.csv')

    # Ma'lumotlarni ko'paytirish
    data = pd.concat([data, data.sample(frac=0.5, random_state=42)], ignore_index=True)

    # Yo'qolgan qiymatlarni to'ldirish
    data = data.fillna('')

    # Ma'lumotlarni tozalash
    data['text'] = data['text'].str.replace('[^a-zA-Z\s]', '').str.lower()

    # Ma'lumotlarni normallashtirish
    vectorizer = CountVectorizer()
    features = vectorizer.fit_transform(data['text'])

    # Ma'lumotlarni o'quv va sinov to'plamlariga bo'lish
    train_features, test_features, train_labels, test_labels = train_test_split(features, data['label'], test_size=0.2,
                                                                                random_state=42)

    # Trening ma'lumotlariga logistik regressiya modelini o'rgatish
    classifier = LogisticRegression()
    classifier.fit(train_features, train_labels)

    # Sinov ma'lumotlari bo'yicha modelni baholash
    accuracy = classifier.score(test_features, test_labels)
    print("Aniqlik:", accuracy)

    # Yangi matn kiritish yorlig'ini bashorat qilish uchun modeldan foydalanish
    new_text = [text.lower().replace('[^a-zA-Z\s]', '')]
    new_features = vectorizer.transform(new_text)
    predicted_label = classifier.predict(new_features)[0]
    return {"text": new_text[0], "label": predicted_label}