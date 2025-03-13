import os

'''
    Para esse exercicio, consideramos uma lista de listas de inteiros que represantam 
    uma grade bidimensional com n  linhas e m colunas. Uma celula é chamada de  celula dominante 
    se tiver um valor estritamente maior do que todos os seus vizinhos. Duas celulas sao vizinhas 
    quando compatilham um lado comum ou um canto comum, então uma celula pode ter ate 8 vizinhos.
    A função numCells recebe um vetor e encontra o numero de celulas dominante na grade.
'''
def numCells(grid):
    linhas = len(grid)
    colunas = len(grid[0]) if linhas > 0 else 0
    contagem = 0

    def eh_dominante(linha, coluna):
        """Verifica se uma célula é dominante."""
        valor_celula = grid[linha][coluna]
        for i in range(max(0, linha - 1), min(linhas, linha + 2)):
            for j in range(max(0, coluna - 1), min(colunas, coluna + 2)):
                if i == linha and j == coluna:
                    continue  # Ignora a própria célula
                if grid[i][j] >= valor_celula:
                    return False
        return True

    for i in range(linhas):
        for j in range(colunas):
            if eh_dominante(i, j):
                contagem += 1

    return contagem

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
