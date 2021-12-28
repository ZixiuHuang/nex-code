#@markdown <h3> 📥 Setup environment</h3>
import os
from google.colab import files
from skimage import io, transform
import numpy as np

## utility function
def image2datadir(image_path):
  img = io.imread(image_path)
  oh, ow, oc = img.shape
  ratio = image_width / ow
  down_img = transform.resize(img, (int(oh * ratio), (ow * ratio)),anti_aliasing=True)
  down_img *= 255
  down_img = down_img.astype(np.uint8)
  _, filename = os.path.split(image_path)
  io.imsave(os.path.join('data/demo/images',filename),down_img)
  os.remove(image_path)


print('setting up software...')
get_ipython().system_raw('pip install lpips')
if not os.path.exists('train.py'): # we already clone the repo
  get_ipython().system_raw('git clone https://github.com/nex-mpi/nex-code')
  %cd nex-code
# clear previous run directory and prepre new one
!rm -rf data/demo
!rm -rf data/runs
!rm -rf data/upload
!mkdir -p data/demo
!mkdir -p runs
# prepare the dataset
if onedrive_dataset == ':images_upload:':
  if not 'preupload_datasets' in globals() or preupload_datasets is None:
    uploaded = files.upload()
    image_files = uploaded.keys()
    del uploaded
  else:
    image_files = preupload_datasets
  if len(image_files) < 12:
    print("Failed, You must contain at least 12 images.")
  else:
    !mkdir -p data/demo/images
    !mkdir -p data/demo/sparse
    for f in image_files:
      image2datadir(f)
    get_ipython().system_raw('apt install colmap')
    print('Run SFM')
    !colmap feature_extractor --database_path data/demo/database.db --image_path data/demo/images --ImageReader.single_camera 1 --ImageReader.camera_model SIMPLE_PINHOLE --SiftExtraction.use_gpu=false
    !colmap exhaustive_matcher --database_path data/demo/database.db  --SiftMatching.use_gpu=false
    !colmap mapper --database_path data/demo/database.db --image_path data/demo/images --Mapper.ba_refine_principal_point 1 --Mapper.num_threads 2 --Mapper.extract_colors 0 --export_path data/demo/sparse
    !colmap image_undistorter --image_path data/demo/images --input_path data/demo/sparse/0 --output_path data/demo/dense --output_type COLMAP
    # we have to import colmap_runner after repo succesfull load
    from utils.colmap_runner import load_colmap_data, save_poses
    poses, pts3d, perm, hwf_cxcy = load_colmap_data('data/demo')
    save_poses('data/demo', poses, pts3d, perm, hwf_cxcy)
else:
  get_ipython().system_raw('wget -O data/demo/data.zip {}'.format(onedrive_dataset))
  get_ipython().system_raw('unzip -o -d data/demo/ data/demo/data.zip')
  get_ipython().system_raw('rm data/demo/data.zip')
