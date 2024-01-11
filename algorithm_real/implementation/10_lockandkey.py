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
def solution(key, lock):
    answer = True
    
    return answer


def input_integer_list():
    try:
        input_str = input()
        # 문자열을 파이썬 리스트로 변환
        nested_list = eval(input_str)
        
        # 리스트 내의 모든 요소를 정수로 변환
        int_nested_list = [[int(element) for element in sublist] for sublist in nested_list]

        return int_nested_list

    except (ValueError, SyntaxError) as e:
        print("올바른 형식으로 입력하세요.")
        return None


key = input_integer_list()
lock = input_integer_list()

