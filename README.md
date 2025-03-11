# 3d-datasets-supplement

This repository contains supplementary materials for common 3D datasets.

## ShapeNet
[3D-R2N2,Pix2Vox] These methods use ShapeNet with supplementary rendering images(.png).
- ShapeNet rendering images: http://cvgl.stanford.edu/data2/ShapeNetRendering.tgz
- ShapeNet voxelized models: http://cvgl.stanford.edu/data2/ShapeNetVox32.tgz


## Pix3D
[Pix2Vox]These methods use Pix3D with supplementary voxel models(.binvox).

Pix3D images & voxelized models: http://pix3d.csail.mit.edu/data/pix3d.zip

To convert .obj files to .binvox files, please put pix3d, binvox and pix3d_obj2binvox.py in the same folder and run the following command:
`python3 pix3d_obj2binvox.py`

> Note: binvox file in this repository is suitable for MacOS, if you want to use it in Linux or Windows, please refer to the offical website: https://www.patrickmin.com/binvox/


## Pascal3D+
[Pix2Vox]These methods use Pascal3D+.

- Pascal3D+[Release 1.0]: ftp://cs.stanford.edu/cs/cvgl/PASCAL3D+_release1.0.zip
- Pascal3D+[Release 1.1]: ftp://cs.stanford.edu/cs/cvgl/PASCAL3D+_release1.1.zip

> Note: Although Pascal3D+ is mentioned in the paper and code. According to the author, Pix2Vox didn't use Pascal3D+.

## GSO
[Zero 1-2-3, Splatter Image, Unique3D]These methods use GSO.
GSO:https://app.gazebosim.org/GoogleResearch/fuel/collections/Scanned%20Objects%20by%20Google%20Research

First, download the script to GSO/.
Then, run the following command:
```python
python3 download_collection.py -o "GoogleResearch" -c "Scanned Objects by Google Research"
```

## Objaverse
[Zero 1-2-3 XL, Unique3D]These methods use Objaverse.
Objaverse: https://objaverse.allenai.org/