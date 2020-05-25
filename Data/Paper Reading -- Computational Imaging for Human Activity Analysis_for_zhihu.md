# Paper Reading -- "Computational Imaging for Human Activity Analysis"

## Author

Suren Jayasuriya
School of Arts, Media and Engineering
School of Electrical, Computer and Energy Engineering
Arizona State University, e-mail: sjayasur@asu.edu

## Abbreviation

- Photoplethysmography: PPG
- remote Photoplethysmography: rPPG (远程光体积描记法) 
- Pulse Rate: PR
- Pulse Rate Variability: PRV
- Blood Pressure: BP
- Breathing Rate: BR
- Blood Oxygen Level: SpO2
- Independent Component Analysis: ICA

## Low-level Physiological Sensing for Vitals Monitoring and Skin Imaging

- 为了得到血管的像，光需要穿透表皮层和真皮层，到达位于皮下区域的血管位置，而这中间的穿透造成了很多散射。

  解决方案：使用红外光谱，以及使用额外的照明设备。

  > To combat this, researchers have used infrared wavelengths to visualize blood vessels which penetrate skin deeper [59]. In addition, active illumination techniques such as Laser Speckle Constrast Imaging [14] and Sidestream Dark Field (SDF) Imaging [18] have been developed specifically to image blood vessels.

- 增强近红外光谱区域的血管等透视效果：

  使用带通滤波器将近红外波段的光从视频中单独滤出来，放大N倍后再加回去。

  > This technique decomposes a video into a spatial pyramid, and then temporally bandpass filters the
  > video signal at every level of the pyramid. Then this band-passed video is multiplied by a constant and added back onto the original pyramid before reconstructing the entire video.

  <img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/Paper Reading -- Computational Imaging for Human Activity Analysis/image-20200524105814801.jpg" alt="image-20200524105814801" style="zoom:33%;" />

- 有一种算法可以把直射光（光源-物体-照相机）和散射光（多次反射的光和环境光）分开。其中，含有血管信息的光是非直接光（散射）。

  > An algorithm to perform direct/global separation, where light is separated into a direct component, where light bounces only once in the scene between illumination source and camera, and indirect/global component where light undergoes multiple bounces in the scene [36].

  Nayar SK, Krishnan G, Grossberg MD, Raskar R (2006) Fast separation of direct and global components of a scene using high frequency illumination. In: ACM SIGGRAPH 2006 Papers, pp 935–944

- 实时直间接光分离算法对光源与照相机间的位置关系敏感。有新的项目使用硬件直接对直间接光进行分离。这种方法对环境光干扰抗性高，且可以直接后置生理信号提取算法。

  > One system utilized a synchronized projector-camera system that could directly triangulate light from certain planes present in the scene, which was applied to capture blood vessels in the arm [49]. However, this system was sensitive to misalignments between the target and the camera system. A more advanced system was presented in [27] where researchers used a variation of the synchronized projector-camera system to capture bands of indirect light in real-time. The Episcan3D system, originally presented in [38], was utilized as a hardware implementation to show this idea in practice.

  <img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/Paper Reading -- Computational Imaging for Human Activity Analysis/image-20200524112533822.jpg" alt="image-20200524112533822" style="zoom:33%;" />

## Computational Cameras for Motion Sensing

- Event-based Cameras. (基于事件的相机)这类相机的时间分辨率极高，在KHz级别，且耗电量低，为μW单位，但带来的问题是相比于RGB相机画质上的损失，因为它的输出是0/1或-1/0/1。

  > Event-based sensors (also known as dynamic vision sensors) utilize pixels which output binary or trinary pixels when the pixel changes value temporally in brightness [32]. As such, these sensors encode a stream of events for the spatial location, time, and signed brightness change (typically +/- 1) that is asynchronously read off the sensor array. We recommend the reader to the survey paper [16] for a comprehensive overview for these sensors.

  <img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/Paper Reading -- Computational Imaging for Human Activity Analysis/image-20200524114611229.jpg" alt="image-20200524114611229" style="zoom:33%;" />

## Coded Exposure

- 编码曝光：由于信噪比和曝光时间是冲突的两个量，所以为了在平衡二者的基础上尽可能降低曝光时间，这里使用了编码曝光技术，即在相机内部进行了一项“输入曝光信号->最终输出图像”的一个矩阵运算，将运动模糊进行优化。

  > To combat this classical tradeoffs, researchers in computational photography have exploited coded exposure by varying the exposure signal sent to the pixels in pseudorandom codes, and then decoding the resulting motion blur that occurs to recover back the original video at high frame rates and high SNR.





- 保护隐私的照相机硬件：或是再照相机硬件层面执行隐私编码工作，或是直接对源图像进行加水印或动画化，亦或是操控增益、曝光或数字化后信息。

  > For computational cameras, one approach is to perform privacy algorithms at the camera level, and using encryption or other methods for information afterwards [9, 15]. Another approach is to build sensors which preserve privacy through watermarking [37] or cartooning [54] or manipulating gain/digitization/exposure [42].

## Lensless Camera

无镜头照相机使用一个同心圆衍射薄膜取代了传统的镜头，**但并没有取代后面的感光器件**。光源发出/反射的光透过这个薄膜发生衍射现象生成一张结果图像。这个图像中除了像本身的信息，甚至还携带有距离信息。经过算法反推/机器学习训练后，可以重建出原始图像。

这里的重建环节则可以做文章。可以训练出来一种只重建脸以外图像部分的网络，而只有当得到授权的用户访问时才会重建出完整图像。

<img src="https://raw.githubusercontent.com/miracleyoo/Markdown4Zhihu/master/Data/Paper Reading -- Computational Imaging for Human Activity Analysis/161115.jpg" alt="[image] Figure: Principle of newly developed lensless camera technology" style="zoom:70%;" />