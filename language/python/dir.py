import os


if __name__ == '__main__':
    for file in os.listdir('./'):
        # find keyword
        if file.find('contract-'):
            print('find it')

        if file.endswith('.txt'):
            print(os.path.join('/mydir', file))

