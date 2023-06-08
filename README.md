# EdgeAI_final_project
NTUST EdgeAI final project, original repo: https://github.com/PaddlePaddle/PaddleDetection

## Set up enviroment
```
pip install -r requirements.txt
python setup.py install
```

## Inference
```
python deploy/pipeline/pipeline.py \
    --config deploy/pipeline/config/examples/infer_cfg_fall_down.yml \
    --video_file=/input_video/test2.mp4 \
    --device=cpu
```
* put the file you want to inferneve at --video_file

## Prepare training data (coco with person in the image 約1600張)
```
!wget https://bj.bcebos.com/v1/paddledet/data/keypoint/coco_val_person_mini.tar
!tar -xf coco_val_person_mini.tar -C ./dataset/
!mv ./dataset/coco_val_person_mini/* ./dataset/coco
#把文件名字改一下
!cp ./dataset/coco/annotations/instances_train2017.json ./dataset/coco/annotations/person_keypoints_train2017.json
!cp ./dataset/coco/annotations/instances_val2017.json ./dataset/coco/annotations/person_keypoints_val2017.json
```
## Training
```
python tools/train.py -c configs/keypoint/hrnet/dark_hrnet_w32_256x192.yml
```