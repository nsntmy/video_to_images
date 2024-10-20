import cv2
import os
import sys
import concurrent.futures

def save_frames(video_path):
    print(f"video_path : {video_path}")
    # 動画ファイルを開く
    video = cv2.VideoCapture(video_path)

    # 動画ファイルが正しく開けたか確認する
    if not video.isOpened():
        print(f"Failed to open the video file: {video_path}")
        return

    # ファイル名から拡張子を除いたディレクトリ名を作成する
    dir_name = os.path.splitext(os.path.basename(video_path))[0]

    # 保存用ディレクトリのパスを作成する
    output_dir = os.path.join(os.path.dirname(video_path), dir_name)

    # 保存用ディレクトリを作成する
    os.makedirs(output_dir, exist_ok=True)

    # フレームのカウンタを初期化する
    frame_counter = 0

    # 動画のフレームを読み込み、画像として保存する
    while True:
        # フレームを読み込む
        ret, frame = video.read()

        # フレームの読み込みが失敗したらループを終了する
        if not ret:
            break

        # 保存する画像ファイル名を作成する
        image_file = os.path.join(output_dir, f"frame_{frame_counter:06d}.jpg")

        # 画像を保存する
        ret = cv2.imwrite(image_file, frame)
        if not ret:
            print(f"imwrite failed : {image_file}")
        else:
            # "."を出力する
            print(".", end="", flush=True)

            # フレームカウンタをインクリメントする
            frame_counter += 1

            # 10枚ごとに改行する
            if frame_counter % 10 == 0:
                print("", end="")

    # 動画ファイルを解放する
    video.release()

    print(f"\n{frame_counter} frames saved.")

def process_file(file_path):
    # 指定されたパスがディレクトリかファイルかを判別する
    if os.path.isfile(file_path):
        save_frames(file_path)
    elif os.path.isdir(file_path):
        # ディレクトリ内の動画ファイルに対して並列処理を行う
        video_files = [f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f))]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(save_frames, [os.path.join(file_path, video_file) for video_file in video_files])

if __name__ == "__main__":
    # コマンドライン引数からパスを取得する
    if len(sys.argv) < 2:
        print("Please provide the path to a video file or a directory as a command-line argument.")
    else:
        file_path = sys.argv[1]
        # 絶対パスに変換
        file_path = os.path.abspath(file_path)
        process_file(file_path)

