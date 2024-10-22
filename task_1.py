import heapq


def min_cost_to_connect_cables(cables):
    # Створюємо мін-heap для зберігання довжин кабелів
    heapq.heapify(cables)
    total_cost = 0

    # Поки не залишиться лише один кабель
    while len(cables) > 1:
        # Вибираємо два найменші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Вартість їх об'єднання
        cost = first + second

        # Додаємо вартість до загальних витрат
        total_cost += cost

        # Додаємо новий кабель назад в heap
        heapq.heappush(cables, cost)

    return total_cost


# Приклад використання
cables = [4, 3, 2, 6]
result = min_cost_to_connect_cables(cables)
print(f"Мінімальні витрати на з'єднання кабелів: {result}")