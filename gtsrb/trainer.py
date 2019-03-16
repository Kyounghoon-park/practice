from gtsrb.model import Gtsrb
import matplotlib.pyplot as plt

class Trainer:
    def __init__(self, dataset):
        gt = Gtsrb()
        self.dataset = dataset
        
    def excute(self):
        gt = Gtsrb()
        dataset = self.dataset
        print("X 데이터셋".format(dataset.X.shape))
        print("y 데이터셋".format(dataset.y.shape))

        plt.imshow(
            dataset.X[0, :, :, :].reshape(gt.RESIZE_IMAGE)
        ) # 표본 이미지

        plt.imshow(dataset.X[-1, :, :, :].reshape(gt.RESIZE_IMAGE)) #답
        print("레이블 :{}".format(dataset.y[-1, :]))

        plt.show()
        
    
