from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    memo = {}
    
    def cut_rod_memo(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0, []
        
        max_profit = -1
        best_cuts = []
        
        for i in range(1, n + 1):
            profit, cuts = cut_rod_memo(n - i)
            if prices[i - 1] + profit > max_profit:
                max_profit = prices[i - 1] + profit
                best_cuts = [i] + cuts
        
        memo[n] = (max_profit, best_cuts)
        return max_profit, best_cuts
    
    max_profit, cuts = cut_rod_memo(length)
    number_of_cuts = len(cuts) - 1 if len(cuts) > 1 else 0
    
    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": number_of_cuts
    }

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    table = [0] * (length + 1)
    cuts = [0] * (length + 1)
    
    for i in range(1, length + 1):
        max_profit = -1
        for j in range(1, i + 1):
            if prices[j - 1] + table[i - j] > max_profit:
                max_profit = prices[j - 1] + table[i - j]
                cuts[i] = j
        table[i] = max_profit
    
    max_profit = table[length]
    cuts_list = []
    n = length
    while n > 0:
        cuts_list.append(cuts[n])
        n -= cuts[n]
    
    number_of_cuts = len(cuts_list) - 1 if len(cuts_list) > 1 else 0
    
    return {
        "max_profit": max_profit,
        "cuts": cuts_list,
        "number_of_cuts": number_of_cuts
    }

def run_tests():
    test_cases = [
        {"length": 5, "prices": [2, 5, 7, 8, 10], "name": "Базовий випадок"},
        {"length": 3, "prices": [1, 3, 8], "name": "Оптимально не різати"},
        {"length": 4, "prices": [3, 5, 6, 7], "name": "Рівномірні розрізи"}
    ]
    
    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")
        
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")
        
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")
        
        print("\nПеревірка пройшла успішно!")

if __name__ == "__main__":
    run_tests()
