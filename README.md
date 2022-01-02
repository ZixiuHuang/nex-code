# 简要介绍

## 1. 实验环境

* Ubuntu 18.04

* CUDA 11.0
* GPU：Tesla V100-PCIE-32GB

## 2. 开发工具

* 语言：python
* 依赖库：PyTorch、OpenCV（版本详见requirements.txt）
* COLMAP（运行SfM算法）

## 3. 参考论文

1. [A New Image Contrast Enhancement Algorithm using Exposure Fusion Framework](https://baidut.github.io/OpenCE/caip2017.html)
2. [NeX: Real-time View Synthesis with Neural Basis Expansion](https://nex-mpi.github.io/)

## 4. 流程概览



## 5. 运行步骤

### 5.1 图像对比度增强、resize

```shell
$python image_enhancement.py \
	-image_dir ./data/original_images/ #输入图像文件路径
	-out_dir ./data/images/			 #输出图像文件路径
	-resize 25 #缩放比例
```

> 经过增强处理、resize至1000×750的数据集已保存在./data/images/中

### 5.2 COLMAP三维重建

COLMAP 安装

```shell
$apt install colmap
```

COLMAP运行SfM算法

```shell
# 特征提取
$colmap feature_extractor \
	--database_path data/database.db \
	--image_path data/images \
	--ImageReader.single_camera 1 \
	--ImageReader.camera_model SIMPLE_PINHOLE \
	--SiftExtraction.use_gpu=false 

#特征匹配
$colmap exhaustive_matcher \
	--database_path data/database.db  \
	--SiftMatching.use_gpu=false

#相机位姿求解与优化
$colmap mapper \
	--database_path data/database.db \
	--image_path data/images \
	--Mapper.ba_refine_principal_point 1 
	--Mapper.num_threads 2 \
	--Mapper.extract_colors 0 \
	--export_path data/sparse

#图像畸变矫正
$colmap image_undistorter \
	--image_path data/images \
	--input_path data/sparse/0 \
	--output_path data/dense \
	--output_type COLMAP
```

> 经过SfM处理生成的相机参数、稀疏点云已保存在./data/目录下

### 5.3 NeX训练

```shell
!python train.py \
       	   -scene data/ \ #文件路径（包含图片、重建后的相机参数、稀疏点云）
	     -model_dir module/ \ #模型的保存路径
	     -epoch 4000 \   
	     -checkpoint 500 \ #每500epoch保存checkpoint
	     -vstep 50 \ #每50epoch输出训练进度
	     -ray 8000 \ #采样数
	     -hidden_layer 4 \	#第一个MLP的隐藏层数量
	     -hidden_node 384 \	#每层结点数
	     -mlp_type relu \	#激活函数：relu 或 siren
	     -basis_hidden_layer 1 \ #第二个MLP的隐藏层数
	     -basis_hidden_node 64 \	#第二个MLP的每层结点数
            -layers 16 \ #MPI模块层数
            -sublayers 12 \ #MPI模块内包含的层数，即总MPI层数=layers*sublayers
	     -num_worker 4 \ #读取数据的线程数
       	   # -pretrained module_1k/ #预训练模型路径
```

















