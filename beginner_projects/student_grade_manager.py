students_names = ['mubaraq', 'baseet', 'kunle', 'wale', 'mbappe']
scores = [79, 82, 77, 80, 88]

print(f'{students_names[0]}: {scores[0]}')
print(f'{students_names[1]}: {scores[1]}')
print(f'{students_names[2]}: {scores[2]}')
print(f'{students_names[3]}: {scores[3]}')
print(f'{students_names[4]}: {scores[4]}')

highest_score = max(scores)
highest_index = scores.index(highest_score)
highest_student = students_names[highest_index]
print(f'Highest score: {highest_student}:- {highest_score}')

lowest_score = min(scores)
lowest_index = scores.index(lowest_score)
lowest_student = students_names[lowest_index]
print(f'Lowest score: {lowest_student}:- {lowest_score}')

class_average = sum(scores) / len(scores)
print(class_average)

sorted_names = sorted(students_names)   
sorted_scores = sorted(scores, reverse=True)
print(f'Names alphabetically: {sorted_names}')
print(f'Scores highest to lowest: {sorted_scores}')