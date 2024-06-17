import csv
import itertools

def read_input(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return [(float(row['x']), float(row['y'])) for row in reader]

def write_output(file_path, path):
    with open(file_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['index'])
        for index in path:
            writer.writerow([index])

def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def total_distance(path, points):
    return sum(distance(points[path[i]], points[path[i + 1]]) for i in range(len(path) - 1)) + distance(points[path[-1]], points[path[0]])

def three_opt_swap(path, i, j, k):
    new_path = path[:i] + path[i:j][::-1] + path[j:k][::-1] + path[k:]
    return new_path

def three_opt(points):
    path = list(range(len(points)))
    improvement = True
    while improvement:
        improvement = False
        for (i, j, k) in itertools.combinations(range(len(path)), 3):
            new_path = three_opt_swap(path, i, j, k)
            if total_distance(new_path, points) < total_distance(path, points):
                path = new_path
                improvement = True
    return path

if __name__ == "__main__":
    input_file = 'input_5.csv'
    output_file = 'output_5.csv'
    points = read_input(input_file)
    path = three_opt(points)
    write_output(output_file, path)
    print(total_distance(path, points))
