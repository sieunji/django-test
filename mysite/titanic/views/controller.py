from mysite.titanic.models.dataset import Dataset
from mysite.titanic.models.service import Service
from mysite.titanic.templates.plot import Plot

class Controller(object):
    dataset = Dataset()
    service = Service()

if __name__ == '__main__':
    api = Controller()
    while 1:
        menu = input('0-종료 1-데이터출력')
        if menu =='0':
            break
        elif menu =='1':
            plot = Plot('train.csv')
            plot.print_survived_dead()
