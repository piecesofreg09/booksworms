from bookworms.train import train
from bookworms.visualize import visualize


def test():
    print('training input json')
    train(['input.json'], 10, 10)
    
    print('')
    print('when no input file is specified')
    train([], 10, 10)
    
    print('')
    print('visualize')
    visualize()


if __name__ == '__main__':
    test()
    
