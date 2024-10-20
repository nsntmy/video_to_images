[English](README.md) | [日本語](README.ja.md)

<img src="https://img.shields.io/badge/-Python-3776AB.svg?logo=python&style=plastic">

# Video to images
A script that splits a video file into still image files and saves them.

## Required libraries
* OpenCV

## Usage

```shell
python video_to_images.py [path_to_your_video_file_or_directory]
```

## Specification

The library path you are using can specify a video file or a directory containing video files. If a directory is specified, all files contained in it will be processed. (Subdirectories are not included)

The output image will be saved in the directory where the target file exists, by creating a directory with the name excluding the file extension.
Required libraries

example)

```
python video_to_images.py C:\Movie

C:\Movie
│  P1001271.MP4
│  P1001272.MP4
│  
├─P1001271
│       frame_000000.jpg
│       frame_000001.jpg
│       frame_000002.jpg
│              :
│  
└─P1001272
        frame_000000.jpg
        frame_000001.jpg
        frame_000002.jpg
               :
```
