
import numpy as np
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Task:
    task_id: int
    arrival_time: int
    processing_time: int
    deadline: int
    remaining_time: int
    waiting_time: int = 0
    start_time: Optional[int] = None
    completion_time: Optional[int] = None

    def is_complete(self):
        return self.remaining_time <= 0


class Scheduler:
    def select_task(self, ready_queue: List[Task], t: int) -> int:
        raise NotImplementedError


class SchedulerEnv:
    def __init__(self, tasks: List[Task], scheduler: Scheduler, max_time: int = 100000):
        self.tasks = sorted(tasks, key=lambda x: x.arrival_time)
        self.scheduler = scheduler
        self.max_time = max_time

        self.time = 0
        self.ready_queue: List[Task] = []
        self.completed_tasks: List[Task] = []
        self.task_ptr = 0

    def step(self):
        while self.task_ptr < len(self.tasks) and self.tasks[self.task_ptr].arrival_time <= self.time:
            self.ready_queue.append(self.tasks[self.task_ptr])
            self.task_ptr += 1

        if self.ready_queue:
            idx = self.scheduler.select_task(self.ready_queue, self.time)
            task = self.ready_queue[idx]

            if task.start_time is None:
                task.start_time = self.time

            task.remaining_time -= 1

            for i, other in enumerate(self.ready_queue):
                if i != idx:
                    other.waiting_time += 1

            if task.is_complete():
                task.completion_time = self.time + 1
                self.completed_tasks.append(task)
                self.ready_queue.pop(idx)

        self.time += 1

    def run(self):
        while (
            self.time < self.max_time and
            (self.task_ptr < len(self.tasks) or len(self.ready_queue) > 0)
        ):
            self.step()

        return self.completed_tasks


def compute_metrics(tasks: List[Task]):
    n = len(tasks)

    waiting_times = np.array([t.waiting_time for t in tasks])
    avg_waiting_time = waiting_times.mean()

    deadline_misses = sum(
        1 for t in tasks if t.completion_time > t.deadline
    )
    deadline_miss_rate = deadline_misses / n

    total_time = max(t.completion_time for t in tasks)
    throughput = n / total_time

    return {
        "avg_waiting_time": avg_waiting_time,
        "deadline_miss_rate": deadline_miss_rate,
        "throughput": throughput
    }
