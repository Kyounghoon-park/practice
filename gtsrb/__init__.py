from gtsrb.trainer import Trainer
from gtsrb.model import Gtsrb

if __name__ == '__main__':
    model = Gtsrb()
    dataset =  model.read_dataset(
            'images/',
            model.N_CLASSES,
            model.RESIZE_IMAGE)
    trainer = Trainer(model)
    trainer.excute()


