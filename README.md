# Real-time-Domain-Adaptation-in-Semantic-Segmentation
Final Project for the 24/25 Advanced Machine Learning course @PoliTO. The topic is working with semantic segmentation networks, with a focus on PIDNet, using the LoveDA chinese satellite images dataset, and try to bridge the gap between Urban and Rural domains through DA methods AdaptSegNet and DACS.

The project has been developed by Buhnila Dragos-Constantin (s331394), Kharrat Jad (s324896), and Gigante Fabio (s328890).  

Please check the provided paper for the results and their analysis. Although the results are not desirable, we belive that the work done may give insight towards the possible issues that caused such outcome.  

From the paper  
`Semantic segmentation is a fundamental task in computer vision, essential for real-time applications like autonomous driving and surveillance. However, domain shifts between training and deployment environments can severely worsen model performance. This project explores real-time domain adaptation in semantic segmentation networks, focusing on PIDNet trained on the LoveDA dataset. Despite implementing adversarial training and image-to-image translation techniques, these approaches failed to significantly improve model performance on the target domain. In contrast, data augmentation strategies proved effective, leading to a measurable improvement in mean Intersection over Union (mIoU) when applied during training. These results may highlight the challenges in applying advanced domain adaptation methods to real-time systems and seem to suggest that simple data augmentation may offer a more practical solution in certain scenarios.`  

Note that the development of the project was done entirely using Googlel Colab, meaning that in order to be able to run the provided software, you may either need to install the required plugins and libraries to use the project, or just upload things to Google Drive.  
