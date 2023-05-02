# import pandas as pd
# import numpy as np
# import tensorflow as tf
# from sklearn.model_selection import train_test_split
#
#
# def checkText(text: str, dataFile: str = 'negPosWords') -> dict:
#     # Ma'lumotlar bazasini yuklash va tasodifiy tartibda saqlash
#     data = pd.read_csv(f'{dataFile}.csv')
#     data = data.sample(frac=1).reset_index(drop=True)
#     data['text'] = data['text'].str.lower()
#
#     # Matnni oldindan qayta ishlash
#     tokenizer = tf.keras.preprocessing.text.Tokenizer()
#     tokenizer.fit_on_texts(data['text'])
#     sequences = tokenizer.texts_to_sequences(data['text'])
#     padded_sequences = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=100)
#
#     # Label larni vektorlashtirish
#     labels = tf.keras.utils.to_categorical(data['label'].values)
#
#     # Ma'lumotlarni ajratish
#     X_train, X_test, y_train, y_test = train_test_split(padded_sequences, labels, test_size=0.2)
#
#     # Modelni aniqlash
#     model = tf.keras.models.Sequential([
#         tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=64),
#         tf.keras.layers.LSTM(128, return_sequences=True),
#         tf.keras.layers.Dropout(0.2),
#         tf.keras.layers.LSTM(64),
#         tf.keras.layers.Dropout(0.2),
#         tf.keras.layers.Dense(32, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
#         tf.keras.layers.Dense(2, activation='softmax')
#     ])
#
#     # Optimizatsiya algoritmini tanlash
#     optimizer = tf.keras.optimizers.RMSprop(learning_rate=0.001)
#     loss = tf.losses.CategoricalCrossentropy()
#
#     # Modelni kompilyatsiya qilish
#     model.compile(optimizer=optimizer, loss=loss, metrics=['accuracy'])
#
#     # Modelni o'qitish
#     model.fit(X_train, y_train, epochs=20, batch_size=64, validation_split=0.1)
#
#     # Modelni baholash
#     loss, accuracy = model.evaluate(X_test, y_test)
#     print(f"Sinov yo'qotishi: {loss:.3f}, Sinov aniqligi: {accuracy:.3f}")
#
#     # Bashorat qilish (natijani olish)
#     text = text.lower()
#     sequence = tokenizer.texts_to_sequences([text])
#     padded_sequence = tf.keras.preprocessing.sequence.pad_sequences(sequence, maxlen=100)
#     prediction = model.predict(padded_sequence)
#     label = np.argmax(prediction)
#     return {'matn': text, 'natija': label}
