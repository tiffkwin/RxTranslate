# RxTranslate

## The Problem
"A basic principle of effective communication is to know the audience. This principle is especially important for patient-provider interactions that involve risk and diagnostic information, preventive measures, and instructions on medication regimens. But a message said is not necessarily a message understood." - Dr. Sherine El-Toukhy

Our teammate Maria knows what it is like to live in America with parents who struggle with the language barrier which can oftentimes be a large obstacle in the path to effective healthcare.

She has often had to help translate the instructions that come with their prescriptions into Spanish and also make sure to inform them of any severe drug interactions they could experience when multiple prescriptions are in their therapeutic regimen. The lack of understanding surrounding these health experiences for Maria's family members is common for many individuals in America today and can be a serious cause for concern.

## The Effect
A study reported that 44.9% with limited-English proficiency reported low health literacy versus 13.8% of English speakers. In the full sample, **respondents with both limited-English proficiency/low health literacy reported the highest prevalence of poor health** (45.1%), followed by limited-English proficiency-only (41.1%), low health literacy-only (22.2%), and neither (13.8%), a hierarchy that remained significant in multivariate models. 

In 2013, about 41% of the US population (25.1 million people) was considered Limited English Proficient (LEP).

## The Solution
RxTranslate aims to bridge this gap through an easy-to-use system. Simply take a picture of the pill bottle/prescription label and RxTranslate will extract the text from the image, translate the instructions and other relevant information to a specified target language, and then also scrape the web in order to provide a comprehensive list of specific drug interactions that may be a concern for the patient.

## Next Steps
In the future, we aim to develop an enhanced user experience by building out a frontend in React. We will also employ machine learning models to filter out non-crucial information on the label and implement the use of user profiles to further customize the health experience with patient information such as current medications, allergies, and more.

## Installing

```
git clone https://github.com/tiffkwin/RxTranslate.git
```

```
pip install -r requirements.txt
```

## Usage
Note: you will need to set up your own Google API credentials for Google Cloud Vision and Google Translate.

Position a pill bottle/prescription label in front of the webcam.

```
python rxtranslate.py
```



