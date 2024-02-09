# Virtual 3D Dress TryOn with M3D-VTON

This project is a Graphical User Interface (GUI) application developed using Tkinter and the M3D-VTON (Monocular-to-3D Virtual Try-On Network). The application allows users to virtually try on dresses in a 3D environment. MeshLab is required to visualize the output, and the generated measurements are displayed after the virtual try-on.

## Requirements

- Python >= 3.8.0
- PyTorch == 1.6.0
- torchvision == 0.7.0
- Meshlab
- tk-tools

## Data Preparation

### MPV3D Dataset

1. Download the MPV3D Dataset.

2. Run the following script to preprocess the data:
   ```bash
   python util/data_preprocessing.py --MPV3D_root path/to/MPV3D/dataset
   ```

### Custom Data

If you want to process your own data, follow these steps:

1. Prepare an in-shop clothing image (C) and a frontal person image (P) with a resolution of 320x512. Place them in the corresponding folders:
   - C: mpv3d_example/cloth
   - P: mpv3d_example/image

2. Obtain the mask of C by thresholding or using remove.bg. Save it in the folder:
   - C mask: mpv3d_example/cloth-mask

3. Obtain the human segmentation layout by applying 2D-Human-Paring on P. Save it in the folder:
   - Human segmentation: mpv3d_example/image-parse

4. Obtain the human joints by applying OpenPose (25 keypoints) on P. Save it in the folder:
   - Human joints: mpv3d_example/pose

5. Run the data processing script:
   ```bash
   python util/data_preprocessing.py --MPV3D_root mpv3d_example
   ```

6. Data preparation is now finished, and you can proceed to run inference.

### Download the dataset from : https://drive.google.com/file/d/1qcynpXZ9eSlzTV-RDCr-Yip3GcuU314h/view

### Download the pretrained model from here :  https://drive.google.com/file/d/1Yk3pXKw00u6CUIu-Fe_8W0mV-aTBV-r9/view?usp=sharing and place in assets folder 

### Download the pretrained model folder extract and replace from here : https://drive.google.com/file/d/1t_5ff2R8eL6a52EN-Gn5F19v_-SSLTNj/view?usp=sharing



### Demo:
https://drive.google.com/file/d/1xpQGyfmniCOPGy56SBpDeWyWGCPdhipN/view?usp=sharing


![Screenshot 2024-02-09 134200](https://github.com/chethanachars/Virtual-3D-Dress-TryOn/assets/158150756/f2830162-e8c9-4700-9b9a-9de96db2a914)

![Screenshot 2024-02-09 133957](https://github.com/chethanachars/Virtual-3D-Dress-TryOn/assets/158150756/f3d4260e-ac71-4e72-8bc5-1f777b40d5d8)

![Screenshot 2024-02-09 134045](https://github.com/chethanachars/Virtual-3D-Dress-TryOn/assets/158150756/f1b160f4-db9a-44cc-b915-5403abfeef3e)

![Screenshot 2024-02-09 134119](https://github.com/chethanachars/Virtual-3D-Dress-TryOn/assets/158150756/69c680ff-cfca-4fbb-97da-f0a08d1317f0)


## Running Inference

1. Run the GUI using the following command:
   ```bash
   python GUI.py
   ```

2. MeshLab is required to visualize the output. Make sure to have MeshLab installed.

3. After the virtual try-on, select the emd points as in Demo video measurements will be displayed.

## Note

- Ensure that the dependencies are installed before running the application.
- For visualizing the 3D output, MeshLab must be installed on your system.

Feel free to reach out for any issues or improvements. Happy Virtual Dress TryOn!

#Note this project is a GUI version with some changes from the this project https://github.com/fyviezhao/M3D-VTON , please make sure to check that 
---

Make sure to replace placeholders like `path/to/MPV3D/dataset` with the actual paths and update any additional details as needed.
