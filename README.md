# Pipeline-DistanceMetric
July 2023 - María Sánchez Ruiz



A new metric for measuring the distance between a reference audio and an automatically generated audio.



## What you need?
To use this metric, you will need to download Meta AI's ImageBind model first. You can get it from [ImageBind](https://github.com/facebookresearch/ImageBind). This model will allow you to extract the embeddings of your images and audios to compute this metric.


## Get started

Once you have the files from this repository in the main directory of your ImageBind project, you're ready to go.


## Running the pipeline

Run the following command:


```console
python pipeline.py --ref_image <path2refImage> --ref_audio <path2refAudio> --ob_image <path2obImage> --gen_audio <path2genAudio>
```
Where:


- `<path2refImage>` is the path to your reference image. There can only be one reference image.
- `<path2refAudio>` is the path to your reference audio file. There can only be one reference audio.
- `<path2obImage>` is the path to your objective images folder. These are the images that you used to generate audio. There can be N images files in this folder path.
- `<path2genAudio>` is the path to your generated audios folder, the ones that you want to measure. These audios are the ones you have generated automatically and you want to try the metric on. There can be N audios files in in this folder path.

> **Note**: IMPORTANT: The number of files in folders `<path2obImage>` and `<path2genAudio>` must match.

> __Note__ Your Reference Image is an image of your choice to which you will associate a sound.
> __Note__ Your Reference Sound is the sound you think matches the reference image you have chosen.

