import os.path

import cv2

def extract_frames(input_video_path, output_folder):
    resize_height = 128
    resize_width = 171

    # 打开视频文件
    cap = cv2.VideoCapture(input_video_path)

    # 检查视频是否成功打开
    if not cap.isOpened():
        print("Error: 无法打开视频文件.")
        return

    # 获取视频帧率
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # 设置帧计数器
    frame_count = 0
    filename_index = 0
    while True:
        # 读取一帧
        ret, frame = cap.read()

        # 检查是否成功读取帧
        if not ret:
            break

        # 每3帧抽取一帧
        if frame_count % 3 == 0:
            # 构造保存路径
            if not os.path.exists(output_folder):
                os.mkdir(output_folder)

            save_path = output_folder + '/' + '0000{}.jpg'.format(str(filename_index))
            filename_index += 1

            # 保存抽取的帧
            frame = cv2.resize(frame, (resize_width, resize_height))
            cv2.imwrite(save_path, frame)
            # print(f"保存帧: {save_path}")

        # 增加帧计数器
        frame_count += 1

    # 释放视频捕获对象
    cap.release()

    print("帧抽取完成.")

if __name__ == '__main__':
    # 输入视频文件路径和输出文件夹路径
    input_video_path = "updown_55.mp4"
    output_folder = './mydata/up_down/updown_55'

    # 调用函数进行帧抽取
    extract_frames(input_video_path, output_folder)


