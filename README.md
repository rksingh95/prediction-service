# ML_ModelPrediction


# Docker Image:

https://hub.docker.com/repository/docker/rsingh95/endoscopic_guidance
 
 
 
# Perdiction of the mutiple trained models (NASNet, RESNET, VGG16 VGG19, DENSENET) to be integrated with micro service using Flask API request.

Image is updated and loaded on MongoDB for future use, and the user gets a response of the predicted lable while using service and upload image for prediction.

## POST Service 
* http://127.0.0.1:5000/upload-image/

´´´
Payload as image file only ion .jpeg format
´´

Response: 
{
    "Given class of image is ": "esophagitis-a"
}

## GET Service 
* http://127.0.0.1:5000/prediction-history/

Response Json:

    [
        {
            "file_name": "ulcerative-colitis-grade-1-2_0_7470.jpg",
            "predicted_label": "ulcerative-colitis-grade-1-2"
        },
        {
            "file_name": "ulcerative-colitis-grade-2_0_8245.jpg",
            "predicted_label": "dyed-lifted-polyps"
        },
        {
            "file_name": "ulcerative-colitis-grade-2_0_8311.jpg",
            "predicted_label": "dyed-lifted-polyps"
        },
        {
            "file_name": "ulcerative-colitis-grade-3_0_8.jpg",
            "predicted_label": "ulcerative-colitis-grade-3"
        }
    ]
    


#NASNET MODEL PREDICTION
![banner](static/images/predictions.jpg)

Image is updated and loaded on MongoDB for future use, and the user gets a response of the predicted lable while using service and upload image for prediction.



## RESNET MODEL PREDICTION
![banner](https://raw.githubusercontent.com/rksingh95/MLPredictModelFlask/master/static/images/predictions.jpg)
![banner](static/images/response.jpg)
