from typing import List, Tuple, Dict


def to_intervals(intervals: List[int]) -> List[Tuple[int, int]]:
    return [(intervals[i], intervals[i + 1]) for i in range(0, len(intervals), 2)]


def intersect_intervals(
    intervals1: List[Tuple[int, int]], intervals2: List[Tuple[int, int]]
) -> List[Tuple[int, int]]:
    result = []
    i = j = 0
    start = -1
    while i < len(intervals1) and j < len(intervals2):
        start1, end1 = intervals1[i]
        start2, end2 = intervals2[j]

        start = max(start1, start2, start)
        end = min(end1, end2)

        if start < end:
            result.append((start, end))
            start = end

        if end1 < end2:
            i += 1
        else:
            j += 1

    return result


def total_time(intervals: List[Tuple[int, int]]) -> int:
    return sum(end - start for start, end in intervals if end > start)


def appearance(intervals: Dict[str, List[int]]) -> int:
    lesson = to_intervals(intervals["lesson"])
    pupil = to_intervals(intervals["pupil"])
    tutor = to_intervals(intervals["tutor"])

    pupil_on_lesson = intersect_intervals(pupil, lesson)
    tutor_on_lesson = intersect_intervals(tutor, lesson)

    res_time = intersect_intervals(pupil_on_lesson, tutor_on_lesson)

    return total_time(res_time)


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
    # никто не пришел на урок
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1, 2],
             'tutor': [1, 2]},
    'answer': 0
    },
    # пришел только учитель
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1, 2],
             'tutor': [1594692000, 1594695600]},
    'answer': 0
    },
    # пришел только ученик
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692000, 1594692000],
             'tutor': [1, 2]},
    'answer': 0
    },
    # были оба на всем уроке
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692000, 1594695600],
             'tutor': [1594692000, 1594695600]},
    'answer': 3600 
    },
    
    
]

if __name__ == "__main__":
    for i, test in enumerate(tests):
        test_answer = appearance(test["intervals"])
        assert test_answer == test["answer"], (
            f"Error on test case {i}, got {test_answer}, expected {test['answer']}"
        )
