from horizon.next.connections import RedshiftConnection

def create_job_status_dict(job, status):
    job_status_dict = {}
    
    for i,job_id in enumerate(job):
        if i < len(status):
            job_status_dict[job_id] = status[i]
        else:
            job_status_dict[job_id] = 'missing'
    return job_status_dict

def find_local_maxima(data):
    maxima = []
    n = len(data)
    for i, item in enumerate(data):
        left = i - 1
        right = i + 1
        if left >= 0 and right < n:
            if item > data[left] and item > data[right]:
                maxima.append((data[i],i))

    #print values to output
    for val, position in maxima:
        print(f'{val} at position {position}')
    
    return maxima

class BaseConnection:
    def __init__(self, credentials):
        self.rs_connection = RedshiftConnection(credentials)

    def set_timeout(self, timeout=10):
        self.rs_connection.timeout = timeout


class MyDBConnection(BaseConnection):
    def set_timeout(self, timeout=20):
        self.rs_connection.timeout = timeout

