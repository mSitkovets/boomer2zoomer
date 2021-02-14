# boomer2zoomer

## Inspiration
We want to bridge the generational gap between teachers and students, hence the name boomer2zoomer.

## What it does
boomer2zoomer is a slang and profanity recognition software built for virtual classrooms. While on a voice or video call, it will recognize when swearing, slang, or offensive words are said, and produces a pop-up window. For slang, the definition of the word is provided. For swearing and offensive words, a warning is given, and, when applicable, the history of the word and why it is inappropriate.

## How we built it
We first fetch a user's recording via their mic and convert it to text using Google's speech-to-text converter. Then, after processing the word, we first check if the word is contained in the list of custom-built neural network that learns slangs. If it is popular slang, we input the word to UrbanDictionary's API and display the meaning of the word to the user.

## Challenges we ran into
We tried several different speech recognition libraries for processing the audio input, starting with Google Cloud Speech to Text. We specifically wanted to recognize slang and profanity, but Google Cloud was only able to recognize words that already exist in the dictionary, so words such as "yeet" and "poggers" could not be identified. Next, we tried IBM Watson since there is a feature to add custom words. However, this turned out to be a paid feature. Next, we tried Amazon Transcribe (AWS Speech to Text), but it was not possible to use without providing credit card information. In the end, we went back to Google Cloud Speech to Text, and created a machine learning model to recognize specific slang words.

When creating our machine learning model, we recorded 300 audio files to use as a training set. When normalizing the dataset, we tried to remove the "extra" parts of the files, such as the silence at the beginning and end, using the tools Unsilence and ffmpeg. Attempts at using both these tools were unsuccessful, so in the end we divided the frequencies by highest one, allowing us to keep all the audio clips in similar ranges.

## Accomplishments that we're proud of
- Made an entire neural network from scratch within two hours
- Working in a team with dope members
- Learning how to build a neural network and train a machine learning model where only one team member had previous knowledge
- Making a funny but useful project
- Learning how APIs work and figuring out how to use tkinter

## What we learned
- Machine learning
- Creating a neural network
- Handling JSON
- Using Flask

## What's next for boomer2zoomer
- Integrating boomer2zoomer with popular video conferencing services like Zoom, Google Meet, and Microsoft Teams
- Adding more slang words for recognition
- Improve visual appeal of formatting of pop-up windows 
- Improving accuracy rate of machine learning model
