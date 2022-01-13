from diagrams import Cluster, Diagram, Edge, Node


resources_number = int(input('Enter the number of resources: '))
resources = []
allocated_processes = {}
for i in range(resources_number):
    resources.append(int(input(f'Enter the count of R{i}: ')))
    allocated_processes[f'R{i}'] = list(map(lambda x: int(x[1]), input(f'Enter the processes that R{i} is allocated to them: ').split()))

processes_number = int(input('Enter the number of processes: '))
requested_resources = {}
for i in range(processes_number):
    requested_resources[f'P{i}'] = list(map(lambda x: int(x[1]), input(f'Enter the resources that P{i} requests: ').split()))


with Diagram("Resource Allocation Graph", show=True, direction="TB"):
    processes = []
    for i in range(processes_number):
        processes.append(Node(f"P{i}", shape='circle', style='filled', color='#bcd49f'))

    res = []
    for i in range(resources_number):
        with Cluster(f"R{i}"):
            res.append([Node(shape='point', fixedsize="true", width="0.2", height="0.2") for _ in range(resources[i])])
        for j in range(len(allocated_processes[f'R{i}'])):
            process = allocated_processes[f'R{i}'][j]
            res[-1][j] >> Edge(color='black') >> processes[process]

    for i in range(processes_number):
        for resource in requested_resources[f'P{i}']:
            processes[i] >> Edge(style='dashed', color='black') >> res[resource][0]
