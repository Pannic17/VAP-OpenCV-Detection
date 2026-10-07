# VAP-OpenCV-Detection

VC-V 项目的 Python / OpenCV 检测实验仓库，包含摄像头预览程序、静态图片检测函数，以及手部、手掌、拳头和人脸相关的 Haar 级联 XML 文件。

**主项目入口：[V_UE427](https://github.com/Pannic17/VAP-UE427)**
相关原型：[VAP-Unity](https://github.com/Pannic17/VAP-Unity)

## 文件结构

```text
main.py          摄像头预览入口及 detect() 静态图片检测函数
hc_hand_1.xml    默认检测分类器
hc_hand_2.xml
hc_hand_3.xml
hc_hand_4.xml    其他手部分类器
hc_palm.xml     手掌分类器
hc_fist.xml     拳头分类器
hc_face.xml     人脸分类器
```

## 运行摄像头预览

准备 Python 3、可用摄像头及支持桌面窗口的 OpenCV 包，在本仓库目录执行：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install opencv-python
.\.venv\Scripts\python.exe main.py
```

程序通过 `cv2.VideoCapture(0)` 打开默认摄像头并显示 `frame` 窗口。窗口获得焦点后按 **q** 退出。需要其他摄像头时，修改代码中的设备索引。

## 静态图片检测

在仓库根目录准备图片后，可直接调用检测函数：

```powershell
.\.venv\Scripts\python.exe -c "from main import detect, HAAR_CASCADE_PATH; detect('your-image.png', HAAR_CASCADE_PATH)"
```

`HAAR_CASCADE_PATH` 默认指向 `hc_hand_1.xml`。函数将图片转为灰度图，使用 `detectMultiScale(scaleFactor=1.02, minNeighbors=5)` 检测，打印矩形坐标与尺寸，并在 `RESULT` 窗口显示绿色检测框；按任意键关闭该窗口。

## 当前状态与限制

- 默认 `main.py` 循环仅预览摄像头；静态图片检测调用处于注释状态，未实现实时摄像头检测。
- 示例中的 `Test8.png` 未包含在仓库中，检测时需要提供自己的图片。
- 图片和 XML 路径以当前工作目录为基准；代码未处理图片读取失败、分类器加载失败或摄像头读取失败。
- 仓库未锁定 Python / OpenCV 依赖版本，也未实现向 UE 或 Unity 发送检测结果的通信接口。
- 本次仅整理文档，尚未安装运行依赖或进行摄像头、分类器效果验证。
