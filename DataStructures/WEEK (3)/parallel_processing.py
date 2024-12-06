from collections import namedtuple

AssignedJob = namedtuple('AssignedJob', ['worker', 'started_at'])


class JobQueue:
    def __init__(self, n_workers, jobs):
        self.n = n_workers
        self.jobs = jobs
        self.finishTime = []
        self.assigned_jobs = []
        for i in range(self.n):
            self.finishTime.append([i, 0])

    def SiftDown(self, i):
        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < self.n:
            if self.finishTime[min_index][1] > self.finishTime[left][1]:
                min_index = left
            elif self.finishTime[min_index][1] == self.finishTime[left][1]:
                if self.finishTime[min_index][0] > self.finishTime[left][0]:
                    min_index = left
        if right < self.n:
            if self.finishTime[min_index][1] > self.finishTime[right][1]:
                min_index = right
            elif self.finishTime[min_index][1] == self.finishTime[right][1]:
                if self.finishTime[min_index][0] > self.finishTime[right][0]:
                    min_index = right
        if min_index != i:
            self.finishTime[i], self.finishTime[min_index] = self.finishTime[min_index], self.finishTime[i]
            self.SiftDown(min_index)

    def NextWorker(self, job):
        root = self.finishTime[0]
        next_worker = root[0]
        started_at = root[1]
        self.assigned_jobs.append(AssignedJob(next_worker,started_at))
        self.finishTime[0][1] += job
        self.SiftDown(0)


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    job_queue = JobQueue(n_workers, jobs)
    for job in jobs:
        job_queue.NextWorker(job)
    assigned_jobs = job_queue.assigned_jobs

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
