# 잠겨있는 자물쇠는 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자 형태이고 특이한 모양의 열쇠는 M x M 크기인 정사각 격자 형태로 되어 있습니다.
# 자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다. 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다. 
# 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 
# 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.
# 열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 열쇠로 자물쇠를 열수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.
# key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
# lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
# M은 항상 N 이하입니다.
# 입력예시 key	                        lock	                         result
# [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]	true
'''
def solution(key, lock):
    answer = True
    return answer
'''
'''
# 나의 풀이 ---> 3일 고민했으나 fail
import numpy as np
def solution(key, lock):
    answer = True
    k_r, k_c = key_row, key_col = np.ndarray(key)
    l_r, l_c = lock_row, lock_col = np.ndarray(lock)
    unlock = np.ones((lock_row, lock_col))
    lock_0_count = np.count_nonzero( lock == 0)
    key_1_count = np.count_nonzero( key == 1)
    new_key = np.zeros((lock_row, lock_col))

    def isunlock(key, lock):
        if np.ndarray(key) + np.ndarray(lock) == unlock:
            return True
        else:
            return False

    def make_key(new_key, key, start, end, lock_row, lock_col):
        new_key = list(np.zeros((lock_row, lock_col)))
        for i in range

    
    def shift_key(key):


    if lock_count > key_count:
        return False
    
    else:
    
    return answer
'''
# 교재 풀이
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행
    m = len(a[0]) # 열
    result =[[0] * n for _ in range(m)] # 행 열이 바뀐 갯수로 해야함
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]  # index 열->행 되고  index 행 크기에서 행index-1 -> 열 
    return result

def check(new_lock):
    lock_length = len(new_lock)//3
    for i in range(lock_length, lock_length * 2): # 3배로 변경했으니 인덱스는 자물쇠 크기 ~ 자물쇠 크기 * 2
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True
                
            
def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠를 기존의 3배 크기로 변경
    new_lock = [[0]*(n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(m):
            new_lock[i + n][j + n] = lock[i][j]
        
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n * 2):
            for y in range(n * 2):
                # 열쇠 끼우기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock) == True:
                    return True
                # 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
                    
    return False


def convert_to_integer_list(matrix):
    try:
        result = [[int(element) for element in row] for row in matrix]
        return result
    except ValueError as e:
        print(f"Error: {e}. Please make sure the input contains only integers.")
        return None



import ast

def input_matrix_from_terminal():
    try:
        input_str = input()
        matrix = ast.literal_eval(input_str)
        
        # Validate the input to ensure it's a 2D list
        if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            raise ValueError("Invalid input. Please enter a valid 2D list.")

        # Convert elements to integers
        result = [[int(element) for element in row] for row in matrix]
        return result
    except (ValueError, SyntaxError) as e:
        print(f"Error: {e}. Please enter a valid 2D list.")
        return None
    
key = input_matrix_from_terminal()
lock = input_matrix_from_terminal()
print(solution(key, lock))

