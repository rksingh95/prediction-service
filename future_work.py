
# TODO Future implantation
# Create image prediction in tabular format
#     # Read image
#     model = load_model("models/resnet152_class_23_epoch_50.h5")
#     loss = tf.keras.losses.CategoricalCrossentropy()
#     optimizer = tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE)
#     model.compile(optimizer=optimizer, loss=loss, metrics=['accuracy'])
#     image = cv2.imread(r"D:\test_data/" + category + '/' + name)
#     # Preprocess image
#     image = cv2.imread(IMG_PATH, 1)
#     image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
#     image = image.astype("float") / 255.0
#     image = img_to_array(image)
#     image = np.expand_dims(image, axis=0)
#     predictions = model.predict(image).ravel()
#     # Print predictions
#     print(predictions)
#     # Get the class with the highest probability
#     prediction = np.argmax(predictions)
#     # Check if the prediction is correct
#     correct = True if classes[prediction].lower() == category else False
#     # Draw the image and show the best prediction
#     image = cv2.resize(image, (256, 256))
#     cv2.putText(image, '{0}: {1} %'.format(classes[prediction], str(round(predictions[prediction] * 100, 2))),
#                 (12, 22), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 0), 2)
#     cv2.putText(image, '{0}: {1} %'.format(classes[prediction], str(round(predictions[prediction] * 100, 2))),
#                 (10, 20), cv2.FONT_HERSHEY_DUPLEX, 0.7, (65, 105, 225), 2)
#     cv2.putText(image, '{0}'.format('CORRECT!' if correct else 'WRONG!'), (12, 50), cv2.FONT_HERSHEY_DUPLEX, 0.7,
#                 (0, 0, 0), 2)
#     cv2.putText(image, '{0}'.format('CORRECT!' if correct else 'WRONG!'), (10, 48), cv2.FONT_HERSHEY_DUPLEX, 0.7,
#                 (0, 255, 0) if correct else (0, 0, 255), 2)
#
#     # Append the image
#     blocks.append(image)
#
#
# # Display images and predictions
# row1 = np.concatenate(blocks[0:3], axis=1)
# row2 = np.concatenate(blocks[3:6], axis=1)
# # cv2.imshow('Predictions', np.concatenate((row1, row2), axis=0))
# cv2.imwrite('D:/New folder/New folderpredictions_renet50.jpg', np.concatenate((row1, row2), axis=0))
# cv2.waitKey(0)
