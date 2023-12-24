import cv2


def videocapture():
    cap = cv2.VideoCapture(1)  # 生成读取摄像头对象

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取视频的宽度
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 获取视频的高度
    fps = cap.get(cv2.CAP_PROP_FPS)  # 获取视频的帧率
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))  # 视频的编码
    # 定义视频对象输出
    #writer = cv2.VideoWriter("video_result.mp4", fourcc, fps, (width, height))
    while cap.isOpened():
        ret, frame = cap.read()  # 读取摄像头画面
        print(frame)
        frame = cv2.flip(frame, 1)
        cv2.imshow('video', frame)  # 显示画面
        key = cv2.waitKey(24)
        #writer.write(frame)  # 视频保存
        # 按Q退出
        if key == ord('q'):
            break
    cap.release()  # 释放摄像头
    cv2.destroyAllWindows()  # 释放所有显示图像窗口


if __name__ == '__main__':
    videocapture()