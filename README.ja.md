[English](README.md) | [日本語](README.ja.md)

<img src="https://img.shields.io/badge/-Python-3776AB.svg?logo=python&style=plastic">

# Video to images
動画ファイルを静止画ファイルに分割して保存するスクリプト

## 必要なライブラリ
* OpenCV

## 使用方法

```shell
python video_to_images.py [path_to_your_video_file_or_directory]
```

## 仕様

パスには動画ファイルか動画ファイルを含むディレクトリを指定することができます。
ディレクトリを指定した場合は含まれるファイルすべてに対して処理を実行します。(サブディレクトリは非対象)

出力される画像は、対象のファイルが存在するディレクトリに、対象ファイルの拡張子を除いた名前のディレクトリを作成し、そのディレクトリ内に保存されます。

例)

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
